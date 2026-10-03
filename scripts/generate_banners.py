import subprocess
import os
import shutil
from PIL import Image

WORKSPACE_DIR = r"C:\Users\admin\Documents\Github\portfolio-cv"
PUBLIC_DIR = os.path.join(WORKSPACE_DIR, "public", "linkedin-banners")
ARTIFACT_DIR = r"C:\Users\admin\.gemini\antigravity-cli\brain\bfbfffe4-28e7-4a39-ba57-461fbf0b67fe"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

os.makedirs(PUBLIC_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

# -------------------------------------------------------------
# HTML TEMPLATE 1: Elite Dark Mode (Identity & Value Pillars)
# -------------------------------------------------------------
html_variant_a = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Banner Variant A</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #05070b;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    display: flex;
    background-image: 
      radial-gradient(circle at 85% 30%, rgba(14, 165, 233, 0.09) 0%, transparent 60%),
      radial-gradient(circle at 50% 100%, rgba(99, 102, 241, 0.05) 0%, transparent 50%),
      linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
  }

  /* Safe zone for LinkedIn circular profile picture */
  .safe-zone {
    width: 440px;
    height: 100%;
    position: relative;
    padding: 32px 40px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
  }

  .status-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #94a3b8;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 6px 12px;
    border-radius: 9999px;
    width: fit-content;
  }

  .pulse-dot {
    width: 7px;
    height: 7px;
    background-color: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 8px #10b981;
  }

  .safe-zone-bottom {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #475569;
    letter-spacing: 0.1em;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  /* Main content right */
  .content-zone {
    flex: 1;
    padding: 36px 48px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
  }

  .top-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .meta-tagline {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.25em;
    color: #38bdf8;
    text-transform: uppercase;
    font-weight: 600;
  }

  .badge-tier {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #cbd5e1;
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid rgba(56, 189, 248, 0.25);
    padding: 4px 10px;
    border-radius: 4px;
    letter-spacing: 0.1em;
  }

  .header-block {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-top: 4px;
  }

  .name-row {
    display: flex;
    align-items: baseline;
    gap: 18px;
  }

  h1.name {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #ffffff;
    line-height: 1;
  }

  .role-title {
    font-size: 20px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: 0.02em;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .separator {
    color: #334155;
    font-weight: 300;
  }

  .tagline {
    font-size: 15px;
    color: #94a3b8;
    line-height: 1.4;
    font-weight: 400;
    max-width: 950px;
  }

  .tagline strong {
    color: #e2e8f0;
    font-weight: 600;
  }

  /* Pillars Grid */
  .pillars-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 14px;
  }

  .pillar-card {
    background: rgba(15, 23, 42, 0.55);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-top: 1px solid rgba(56, 189, 248, 0.35);
    border-radius: 8px;
    padding: 14px 18px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    backdrop-filter: blur(10px);
  }

  .pillar-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #38bdf8;
    font-weight: 600;
    letter-spacing: 0.1em;
  }

  .pillar-title {
    font-size: 13.5px;
    font-weight: 700;
    color: #f1f5f9;
    letter-spacing: -0.01em;
  }

  .pillar-desc {
    font-size: 11.5px;
    color: #64748b;
    line-height: 1.35;
  }
