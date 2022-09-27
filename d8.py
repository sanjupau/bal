import imageio
import matplotlib.pyplot as plt
image = imageio.imread('/home/anaconda/Desktop/scenery.jpg')
plt.imshow(image)

print('Type of the image : ' , type(image))
print()
print('Shape of the image : {}'.format(image.shape))
print('Image Height : {}'.format(image.shape[0]))
print('Image Width : {}'.format(image.shape[1]))
print('Dimension of Image : {}'.format(image.ndim))

print('Image size {}'.format(image.size))
print('Maximum RGB value in this image {}'.format(image.max()))
print('Minimum RGB value in this image {}'.format(image.min()))

# A specific pixel located at Row : 100 ; Column : 50
# Each channel's value of it, gradually R , G , B
print('Value of only R channel {}'.format(image[ 100, 50, 0]))
print('Value of only G channel {}'.format(image[ 100, 50, 1]))
print('Value of only B channel {}'.format(image[ 100, 50, 2]))

plt.title('R channel')
plt.ylabel('Height {}'.format(image.shape[0]))
plt.xlabel('Width {}'.format(image.shape[1]))
plt.imshow(image[ : , : , 0])
plt.show()

plt.title('G channel')
plt.ylabel('Height {}'.format(image.shape[0]))
plt.xlabel('Width {}'.format(image.shape[1]))
plt.imshow(image[ : , : , 1])
plt.show()

plt.title('B channel')
plt.ylabel('Height {}'.format(image.shape[0]))
plt.xlabel('Width {}'.format(image.shape[1]))
plt.imshow(image[ : , : , 2])
plt.show()
