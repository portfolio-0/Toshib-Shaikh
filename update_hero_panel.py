import re

with open("style.css", "r") as f:
    css = f.read()

# Replace the #hero block
hero_block = """#hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 100px;
  padding-bottom: 60px;
}

.hero-glass-panel {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  max-width: 1200px;
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 10px 40px rgba(0,0,0,0.3);
  border-radius: 32px;
  position: relative;
  overflow: hidden;
}"""

css = re.sub(
    r'#hero\s*\{\n\s*min-height:\s*100vh;\n\s*display:\s*grid;\n\s*grid-template-columns:\s*1fr\s*1fr;\n\s*padding-top:\s*80px;\n\}',
    hero_block,
    css
)

# Replace .hero-left block
hero_left_block = """.hero-left {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px 70px;
  position: relative;
  z-index: 2;
}"""

# Notice that the regex matches the OLD hero-left that I just generated earlier in rebuild_glass.py
css = re.sub(
    r'\.hero-left\s*\{\n\s*margin-right:\s*10px;\n\s*background:\s*rgba\(0,\s*0,\s*0,\s*0\.25\);\n\s*backdrop-filter:\s*blur\(20px\);\n\s*-webkit-backdrop-filter:\s*blur\(20px\);\n\s*border:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.1\);\n\s*box-shadow:\s*0\s*10px\s*40px\s*rgba\(0,0,0,0\.3\);\n\s*display:\s*flex;\n\s*flex-direction:\s*column;\n\s*justify-content:\s*center;\n\s*padding:\s*80px\s*70px;\n\s*border-radius:\s*32px;\n\s*position:\s*relative;\n\s*overflow:\s*hidden;\n\}',
    hero_left_block,
    css
)

with open("style.css", "w") as f:
    f.write(css)

print("Hero panel styles updated.")
