content=open('index.html',encoding='utf-8').read()
checks=[
  ('DOCTYPE',         '<!DOCTYPE html>' in content),
  ('Logo img',        'logo.png' in content),
  ('No 5-star',       '5-star' not in content and '5 Star' not in content),
  ('No phone num',    '01482' not in content),
  ('No WhatsApp link','wa.me' not in content),
  ('Cookie Banner',   'cookie-bar' in content),
  ('Security Meta',   'Content-Security-Policy' in content),
  ('Honeypot',        '_gotcha' in content),
  ('Rel Noopener',    'noopener' in content),
  ('Autocomplete',    'autocomplete="name"' in content),
  ('wrap CSS',        '.wrap' in content and 'max-width:var(--max)' in content),
  ('max 1200px',      '--max:1200px' in content),
  ('No Tailwind',     'cdn.tailwindcss' not in content),
  ('Hero',            'pcv' in content),
  ('Humber bridge',   'hero-bridge' in content),
  ('AI section',      'AI Receptionist' in content),
  ('Google Ads',      'ads-grid' in content),
  ('Process',         'process-grid' in content),
  ('FAQ',             '<details' in content),
  ('Contact form',    'formspree.io' in content),
  ('Process JS',      'IntersectionObserver' in content),
  ('Closed',          content.strip().endswith('</html>')),
]
fails=[]
for name,ok in checks:
    print(('[OK] ' if ok else '[FAIL] ')+name)
    if not ok: fails.append(name)
print(f'Passed {len(checks)-len(fails)}/{len(checks)} | Size: {len(content.encode())//1024}KB')
