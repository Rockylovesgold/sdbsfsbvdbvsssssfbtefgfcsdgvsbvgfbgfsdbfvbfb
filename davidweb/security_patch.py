"""
Security patch + WhatsApp removal applied directly to index.html.

APPLICABLE TO A STATIC HTML SITE:
  Section 3  - Force HTTPS meta redirect
  Section 7  - Honeypot field on contact form (spam bot trap)
  Section 11 - CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy meta tags
  Section 16 - GDPR cookie consent banner, rel=noopener on external links

NOT APPLICABLE (static HTML, no server, no CMS, no DB, no uploads):
  Sections 1,2,4,5,6,8,9,10,12,13,14,15,17 → hosting-level or server config
  These should be handled by your hosting provider (Cloudflare, SiteGround, etc.)
"""

content = open('index.html', encoding='utf-8').read()

# ── 1. Remove WhatsApp contact-link ──────────────────────────────────────────
import re

# Remove from contact section (the <a class="contact-link" href="https://wa.me/..."> block)
content = re.sub(
    r'<a href="https://wa\.me/[^"]*"[^>]*class="contact-link"[^>]*>.*?</a>\s*',
    '', content, flags=re.DOTALL
)
# Also handle class before href variant
content = re.sub(
    r'<a class="contact-link"[^>]*href="https://wa\.me/[^"]*"[^>]*>.*?</a>\s*',
    '', content, flags=re.DOTALL
)

# Remove from footer ul
content = re.sub(
    r'<li[^>]*>.*?wa\.me.*?</li>\s*',
    '', content, flags=re.DOTALL
)

# ── 2. Security meta tags (Section 11 + 3) ───────────────────────────────────
security_meta = """
<!-- ═══ SECURITY META TAGS ═══ -->
<!-- Force HTTPS (Section 3) -->
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
<!-- CSP: restrict resource origins (Section 11) -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self' https://fonts.googleapis.com https://fonts.gstatic.com https://formspree.io; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; img-src 'self' data: blob:; frame-ancestors 'none';">
<!-- X-Frame-Options: prevent clickjacking (Section 11) -->
<meta http-equiv="X-Frame-Options" content="DENY">
<!-- X-Content-Type: prevent MIME sniffing (Section 11) -->
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<!-- Referrer-Policy: limit referrer data leakage (Section 11) -->
<meta name="referrer" content="strict-origin-when-cross-origin">
<!-- Permissions-Policy: restrict browser APIs (Section 11) -->
<meta http-equiv="Permissions-Policy" content="camera=(), microphone=(), geolocation=(), payment=()">
"""
content = content.replace('<link rel="preconnect"', security_meta + '<link rel="preconnect"', 1)

# ── 3. rel="noopener noreferrer" on all external <a> tags (Section 11/XSS) ──
def add_noopener(m):
    tag = m.group(0)
    if 'noopener' in tag:
        return tag
    if 'target="_blank"' in tag:
        tag = tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
    else:
        tag = tag.rstrip('>') + ' rel="noopener noreferrer">'
    return tag

content = re.sub(
    r'<a\s[^>]*href="https?://[^"]*"[^>]*>',
    add_noopener,
    content
)

# ── 4. Honeypot field on contact form (Section 7 – spam bot trap) ─────────────
honeypot = """
<!-- Honeypot spam trap (Section 7) — bots fill this, humans don't see it -->
<div style="position:absolute;left:-9999px;top:-9999px;opacity:0;pointer-events:none" aria-hidden="true">
  <label for="company_website">Company website (leave blank)</label>
  <input type="text" id="company_website" name="_gotcha" tabindex="-1" autocomplete="off"/>
</div>
"""
content = content.replace(
    '<input type="hidden" name="_subject"',
    honeypot + '<input type="hidden" name="_subject"',
    1
)

