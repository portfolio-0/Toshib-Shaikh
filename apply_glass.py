import re

with open('style.css', 'r') as f:
    css = f.read()

# 1. Body background
css = re.sub(
    r'body\s*\{\n\s*font-family:\s*\'Inter\',\s*sans-serif;\n\s*background:\s*var\(--cream\);\n\s*color:\s*var\(--green\);',
    r'''body {
  font-family: 'Inter', sans-serif;
  background: linear-gradient(135deg, var(--green-dark), var(--green), var(--green-light));
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  color: var(--cream);''',
    css
)

css += "\n@keyframes gradientBG { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }\n"

# 2. Hero sections
css = re.sub(
    r'\.hero-left\s*\{\n\s*background:\s*linear-gradient\([^)]+\);',
    r'.hero-left {\n  background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border-right: 1px solid rgba(255, 255, 255, 0.1);\n  border-bottom: 1px solid rgba(255, 255, 255, 0.1);',
    css
)

css = re.sub(
    r'\.hero-right\s*\{\n\s*background:\s*linear-gradient\([^)]+\);',
    r'.hero-right {\n  background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border-left: 1px solid rgba(255, 255, 255, 0.1);\n  border-bottom: 1px solid rgba(255, 255, 255, 0.1);',
    css
)

# Replace the img-placeholder CSS with .hero-photo
css = re.sub(
    r'\.img-placeholder-icon\s*\{.*?\.hero-right\s*p\s*\{[^\}]+\}',
    r'''.hero-photo {
  max-width: 80%;
  height: auto;
  border-radius: 20px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
}''',
    css,
    flags=re.DOTALL
)

# 3. Section backgrounds
css = re.sub(r'#services\s*\{\n\s*background:\s*linear-gradient\([^)]+\);\n\}', r'#services {\n  background: transparent;\n}', css)
css = re.sub(r'#showcase\s*\{\n\s*background:\s*linear-gradient\([^)]+\);', r'#showcase {\n  background: transparent;', css)
css = re.sub(r'#tools\s*\{\n\s*background:\s*linear-gradient\([^)]+\);\n\}', r'#tools {\n  background: transparent;\n}', css)
css = re.sub(r'#clients\s*\{\n\s*background:\s*linear-gradient\([^)]+\);', r'#clients {\n  background: transparent;', css)
css = re.sub(r'#cta\s*\{\n\s*background:\s*linear-gradient\([^)]+\);', r'#cta {\n  background: transparent;', css)

# 4. Service cards (add glass)
css = re.sub(
    r'\.service-card\s*\{\n\s*background:\s*linear-gradient\([^)]+\);',
    r'.service-card {\n  background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);',
    css
)
css = re.sub(
    r'\.service-card:hover\s*\{[\s\S]*?background:\s*linear-gradient\([^)]+\);\n\}',
    r'.service-card:hover {\n  transform: translateY(-8px) scale(1.01);\n  box-shadow: 0 20px 50px rgba(0,0,0,0.3);\n  background: rgba(255, 255, 255, 0.1);\n}',
    css
)

# 5. Fix text colors in sections that were cream/light
css = re.sub(
    r'\.section-label\s*\{\n\s*font-size:',
    r'.section-label {\n  color: rgba(255,255,255,0.5) !important;\n  font-size:',
    css
)
css = re.sub(
    r'\.section-title\s*\{\n\s*font-size:\s*clamp\([^)]+\);\n\s*font-weight:\s*900;\n\s*color:\s*var\(--green\);',
    r'.section-title {\n  font-size: clamp(1.9rem, 3vw, 2.8rem);\n  font-weight: 900;\n  color: var(--cream);',
    css
)
css = re.sub(
    r'\.section-sub\s*\{\n\s*font-size:\s*0\.97rem;\n\s*color:\s*var\(--green\);',
    r'.section-sub {\n  font-size: 0.97rem;\n  color: rgba(255,255,255,0.7);',
    css
)

# 6. glass for cards and tools
# .tool-row
css = re.sub(
    r'\.tool-row\s*\{\n\s*display:\s*flex;[\s\S]*?background:\s*linear-gradient\([^)]+\);',
    r'.tool-row {\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  padding: 16px 20px;\n  background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);',
    css
)
css = re.sub(
    r'\.tool-row:hover\s*\{\n\s*background:\s*linear-gradient\([^)]+\);',
    r'.tool-row:hover {\n  background: rgba(255, 255, 255, 0.1);',
    css
)

# stat-box
css = re.sub(
    r'\.stat-box\s*\{\n\s*background:\s*linear-gradient\([^)]+\);',
    r'.stat-box {\n  background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);',
    css
)

# currently-at
css = re.sub(
    r'\.currently-at\s*\{\n\s*background:\s*linear-gradient\([^)]+\);',
    r'.currently-at {\n  background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);',
    css
)

# CTA button
css = re.sub(
    r'\.view-clients-btn\s*\{\n\s*display:\s*inline-block;\n\s*border:\s*2px solid var\(--green\);\n\s*color:\s*var\(--green\);',
    r'.view-clients-btn {\n  display: inline-block;\n  border: 2px solid rgba(255,255,255,0.3);\n  color: var(--cream);',
    css
)
css = re.sub(
    r'\.view-clients-btn:hover\s*\{\n\s*background:\s*var\(--green\);\n\s*color:\s*var\(--cream\);',
    r'.view-clients-btn:hover {\n  background: rgba(255,255,255,0.1);\n  color: var(--cream);',
    css
)

# submit-btn and hero-btn background to be more glassy
css = re.sub(
    r'\.submit-btn\s*\{\n\s*background:\s*linear-gradient\([^)]+\);\n\s*color:\s*var\(--green\);',
    r'.submit-btn {\n  background: rgba(255,255,255,0.85);\n  color: var(--green);',
    css
)

css = re.sub(
    r'\.hero-btn\s*\{\n\s*(display.*?)\n\s*background:\s*linear-gradient\([^)]+\);\n\s*color:\s*var\(--green\);',
    r'.hero-btn {\n  \1\n  background: rgba(255,255,255,0.85);\n  color: var(--green);',
    css
)

# Replace any explicit color: var(--green) that should be cream now that bg is dark green
# Nav CTA
css = re.sub(
    r'nav \.nav-cta\s*\{\n\s*background:\s*linear-gradient\([^)]+\);\n\s*color:\s*var\(--green\);',
    r'nav .nav-cta {\n  background: rgba(255,255,255,0.85);\n  color: var(--green);',
    css
)

with open('style.css', 'w') as f:
    f.write(css)

print("Done")
