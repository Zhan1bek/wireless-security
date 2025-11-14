# Wireless Network Security Assessment

This repository contains a wireless security assessment performed using passive Wi‑Fi scanning tools on Windows (`netsh wlan show networks mode=bssid`), following the EC‑Council EHE Module 08 concepts.

The assessment includes:

- Wireless network discovery (16 detected networks)
- Encryption assessment and security rating
- Vulnerability analysis for all detected networks
- Attack vector analysis for selected networks
- Security recommendations for home and enterprise environments
- Technical documentation with a clean repository structure

All scanning was performed ethically and passively. No active attacks or unauthorized access attempts were made.

---

## 📁 Repository Structure

```text
wireless-security-assessment/
│── README.md
│── data/
│   ├── scan_results.csv
│   ├── raw_output.txt
│── analysis/
│   ├── security_analysis.md
│   ├── vulnerability_report.md
│   └── screenshots/
│── recommendations/
│   └── security_recommendations.md
│── scripts/
│   ├── wifi_scanner.py
│   └── requirements.txt
└── tools/
    └── tool_comparison.md
```

---

## Tools Used

- **Windows `netsh`** (built‑in command‑line Wi‑Fi scanner)
- Standard laptop Wi‑Fi network interface

Optional / mentioned in documentation:

- Python (for potential automation via `wifi_scanner.py`)
- Third‑party Wi‑Fi tools (Wireshark, nmcli, etc.) – referenced but not required

---

## Ethical Notice

This project was completed for educational purposes in a cybersecurity course.

- Only networks in the immediate vicinity were scanned.
- Only passive discovery was used (no packet injection or brute‑force).
- No attempts were made to bypass authentication or encryption.
- No confidential data was intercepted.

Always follow local laws, institutional policies, and ethical guidelines when performing any kind of network assessment.
