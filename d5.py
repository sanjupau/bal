# import required image module
from PIL import Image

# Open an already existing image
imageObject = Image.open("/home/anaconda/Desktop/dog.jpg")

# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)

# Show the original image
imageObject.show()

# Show the horizontal flipped image
hori_flippedImage.show()

#vertical flipped image
Vert_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
Vert_flippedImage.show()

#show 90 degree flipped image
degree_flippedImage = imageObject.transpose(Image.ROTATE_90)
degree_flippedImage.show()
