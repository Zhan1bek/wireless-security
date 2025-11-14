# Tool Comparison

This document briefly compares several tools that can be used for wireless discovery and analysis.

| Tool        | Platform     | Type     | Strengths                                           | Limitations                             |
|------------|--------------|----------|-----------------------------------------------------|-----------------------------------------|
| netsh      | Windows      | CLI      | Built-in, no install needed, good basic info        | Output not structured, Windows-only     |
| pywifi     | Cross-platform (Windows/Linux) | Python lib | Scriptable, automation-friendly, integrates in apps | Requires Python and drivers             |
| nmcli      | Linux (NetworkManager) | CLI | Rich Wi‑Fi info, scripting support                 | Only on systems using NetworkManager    |
| wdutil     | macOS        | CLI      | Modern Wi‑Fi diagnostics on macOS                   | Requires sudo and familiarity with CLI  |
| Wireshark  | Cross-platform | GUI   | Deep packet inspection and protocol analysis        | More complex, not just for quick scans |

For this assignment, the **native `netsh` tool on Windows** was used to discover nearby Wi‑Fi networks, which was sufficient to collect SSID, BSSID, signal strength, channel, frequency band, and basic security information.
