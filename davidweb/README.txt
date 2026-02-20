DEPLOYMENT INSTRUCTIONS
=======================

Your website is fully built and ready to deploy.

FILES INCLUDED:
1. index.html      - The complete website (HTML + CSS + JS)
2. logo.png        - Your logo (ChatGPT image used)
3. netlify.toml    - Security headers (for Netlify hosting)
4. .htaccess       - Security headers (for Apache/cPanel hosting)
5. gen.py          - Python script to regenerate index.html if needed

HOW TO RUN LOCALLY:
- Double-click `index.html` to open in your browser.
- OR run `python gen.py` to regenerate the file.

HOW TO DEPLOY:
1. Upload `index.html` AND `logo.png` to your hosting provider (e.g. Netlify, Cloudflare Pages, cPanel).
2. If using Netlify, also upload `netlify.toml`.
3. If using cPanel/Apache, also upload `.htaccess`.

SECURITY FEATURES ENABLED:
- Content Security Policy (CSP)
- X-Frame-Options (Clickjacking protection)
- Referrer Policy
- Permissions Policy
- Honeypot field (Spam protection on contact form)
- GDPR Cookie Consent banner
- `rel="noopener noreferrer"` on external links
- WhatsApp link removed (as requested)

Enjoy your new website!
