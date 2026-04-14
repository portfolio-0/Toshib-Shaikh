with open("style.css", "r") as f:
    text = f.read()

# .hero-left
text = text.replace(
    "background: linear-gradient(160deg, var(--green-dark) 0%, var(--green) 55%, var(--green-light) 100%);",
    "background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border: 1px solid rgba(255, 255, 255, 0.1);"
)

# #services
text = text.replace(
    "background: linear-gradient(170deg, var(--cream) 0%, #ededcc 100%);",
    "background: transparent;"
)

# .service-card
text = text.replace(
    "background: linear-gradient(145deg, var(--green) 0%, var(--green-mid) 100%);",
    "background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);"
)

# .service-card:hover
text = text.replace(
    "background: linear-gradient(145deg, var(--green-light) 0%, var(--green) 100%);",
    "background: rgba(255, 255, 255, 0.1);"
)

# #showcase
text = text.replace(
    "background: linear-gradient(155deg, var(--green-dark) 0%, var(--green) 50%, var(--green-mid) 100%);",
    "background: transparent;"
)

# #tools
text = text.replace(
    "background: linear-gradient(170deg, #ededcc 0%, var(--cream) 100%);",
    "background: transparent;"
)

# .tool-row
text = text.replace(
    "background: linear-gradient(135deg, var(--green) 0%, var(--green-mid) 100%);",
    "background: rgba(255, 255, 255, 0.05);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);"
)

# .tool-row:hover
text = text.replace(
    "background: linear-gradient(135deg, var(--green-light) 0%, var(--green) 100%);",
    "background: rgba(255, 255, 255, 0.1);"
)

# #clients
text = text.replace(
    "background: linear-gradient(155deg, var(--green-dark) 0%, var(--green) 55%, var(--green-mid) 100%);",
    "background: transparent;"
)

# #cta
text = text.replace(
    "background: linear-gradient(160deg, var(--green) 0%, var(--green-mid) 60%, var(--green-dark) 100%);",
    "background: transparent;"
)

with open("style.css", "w") as f:
    f.write(text)

print("Exact replacements done!")
