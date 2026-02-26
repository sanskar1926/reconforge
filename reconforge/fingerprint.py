import requests
from rich.console import Console

console = Console()

NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fingerprint_services(scan_results):
    all_vulns = []
    
    for service in scan_results:
        keyword = service.get('version') or service.get('service')
        if not keyword:
            continue
            
        console.print(f"[yellow][*] Looking up CVEs for: {keyword}[/]")
        cves = query_nvd(keyword)
        
        for cve in cves:
            all_vulns.append({
                'port': service['port'],
                'service': service['service'],
                'version': service['version'],
                'cve_id': cve['id'],
                'severity': cve['severity'],
                'description': cve['description']
            })
    
    return all_vulns

def query_nvd(keyword):
    try:
        resp = requests.get(NVD_API, params={
            'keywordSearch': keyword,
            'resultsPerPage': 3
        }, timeout=10)
        
        data = resp.json()
        results = []
        
        for item in data.get('vulnerabilities', []):
            cve = item['cve']
            metrics = cve.get('metrics', {})
            severity = 'UNKNOWN'
            
            if 'cvssMetricV31' in metrics:
                severity = metrics['cvssMetricV31'][0]['cvssData']['baseSeverity']
            elif 'cvssMetricV2' in metrics:
                severity = metrics['cvssMetricV2'][0]['baseSeverity']
            
            description = cve['descriptions'][0]['value'][:120]
            
            results.append({
                'id': cve['id'],
                'severity': severity,
                'description': description
            })
        
        return results
    
    except Exception as e:
        console.print(f"[red][-] CVE lookup failed: {e}[/]")
        return []
