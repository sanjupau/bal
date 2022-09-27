import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

img1 = mpimg.imread('/home/anaconda/Desktop/dog.jpg')
imgplot = plt.imshow(img1)
plt.show()

image = Image.open('/home/anaconda/Desktop/dog.jpg')
print(f"Original size : {image.size}")

goku_resized = image.resize((200, 200))
goku_resized.save('goku_400.jpeg')

img = mpimg.imread('goku_400.jpeg')
imgplot = plt.imshow(img)
plt.show()
