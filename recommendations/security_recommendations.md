
## Recommendations for Home Users

1. **Use WPA3 or at least WPA2-Personal with a strong passphrase**
   - Prefer WPA3-Personal if the router and devices support it.
   - Use a passphrase with **16+ characters**, mixing words, numbers, and symbols.
   - Avoid dictionary words, phone numbers, or names.

2. **Disable WPS (Wi‑Fi Protected Setup)**
   - WPS PIN mode is vulnerable to brute‑force attacks.
   - In router settings: *WPS → Disable*.

3. **Change default SSID and admin credentials**
   - Avoid vendor-like SSIDs such as `Zentec Z031 …`.
   - Change the router’s **web admin username/password** as well.
   - This makes it harder for attackers to identify model-specific exploits.

4. **Separate IoT devices**
   - Place smart TVs, cameras, and IoT gadgets on a **separate guest network**.
   - Limit their access to only the internet, not your main LAN with laptops/phones.

5. **Keep firmware up to date**
   - Regularly check for router firmware updates.
   - Patches often fix security issues such as KRACK, chipset bugs, and vulnerabilities discovered after release.

---

## Recommendations for Enterprise Networks

1. **Use WPA2-Enterprise or WPA3-Enterprise with 802.1X**
   - Authenticate users via a **RADIUS server** and per‑user credentials or certificates.
   - Avoid PSK-based corporate networks.

2. **Implement strong identity and certificate management**
   - Use mutual TLS or EAP-TLS where possible.
   - Revoke credentials quickly when employees leave.

3. **Segment the network with VLANs**
   - Separate:
     - Corporate / internal network
     - Guest Wi‑Fi
     - IoT / building management devices
   - Restrict traffic between VLANs with firewalls.

4. **Monitor wireless activity with WIDS/WIPS**
   - Deploy wireless intrusion detection and prevention systems.
   - Detect:
     - Rogue access points
     - Evil twin attacks
     - Suspicious deauthentication floods.

5. **Optimize channel planning and load**
   - Some enterprise APs observed (e.g., KBTU) show high channel utilization.
   - Regular surveys can help:
     - Reduce interference
     - Balance client load
     - Improve performance and reliability.

6. **Develop and enforce a Wi‑Fi security policy**
   - Define:
     - Minimum encryption standard (WPA2-Enterprise or better)
     - Password rules (for guest networks)
     - Procedures for key rotation and incident response.
   - Train staff about phishing and social engineering related to Wi‑Fi.

---

## Conclusion

The scanned environment already demonstrates relatively modern Wi‑Fi security (WPA2/WPA3).  
However, many networks still rely on **WPA2-Personal**, making password strength and good operational practices critical.  
By applying the recommendations above, both home users and enterprises can significantly reduce the risk of compromise.
