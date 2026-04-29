from PIL import Image, ImageDraw, ImageOps
import sys

def round_corners(input_path, output_path, radius):
    img = Image.open(input_path).convert("RGBA")
    
    # Create a mask for rounded corners
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + img.size, radius=radius, fill=255)
    
    # Apply the mask
    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    
    output.save(output_path)

if __name__ == "__main__":
    round_corners("public/perfil.jpg", "public/perfil_rounded.png", radius=30)
    print("Image rounded successfully: public/perfil_rounded.png")
