import re

# 1. Update index.html for Video Showcase
with open("index.html", "r") as f:
    html = f.read()

showcase_replacement = """    <div class="video-grid video-grid-top" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
      <div class="video-placeholder reveal" style="padding: 0; display: block; overflow: hidden;">
        <video src="intro bsr .mp4" controls preload="metadata" style="width: 100%; height: 100%; object-fit: cover;"></video>
        <div class="video-label">Coach BSR Intro</div>
      </div>
      <div class="video-placeholder reveal" style="padding: 0; display: block; overflow: hidden;">
        <video src="intro chitresh sir .mp4" controls preload="metadata" style="width: 100%; height: 100%; object-fit: cover;"></video>
        <div class="video-label">Intro Chitresh Sir</div>
      </div>
    </div>

    <div class="video-grid video-grid-bottom" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;">
      <a href="https://youtu.be/81o1W-Tavi4?si=XiEl5JN5Mvs0UASx" target="_blank" class="video-placeholder reveal" style="padding: 0; display: block; overflow: hidden; text-decoration: none;">
        <img src="https://img.youtube.com/vi/81o1W-Tavi4/hqdefault.jpg" style="width: 100%; height: 100%; object-fit: cover;" />
        <div class="play-btn" style="position: absolute; top: 50%; left: 50%; margin: -27px 0 0 -27px; z-index: 2;">
          <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
        </div>
        <div class="video-label">Abhishek Kar Podcast</div>
      </a>
      
      <a href="https://youtube.com/shorts/jWPcr5evZ18?si=0eMpewU6nlNtrWxi" target="_blank" class="video-placeholder reveal" style="padding: 0; display: block; overflow: hidden; text-decoration: none;">
        <img src="https://img.youtube.com/vi/jWPcr5evZ18/hqdefault.jpg" style="width: 100%; height: 100%; object-fit: cover;" />
        <div class="play-btn" style="position: absolute; top: 50%; left: 50%; margin: -27px 0 0 -27px; z-index: 2;">
          <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
        </div>
        <div class="video-label">Deepak Daiya</div>
      </a>

      <a href="https://www.instagram.com/reel/DUlFeMIiTNd/?igsh=MWJrN2l4NTV4YjMwaQ==" target="_blank" class="video-placeholder reveal" style="padding: 0; display: block; overflow: hidden; text-decoration: none;">
        <img src="anurag rishi.png" style="width: 100%; height: 100%; object-fit: cover;" />
        <div class="play-btn" style="position: absolute; top: 50%; left: 50%; margin: -27px 0 0 -27px; z-index: 2;">
          <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
        </div>
        <div class="video-label">Anurag Rishi Reel</div>
      </a>
    </div>"""

# Safely replace the old .video-grid
html = re.sub(r'<div class="video-grid">[\s\S]*?</div>\s*</section>', showcase_replacement + '\n  </section>', html)

with open("index.html", "w") as f:
    f.write(html)

# 2. Update style.css for Clients Grid layout
with open("style.css", "r") as f:
    css = f.read()

# Make clients grid 2 columns
css = re.sub(
    r'\.clients-grid\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*repeat\(3,\s*1fr\);\s*gap:\s*14px;\s*\}',
    r'.clients-grid {\n  display: grid;\n  grid-template-columns: repeat(2, 1fr);\n  gap: 20px;\n}',
    css
)

# Make client card horizontal
css = re.sub(
    r'\.client-card\s*\{[\s\S]*?flex-direction:\s*column;\s*gap:\s*14px;',
    r'''.client-card {
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  border-radius: 18px;
  padding: 28px 24px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 24px;''',
    css
)

# Make avatar large, grayscale
css = re.sub(
    r'\.client-avatar\s*\{[\s\S]*?width:\s*46px;\s*height:\s*46px;',
    r'''.client-avatar {
  width: 90px; height: 90px;
  filter: grayscale(100%);
  flex-shrink: 0;''',
    css
)

# Responsive fixes
css = css.replace(
    ".clients-grid { grid-template-columns: 1fr 1fr; }",
    ".clients-grid { grid-template-columns: 1fr; }"
)
css = css.replace(
    "@media (max-width: 900px) {\n",
    "@media (max-width: 900px) {\n  .video-grid-top { grid-template-columns: 1fr !important; } \n  .video-grid-bottom { grid-template-columns: 1fr !important; }\n"
)


with open("style.css", "w") as f:
    f.write(css)

print("Updated Showcase videos and Clients layout!")
