import subprocess
import os
import shutil
from PIL import Image

WORKSPACE_DIR = r"C:\Users\admin\Documents\Github\portfolio-cv"
PUBLIC_DIR = os.path.join(WORKSPACE_DIR, "public", "linkedin-banners")
BRAIN_PARENT = r"C:\Users\admin\.gemini\antigravity-cli\brain\bad2105d-0e07-4e8f-82d3-2974867f09a3"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

os.makedirs(PUBLIC_DIR, exist_ok=True)
os.makedirs(BRAIN_PARENT, exist_ok=True)

# -------------------------------------------------------------
# TEMPLATE 1: Variante en Español (Directa, sin humo, sin párrafos)
# -------------------------------------------------------------
html_variant_1 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variante 1 (ES)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #06080d;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    display: flex;
    background-image: 
      radial-gradient(circle at 80% 25%, rgba(14, 165, 233, 0.08) 0%, transparent 55%),
      radial-gradient(circle at 95% 85%, rgba(99, 102, 241, 0.06) 0%, transparent 50%),
      linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
  }

  /* Safe zone for LinkedIn circular profile picture (left 420px) */
  .safe-zone {
    width: 420px;
    height: 100%;
    position: relative;
    border-right: 1px solid rgba(255, 255, 255, 0.04);
  }

  /* Main content right */
  .content-zone {
    flex: 1;
    padding: 56px 64px 56px 56px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 28px;
    position: relative;
  }

  .header-block {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  h1.name {
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff;
    line-height: 1.1;
  }

  .role-title {
    font-size: 20px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: 0.01em;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .role-separator {
    color: #334155;
    font-weight: 300;
  }

  .role-sub {
    color: #94a3b8;
    font-weight: 400;
  }

  /* 3 Clean Focus Badges */
  .badges-row {
    display: flex;
    gap: 12px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    color: #e2e8f0;
    letter-spacing: 0.01em;
    backdrop-filter: blur(10px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 13px;
  }

  /* Bottom Stack bar */
  .footer-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-top: 18px;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #64748b;
  }

  .stack-label {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 600;
    color: #475569;
  }

  .stack-items {
    color: #94a3b8;
    letter-spacing: 0.05em;
  }
</style>
</head>
<body>
  <div class="safe-zone"></div>
  <div class="content-zone">
    <div class="header-block">
      <h1 class="name">Jorge Tricarico</h1>
      <div class="role-title">
        <span>AI Engineer</span>
        <span class="role-separator">|</span>
        <span class="role-sub">QA Automation &amp; Agentic Systems</span>
      </div>
    </div>

    <div class="badges-row">
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Agentes de IA para Calidad</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Frameworks de Testing (Web • Mobile • API)</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Auditoría &amp; Evaluación de LLMs</span>
      </div>
    </div>

    <div class="footer-row">
      <span class="stack-label">Core Stack</span>
      <span>•</span>
      <span class="stack-items">Python · LangGraph · Playwright · Docker · CI/CD</span>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 2: Variante en Inglés (Global Tech Edition)
# -------------------------------------------------------------
html_variant_2 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Banner Variant 2 (EN)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #06080d;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    display: flex;
    background-image: 
      radial-gradient(circle at 80% 25%, rgba(14, 165, 233, 0.08) 0%, transparent 55%),
      radial-gradient(circle at 95% 85%, rgba(99, 102, 241, 0.06) 0%, transparent 50%),
      linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
  }

  .safe-zone {
    width: 420px;
    height: 100%;
    position: relative;
    border-right: 1px solid rgba(255, 255, 255, 0.04);
  }

  .content-zone {
    flex: 1;
    padding: 56px 64px 56px 56px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 28px;
    position: relative;
  }

  .header-block {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  h1.name {
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff;
    line-height: 1.1;
  }

  .role-title {
    font-size: 20px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: 0.01em;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .role-separator {
    color: #334155;
    font-weight: 300;
  }

  .role-sub {
    color: #94a3b8;
    font-weight: 400;
  }

  .badges-row {
    display: flex;
    gap: 12px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    color: #e2e8f0;
    letter-spacing: 0.01em;
    backdrop-filter: blur(10px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 13px;
  }

  .footer-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-top: 18px;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #64748b;
  }

  .stack-label {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 600;
    color: #475569;
  }

  .stack-items {
    color: #94a3b8;
    letter-spacing: 0.05em;
  }
</style>
</head>
<body>
  <div class="safe-zone"></div>
  <div class="content-zone">
    <div class="header-block">
      <h1 class="name">Jorge Tricarico</h1>
      <div class="role-title">
        <span>AI Engineer</span>
        <span class="role-separator">|</span>
        <span class="role-sub">QA Automation &amp; Agentic Systems</span>
      </div>
    </div>

    <div class="badges-row">
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>AI Agents for Quality Engineering</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Test Automation (Web • Mobile • API)</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>LLM Evals &amp; Governance</span>
      </div>
    </div>

    <div class="footer-row">
      <span class="stack-label">Core Stack</span>
      <span>•</span>
      <span class="stack-items">Python · LangGraph · Playwright · Docker · CI/CD</span>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 3: Variante Ultra-Minimalista (Sobria, estilo Vercel / Linear)
# -------------------------------------------------------------
html_variant_3 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variant 3 (Minimal)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #040508;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    display: flex;
    background-image: 
      radial-gradient(circle at 90% 40%, rgba(255, 255, 255, 0.04) 0%, transparent 60%);
  }

  .safe-zone {
    width: 440px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 64px 72px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 22px;
    position: relative;
  }

  .top-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #38bdf8;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    font-weight: 500;
  }

  h1.name {
    font-size: 44px;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #ffffff;
    line-height: 1;
  }

  .subtitle {
    font-size: 19px;
    color: #94a3b8;
    font-weight: 400;
    letter-spacing: 0.01em;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .dot {
    color: #334155;
  }

  .divider-line {
    width: 100%;
    height: 1px;
    background: linear-gradient(to right, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.02));
    margin-top: 6px;
  }

  .tags-row {
    display: flex;
    align-items: center;
    gap: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #64748b;
  }

  .tags-row span.active {
    color: #cbd5e1;
  }
</style>
</head>
<body>
  <div class="safe-zone"></div>
  <div class="content-zone">
    <span class="top-label">AI Engineer &bull; QA Automation</span>
    <h1 class="name">Jorge Tricarico</h1>
    <div class="subtitle">
      <span>Agentes de Calidad</span>
      <span class="dot">&bull;</span>
      <span>Frameworks de Testing</span>
      <span class="dot">&bull;</span>
      <span>Evaluación de LLMs</span>
    </div>
    <div class="divider-line"></div>
    <div class="tags-row">
      <span class="active">Python</span>
      <span>/</span>
      <span class="active">LangGraph</span>
      <span>/</span>
      <span class="active">Playwright</span>
      <span>/</span>
      <span class="active">CI/CD Pipelines</span>
    </div>
  </div>
</body>
</html>
"""

configs = [
    ("linkedin-banner-clean-es.png", "temp_es.html", html_variant_1, "Variante 1: Español Directa"),
    ("linkedin-banner-clean-en.png", "temp_en.html", html_variant_2, "Variante 2: English Global Tech"),
    ("linkedin-banner-clean-minimal.png", "temp_min.html", html_variant_3, "Variante 3: Ultra Minimalista Vercel Style")
]

for img_name, html_name, html_content, label in configs:
    temp_html = os.path.join(WORKSPACE_DIR, html_name)
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    temp_img = os.path.join(WORKSPACE_DIR, img_name)
    cmd = [
        CHROME_PATH,
        "--headless=new",
        f"--screenshot={temp_img}",
        "--window-size=1584,396",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        temp_html
    ]
    print(f"Rendering {label}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error: {res.stderr}")
    else:
        # Copy to public/linkedin-banners/
        dest_pub = os.path.join(PUBLIC_DIR, img_name)
        shutil.copy2(temp_img, dest_pub)
        
        # Copy to brain
        dest_brain = os.path.join(BRAIN_PARENT, img_name)
        shutil.copy2(temp_img, dest_brain)
        print(f"Generated: {dest_pub}")
        
    if os.path.exists(temp_html):
        os.remove(temp_html)
    if os.path.exists(temp_img):
        os.remove(temp_img)

print("Finished rendering all clean banners!")
