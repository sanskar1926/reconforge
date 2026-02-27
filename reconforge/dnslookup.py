import dns.resolver
from rich.console import Console
from rich.table import Table

console = Console()

RECORD_TYPES = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']

def run_dns_lookup(target):
    console.print(f"\n[bold yellow][*] Running DNS Lookup on {target}...[/]\n")

    table = Table(title=f"DNS Records — {target}", border_style="cyan", show_lines=True)
    table.add_column("Record Type", style="bold yellow", width=15)
    table.add_column("Value", style="white")

    found_any = False

    for record_type in RECORD_TYPES:
        try:
            answers = dns.resolver.resolve(target, record_type)
            for rdata in answers:
                table.add_row(record_type, str(rdata))
                found_any = True
        except Exception:
            pass

    if found_any:
        console.print(table)
    else:
        console.print("[red][-] No DNS records found for this target.[/]")
