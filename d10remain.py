(a)thresholding
from PIL import Image
import matplotlib.pyplot as plt
# Method to process the red band
def pixelProcRed(intensity):
 return 0
# Method to process the green band
def pixelProcGreen(intensity):
 return intensity
# Method to process the blue band
def pixelProcBlue(intensity):
 return 0
# Create an image object
imageObject = Image.open("/home/anaconda/Desktop/dog.jpg")
plt.figure(0)
plt.imshow(imageObject)
# Split the red, green and blue bands from the Image
multiBands = imageObject.split()
# Apply point operations that does thresholding on each color band
redBand = multiBands[0].point(pixelProcRed)
greenBand = multiBands[1].point(pixelProcGreen)
blueBand = multiBands[2].point(pixelProcBlue)
# Display the individual band after thresholding
plt.figure(1)
plt.title("redBand")
plt.imshow(redBand)
plt.figure(2)
plt.title("greenBand")
plt.imshow(greenBand)
plt.figure(3)
plt.title("blueBand")
plt.imshow(blueBand)
# Create a new image from the thresholded red, green and blue brands
newImage = Image.merge("RGB", (redBand, greenBand, blueBand))
# Display the merged image after thresholding
plt.figure(4)
plt.title("After Merging")
plt.imshow(newImage)

(b)contrast
