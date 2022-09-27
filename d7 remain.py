(a)
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

(b)
