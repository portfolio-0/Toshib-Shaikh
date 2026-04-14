import re

with open("index.html", "r") as f:
    html = f.read()

# Replace client avatars with images
html = html.replace(
    '<div class="client-avatar">AR</div>',
    '<img src="anurag rishi.png" class="client-avatar" alt="Anurag Rishi" style="object-fit: cover; padding: 0;" />'
)

html = html.replace(
    '<div class="client-avatar">AK</div>',
    '<img src="Abhishek kar.png" class="client-avatar" alt="Abhishek Kar" style="object-fit: cover; padding: 0;" />'
)

html = html.replace(
    '<div class="client-avatar">CB</div>',
    '<img src="coach bsr.png" class="client-avatar" alt="Coach BSR" style="object-fit: cover; padding: 0;" />'
)

html = html.replace(
    '<div class="client-avatar">CS</div>',
    '<img src="chitresh soni.png" class="client-avatar" alt="Chitresh Soni" style="object-fit: cover; padding: 0;" />'
)

html = html.replace(
    '<div class="client-avatar">SO</div>',
    '<img src="seekho.webp" class="client-avatar" alt="Seekho" style="object-fit: cover; padding: 0;" />'
)

# Featured client background (Deepak Daiya)
html = html.replace(
    '<div class="client-featured reveal">',
    '''<!-- Added background style for Deepak Daiya per user request -->
    <div class="client-featured reveal" style="background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('deepak daiya.jpg') center/cover; background-blend-mode: luminosity; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5); border: 1px solid rgba(255, 255, 255, 0.1);">'''
)

# Change DD to also be his image or just remove cf-avatar.
# Actually I'll leave the cf-avatar as it is, or change it to his image.
html = html.replace(
    '<div class="cf-avatar">DD</div>',
    '<img src="deepak daiya.jpg" class="cf-avatar" alt="Deepak Daiya" style="object-fit: cover; filter: grayscale(100%); padding: 0;" />'
)

with open("index.html", "w") as f:
    f.write(html)
