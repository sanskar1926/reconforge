import click
from rich.console import Console
from reconforge.scanner import run_scan
from reconforge.fingerprint import fingerprint_services
from reconforge.display import show_banner, show_scan_results, show_vuln_results, show_summary
from reconforge.osdetect import detect_os
from reconforge.brutecheck import run_brute_check
from reconforge.dnslookup import run_dns_lookup

console = Console()

@click.command()
@click.argument('target')
@click.option('--ports', default='1-1000', help='Port range to scan (default: 1-1000)')
@click.option('--os', 'os_detect', is_flag=True, help='Enable OS detection')
@click.option('--brute', is_flag=True, help='Test for default/weak credentials')
@click.option('--dns', 'dns_lookup', is_flag=True, help='Run DNS lookup on target')
def main(target, ports, os_detect, brute, dns_lookup):
    """
    ReconForge - Automated Recon & Vulnerability Fingerprinter

    Examples:

      reconforge scanme.nmap.org

      reconforge scanme.nmap.org --dns

      reconforge 192.168.1.105 --ports 1-500 --os --brute
    """
    show_banner()
    console.print(f"[bold cyan][*] Target:[/] {target} | [bold cyan]Ports:[/] {ports}\n")

    # Phase 1 - Scan
    scan_results = run_scan(target, ports)
    show_scan_results(scan_results)

    if not scan_results:
        console.print("[red][-] No open ports found. Exiting.[/]")
        return

    # Phase 2 - CVE Lookup
    console.print("\n[bold yellow][*] Starting vulnerability fingerprinting...[/]\n")
    vuln_results = fingerprint_services(scan_results)
    show_vuln_results(vuln_results)

    # Phase 3 - OS Detection (optional)
    if os_detect:
        detect_os(target)

    # Phase 4 - Brute Check (optional)
    if brute:
        run_brute_check(target, scan_results)

    # Phase 5 - DNS Lookup (optional)
    if dns_lookup:
        run_dns_lookup(target)

    # Summary
    show_summary(scan_results, vuln_results)

if __name__ == '__main__':
    main()
