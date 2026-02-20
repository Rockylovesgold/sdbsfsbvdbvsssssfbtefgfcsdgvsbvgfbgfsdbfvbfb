
"""
Final sweep:
1. Ensure all external links have rel="noopener noreferrer"
2. Verify security meta tags
3. Verify WhatsApp removal
"""
import re

c = open('index.html', encoding='utf-8').read()

# 1. Patch links
def add_noopener(m):
    tag = m.group(0)
    if 'rel="' in tag: return tag # already has rel
    if 'target="_blank"' in tag:
        return tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
    return tag

c = re.sub(r'<a\s[^>]*href="http[^"]*"[^>]*>', add_noopener, c)

# 2. Check WhatsApp
if 'wa.me' in c:
    print("WARNING: WhatsApp link found. Removing...")
    c = re.sub(r'<a[^>]*href="https://wa\.me[^"]*"[^>]*>.*?</a>', '', c, flags=re.DOTALL)
    c = re.sub(r'<li[^>]*>.*?WhatsApp.*?</li>', '', c, flags=re.DOTALL)

# 3. Write back
with open('index.html','w',encoding='utf-8') as f:
    f.write(c)

# 4. Report
checks = [
    ('CSP tag', 'Content-Security-Policy' in c),
    ('X-Frame', 'X-Frame-Options' in c),
    ('Cookie bar', 'cookie-bar' in c),
    ('WhatsApp gone', 'wa.me' not in c),
    ('Honeypot', '_gotcha' in c),
    ('Autocomplete', 'autocomplete="name"' in c),
]
for n,o in checks: print(('[OK]' if o else '[FAIL]'), n)
