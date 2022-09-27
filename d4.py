from PIL import Image, ImageDraw
img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.line((200, 100, 300, 200), fill=(0, 0, 230), width=10)
img.show()

from PIL import Image, ImageDraw
img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.ellipse((200, 125, 300, 200), fill=(255, 0, 0), outline=(0, 0, 0))
img.show()

from PIL import Image, ImageDraw
img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.rectangle((200, 125, 300, 200),fill=(0, 255, 0),outline=(0, 0, 0))
img.show()


from PIL import Image, ImageDraw
img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.polygon(((200, 200), (300, 100), (250, 50)),fill=(0, 0, 255),outline=(0, 0, 0))
img.show()
