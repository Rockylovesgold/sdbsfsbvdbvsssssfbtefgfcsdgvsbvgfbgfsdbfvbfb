f = open('index.html','a',encoding='utf-8')

# PORTFOLIO
f.write(r"""
<section id="portfolio" class="section rv" style="background:var(--bg)">
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem">Our Work</div>
  <h2>Real Website Transformations</h2>
  <p>Drag the line to compare. These are the results a proper redesign delivers for a Hull business.</p>
</div>
<div class="compare-wrap">
  <div class="compare-header">
    <div style="display:flex;align-items:center;gap:.85rem"><div class="compare-badge">01</div><div><div style="color:var(--white);font-weight:600;font-size:.9rem">Local Hull Trade Business</div><div style="color:#64748b;font-size:.78rem">Website redesign project</div></div></div>
    <div style="display:flex;gap:1.5rem;font-size:.78rem;flex-wrap:wrap"><span style="color:#64748b">Before: <strong style="color:#f87171">~3 enquiries/mo</strong></span><span style="color:#64748b">After: <strong style="color:#4ade80">~25 enquiries/mo</strong></span></div>
  </div>
  <div class="compare-stage">
    <div style="position:absolute;inset:0;background:#060a14;display:flex;flex-direction:column">
      <div style="background:#0b1220;padding:.65rem 1.5rem;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,.07)">
        <div style="display:flex;align-items:center;gap:.5rem"><div style="width:26px;height:26px;border-radius:6px;background:linear-gradient(135deg,#F5A623,#D97706);display:flex;align-items:center;justify-content:center;font-size:.9rem">&#9889;</div><span style="color:white;font-weight:800;font-size:.85rem;font-family:Syne,sans-serif">Hull Trade Pro</span></div>
        <div style="display:flex;gap:1.5rem;align-items:center"><span style="color:#64748b;font-size:.7rem">Services</span><span style="color:#64748b;font-size:.7rem">Areas</span><span style="background:#F5A623;color:#0a0a0a;font-size:.7rem;font-weight:700;padding:.3rem .9rem;border-radius:7px">Get Quote</span></div>
      </div>
      <div style="flex:1;display:grid;grid-template-columns:1fr 1fr">
        <div style="padding:2rem;display:flex;flex-direction:column;justify-content:center;gap:.9rem">
          <div style="font-size:.6rem;color:#F5A623;text-transform:uppercase;letter-spacing:.2em;font-weight:700">Hull &amp; East Yorkshire</div>
          <div style="font-size:1.6rem;font-weight:900;color:white;font-family:Syne,sans-serif;line-height:1.15">Your Trusted<br/><span style="color:#F5A623">Local Expert.</span></div>
          <div style="font-size:.77rem;color:#64748b;line-height:1.75;max-width:28ch">Reliable, insured, local. Free quotes and same-week appointments across Hull.</div>
          <div style="display:flex;gap:.75rem"><div style="background:#F5A623;color:#0a0a0a;font-size:.75rem;font-weight:700;padding:.55rem 1.25rem;border-radius:8px">Free Quote</div><div style="border:1px solid rgba(255,255,255,.1);color:#94a3b8;font-size:.75rem;padding:.55rem 1.25rem;border-radius:8px">Our Services</div></div>
          <div style="display:flex;gap:1rem"><span style="font-size:.65rem;color:#4ade80">&#10003; Fully Insured</span></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;padding:1.5rem;gap:.65rem;align-content:center">
          <div style="background:rgba(255,255,255,.05);border-radius:10px;padding:.9rem;text-align:center;border:1px solid rgba(245,166,35,.1)"><div style="color:#F5A623;font-size:1rem;font-weight:800;font-family:Syne,sans-serif">24/7</div><div style="color:#475569;font-size:.6rem">Emergency</div></div>
          <div style="background:rgba(255,255,255,.05);border-radius:10px;padding:.9rem;text-align:center;border:1px solid rgba(14,165,233,.1)"><div style="color:#38BDF8;font-size:1rem;font-weight:800;font-family:Syne,sans-serif">Same Day</div><div style="color:#475569;font-size:.6rem">Response</div></div>
          <div style="background:rgba(255,255,255,.05);border-radius:10px;padding:.9rem;text-align:center;border:1px solid rgba(245,166,35,.1)"><div style="color:#F5A623;font-size:1rem;font-weight:800;font-family:Syne,sans-serif">Fixed</div><div style="color:#475569;font-size:.6rem">Pricing</div></div>
          <div style="background:rgba(255,255,255,.05);border-radius:10px;padding:.9rem;text-align:center;border:1px solid rgba(14,165,233,.1)"><div style="color:#38BDF8;font-size:1rem;font-weight:800;font-family:Syne,sans-serif">5.0 &#9733;</div><div style="color:#475569;font-size:.6rem">Google</div></div>
        </div>
      </div>
    </div>
    <div style="position:absolute;top:10px;right:12px;background:var(--amber);color:#0a0a0a;padding:.25rem .75rem;border-radius:99px;font-size:.7rem;font-weight:800;z-index:5">AFTER &#9654;</div>
    <div id="bao1" style="position:absolute;inset:0;height:100%;overflow:hidden;border-right:3px solid var(--amber);z-index:10;width:50%">
      <div style="position:absolute;inset:0;min-width:200%">
        <div style="min-width:50%;background:#d0cbc0;font-family:Arial,sans-serif;height:100%">
          <div style="background:#1a3c6e;color:#ffd700;padding:.5rem 1rem;font-weight:bold;font-size:.72rem;display:flex;justify-content:space-between"><span>HULL TRADE SERVICES LTD</span><span style="color:white;font-size:.6rem">Website Est. 2009</span></div>
          <div style="background:#2a5fa8;display:flex"><span style="color:white;font-size:.62rem;font-weight:bold;padding:.35rem .75rem;background:rgba(255,255,255,.2)">HOME</span><span style="color:#cce;font-size:.62rem;padding:.35rem .75rem">ABOUT</span><span style="color:#cce;font-size:.62rem;padding:.35rem .75rem">SERVICES</span><span style="color:#cce;font-size:.62rem;padding:.35rem .75rem">CONTACT</span></div>
          <table style="width:100%;border-collapse:collapse;background:#ece8df"><tr><td style="width:155px;background:#c5bfb3;padding:.7rem;vertical-align:top;border-right:2px solid #aaa"><div style="background:white;padding:.45rem;margin-bottom:.5rem;border:1px solid #bbb;font-size:.6rem"><b style="font-size:.65rem">Welcome!</b><br/>Trade services in Hull &amp; surrounding areas. Call for a free quote. Est 2006.</div><div style="font-size:.58rem;line-height:2;color:#333"><b>Services:</b><br/>&#x25BA; Plumbing<br/>&#x25BA; Electrical<br/>&#x25BA; Heating</div></td><td style="padding:.7rem;vertical-align:top"><div style="font-size:.6rem;color:#c00;font-weight:bold;margin-bottom:.45rem">&#9888; SPECIAL OFFER — 10% OFF this month!</div><table style="width:100%;border-collapse:collapse;font-size:.6rem"><tr style="background:#1a3c6e;color:white"><td style="padding:.25rem .45rem;border:1px solid #999">Service</td><td style="padding:.25rem .45rem;border:1px solid #999">Price</td></tr><tr style="background:#fff"><td style="padding:.25rem .45rem;border:1px solid #ccc">Plumbing</td><td style="padding:.25rem .45rem;border:1px solid #ccc">POA</td></tr></table><div style="margin-top:.6rem;background:#fffbe6;border:1px solid #cc9900;padding:.35rem;font-size:.56rem;color:#555">Best viewed in Internet Explorer. &copy; 2016</div></td></tr></table>
        </div>
      </div>
      <div style="position:absolute;top:10px;left:10px;background:rgba(10,10,10,.9);color:#f87171;padding:.25rem .75rem;border-radius:99px;font-size:.7rem;font-weight:800">&#9664; BEFORE</div>
    </div>
    <input type="range" min="0" max="100" value="50" class="compare-range" oninput="document.getElementById('bao1').style.width=this.value+'%';document.getElementById('bah1').style.left=this.value+'%'"/>
    <div id="bah1" class="compare-handle"><div class="compare-handle-circle"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:#0a0a0a;font-size:1.2rem">swap_horiz</span></div></div>
  </div>
</div>
<p style="text-align:center;color:#475569;font-size:.82rem;margin-top:1rem;display:flex;align-items:center;justify-content:center;gap:.4rem">
  <span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem">touch_app</span>Drag the handle to compare before &amp; after
</p>
</div>
</section>
""")

