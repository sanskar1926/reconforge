import nmap
from rich.console import Console

console = Console()

def run_scan(target, ports="1-1000"):
    console.print(f"[bold cyan][*] Scanning {target} on ports {ports}...[/]")
    
    nm = nmap.PortScanner()
    nm.scan(hosts=target, ports=ports, arguments='-sV -T4')
    
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in sorted(nm[host][proto].keys()):
                service = nm[host][proto][port]
                if service['state'] == 'open':
                    results.append({
                        'port': port,
                        'state': service['state'],
                        'service': service['name'],
                        'version': f"{service['product']} {service['version']}".strip()
                    })
    return results
