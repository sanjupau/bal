(a)edge
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 7))

# Create an image object
image = Image.open("/home/anaconda/Desktop/dog.jpg")

# Find the edges by applying the filter ImageFilter.FIND_EDGES
imageWithEdges = image.filter(ImageFilter.FIND_EDGES)

# display the original show
plt.figure(0)
plt.imshow(image)

# display the new image with edge detection done
plt.figure(1)
plt.imshow(imageWithEdges)

(b)negative
 # import Pillow modules
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 7))
# Load the image
img = Image.open("/home/anaconda/Desktop/dog.jpg")
# Display the original image
plt.figure(0)
plt.imshow(img)
# Read pixels and apply negative transformation
for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
        # Get pixel value at (x,y) position of the image
        pixelColorVals = img.getpixel((i,j))
         # Invert color
        redPixel = 255 - pixelColorVals[0] # Negate red pixel
        greenPixel = 255 - pixelColorVals[1] # Negate green pixel
        bluePixel = 255 - pixelColorVals[2] # Negate blue pixel
         # Modify the image with the inverted pixel values
        img.putpixel((i,j),(redPixel, greenPixel, bluePixel)) 
# Display the negative image
plt.figure(1)
plt.imshow(img)
