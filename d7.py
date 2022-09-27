(a)array
#Import required libraries
from PIL import Image
from numpy import array

#Open Image & create image object
img = Image.open('/home/anaconda/Desktop/dog.jpg')

#Convert an image to numpy array
img2arr = array(img)

#Print the array
print(img2arr)

#Convert numpy array back to image
arr2im = Image.fromarray(img2arr)

#Display image
arr2im.show()

(b)watermark
#Import required Image library
from PIL import Image, ImageDraw, ImageFont
#Create an Image Object from an Image
im = Image.open('/home/anaconda/Desktop/dog.jpg')
width, height = im.size
draw = ImageDraw.Draw(im)
text =  "ashim rocks"
font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)
# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin
# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()
