import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import copy

# region Constants
IMAGE_PATH = 'images/monkey.jpeg'

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

# noise image
noised = copy.deepcopy(original)
for i in range(dimensions[HEIGHT]):
    for j in range(dimensions[WIDTH]):
        noised[i][j][BLUE] += random.randint(0, NOISE_FLUCTUATION)
        noised[i][j][GREEN] += random.randint(0, NOISE_FLUCTUATION)
        noised[i][j][RED] += random.randint(0, NOISE_FLUCTUATION)


# denoise image
denoise = cv2.fastNlMeansDenoisingColored(noised, None, 10, 10, 7, 21)

# show images
cv2.imshow('original', original)
cv2.imshow("noised", noised)
cv2.imshow('denoised', denoise)

# wait for key, and close
cv2.waitKey(0)
cv2.destroyAllWindows()