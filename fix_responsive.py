import re

with open("style.css", "r") as f:
    css = f.read()

# Make hero side-by-side even at 900px
css = css.replace(
    ".hero-glass-panel { grid-template-columns: 1fr; border-radius: 20px; margin: 0 16px; }",
    ".hero-glass-panel { border-radius: 20px; margin: 0 16px; }  /* intentionally keep grid-template-columns: 1fr 1fr; untouched at 900px so they remain side-by-side */"
)

# However, on tiny mobile devices, it MUST stack, otherwise it breaks entirely
# So let's insert it into the 560px query.
css = css.replace(
    "@media (max-width: 560px) {",
    "@media (max-width: 560px) {\n  .hero-glass-panel { grid-template-columns: 1fr; flex-direction: column; }"
)

with open("style.css", "w") as f:
    f.write(css)