</style>
</head>
<body>
  <!-- Safe Zone for avatar -->
  <div class="safe-zone">
    <div class="status-tag">
      <span class="pulse-dot"></span>
      LATAM // REMOTE • OPEN FOR IMPACT
    </div>
    <div class="safe-zone-bottom">
      <div>SYS.CORE: AGENTIC-AI</div>
      <div>LOC: URUGUAY / GLOBAL</div>
    </div>
  </div>

  <!-- Content Zone -->
  <div class="content-zone">
    <div class="top-meta">
      <div class="meta-tagline">// ENTERPRISE AGENTIC ARCHITECTURES & QA ENGINEERING</div>
      <div class="badge-tier">PRODUCTION GRADE</div>
    </div>

    <div class="header-block">
      <div class="name-row">
        <h1 class="name">JORGE TRICARICO</h1>
        <div class="role-title">
          <span class="separator">|</span>
          AI ENGINEER &amp; AGENTIC SYSTEMS
        </div>
      </div>
      <p class="tagline">
        Architecting <strong>autonomous multi-agent systems</strong> and <strong>deterministic testing platforms</strong> that turn complex business operations into resilient, automated production environments.
      </p>
    </div>

    <!-- 3 Core Pillars -->
    <div class="pillars-row">
      <div class="pillar-card">
        <span class="pillar-num">01 / ARCHITECTURE</span>
        <span class="pillar-title">Autonomous Agent Frameworks</span>
        <span class="pillar-desc">Multi-agent orchestration, stateful graph execution (LangGraph) &amp; self-correcting logic.</span>
      </div>
      <div class="pillar-card">
        <span class="pillar-num">02 / ASSURANCE</span>
        <span class="pillar-title">Enterprise QA Automation</span>
        <span class="pillar-desc">Continuous test-case generation, self-healing test automation &amp; zero-regression pipelines.</span>
      </div>
      <div class="pillar-card">
        <span class="pillar-num">03 / GOVERNANCE</span>
        <span class="pillar-title">LLM Evals &amp; Observability</span>
        <span class="pillar-desc">Automated LLM benchmark harnesses, deterministic guardrails &amp; production telemetry.</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# HTML TEMPLATE 2: Dark Technical Blueprint (Engineering Pipeline)
# -------------------------------------------------------------
html_variant_b = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Banner Variant B</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #040508;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f1f5f9;
    display: flex;
    position: relative;
    background-image: 
      radial-gradient(circle at 90% 40%, rgba(14, 165, 233, 0.08) 0%, transparent 65%),
      linear-gradient(to right, rgba(255, 255, 255, 0.025) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
    background-size: 100% 100%, 48px 48px, 48px 48px;
  }

  .safe-zone {
    width: 440px;
    height: 100%;
    padding: 36px 40px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-right: 1px solid rgba(255, 255, 255, 0.06);
  }

  .sys-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    color: #64748b;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 6px 12px;
    border-radius: 4px;
    width: fit-content;
  }

  .content-zone {
    flex: 1;
    padding: 34px 48px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .header-line {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .identity-group {
    display: flex;
    align-items: baseline;
    gap: 16px;
  }

  h1.brand-name {
    font-size: 34px;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff;
  }

  .title-tag {
    font-size: 18px;
    font-weight: 600;
    color: #38bdf8;
    letter-spacing: 0.01em;
  }

  .terminal-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #64748b;
    letter-spacing: 0.1em;
  }

  /* Pipeline Diagram */
  .pipeline-container {
    background: rgba(8, 12, 20, 0.7);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 8px;
    padding: 20px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
  }

  .pipeline-node {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 4px;
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 6px;
    padding: 12px 16px;
    position: relative;
  }

  .node-kicker {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    color: #38bdf8;
    font-weight: 600;
  }

  .node-label {
    font-size: 15px;
    font-weight: 700;
    color: #ffffff;
  }

  .node-sub {
    font-size: 11px;
    color: #94a3b8;
  }

  .pipeline-arrow {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 2px;
    padding: 0 8px;
  }

  .arrow-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.5px;
    color: #64748b;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .arrow-icon {
    color: #38bdf8;
    font-size: 18px;
    font-weight: bold;
  }

  /* Bottom Stack */
  .stack-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    padding-top: 14px;
  }

  .stack-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #64748b;
    letter-spacing: 0.15em;
    font-weight: 600;
  }

  .stack-badges {
    display: flex;
    gap: 10px;
  }

  .badge-chip {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11.5px;
    color: #cbd5e1;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 5px 12px;
    border-radius: 4px;
    letter-spacing: 0.02em;
  }

  .badge-chip.highlight {
    border-color: rgba(56, 189, 248, 0.4);
    color: #e0f2fe;
    background: rgba(56, 189, 248, 0.06);
  }
