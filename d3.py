import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

img1 = mpimg.imread('/home/anaconda/Desktop/dog.jpg')
imgplot = plt.imshow(img1)
plt.show()

img = Image.open('/home/anaconda/Desktop/dog.jpg')
imgGray = img.convert('LA') # Gray Scale
imshow = plt.imshow(imgGray)
plt.show()
