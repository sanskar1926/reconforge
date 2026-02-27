# ReconForge 🔥

> Automated Recon & Vulnerability Fingerprinting CLI Tool

ReconForge is a Python-based CLI tool that performs network reconnaissance and matches discovered services against the NVD CVE database in real time — all displayed in a clean, professional terminal UI.

Built for ethical hackers, security researchers, and penetration testers.

---

## Installation — One Time Setup
```bash
git clone https://github.com/sanskar1926/reconforge.git
cd reconforge
bash setup.sh
```

---

## Activate (Every New Terminal)
```bash
source venv/bin/activate && alias reconpy="sudo $(pwd)/venv/bin/python3"
```

---

## Usage
```bash
# Basic scan
reconpy -m reconforge.cli scanme.nmap.org

# Custom port range
reconpy -m reconforge.cli 192.168.1.1 --ports 1-500

# DNS lookup
reconpy -m reconforge.cli scanme.nmap.org --dns

# OS detection
reconpy -m reconforge.cli 192.168.1.1 --os

# Weak credential check
reconpy -m reconforge.cli 192.168.1.1 --brute

# Full power — everything at once
reconpy -m reconforge.cli 192.168.1.1 --ports 1-1000 --dns --os --brute
```

---

## Requirements

- Python 3.8+
- Nmap installed (`sudo apt install nmap`)
- Root/sudo privileges for full scan accuracy

---

## Legal Disclaimer

This tool is intended for authorized penetration testing and security research only. Only use against systems you own or have explicit written permission to test. The author is not responsible for misuse.

---

## Author

Made by Sanskar
