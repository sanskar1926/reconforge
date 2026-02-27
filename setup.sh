#!/bin/bash
echo "[*] Setting up ReconForge..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install paramiko dnspython
echo ""
echo "[+] Setup complete!"
echo "[+] Run this command to activate:"
echo ""
echo "    source venv/bin/activate && alias reconpy='sudo $(pwd)/venv/bin/python3'"
echo ""
echo "[+] Then scan with:"
echo ""
echo "    reconpy -m reconforge.cli scanme.nmap.org --ports 1-100"
echo ""
