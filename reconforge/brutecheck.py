import paramiko
import ftplib
import socket
from rich.console import Console
from rich.table import Table

console = Console()

# Default weak credentials to test
DEFAULT_CREDS = [
    ("admin", "admin"),
    ("admin", "password"),
    ("admin", "123456"),
    ("root", "root"),
    ("root", "toor"),
    ("root", "password"),
    ("user", "user"),
    ("user", "password"),
    ("guest", "guest"),
    ("test", "test"),
    ("ubuntu", "ubuntu"),
    ("pi", "raspberry"),
]

def check_ssh(target, port=22):
    console.print(f"\n[bold yellow][*] Testing SSH default credentials on {target}:{port}...[/]\n")
    found = []

    for username, password in DEFAULT_CREDS:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                target,
                port=port,
                username=username,
                password=password,
                timeout=3,
                banner_timeout=5
            )
            console.print(f"[bold red][!!!] WEAK CREDENTIAL FOUND → {username}:{password}[/]")
            found.append((username, password))
            client.close()
        except paramiko.AuthenticationException:
            pass  # wrong creds, keep going
        except (socket.timeout, paramiko.SSHException, OSError):
            break  # host unreachable or SSH not running

    return found

def check_ftp(target, port=21):
    console.print(f"\n[bold yellow][*] Testing FTP default credentials on {target}:{port}...[/]\n")
    found = []

    for username, password in DEFAULT_CREDS:
        try:
            ftp = ftplib.FTP()
            ftp.connect(target, port, timeout=3)
            ftp.login(username, password)
            console.print(f"[bold red][!!!] WEAK CREDENTIAL FOUND → {username}:{password}[/]")
            found.append((username, password))
            ftp.quit()
        except ftplib.error_perm:
            pass  # wrong creds
        except Exception:
            break  # host unreachable

    return found

def run_brute_check(target, scan_results):
    all_found = []

    open_ports = {r['port']: r['service'] for r in scan_results}

    if 22 in open_ports:
        ssh_found = check_ssh(target, 22)
        all_found.extend([('SSH', u, p) for u, p in ssh_found])

    if 21 in open_ports:
        ftp_found = check_ftp(target, 21)
        all_found.extend([('FTP', u, p) for u, p in ftp_found])

    # Display results
    if all_found:
        table = Table(title="Weak Credentials Found", border_style="red")
        table.add_column("Service", style="bold yellow")
        table.add_column("Username", style="bold red")
        table.add_column("Password", style="bold red")
        for service, user, passwd in all_found:
            table.add_row(service, user, passwd)
        console.print(table)
    else:
        console.print("[bold green][+] No default credentials found. Service appears secure.[/]")

    return all_found
