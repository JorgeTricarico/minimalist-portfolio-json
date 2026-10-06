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
# TEMPLATE 1: Name + Role Power Header (ES - Proporciones Reales LinkedIn)
# -------------------------------------------------------------
html_variant_1 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variante 1 (ES - True LinkedIn Proportions)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
      radial-gradient(circle at 80% 25%, rgba(14, 165, 233, 0.12) 0%, transparent 60%),
      radial-gradient(circle at 95% 85%, rgba(99, 102, 241, 0.09) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
  }

  /* Safe zone for LinkedIn circular profile photo (left 340px) */
  .safe-zone {
    width: 340px;
    height: 100%;
    position: relative;
  }

  /* Main content right */
  .content-zone {
    flex: 1;
    padding: 40px 60px 40px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 20px;
    position: relative;
  }

  .header-block {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  h1.name {
    font-size: 80px;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: #ffffff;
    line-height: 1.0;
  }

  .role-title {
    font-size: 34px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .role-separator {
    color: #334155;
    font-weight: 300;
  }

  .role-sub {
    color: #94a3b8;
    font-weight: 400;
  }

  /* 3 Prominent Focus Badges */
  .badges-row {
    display: flex;
    gap: 16px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 14px 26px;
    border-radius: 12px;
    font-size: 23px;
    font-weight: 600;
    color: #f8fafc;
    letter-spacing: 0.01em;
    backdrop-filter: blur(14px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 20px;
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
        <span class="role-sub">Sistemas Agénticos &amp; Arquitectura</span>
      </div>
    </div>

    <div class="badges-row">
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Sistemas Agénticos</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Automatización a Escala</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Auditoría &amp; Evaluación</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 2: AI Engineer Role-Driven Hero (Grandes Proporciones ES)
# -------------------------------------------------------------
html_variant_2 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variante 2 (Role Hero ES)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #05070c;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    display: flex;
    background-image: 
      radial-gradient(circle at 75% 30%, rgba(56, 189, 248, 0.12) 0%, transparent 60%),
      radial-gradient(circle at 20% 80%, rgba(99, 102, 241, 0.08) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.018) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
  }

  .safe-zone {
    width: 340px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 38px 60px 38px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 22px;
    position: relative;
  }

  .top-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    color: #38bdf8;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    font-weight: 700;
  }

  h1.name {
    font-size: 78px;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: #ffffff;
    line-height: 1.0;
  }

  .badges-row {
    display: flex;
    gap: 16px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(56, 189, 248, 0.25);
    padding: 15px 30px;
    border-radius: 12px;
    font-size: 24px;
    font-weight: 600;
    color: #f1f5f9;
    letter-spacing: 0.01em;
    backdrop-filter: blur(14px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 20px;
  }
</style>
</head>
<body>
  <div class="safe-zone"></div>
  <div class="content-zone">
    <div class="top-label">AI Engineer · Sistemas Agénticos &amp; Arquitectura</div>
    <h1 class="name">Jorge Tricarico</h1>

    <div class="badges-row">
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Sistemas Agénticos &amp; Orquestación</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Auditoría Técnica &amp; Evaluación</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 3: Obsidian Cyber Terminal (ES - Escala Real Proporcional)
# -------------------------------------------------------------
html_variant_3 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variant 3 (Obsidian Cyber Proportional)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #07090e;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f1f5f9;
    position: relative;
    display: flex;
    background-image: 
      radial-gradient(circle at 82% 20%, rgba(16, 185, 129, 0.10) 0%, transparent 55%),
      radial-gradient(circle at 92% 80%, rgba(14, 165, 233, 0.09) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.018) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
  }

  .safe-zone {
    width: 340px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 36px 60px 36px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 16px;
  }

  .terminal-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 18px;
    color: #10b981;
    letter-spacing: 0.08em;
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 600;
  }

  .terminal-dot {
    width: 10px;
    height: 10px;
    background-color: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 12px #10b981;
  }

  .header-block {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  h1.name {
    font-size: 76px;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: #ffffff;
    line-height: 1.0;
  }

  .role-title {
    font-size: 32px;
    font-weight: 600;
    color: #38bdf8;
    display: flex;
    align-items: center;
    gap: 16px;
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
    gap: 16px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 14px 26px;
    border-radius: 12px;
    font-size: 22px;
    font-weight: 600;
    color: #f1f5f9;
    white-space: nowrap;
  }

  .badge-item .spark {
    color: #10b981;
    font-size: 19px;
  }
</style>
</head>
<body>
  <div class="safe-zone"></div>
  <div class="content-zone">
    <div class="terminal-tag">
      <span class="terminal-dot"></span>
      <span>agentic_systems // evaluation &amp; technical_audits</span>
    </div>

    <div class="header-block">
      <h1 class="name">Jorge Tricarico</h1>
      <div class="role-title">
        <span>AI Engineer</span>
        <span class="role-separator">|</span>
        <span class="role-sub">Arquitectura de Agentes &amp; Automatización</span>
      </div>
    </div>

    <div class="badges-row">
      <div class="badge-item">
        <span class="spark">⚡</span>
        <span>Sistemas Agénticos</span>
      </div>
      <div class="badge-item">
        <span class="spark">⚡</span>
        <span>Auditoría &amp; Evaluación</span>
      </div>
      <div class="badge-item">
        <span class="spark">⚡</span>
        <span>Automatización &amp; CI/CD</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 4: Ultra-Minimal Linear/Vercel (Grandes Proporciones)
# -------------------------------------------------------------
html_variant_4 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variant 4 (Minimal Bold Proportional)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #030407;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #ffffff;
    display: flex;
    position: relative;
    background-image: 
      radial-gradient(circle at 85% 30%, rgba(255, 255, 255, 0.08) 0%, transparent 60%);
  }

  .safe-zone {
    width: 340px;
    height: 100%;
  }

  .content-zone {
    flex: 1;
    padding: 44px 60px 44px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 22px;
  }

  .tagline-pre {
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    color: #64748b;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    font-weight: 700;
  }

  h1.name {
    font-size: 84px;
    font-weight: 900;
    letter-spacing: -0.04em;
    line-height: 1.0;
    color: #ffffff;
  }

  .headline {
    font-size: 34px;
    font-weight: 400;
    color: #94a3b8;
    letter-spacing: -0.01em;
  }

  .headline strong {
    color: #38bdf8;
    font-weight: 700;
  }

  .divider-line {
    width: 100%;
    height: 1px;
    background: rgba(255, 255, 255, 0.12);
  }

  .tags-row {
    display: flex;
    align-items: center;
    gap: 22px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 22px;
    color: #64748b;
    font-weight: 600;
  }

  .tags-row span.active {
    color: #e2e8f0;
  }
</style>
</head>
<body>
  <div class="safe-zone"></div>
  <div class="content-zone">
    <div class="tagline-pre">Agentic Systems &amp; Software Architecture</div>
    <h1 class="name">Jorge Tricarico</h1>
    <div class="headline">
      <strong>AI Engineer</strong> · Sistemas Agénticos &amp; Auditoría de Agentes
    </div>
    <div class="divider-line"></div>
    <div class="tags-row">
      <span class="active">Python</span>
      <span>/</span>
      <span class="active">LangGraph</span>
      <span>/</span>
      <span class="active">AI Agents</span>
      <span>/</span>
      <span class="active">Auditoría Técnica</span>
      <span>/</span>
      <span class="active">Playwright</span>
      <span>/</span>
      <span class="active">CI/CD</span>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 5: AI Engineer Global Tech (EN - True LinkedIn Proportions)
# -------------------------------------------------------------
html_variant_5 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Banner Variant 5 (Global Tech EN)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
      radial-gradient(circle at 80% 25%, rgba(14, 165, 233, 0.12) 0%, transparent 60%),
      radial-gradient(circle at 95% 85%, rgba(99, 102, 241, 0.09) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
  }

  .safe-zone {
    width: 340px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 40px 60px 40px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 20px;
    position: relative;
  }

  .header-block {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  h1.name {
    font-size: 80px;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: #ffffff;
    line-height: 1.0;
  }

  .role-title {
    font-size: 34px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 16px;
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
    gap: 16px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 14px 26px;
    border-radius: 12px;
    font-size: 23px;
    font-weight: 600;
    color: #f8fafc;
    letter-spacing: 0.01em;
    backdrop-filter: blur(14px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 20px;
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
        <span class="role-sub">Agentic Systems &amp; Software Architecture</span>
      </div>
    </div>

    <div class="badges-row">
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Multi-Agent Architectures</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Software Automation</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Agent Auditing &amp; Evals</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 6: Midnight Executive (EN - True LinkedIn Proportions)
# -------------------------------------------------------------
html_variant_6 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Banner Variant 6 (Executive EN)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #020617;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    display: flex;
    background-image: 
      radial-gradient(circle at 85% 25%, rgba(56, 189, 248, 0.14) 0%, transparent 60%),
      radial-gradient(circle at 95% 85%, rgba(129, 140, 248, 0.10) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.018) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
  }

  .safe-zone {
    width: 340px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 38px 60px 38px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 22px;
    position: relative;
  }

  .top-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    color: #38bdf8;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    font-weight: 700;
  }

  h1.name {
    font-size: 80px;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: #ffffff;
    line-height: 1.0;
  }

  .badges-row {
    display: flex;
    gap: 16px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 15px 30px;
    border-radius: 12px;
    font-size: 24px;
    font-weight: 600;
    color: #f1f5f9;
    letter-spacing: 0.01em;
    backdrop-filter: blur(14px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 20px;
  }
</style>
</head>
<body>
  <div class="safe-zone"></div>
  <div class="content-zone">
    <div class="top-label">AI Engineer · Agentic Systems &amp; Software Architecture</div>
    <h1 class="name">Jorge Tricarico</h1>

    <div class="badges-row">
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Enterprise Agent Workflows</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Agent Auditing &amp; Evaluation Frameworks</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

configs = [
    ("linkedin-banner-clean-es.png", "temp_es.html", html_variant_1, "Variante 1: AI Engineer Integral (ES - Proporcional)"),
    ("linkedin-banner-clean-platform.png", "temp_plat.html", html_variant_2, "Variante 2: Hero Role Driven (ES - Proporcional)"),
    ("linkedin-banner-obsidian-cyber.png", "temp_cyber.html", html_variant_3, "Variante 3: Obsidian Cyber Terminal (ES - Proporcional)"),
    ("linkedin-banner-clean-minimal.png", "temp_min.html", html_variant_4, "Variante 4: Minimal Bold Linear (ES - Proporcional)"),
    ("linkedin-banner-clean-en.png", "temp_en.html", html_variant_5, "Variante 5: Global Tech (EN - Proporcional)"),
    ("linkedin-banner-midnight-exec.png", "temp_exec.html", html_variant_6, "Variante 6: Midnight Executive (EN - Proporcional)")
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

print("Finished rendering all true LinkedIn proportion banners!")
