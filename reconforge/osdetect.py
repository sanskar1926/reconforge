import nmap
from rich.console import Console
from rich.panel import Panel

console = Console()

def detect_os(target):
    console.print(f"\n[bold yellow][*] Detecting OS on {target}...[/]\n")
    nm = nmap.PortScanner()

    try:
        nm.scan(hosts=target, arguments='-O --osscan-guess')

        if target not in nm.all_hosts():
            console.print("[red][-] OS detection failed — target unreachable or blocked OS probes.[/]")
            return None

        host = nm[target]

        if 'osmatch' not in host or not host['osmatch']:
            console.print("[yellow][-] OS detection inconclusive — remote servers often block OS probes.[/]")
            console.print("[dim]    Tip: OS detection works best on local network targets.[/]")
            return None

        os_matches = host['osmatch'][:3]

        console.print(Panel(
            "\n".join([
                f"[bold cyan]{os['name']}[/] — [green]Accuracy: {os['accuracy']}%[/]"
                for os in os_matches
            ]),
            title="OS Detection Results",
            border_style="cyan"
        ))

        return os_matches[0]['name']

    except Exception as e:
        console.print("[yellow][-] OS detection inconclusive — remote servers often block OS probes.[/]")
        console.print("[dim]    Tip: OS detection works best on local network targets.[/]")
        return None
