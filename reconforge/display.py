from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_banner():
    banner = Text()
    banner.append("\n  ReconForge v1.0  ", style="bold red")
    banner.append("🔥\n", style="bold yellow")
    banner.append("  Automated Recon & Vulnerability Fingerprinter\n", style="dim white")
    console.print(Panel(banner, border_style="red", width=60))

def show_scan_results(scan_results):
    table = Table(title="Open Ports", border_style="cyan", show_lines=True)
    table.add_column("Port", style="bold white", width=8)
    table.add_column("State", style="bold green", width=8)
    table.add_column("Service", style="bold yellow", width=12)
    table.add_column("Version", style="white")

    for r in scan_results:
        table.add_row(
            str(r['port']),
            r['state'],
            r['service'],
            r['version'] or "Unknown"
        )
    console.print(table)

def show_vuln_results(vuln_results):
    if not vuln_results:
        console.print("\n[bold green][+] No known CVEs found for detected services.[/]")
        return

    table = Table(title="Vulnerabilities Found", border_style="red", show_lines=True)
    table.add_column("CVE ID", style="bold red", width=18)
    table.add_column("Port", style="white", width=6)
    table.add_column("Service", style="yellow", width=10)
    table.add_column("Description", style="dim white")

    for v in vuln_results:
        table.add_row(
            v['cve_id'],
            str(v['port']),
            v['service'],
            v['description'][:80] + "..."
        )
    console.print(table)

def show_summary(scan_results, vuln_results):
    console.print(Panel(
        f"[bold green]Scan Complete![/]\n"
        f"[cyan]Open Ports Found:[/] {len(scan_results)}\n"
        f"[red]CVEs Identified:[/] {len(vuln_results)}\n"
        f"[yellow]Risk Level:[/] {'HIGH ⚠' if len(vuln_results) > 0 else 'LOW ✓'}",
        border_style="green",
        title="Summary"
    ))