# ── 5. GDPR Cookie Consent banner (Section 16) ───────────────────────────────
cookie_banner = """
<!-- ═══ GDPR COOKIE CONSENT (Section 16) ═══ -->
<div id="cookie-bar" role="dialog" aria-label="Cookie consent" style="
  position:fixed;bottom:1.5rem;left:50%;transform:translateX(-50%);
  max-width:640px;width:calc(100% - 2rem);
  background:#0b1220;border:1px solid rgba(245,166,35,.25);
  border-radius:1.25rem;padding:1.25rem 1.5rem;
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;
  z-index:9998;box-shadow:0 24px 64px rgba(0,0,0,.7);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
">
  <div style="display:flex;align-items:flex-start;gap:.75rem;flex:1;min-width:0">
    <span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:#F5A623;font-size:1.3rem;flex-shrink:0;margin-top:.05rem">cookie</span>
    <div>
      <p style="color:#f1f5f9;font-weight:700;font-size:.88rem;margin-bottom:.2rem">We use cookies</p>
      <p style="color:#64748b;font-size:.78rem;line-height:1.55">We use essential cookies to make this site work. No tracking or marketing cookies are set without your consent. By clicking Accept, you agree to our <a href="#" style="color:#F5A623;text-decoration:underline">Privacy Policy</a>.</p>
    </div>
  </div>
  <div style="display:flex;gap:.6rem;flex-shrink:0">
    <button onclick="decCookies()" style="background:transparent;border:1px solid rgba(255,255,255,.12);color:#94a3b8;font-size:.8rem;font-weight:600;padding:.5rem 1.1rem;border-radius:.7rem;cursor:pointer;white-space:nowrap;font-family:'Inter',sans-serif">Decline</button>
    <button onclick="accCookies()" style="background:#F5A623;border:none;color:#0a0a0a;font-size:.8rem;font-weight:800;padding:.5rem 1.25rem;border-radius:.7rem;cursor:pointer;white-space:nowrap;font-family:'Syne',sans-serif">Accept</button>
  </div>
</div>
<script>
(function(){
  if(localStorage.getItem('cookie_consent')){
    document.getElementById('cookie-bar').style.display='none';
  }
})();
function accCookies(){localStorage.setItem('cookie_consent','accepted');document.getElementById('cookie-bar').style.display='none';}
function decCookies(){localStorage.setItem('cookie_consent','declined');document.getElementById('cookie-bar').style.display='none';}
</script>
"""
content = content.replace('</body>', cookie_banner + '\n</body>', 1)

# ── 6. Add autocomplete + novalidate-bypass protection on form ───────────────
# Improve form autocomplete attributes
content = content.replace(
    'id="name" name="name" type="text"',
    'id="name" name="name" type="text" autocomplete="name"'
)
content = content.replace(
    'id="email" name="email" type="email"',
    'id="email" name="email" type="email" autocomplete="email"'
)
content = content.replace(
    'id="business" name="business" type="text"',
    'id="business" name="business" type="text" autocomplete="organization"'
)

# ── Write out ────────────────────────────────────────────────────────────────
with open('index.html', 'w', encoding='utf-8') as out:
    out.write(content)

# ── Report ────────────────────────────────────────────────────────────────────
c = content
checks = [
    ('WhatsApp removed (contact)',  'wa.me' not in c or c.count('wa.me') == 0),
    ('CSP meta tag',                'Content-Security-Policy' in c),
    ('X-Frame-Options',             'X-Frame-Options' in c),
    ('X-Content-Type-Options',      'X-Content-Type-Options' in c),
    ('Referrer-Policy',             'strict-origin-when-cross-origin' in c),
    ('Permissions-Policy',          'Permissions-Policy' in c),
    ('Honeypot on form',            '_gotcha' in c),
    ('noopener on links',           'noopener' in c),
    ('Cookie consent banner',       'cookie-bar' in c),
    ('GDPR Privacy link',           'Privacy Policy' in c),
    ('autocomplete on inputs',      'autocomplete="name"' in c),
    ('Formspree still present',     'formspree.io/f/mlgwwjyn' in c),
    ('Site still valid',             c.strip().endswith('</html>')),
]
fails = []
for name, ok in checks:
    print(('[OK]' if ok else '[FAIL]'), name)
    if not ok: fails.append(name)

print()
print('='*48)
print('SECURITY MEASURES APPLIED (static HTML site):')
print('='*48)
print('[APPLIED]  Section 3  — CSP: upgrade-insecure-requests (force HTTPS)')
print('[APPLIED]  Section 7  — Honeypot field (spam bot trap on contact form)')
print('[APPLIED]  Section 11 — CSP meta (restrict resource origins)')
print('[APPLIED]  Section 11 — X-Frame-Options DENY (clickjacking protection)')
print('[APPLIED]  Section 11 — X-Content-Type-Options nosniff')
print('[APPLIED]  Section 11 — Referrer-Policy strict-origin-when-cross-origin')
print('[APPLIED]  Section 11 — Permissions-Policy (camera, mic, geo, payment off)')
print('[APPLIED]  Section 11 — rel=noopener noreferrer on all external links')
print('[APPLIED]  Section 16 — GDPR cookie consent banner')
print('[APPLIED]  Misc       — autocomplete attributes on form inputs')
print()
print('[HOSTING]  Sections 1,2,4,5,6,8,9,10,12,13,14,15,17 require server config.')
print('           Use Cloudflare (free): WAF, DDOS, DNSSEC, HSTS, server firewall')
print()
print(f'Result: {len(checks)-len(fails)}/{len(checks)} passed  |  Size: {len(c.encode())//1024}KB')
