import cv2

# region Constants
IMAGE_PATH = 'images/flowers.jpeg'

HEIGHT = 0
WIDTH = 1

BLUE = 0
GREEN = 1
RED = 2

NOISE_FLUCTUATION = 20
# endregion

# get original image
original = cv2.imread(IMAGE_PATH)
dimensions = original.shape

# clear image
clear = cv2.fastNlMeansDenoising(original, None, 15, 7, 21)

# show images
cv2.imshow('cleared', clear)
cv2.imshow('original', original)

# wait for key, and close
cv2.waitKey(0)
cv2.destroyAllWindows()
