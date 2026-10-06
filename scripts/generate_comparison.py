from PIL import Image, ImageDraw, ImageFont
import os

WORKSPACE_DIR = r"C:\Users\admin\Documents\Github\portfolio-cv"
SCREENSHOT_PATH = r"C:\Users\admin\AppData\Local\Temp\orca-paste-1791309060332-06ff3a70-5252-4ede-9159-d04d33d811a7.png"
NEW_BANNER_PATH = os.path.join(WORKSPACE_DIR, "public", "linkedin-banners", "linkedin-banner-obsidian-cyber.png")
OUTPUT_PATH = os.path.join(WORKSPACE_DIR, "public", "linkedin-banners", "comparativa-tamano-antes-despues.png")
BRAIN_PATH = r"C:\Users\admin\.gemini\antigravity-cli\brain\bad2105d-0e07-4e8f-82d3-2974867f09a3\comparativa-tamano-antes-despues.png"

# Load screenshot and new banner
im_shot = Image.open(SCREENSHOT_PATH)
im_new = Image.open(NEW_BANNER_PATH)

# In the screenshot (1111x486), the banner area is roughly y=0 to y=250
# Let's resize new banner to match the screenshot banner width (1111px)
banner_w = 1111
banner_h = int(396 * (1111 / 1584)) # ~277px

im_new_resized = im_new.resize((banner_w, banner_h), Image.Resampling.LANCZOS)

# Create a canvas of 1200 x 750
comp_w = 1200
comp_h = 750
comp = Image.new("RGB", (comp_w, comp_h), "#0a0d14")
draw = ImageDraw.Draw(comp)

# Try to use a nice font, fallback to default
try:
    font_title = ImageFont.truetype("arial.ttf", 22)
    font_sub = ImageFont.truetype("arial.ttf", 16)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# 1. Header Antes
draw.text((45, 20), "❌ ANTES (Tu captura en LinkedIn — Texto pequeño a 40px / 20px / 13px)", fill="#f87171", font=font_title)
draw.text((45, 50), "Mucho espacio vacío, badges chicos y margen izquierdo excesivo (420px):", fill="#94a3b8", font=font_sub)

# Paste cropped banner from screenshot (y: 0 to 240)
shot_crop = im_shot.crop((0, 0, 1111, 240))
comp.paste(shot_crop, (45, 80))

# 2. Header Después
draw.text((45, 360), "✅ AHORA (Proporciones Reales LinkedIn — Tipografía 76px / 32px / 22px)", fill="#4ade80", font=font_title)
draw.text((45, 390), "Diseñado para la escala 0.5x de LinkedIn: ocupa el alto y ancho real, badges legibles y sin 'producción':", fill="#94a3b8", font=font_sub)

# Paste new banner resized
comp.paste(im_new_resized, (45, 420))

comp.save(OUTPUT_PATH)
comp.save(BRAIN_PATH)
print("Saved comparison to:", OUTPUT_PATH)