</style>
</head>
<body>
  <div class="safe-zone">
    <div class="sys-badge">// ENG.BLUEPRINT: 2026.04</div>
    <div style="font-family:'JetBrains Mono', monospace; font-size:11px; color:#475569; line-height:1.6;">
      <div>SCOPE: AUTONOMOUS AGENTS</div>
      <div>CORE: DETERMINISTIC QA</div>
    </div>
  </div>

  <div class="content-zone">
    <div class="header-line">
      <div class="identity-group">
        <h1 class="brand-name">JORGE TRICARICO</h1>
        <div class="title-tag">AI ENGINEER &amp; AGENTIC ARCHITECT</div>
      </div>
      <div class="terminal-meta">[ PRODUCTION ARCHITECTURE ]</div>
    </div>

    <!-- The Pipeline Blueprint -->
    <div class="pipeline-container">
      <div class="pipeline-node">
        <span class="node-kicker">STAGE 01 / INPUT</span>
        <span class="node-label">Complex Business Flows</span>
        <span class="node-sub">Dynamic specs, edge cases &amp; user journeys</span>
      </div>

      <div class="pipeline-arrow">
        <span class="arrow-label">Ingestion</span>
        <span class="arrow-icon">──►</span>
      </div>

      <div class="pipeline-node" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(14, 165, 233, 0.05);">
        <span class="node-kicker" style="color:#38bdf8;">STAGE 02 / REASONING</span>
        <span class="node-label">Autonomous QA Agents</span>
        <span class="node-sub">LangGraph orchestration &amp; self-healing tests</span>
      </div>

      <div class="pipeline-arrow">
        <span class="arrow-label">Validation</span>
        <span class="arrow-icon">──►</span>
      </div>

      <div class="pipeline-node">
        <span class="node-kicker">STAGE 03 / OUTCOME</span>
        <span class="node-label">Deterministic Quality</span>
        <span class="node-sub">Zero-regression confidence &amp; LLM benchmarks</span>
      </div>
    </div>

    <!-- Tech Stack Row -->
    <div class="stack-footer">
      <div class="stack-label">ENGINEERING ARSENAL</div>
      <div class="stack-badges">
        <span class="badge-chip highlight">Python</span>
        <span class="badge-chip highlight">LangGraph</span>
        <span class="badge-chip highlight">Multi-Agent Systems</span>
        <span class="badge-chip">LLM Evaluation</span>
        <span class="badge-chip">Automated Testing</span>
        <span class="badge-chip">CI/CD Telemetry</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# HTML TEMPLATE 3: Swiss Minimalist High-Contrast (Light Mode)
# -------------------------------------------------------------
html_variant_c = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Banner Variant C</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #ffffff;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #09090b;
    display: flex;
    position: relative;
    background-image: 
      linear-gradient(to right, rgba(0, 0, 0, 0.04) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(0, 0, 0, 0.04) 1px, transparent 1px);
    background-size: 36px 36px;
  }

  .safe-zone {
    width: 440px;
    height: 100%;
    padding: 36px 40px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-right: 1.5px solid #e4e4e7;
    background-color: #fafafa;
  }

  .swiss-index {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    font-weight: 700;
    color: #09090b;
    border-left: 2px solid #09090b;
    padding-left: 8px;
  }

  .safe-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    color: #71717a;
    line-height: 1.6;
  }

  .content-zone {
    flex: 1;
    padding: 34px 48px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #ffffff;
  }

  .top-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1.5px solid #09090b;
    padding-bottom: 10px;
  }

  .swiss-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.2em;
    color: #09090b;
    text-transform: uppercase;
  }

  .swiss-location {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    letter-spacing: 0.1em;
    color: #71717a;
  }

  .main-identity {
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-top: 6px;
  }

  .name-row {
    display: flex;
    align-items: baseline;
    gap: 16px;
  }

  h1.name {
    font-size: 40px;
    font-weight: 900;
    letter-spacing: -0.03em;
    color: #09090b;
    line-height: 1;
  }

  .title {
    font-size: 18px;
    font-weight: 700;
    color: #0284c7;
    letter-spacing: 0.01em;
  }

  .statement {
    font-size: 14px;
    color: #52525b;
    line-height: 1.4;
    max-width: 900px;
    margin-top: 2px;
  }

  /* Swiss 3-column value grid */
  .swiss-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 10px;
    border-top: 1px solid #e4e4e7;
    padding-top: 14px;
  }

  .swiss-col {
    display: flex;
    flex-direction: column;
    gap: 3px;
    border-left: 2px solid #09090b;
    padding-left: 12px;
  }

  .col-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    font-weight: 700;
    color: #09090b;
    letter-spacing: 0.1em;
  }

  .col-title {
    font-size: 13.5px;
    font-weight: 700;
    color: #18181b;
  }

  .col-desc {
    font-size: 11.5px;
    color: #71717a;
    line-height: 1.35;
  }

  .swiss-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.12em;
    color: #71717a;
    border-top: 1px solid #e4e4e7;
    padding-top: 8px;
  }
