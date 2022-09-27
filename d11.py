(a)addn of two imgs
import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10,17))

image_1 = cv2.imread('/home/anaconda/Desktop/blue.jpg')
image_1 = imutils.resize(image_1, 1200)
image_2 = cv2.imread('/home/anaconda/Desktop/duck.jpg')
image_2= imutils.resize(image_2, 1200)

RGB_image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)
RGB_image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2RGB)

weighted_sum = cv2.addWeighted(RGB_image_1, 0.5, RGB_image_2, 0.4, 0)

plt.figure(0)
plt.imshow(RGB_image_1)
plt.title("first_images")
plt.show()

plt.figure(1)
plt.title('Second Image')
plt.imshow(RGB_image_2)
plt.show()

plt.figure(2)
plt.title('Image After Addition')
plt.imshow(weighted_sum)
plt.show()

(b)subtraction
import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10,17))

image_3 = cv2.imread('/home/anaconda/Desktop/blue.jpg')
image_4 = cv2.imread('/home/anaconda/Desktop/duck.jpg')

RGB_image_3 = cv2.cvtColor(image_3, cv2.COLOR_BGR2RGB)
RGB_image_4 = cv2.cvtColor(image_4, cv2.COLOR_BGR2RGB)

sub = cv2.subtract(RGB_image_3, RGB_image_4)

plt.figure(3)
plt.title('First Image')
plt.imshow(RGB_image_3)
plt.show()

plt.figure(4)
plt.title('Second Image')
plt.imshow(RGB_image_4)
plt.show()

plt.figure(5)
plt.title('Subtracted Image')
plt.imshow(sub)
plt.show()
