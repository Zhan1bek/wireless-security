## Encryption Rating Scale

- **Critical** – Open networks, WEP
- **High** – WPA / WPA‑TKIP
- **Medium** – WPA2‑Personal (PSK)
- **Low** – WPA2‑Enterprise (802.1X), WPA3‑Personal

---

## Encryption Assessment Table

| # | SSID                                  | Encryption       | Security Rating | Explanation |
|---|---------------------------------------|------------------|----------------|-------------|
| 1 | (hidden)                              | WPA3-Personal    | Low            | WPA3-Personal uses SAE and is resistant to offline dictionary attacks when configured correctly. |
| 2 | KBTU                                  | WPA2-Enterprise  | Low            | Enterprise authentication with 802.1X/RADIUS and per-user credentials provides strong access control. |
| 3 | Zentec Z031 80646F3563BCd31           | WPA2-Personal    | Medium         | WPA2-PSK is secure if a strong passphrase is used, but still vulnerable to handshake capture + offline cracking. |
| 4 | iPhone                                | WPA3-Personal    | Low            | Personal hotspot using WPA3; modern and robust, assuming a non-trivial password. |
| 5 | Ars                                   | WPA2-Personal    | Medium         | Home/office router with WPA2-PSK; overall secure but depends heavily on passphrase strength. |
| 6 | Zentec Z031 C049EF4E7B04d31           | WPA2-Personal    | Medium         | Standard WPA2-PSK configuration on 2.4 GHz. |
| 7 | Galaxy S21 FE 5G 7E8E                 | WPA2-Personal    | Medium         | Mobile hotspot with WPA2-PSK; often configured with weaker passwords in practice. |
| 8 | Zentec Z031 409151D61B84d31           | WPA2-Personal    | Medium         | WPA2-PSK; no visible additional protections. |
| 9 | iPhone Yermakhan Kasymzhomart         | WPA2-Personal    | Medium         | Personal hotspot; WPA2-PSK, depends on password quality. |
|10 | ABC                                   | WPA2-Personal    | Medium         | Generic WPA2-PSK network; potentially guessable password if not hardened. |
|11 | Zentec Z031 80646F3DE624d31           | WPA2-Personal    | Medium         | Uses WPA2-PSK; secure if passphrase is long and random. |
|12 | Zentec Z031 C049EF58FCB4d31           | WPA2-Personal    | Medium         | Same security posture as other Zentec SSIDs. |
|13 | Zentec Z031 64B708139F99d31           | WPA2-Personal    | Medium         | WPA2-PSK; appears to be a consumer router. |
|14 | WPA2-Personal                         | WPA2-Personal    | Medium         | SSID literally “WPA2-Personal”; likely default/temporary config with unknown password quality. |
|15 | Karuka                                | WPA2-Personal    | Medium         | Named SSID with WPA2-PSK; no enterprise controls. |
|16 | (1)                                   | WPA2-Personal    | Medium         | WPA2-PSK network with short SSID; again depends on the passphrase entropy. |

---

## Summary

- **0 networks** using WEP or Open authentication → no *Critical* risks detected at the encryption level.
- **2 networks** use **WPA3-Personal**, providing the strongest protection in this environment.
- **1 network (KBTU)** uses **WPA2-Enterprise**, which is considered *Low* risk due to centralized authentication and better access control.
- **13 networks** use **WPA2-Personal**, which is widely deployed and reasonably secure, but still vulnerable to:
  - Weak or reused PSKs
  - Offline dictionary attacks after capturing the 4-way handshake
  - Social engineering to obtain the passphrase

From an encryption standpoint, the environment is relatively modern and secure, but many networks still rely on shared passwords rather than per-user enterprise authentication.
