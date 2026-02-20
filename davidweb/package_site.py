
"""
Builds the final gen.py script.
Adds logic to copy the logo and write index.html.
"""
import os

content = open("index.html", encoding="utf-8").read()
# Escape triple quotes
content = content.replace('"""', '\\"\\"\\"')

script = f"""# FULLY AUTOMATED WEBSITE GENERATOR
import os
import shutil

print("Generating website...")

# 1. Write index.html
html = r\"\"\"{content}\"\"\"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("- index.html written ({{}} bytes)".format(len(html)))

# 2. Setup logo
logo_src = "ChatGPT Image Feb 19, 2026, 11_43_56 PM.png"
logo_dst = "logo.png"

if os.path.exists(logo_src):
    try:
        shutil.copy(logo_src, logo_dst)
        print("- Logo copied to {{}}".format(logo_dst))
    except Exception as e:
        print("- Warning: Could not copy logo: {{}}".format(e))
else:
    if not os.path.exists(logo_dst):
        print("- Warning: Source logo '{{}}' not found and '{{}}' missing.".format(logo_src, logo_dst))
    else:
        print("- Logo '{{}}' already exists.".format(logo_dst))

print("\\nSUCCESS! Website is ready.")
print("Open index.html in your browser to view.")
"""

with open("gen.py", "w", encoding="utf-8") as f:
    f.write(script)

print("gen.py updated with logo logic.")
