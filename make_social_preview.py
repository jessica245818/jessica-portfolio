from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
image = Image.new("RGB", (W, H), "#F7F6F2")
draw = ImageDraw.Draw(image)

def font(size, bold=False):
    paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()

draw.rounded_rectangle((72, 66, 152, 146), radius=20, fill="#17324D")
draw.text((92, 88), "JG", font=font(28, True), fill="white")
draw.text((72, 205), "JESSICA GEORGE", font=font(24, True), fill="#87521F")
draw.text((72, 256), "Search data and", font=font(66, True), fill="#17324D")
draw.text((72, 332), "machine learning", font=font(66, True), fill="#17324D")
draw.text((76, 445), "Transparent tools for practical content decisions.", font=font(30), fill="#52606D")
draw.rectangle((72, 540, 1128, 544), fill="#D8DEE6")
draw.text((72, 564), "Portfolio · Live scoring demo · Research paper", font=font(22, True), fill="#17324D")
image.save("social-preview.png", optimize=True)