# AI
f.write(r"""
<section id="ai" class="section rv" style="background:var(--bg2)">
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem;background:rgba(14,165,233,.08);border-color:rgba(14,165,233,.2);color:var(--teal)"><span style="width:7px;height:7px;border-radius:50%;background:var(--teal);display:inline-block;animation:pulse-dot 2s infinite"></span>AI-Powered Services</div>
  <h2>AI Automation for <span class="grad-teal">Hull Businesses</span></h2>
  <p>Stop losing time to repetitive tasks. We build AI-powered systems that work around the clock — even when you're out on a job.</p>
</div>
<div class="ai-explainer">
<div>
  <h3 style="font-size:1.5rem;margin-bottom:1rem">What does AI automation actually mean for your business?</h3>
  <p style="max-width:42ch;margin-bottom:1rem;font-size:.93rem">Think of it as hiring a brilliant digital team member who never sleeps, never forgets, and costs a fraction of a salary. They answer calls, follow up with leads, send reminders and update your systems — automatically.</p>
  <p style="max-width:42ch;margin-bottom:1.5rem;font-size:.93rem">For a Hull tradesperson, that means never missing a call while on a job. For a Beverley clinic, it's appointment reminders sending themselves. For an East Yorkshire retailer, abandoned basket emails go out without you lifting a finger.</p>
  <div class="ai-check"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.1rem;flex-shrink:0;margin-top:.1rem">check_circle</span><div><strong>Zero technical knowledge needed</strong><span>We build it, maintain it. You just use it.</span></div></div>
  <div class="ai-check"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.1rem;flex-shrink:0;margin-top:.1rem">check_circle</span><div><strong>Built around your Hull business</strong><span>Not generic software — designed for how you operate.</span></div></div>
  <div class="ai-check"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.1rem;flex-shrink:0;margin-top:.1rem">check_circle</span><div><strong>Typically saves 10+ hours of admin per week</strong><span>Time better spent winning and doing work.</span></div></div>
</div>
<div class="ai-net-wrap">
<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 480 320" fill="none">
  <line x1="240" y1="160" x2="80" y2="75" stroke="rgba(14,165,233,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="400" y2="75" stroke="rgba(14,165,233,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="60" y2="215" stroke="rgba(245,166,35,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="420" y2="215" stroke="rgba(245,166,35,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="160" y2="295" stroke="rgba(14,165,233,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="320" y2="295" stroke="rgba(14,165,233,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <circle r="5" fill="rgba(14,165,233,.9)"><animateMotion dur="2s" repeatCount="indefinite" path="M240,160 L80,75"/><animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/></circle>
  <circle r="5" fill="rgba(245,166,35,.9)"><animateMotion dur="2.5s" repeatCount="indefinite" path="M240,160 L420,215"/><animate attributeName="opacity" values="0;1;0" dur="2.5s" repeatCount="indefinite"/></circle>
  <circle r="5" fill="rgba(14,165,233,.9)"><animateMotion dur="1.8s" repeatCount="indefinite" path="M80,75 L240,160"/><animate attributeName="opacity" values="0;1;0" dur="1.8s" repeatCount="indefinite"/></circle>
  <circle r="5" fill="rgba(245,166,35,.9)"><animateMotion dur="3s" repeatCount="indefinite" path="M60,215 L240,160"/><animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite"/></circle>
  <circle r="5" fill="rgba(14,165,233,.9)"><animateMotion dur="2.2s" repeatCount="indefinite" path="M160,295 L240,160"/><animate attributeName="opacity" values="0;1;0" dur="2.2s" repeatCount="indefinite"/></circle>
  <circle cx="240" cy="160" r="45" fill="rgba(14,165,233,.06)" stroke="rgba(14,165,233,.35)" stroke-width="1.5"/>
  <circle cx="240" cy="160" r="30" fill="rgba(14,165,233,.1)" stroke="rgba(14,165,233,.25)" stroke-width="1.5"/>
  <circle cx="240" cy="160" r="45" fill="none" stroke="rgba(14,165,233,.25)" stroke-width="1"><animate attributeName="r" values="45;62" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values=".3;0" dur="2s" repeatCount="indefinite"/></circle>
  <circle cx="80" cy="75" r="24" fill="rgba(245,166,35,.07)" stroke="rgba(245,166,35,.4)" stroke-width="1.5"/>
  <circle cx="400" cy="75" r="24" fill="rgba(14,165,233,.07)" stroke="rgba(14,165,233,.4)" stroke-width="1.5"/>
  <circle cx="60" cy="215" r="20" fill="rgba(245,166,35,.07)" stroke="rgba(245,166,35,.35)" stroke-width="1.5"/>
  <circle cx="420" cy="215" r="20" fill="rgba(14,165,233,.07)" stroke="rgba(14,165,233,.35)" stroke-width="1.5"/>
  <circle cx="160" cy="295" r="18" fill="rgba(245,166,35,.07)" stroke="rgba(245,166,35,.3)" stroke-width="1.5"/>
  <circle cx="320" cy="295" r="18" fill="rgba(14,165,233,.07)" stroke="rgba(14,165,233,.3)" stroke-width="1.5"/>
</svg>
<div style="position:relative;z-index:10;padding:1.75rem;display:flex;flex-direction:column;justify-content:space-between;min-height:320px">
  <div style="display:flex;justify-content:space-between"><div style="text-align:center;width:70px"><p style="color:var(--amber);font-size:.75rem;font-weight:700">Calls</p><p style="color:#334155;font-size:.68rem">AI answers</p></div><div style="text-align:center;width:70px"><p style="color:var(--teal);font-size:.75rem;font-weight:700">CRM</p><p style="color:#334155;font-size:.68rem">auto-updated</p></div></div>
  <div style="text-align:center"><div style="width:60px;height:60px;border-radius:1rem;background:linear-gradient(135deg,rgba(14,165,233,.18),rgba(245,166,35,.1));border:1px solid rgba(14,165,233,.4);display:flex;align-items:center;justify-content:center;margin:0 auto 8px"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.75rem">smart_toy</span></div><p style="color:var(--white);font-weight:700;font-size:.9rem">AI Hub</p><p style="color:#334155;font-size:.7rem;display:flex;align-items:center;justify-content:center;gap:.3rem;margin-top:.2rem"><span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;animation:pulse-dot 1.5s infinite"></span>Always active</p></div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.5rem"><div style="text-align:center"><p style="color:var(--amber);font-size:.7rem;font-weight:700">Follow-ups</p><p style="color:#334155;font-size:.65rem">automated</p></div><div></div><div style="text-align:center"><p style="color:var(--teal);font-size:.7rem;font-weight:700">Bookings</p><p style="color:#334155;font-size:.65rem">auto-captured</p></div></div>
</div>
</div>
</div>
<div class="ai-cards">
""")
ais=[
  ('call','rgba(14,165,233,.1)','rgba(14,165,233,.2)','var(--teal)','AI Receptionist &amp; Call Handling','Never miss an enquiry again. Our AI answers calls 24/7, collects customer details, handles FAQs and alerts you instantly.',
   ['Covers nights, weekends, bank holidays and busy periods','Learns your services, pricing and availability','Sends you a call summary by text after every call','Qualifies leads so you focus on real opportunities'],
   'rgba(14,165,233,.2)','rgba(14,165,233,.35)','var(--teal)'),
  ('mark_email_read','rgba(245,166,35,.1)','rgba(245,166,35,.2)','var(--amber)','Automated Client Follow-Up','Most businesses lose customers by forgetting to follow up. Our system sends the right message at the right time — automatically.',
   ['Quote follow-ups at 24hrs, 3 days and 1 week — email &amp; SMS','Post-job review requests to build your Google rating','Re-engagement sequences for cold leads and past customers','Personalised with customer names and enquiry details'],
   'rgba(245,166,35,.15)','rgba(245,166,35,.3)','var(--amber)'),
  ('account_tree','rgba(14,165,233,.1)','rgba(14,165,233,.2)','var(--teal)','Business Workflow Automation','We map how your business works, then automate the repetitive handoffs — from first enquiry to completed job.',
   ['Booking confirmations and appointment reminders automated','Automatic quote generation from enquiry form submissions','Connects to WhatsApp, email, Google Sheets and more','Saves an average of 10+ hours of admin every week'],
   'rgba(14,165,233,.2)','rgba(14,165,233,.35)','var(--teal)'),
  ('developer_board','rgba(245,166,35,.1)','rgba(245,166,35,.22)','var(--amber)','Bespoke Backend Systems','Custom dashboards, CRM systems, job management portals and client portals — built precisely around how your Hull business operates.',
   ['Custom CRM — every customer, quote, job and invoice in one place','Job management portals for Hull trade &amp; service businesses','Live reporting dashboards — see performance at a glance','Client portals — customers book, pay and track online'],
   'rgba(245,166,35,.18)','rgba(245,166,35,.35)','var(--amber)'),
]
for icon,ibg,ibdr,iclr,name,desc,bullets,ctabg,ctabdr,ctaclr in ais:
    buls=''.join([f'<li><span style="font-family:\'Material Symbols Outlined\';font-variation-settings:\'FILL\' 0,\'wght\' 400;color:{ctaclr};font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>{b}</li>' for b in bullets])
    f.write(f"""<div class="card ai-card"><div class="ai-card-icon" style="background:{ibg};border:1px solid {ibdr}"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:{iclr};font-size:1.6rem">{icon}</span></div><div><h3>{name}</h3><p>{desc}</p></div><ul class="ai-bullets">{buls}</ul><a href="#contact" class="ai-cta" style="background:{ctabg};border-color:{ctabdr};color:{ctaclr}">Enquire<span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem">arrow_forward</span></a></div>\n""")
f.write("</div></div></section>\n")
f.close()
print("portfolio+ai ok")