</style>
</head>
<body>
  <div class="safe-zone">
    <div class="swiss-index">SPEC: JT-2026.V1</div>
    <div class="safe-meta">
      <div>DISCIPLINE: AI SYSTEMS ENG</div>
      <div>CORE: AGENTIC QUALITY</div>
      <div>LOCATION: LATAM // GLOBAL</div>
    </div>
  </div>

  <div class="content-zone">
    <div class="top-meta">
      <div class="swiss-sub">SYSTEM SPECIFICATION // AUTONOMOUS AI &amp; QA PLATFORMS</div>
      <div class="swiss-location">PRODUCTION ARCHITECTURE</div>
    </div>

    <div class="main-identity">
      <div class="name-row">
        <h1 class="name">JORGE TRICARICO</h1>
        <div class="title">AI ENGINEER · AGENTIC SYSTEMS ARCHITECT</div>
      </div>
      <p class="statement">
        Designing resilient multi-agent orchestration frameworks and deterministic test automation platforms for mission-critical enterprise software.
      </p>
    </div>

    <div class="swiss-grid">
      <div class="swiss-col">
        <span class="col-label">01 / ARCHITECTURE</span>
        <span class="col-title">Multi-Agent Systems</span>
        <span class="col-desc">Stateful orchestration, LangGraph graph workflows &amp; autonomous self-correcting agents.</span>
      </div>
      <div class="swiss-col">
        <span class="col-label">02 / AUTOMATION</span>
        <span class="col-title">Enterprise QA Platforms</span>
        <span class="col-desc">Autonomous test generation, self-healing test frameworks &amp; zero-regression pipelines.</span>
      </div>
      <div class="swiss-col">
        <span class="col-label">03 / GOVERNANCE</span>
        <span class="col-title">LLM Evals &amp; Observability</span>
        <span class="col-desc">Deterministic benchmarks, safety guardrails &amp; auditable production telemetry.</span>
      </div>
    </div>

    <div class="swiss-footer">
      <span>STACK: PYTHON · LANGGRAPH · MULTI-AGENT · LLM EVALUATION · CI/CD · ENTERPRISE TESTING</span>
      <span>EDITION: SWISS EDITORIAL 2026</span>
    </div>
  </div>
</body>
</html>
"""

variants = [
    ("linkedin-banner-variant-a.png", "variant_a.html", html_variant_a),
    ("linkedin-banner-variant-b.png", "variant_b.html", html_variant_b),
    ("linkedin-banner-variant-c.png", "variant_c.html", html_variant_c),
]

for img_name, html_name, html_content in variants:
    temp_html_path = os.path.join(WORKSPACE_DIR, html_name)
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    temp_img_path = os.path.join(WORKSPACE_DIR, img_name)
    cmd = [
        CHROME_PATH,
        "--headless=new",
        f"--screenshot={temp_img_path}",
        "--window-size=1584,396",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        temp_html_path
    ]
    print(f"Rendering {img_name}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error rendering {img_name}: {res.stderr}")
    else:
        im = Image.open(temp_img_path)
        print(f"Successfully generated {img_name} with size {im.size}")
        
        # Copy to public/linkedin-banners/
        dest_public = os.path.join(PUBLIC_DIR, img_name)
        shutil.copy2(temp_img_path, dest_public)
        print(f"Copied to: {dest_public}")
        
        # Copy to artifact directory
        dest_artifact = os.path.join(ARTIFACT_DIR, img_name)
        shutil.copy2(temp_img_path, dest_artifact)
        print(f"Copied to: {dest_artifact}")
        
    # Clean up temp html
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

print("All banners generated and distributed successfully!")
