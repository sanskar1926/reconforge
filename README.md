# ReconForge 🔥

> Automated Recon & Vulnerability Fingerprinting CLI Tool

ReconForge is a Python-based CLI tool that performs network reconnaissance and matches discovered services against the NVD CVE database in real time — all displayed in a clean, professional terminal UI.

Built for ethical hackers, security researchers, and penetration testers.

---

## Features

- Fast Nmap-based port and service scanning
- Live CVE lookup via NVD API (no API key needed)
- Beautiful Rich terminal UI with colored tables
- Risk level assessment in summary
- Lightweight — no bloat, no GUI, just terminal

---

## Installation
```bash
git clone https://github.com/YOURUSERNAME/reconforge
cd reconforge
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage
```bash
# Basic scan
python3 -m reconforge.cli scanme.nmap.org

# Custom port range
python3 -m reconforge.cli 192.168.1.105 --ports 1-65535
```

---

## Example Output
```
  ReconForge v1.0  🔥
  Automated Recon & Vulnerability Fingerprinter

[*] Target: scanme.nmap.org | Ports: 1-100

Open Ports
┌──────┬───────┬─────────┬─────────────────────────────────────┐
│ Port │ State │ Service │ Version                             │
├──────┼───────┼─────────┼─────────────────────────────────────┤
│ 22   │ open  │ ssh     │ OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 │
│ 80   │ open  │ http    │ Apache httpd 2.4.7                  │
└──────┴───────┴─────────┴─────────────────────────────────────┘

Vulnerabilities Found
┌────────────────┬──────┬─────────┬──────────────────────────────────┐
│ CVE ID         │ Port │ Service │ Description                      │
├────────────────┼──────┼─────────┼──────────────────────────────────┤
│ CVE-2021-44224 │ 80   │ http    │ A crafted URI sent to httpd...   │
└────────────────┴──────┴─────────┴──────────────────────────────────┘

Summary
  Scan Complete!
  Open Ports Found: 2
  CVEs Identified: 1
  Risk Level: HIGH ⚠
```

---

## Requirements

- Python 3.8+
- Nmap installed on system (`sudo apt install nmap`)
- Root/sudo privileges for full scan accuracy

---

## Legal Disclaimer

This tool is intended for authorized penetration testing and security research only. Only use against systems you own or have explicit written permission to test. The author is not responsible for misuse.

---

## Author

Made by Sanskar
