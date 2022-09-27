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

(b)contrast stretching
from PIL import Image
import matplotlib.pyplot as plt
# Method to process the red band of the image
def normalizeRed(intensity):
 
 iI = intensity
 minI = 86
 maxI = 230
 minO = 0
 maxO = 255
 iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
 return iO
# Method to process the green band of the image
def normalizeGreen(intensity):
 iI = intensity
 minI = 90
 maxI = 225
 minO = 0
 maxO = 255
 iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
 return iO
# Method to process the blue band of the image
def normalizeBlue(intensity):
 iI = intensity
 minI = 100
 maxI = 210
 minO = 0
 maxO = 255
 iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
 return iO
# Create an image object
imageObject = Image.open("/home/anaconda/Desktop/dog.jpg")
# Split the red, green and blue bands from the Image
multiBands = imageObject.split()
# Apply point operations that does contrast stretching on each color band
normalizedRedBand = multiBands[0].point(normalizeRed)
normalizedGreenBand = multiBands[1].point(normalizeGreen)
normalizedBlueBand = multiBands[2].point(normalizeBlue)
# Create a new image from the contrast stretched red, green and blue brands
normalizedImage = Image.merge("RGB", (normalizedRedBand, 
normalizedGreenBand, normalizedBlueBand))
# Display the image before contrast stretching
plt.figure(0)
plt.title("Original")
plt.imshow(imageObject)
# Display the image after contrast stretching
plt.figure(1)
plt.title("After Contrast Stretching")
plt.imshow(normalizedImage)
