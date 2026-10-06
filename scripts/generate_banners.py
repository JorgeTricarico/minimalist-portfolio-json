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
# TEMPLATE 1: Variante en Español (AI Engineer Integral - Grande & Legible)
# -------------------------------------------------------------
html_variant_1 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variante 1 (ES - Large)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
      radial-gradient(circle at 80% 25%, rgba(14, 165, 233, 0.10) 0%, transparent 60%),
      radial-gradient(circle at 95% 85%, rgba(99, 102, 241, 0.08) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
  }

  /* Safe zone for LinkedIn circular profile picture (left 330px) */
  .safe-zone {
    width: 330px;
    height: 100%;
    position: relative;
  }

  /* Main content right */
  .content-zone {
    flex: 1;
    padding: 44px 56px 44px 20px;
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
    font-size: 60px;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #ffffff;
    line-height: 1.05;
  }

  .role-title {
    font-size: 26px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .role-separator {
    color: #334155;
    font-weight: 300;
  }

  .role-sub {
    color: #94a3b8;
    font-weight: 400;
  }

  /* Focus Badges */
  .badges-row {
    display: flex;
    gap: 14px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.10);
    padding: 12px 22px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 600;
    color: #f1f5f9;
    letter-spacing: 0.01em;
    backdrop-filter: blur(12px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 15px;
  }

  /* Bottom Stack bar */
  .footer-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    color: #64748b;
  }

  .stack-label {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 700;
    color: #475569;
  }

  .stack-items {
    color: #cbd5e1;
    letter-spacing: 0.03em;
    font-weight: 500;
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
        <span>Sistemas Agénticos &amp; Multi-Agente</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Automatización &amp; Plataformas</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Auditoría &amp; Evaluación de Agentes</span>
      </div>
    </div>

    <div class="footer-row">
      <span class="stack-label">Core Stack</span>
      <span>•</span>
      <span class="stack-items">Python · LangGraph · AI Agents · Playwright · Docker · CI/CD</span>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 2: Variante en Inglés (AI Engineer Global Tech - Large)
# -------------------------------------------------------------
html_variant_2 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Banner Variant 2 (EN - Large)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
      radial-gradient(circle at 80% 25%, rgba(14, 165, 233, 0.10) 0%, transparent 60%),
      radial-gradient(circle at 95% 85%, rgba(99, 102, 241, 0.08) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
  }

  .safe-zone {
    width: 330px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 44px 56px 44px 20px;
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
    font-size: 60px;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #ffffff;
    line-height: 1.05;
  }

  .role-title {
    font-size: 26px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 14px;
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
    gap: 14px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.10);
    padding: 12px 22px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 600;
    color: #f1f5f9;
    letter-spacing: 0.01em;
    backdrop-filter: blur(12px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 15px;
  }

  .footer-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    color: #64748b;
  }

  .stack-label {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 700;
    color: #475569;
  }

  .stack-items {
    color: #cbd5e1;
    letter-spacing: 0.03em;
    font-weight: 500;
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
        <span>Software Automation &amp; Scale</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Agent Audits &amp; Evaluations</span>
      </div>
    </div>

    <div class="footer-row">
      <span class="stack-label">Core Stack</span>
      <span>•</span>
      <span class="stack-items">Python · LangGraph · AI Agents · Playwright · Docker · CI/CD</span>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 3: Variante Obsidian Cyber Terminal (ES - Scaled UP)
# -------------------------------------------------------------
html_variant_3 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variant 3 (Obsidian Cyber Scaled)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
      radial-gradient(circle at 82% 20%, rgba(16, 185, 129, 0.09) 0%, transparent 55%),
      radial-gradient(circle at 92% 80%, rgba(14, 165, 233, 0.08) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.018) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 32px 32px, 32px 32px;
  }

  .safe-zone {
    width: 330px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 40px 56px 40px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 18px;
  }

  .terminal-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: #10b981;
    letter-spacing: 0.08em;
    display: flex;
    align-items: center;
    gap: 9px;
  }

  .terminal-dot {
    width: 8px;
    height: 8px;
    background-color: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 10px #10b981;
  }

  .header-block {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  h1.name {
    font-size: 60px;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #ffffff;
    line-height: 1.05;
  }

  .role-title {
    font-size: 26px;
    font-weight: 600;
    color: #38bdf8;
    display: flex;
    align-items: center;
    gap: 14px;
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
    gap: 14px;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.10);
    padding: 12px 22px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 600;
    color: #f1f5f9;
  }

  .badge-item .spark {
    color: #10b981;
    font-size: 15px;
  }

  .footer-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    color: #64748b;
  }

  .stack-label {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 700;
    color: #475569;
  }

  .stack-items {
    color: #cbd5e1;
    letter-spacing: 0.03em;
    font-weight: 500;
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
        <span>Sistemas Agénticos &amp; Orquestación</span>
      </div>
      <div class="badge-item">
        <span class="spark">⚡</span>
        <span>Auditoría &amp; Evaluación de Agentes</span>
      </div>
      <div class="badge-item">
        <span class="spark">⚡</span>
        <span>Automatización &amp; CI/CD</span>
      </div>
    </div>

    <div class="footer-row">
      <span class="stack-label">Stack</span>
      <span>•</span>
      <span class="stack-items">Python · LangGraph · AI Agents · Playwright · Docker · CI/CD</span>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 4: Variante Simplificada (2 Badges Grandes de Alto Impacto)
# -------------------------------------------------------------
html_variant_4 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variant 4 (High Impact 2 Badges)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
      radial-gradient(circle at 75% 30%, rgba(56, 189, 248, 0.10) 0%, transparent 60%),
      radial-gradient(circle at 20% 80%, rgba(99, 102, 241, 0.06) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.018) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
  }

  .safe-zone {
    width: 330px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 44px 56px 44px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 22px;
    position: relative;
  }

  .header-block {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  h1.name {
    font-size: 64px;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #ffffff;
    line-height: 1.05;
  }

  .role-title {
    font-size: 28px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 14px;
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
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(56, 189, 248, 0.20);
    padding: 14px 26px;
    border-radius: 10px;
    font-size: 19px;
    font-weight: 600;
    color: #f1f5f9;
    letter-spacing: 0.01em;
    backdrop-filter: blur(14px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 17px;
  }

  .footer-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    color: #64748b;
  }

  .stack-label {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 700;
    color: #475569;
  }

  .stack-items {
    color: #cbd5e1;
    letter-spacing: 0.04em;
    font-weight: 500;
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
        <span class="role-sub">Agentes de IA &amp; Arquitectura de Software</span>
      </div>
    </div>

    <div class="badges-row">
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Sistemas Agénticos &amp; Orquestación</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Auditoría Técnica &amp; Evaluación de Agentes</span>
      </div>
    </div>

    <div class="footer-row">
      <span class="stack-label">Ecosistema</span>
      <span>•</span>
      <span class="stack-items">Python · LangGraph · AI Agents · Playwright · Docker · CI/CD</span>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# TEMPLATE 5: Variante Ultra-Minimal Linear / Vercel (Bold Large)
# -------------------------------------------------------------
html_variant_5 = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Banner Variant 5 (Minimal Bold)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
      radial-gradient(circle at 85% 30%, rgba(255, 255, 255, 0.06) 0%, transparent 60%);
  }

  .safe-zone {
    width: 330px;
    height: 100%;
  }

  .content-zone {
    flex: 1;
    padding: 50px 60px 50px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 20px;
  }

  .tagline-pre {
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    color: #64748b;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    font-weight: 600;
  }

  h1.name {
    font-size: 64px;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.05;
    color: #ffffff;
  }

  .headline {
    font-size: 26px;
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
    background: rgba(255, 255, 255, 0.10);
    margin: 4px 0;
  }

  .tags-row {
    display: flex;
    align-items: center;
    gap: 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 17px;
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
      <span class="active">Agent Audits</span>
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
# TEMPLATE 6: Variante Midnight Executive (EN - Large & Punchy)
# -------------------------------------------------------------
html_variant_6 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Banner Variant 6 (Executive EN - Large)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
      radial-gradient(circle at 85% 25%, rgba(56, 189, 248, 0.11) 0%, transparent 60%),
      radial-gradient(circle at 95% 85%, rgba(129, 140, 248, 0.09) 0%, transparent 55%),
      linear-gradient(to right, rgba(255, 255, 255, 0.018) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
  }

  .safe-zone {
    width: 330px;
    height: 100%;
    position: relative;
  }

  .content-zone {
    flex: 1;
    padding: 44px 56px 44px 20px;
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
    font-size: 60px;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #ffffff;
    line-height: 1.05;
  }

  .role-title {
    font-size: 26px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 14px;
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
    gap: 14px;
    flex-wrap: nowrap;
  }

  .badge-item {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.10);
    padding: 12px 22px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 600;
    color: #f1f5f9;
    letter-spacing: 0.01em;
    backdrop-filter: blur(12px);
  }

  .badge-item .spark {
    color: #38bdf8;
    font-size: 15px;
  }

  .footer-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    color: #64748b;
  }

  .stack-label {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 700;
    color: #475569;
  }

  .stack-items {
    color: #cbd5e1;
    letter-spacing: 0.03em;
    font-weight: 500;
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
        <span>Enterprise Agent Workflows</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Software Automation &amp; Scale</span>
      </div>
      <div class="badge-item">
        <span class="spark">✦</span>
        <span>Agent Auditing &amp; Evals</span>
      </div>
    </div>

    <div class="footer-row">
      <span class="stack-label">Core Stack</span>
      <span>•</span>
      <span class="stack-items">Python · LangGraph · AI Agents · Playwright · Docker · CI/CD</span>
    </div>
  </div>
</body>
</html>
"""

configs = [
    ("linkedin-banner-clean-es.png", "temp_es.html", html_variant_1, "Variante 1: AI Engineer Integral (ES - Large)"),
    ("linkedin-banner-clean-en.png", "temp_en.html", html_variant_2, "Variante 2: AI Engineer Global Tech (EN - Large)"),
    ("linkedin-banner-obsidian-cyber.png", "temp_cyber.html", html_variant_3, "Variante 3: Obsidian Cyber Terminal (ES - Scaled)"),
    ("linkedin-banner-clean-platform.png", "temp_plat.html", html_variant_4, "Variante 4: Alto Impacto 2 Badges (ES)"),
    ("linkedin-banner-clean-minimal.png", "temp_min.html", html_variant_5, "Variante 5: Minimal Bold Linear Style (ES)"),
    ("linkedin-banner-midnight-exec.png", "temp_exec.html", html_variant_6, "Variante 6: Midnight Executive (EN - Large)")
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

print("Finished rendering all 6 larger, highly-visible AI Engineer banners!")
