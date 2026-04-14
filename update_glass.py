import re

with open("style.css", "r") as f:
    text = f.read()

# 1. Update the body background to be exactly the hero green with blobs
body_replacement = """body {
  font-family: 'Inter', sans-serif;
  background-color: var(--green);
  background-image: 
    radial-gradient(circle at 20% 30%, rgba(93, 222, 122, 0.25) 0%, transparent 40%),
    radial-gradient(circle at 80% 80%, rgba(245, 245, 220, 0.1) 0%, transparent 40%),
    radial-gradient(circle at 50% 50%, rgba(93, 222, 122, 0.15) 0%, transparent 60%),
    linear-gradient(160deg, var(--green-dark) 0%, var(--green) 55%, var(--green-light) 100%);
  background-attachment: fixed;
  color: var(--cream);
  overflow-x: hidden;
  opacity: 0;
  transition: opacity 0.5s ease;
}"""

# Replace body section
text = re.sub(r'body\s*\{[\s\S]*?transition:\s*opacity\s*0\.5s\s*ease;\n\}', body_replacement, text)

# 2. Make glass stronger for panels globally
strong_glass_bg = "background: rgba(255, 255, 255, 0.08);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);"
strong_border = "border: 1px solid rgba(255, 255, 255, 0.2);"

# Fix hero-left
text = text.replace(
    "background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border-right: 1px solid rgba(255, 255, 255, 0.1);\n  border-bottom: 1px solid rgba(255, 255, 255, 0.1);",
    strong_glass_bg + "\n  " + strong_border + "\n  border-radius: 32px;\n  box-shadow: 0 10px 40px rgba(0,0,0,0.2);"
)

# Fix hero-right
text = text.replace(
    "background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border-left: 1px solid rgba(255, 255, 255, 0.1);\n  border-bottom: 1px solid rgba(255, 255, 255, 0.1);",
    strong_glass_bg + "\n  " + strong_border + "\n  border-radius: 32px;\n  box-shadow: 0 10px 40px rgba(0,0,0,0.2);"
)

# Fix hero block overall layout to respect the border radius
text = text.replace(
    ".hero-left {\n",
    ".hero-left {\n  margin-right: 10px;\n"
).replace(
    ".hero-right {\n",
    ".hero-right {\n  margin-left: 10px;\n"
)

# Other elements
text = text.replace("background: rgba(255, 255, 255, 0.05);", "background: rgba(255, 255, 255, 0.08);")
text = text.replace("border: 1px solid rgba(255, 255, 255, 0.1);", "border: 1px solid rgba(255, 255, 255, 0.2);")
text = text.replace("border: 1px solid rgba(245,245,220,0.1);", "border: 1px solid rgba(255, 255, 255, 0.2);")
text = text.replace("border: 1px solid rgba(245,245,220,0.06);", "border: 1px solid rgba(255, 255, 255, 0.2);")

# Enhance general glass feel
text = text.replace("backdrop-filter: blur(16px);", "backdrop-filter: blur(24px); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);")
text = text.replace("-webkit-backdrop-filter: blur(16px);", "-webkit-backdrop-filter: blur(24px);")

# Remove repeating-linear gradient in hero-right::before to make it pure clean glass
text = re.sub(r'\.hero-right::before\s*\{[\s\S]*?\}', '', text)

with open("style.css", "w") as f:
    f.write(text)

print("Glass enhanced")
