content=open('index.html',encoding='utf-8').read()
checks=[
  ('DOCTYPE',         '<!DOCTYPE html>' in content),
  ('Nav',             'Hull Web Fixers' in content and 'AI Automation' in content),
  ('No fake reviews', 'JT Plumbing' not in content and 'Sarah Kemp' not in content),
  ('No pricing',      '£199' not in content and '£499' not in content),
  ('Hero',            'twt' in content and 'pcv' in content),
  ('Ticker',          'rtk' in content and 'AI Receptionist' in content),
  ('Stats',           'data-t' in content and 'will vary' in content),
  ('Services 6',      content.count('<h3') >= 6),
  ('Portfolio',       'bao1' in content and 'swap_horiz' in content),
  ('AI Automation',   'AI Receptionist' in content and 'Bespoke Backend' in content),
  ('AI Follow-Up',    'Client Follow-Up' in content),
  ('AI Workflow',     'Workflow Automation' in content),
  ('AI Network SVG',  'animateMotion' in content),
  ('Google Ads',      'Search Preview' in content),
  ('Facebook Ads',    '1877F2' in content),
  ('Process',         'Free Consultation' in content),
  ('FAQ',             'details' in content and len([x for x in content.split('<details') if x.strip()]) >= 7),
  ('Formspree',       'formspree.io/f/mlgwwjyn' in content),
  ('Contact fields',  'name="name"' in content and 'name="service"' in content),
  ('Hull bridge SVG', 'animateMotion' in content and 'Humber' in content),
  ('Footer',          'hullwebfixers.co.uk' in content),
  ('JS typewriter',   'typewriter' in content.lower() or 'twt' in content),
  ('JS particles',    'requestAnimationFrame' in content),
  ('JS counters',     'IntersectionObserver' in content),
  ('Closed',          content.strip().endswith('</html>')),
]
fails=[]
for name,ok in checks:
    print(('[OK] ' if ok else '[FAIL] ')+name)
    if not ok: fails.append(name)
print(f'Passed {len(checks)-len(fails)}/{len(checks)}')
print(f'File: {len(content.encode())//1024}KB')
