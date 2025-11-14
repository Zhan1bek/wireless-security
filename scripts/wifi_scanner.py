#!/usr/bin/env python3
"""Simple Windows Wi‑Fi scanner wrapper around `netsh`.

This script is optional and provided for automation purposes.
It calls `netsh wlan show networks mode=bssid` and saves the raw output to a timestamped file.
"""

import subprocess
from datetime import datetime
import os


def scan_windows():
    cmd = ["netsh", "wlan", "show", "networks", "mode=bssid"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return result.stdout


def main():
    print("[+] Starting Wi‑Fi scan using netsh...")
    output = scan_windows()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"wifi_scan_{timestamp}.txt"

    out_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.abspath(os.path.join(out_dir, filename))

    with open(path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"[+] Scan complete. Results saved to: {path}")


if __name__ == "__main__":
    main()
