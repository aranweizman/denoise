import cv2


#  region Constants
IMAGE_PATH = 'images/monkey.jpeg'
HEIGHT = 0
WIDTH = 1
CHANNEL_COUNT = 3

BLUE = 0
GREEN = 1
RED = 2

KERNEL_SIGMA_X = 80
KERNEL_SIGMA_Y = 80
#  endregion


# get image
original = cv2.imread(IMAGE_PATH)
dimensions = original.shape

#  center coordinates
center_x = original.shape[WIDTH] // 2
center_y = original.shape[HEIGHT] // 2

# get 2D Gaussian kernel
kernel_x = cv2.getGaussianKernel(original.shape[WIDTH], KERNEL_SIGMA_X)
kernel_y = cv2.getGaussianKernel(original.shape[HEIGHT], KERNEL_SIGMA_Y)

kernel = kernel_x.T * kernel_y

# normalize kernel
beta = kernel[0][0]  # beta subtraction
kernel -= beta

alpha = 1/(kernel[center_y][center_x])  # alpha factoring
kernel = alpha * kernel

# darken image by kernel
split = cv2.split(original.copy())
split[BLUE] = split[BLUE] * kernel
split[GREEN] = split[GREEN] * kernel
split[RED] = split[RED] * kernel

dark = (cv2.merge(split)).astype('uint8')

cv2.imshow('original', original)
cv2.imshow('darkened', dark)

cv2.waitKey(0)
cv2.destroyAllWindows()
