import re

with open("style.css", "r") as f:
    css = f.read()

# 1. Fix the body background to use the pure green gradient the user likes
body_replacement = """body {
  font-family: 'Inter', sans-serif;
  background: linear-gradient(160deg, var(--green-dark) 0%, var(--green) 55%, var(--green-light) 100%);
  background-attachment: fixed;
  color: var(--cream);
  overflow-x: hidden;
  opacity: 0;
  transition: opacity 0.5s ease;
}"""

css = re.sub(r'body\s*\{[\s\S]*?transition:\s*opacity\s*0\.5s\s*ease;\n\}', body_replacement, css)

# 2. The Apple dark glass style
apple_dl_glass = """  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);"""

# Let's write a function to replace the messy glass properties with clean apple glass
def apply_glass(selector_regex):
    global css
    # Replace the existing background/backdrop filters in the matched selector block
    # Since my previous script added explicit backgrounds and borders, I'll strip them out and insert apple_dl_glass
    pass

# Instead of regex the selectors, I'll just find and replace all the white-ish glass occurrences.
# Previous script added: background: rgba(255, 255, 255, 0.08); backdrop-filter: blur(24px); etc.

# First, let's remove exactly what was added to .hero-right
css = re.sub(
    r'\.hero-right\s*\{\s*margin-left:\s*10px;\s*background:\s*rgba\(255,\s*255,\s*255,\s*0\.08\);\s*backdrop-filter:\s*blur\(24px\);\s*-webkit-backdrop-filter:\s*blur\(24px\);\s*border:\s*1px solid rgba\(255,\s*255,\s*255,\s*0\.2\);\s*border-radius:\s*32px;\s*box-shadow:\s*0 10px 40px rgba\(0,0,0,0\.2\);',
    r'.hero-right {\n  /* Pure green background for the image per user request */\n  background: transparent;',
    css
)
css = re.sub(
    r'\.hero-right\s*\{\s*background:\s*rgba\(255,\s*255,\s*255,\s*0\.05\)[^}]+\}',
    r'.hero-right {\n  background: transparent;\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  justify-content: center;\n  position: relative;\n}',
    css
)

# And .hero-left
css = re.sub(
    r'\.hero-left\s*\{\s*margin-right:\s*10px;[^}]+\}',
    r'''.hero-left {
  margin-right: 10px;
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 10px 40px rgba(0,0,0,0.3);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px 70px;
  border-radius: 32px;
  position: relative;
  overflow: hidden;
}''',
    css
)

# Fix .service-card
css = re.sub(
    r'\.service-card\s*\{[\s\S]*?cursor:\s*default;',
    r'''.service-card {
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  padding: 42px 34px;
  border-radius: 20px;
  transition: transform 0.35s var(--ease), box-shadow 0.35s, background 0.35s;
  cursor: default;''',
    css
)

# Fix .video-placeholder
css = re.sub(
    r'\.video-placeholder\s*\{[\s\S]*?aspect-ratio:\s*16/9;',
    r'''.video-placeholder {
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  aspect-ratio: 16/9;''',
    css
)

# Fix nav to use dark glass
css = re.sub(
    r'nav\s*\{\s*position:\s*fixed;[\s\S]*?padding:\s*14px\s*28px;',
    r'''nav {
  position: fixed;
  top: 16px; left: 50%; right: auto;
  transform: translateX(-50%);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  padding: 14px 28px;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);''',
    css
)

# Fix .client-card, .tool-row, .stat-box, .currently-at
for cls in [".client-card", ".tool-row", ".stat-box", ".currently-at"]:
    css = re.sub(
        rf'\{cls}\s*\{{[\s\S]*?background:\s*[^;]+;[\s]*backdrop-filter:[^;]+;[\s]*-webkit-backdrop-filter:[^;]+;',
        f'''{cls} {{
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);''',
        css
    )

# Contact form inputs
css = re.sub(
    r'\.contact-form\s*input,\s*\.contact-form\s*textarea\s*\{\s*background:\s*[^;]+;',
    r'.contact-form input,\n.contact-form textarea {\n  background: rgba(0, 0, 0, 0.2);',
    css
)

# Also ensure .client-card has its border set correctly (if we didn't overwrite properly above)
css = re.sub(r'border:\s*1px solid rgba\(245,245,220,0\.09\);', '', css)

# Make sure hero-photo doesn't have an opaque background
# and aligns well
css = re.sub(
    r'\.hero-photo\s*\{[^}]+\}',
    r'''.hero-photo {
  max-width: 90%;
  height: auto;
  border-radius: 20px;
  object-fit: cover;
  filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));
}''',
    css
)

# Strip out the random backgrounds applied to hero-right
css = re.sub(r'\.hero-right\s*\{\n\s*background:\s*transparent;\n\s*display:\s*flex;[\s\S]*?position:\s*relative;\n\s*overflow:\s*hidden;\n\s*border-radius:[^}]+\}', 
r'''.hero-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
}''', css)

with open("style.css", "w") as f:
    f.write(css)

print("Glass style rebuilt cleanly.")
