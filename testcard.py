from PIL import Image, ImageDraw, ImageFont


with Image.open("BingoCard.jpg").convert("RGBA") as base:
    text = Image.new("RGBA", base.size, (255, 255, 255, 0))
    font = ImageFont.truetype("Roboto-Light.ttf", size=40)
    drawing = ImageDraw.Draw(text)
    drawing.text((10, 10),"'Where's the pharmacy?'", font=font, fill=(0, 0, 0,255))
    out = Image.alpha_composite(base, text)
    out.show()