import re

with open('style.css', 'r') as f:
    css = f.read()

# client-card
css = re.sub(
    r'\.client-card\s*\{\n\s*background:\s*rgba\([^)]+\);',
    r'.client-card {\n  background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);',
    css
)

# video-placeholder
css = re.sub(
    r'\.video-placeholder\s*\{\n\s*background:\s*rgba\([^)]+\);',
    r'.video-placeholder {\n  background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);',
    css
)

# nav
css = re.sub(
    r'nav\s*\{\n\s*position:\s*fixed;[\s\S]*?background:\s*rgba\([^)]+\);',
    r'nav {\n  position: fixed;\n  top: 16px; left: 50%; right: auto;\n  transform: translateX(-50%);\n  z-index: 100;\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  gap: 40px;\n  padding: 14px 28px;\n  background: rgba(255, 255, 255, 0.1);',
    css
)


with open('style.css', 'w') as f:
    f.write(css)

print("Client cards and videos updated")
