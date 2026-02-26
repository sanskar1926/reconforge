import click
from rich.console import Console
from reconforge.scanner import run_scan
from reconforge.fingerprint import fingerprint_services
from reconforge.display import show_banner, show_scan_results, show_vuln_results, show_summary

console = Console()

@click.command()
@click.argument('target')
@click.option('--ports', default='1-1000', help='Port range to scan (default: 1-1000)')
def main(target, ports):
    """
    ReconForge - Automated Recon & Vulnerability Fingerprinter

    Example usage:

      reconforge scanme.nmap.org

      reconforge 192.168.1.105 --ports 1-65535
    """
    show_banner()
    console.print(f"[bold cyan][*] Target:[/] {target} | [bold cyan]Ports:[/] {ports}\n")

    # Phase 1
    scan_results = run_scan(target, ports)
    show_scan_results(scan_results)

    if not scan_results:
        console.print("[red][-] No open ports found. Exiting.[/]")
        return

    # Phase 2
    console.print("\n[bold yellow][*] Starting vulnerability fingerprinting...[/]\n")
    vuln_results = fingerprint_services(scan_results)
    show_vuln_results(vuln_results)

    # Summary
    show_summary(scan_results, vuln_results)

if __name__ == '__main__':
    main()
