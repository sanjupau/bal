import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

img1 = mpimg.imread('/home/anaconda/Desktop/dog.jpg')
imgplot = plt.imshow(img1)
plt.show()
