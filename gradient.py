import cv2
import copy

#  region Constants
IMAGE_PATH = 'images/monkey.jpeg'
HEIGHT = 0
WIDTH = 1
CHANNEL_COUNT = 3

GAMMA = 0.5
#  endregion


# get image
original = cv2.imread(IMAGE_PATH)
dimensions = original.shape

#  center coordinates
center_x = original.shape[1] // 2
center_y = original.shape[0] // 2

max_radius = (center_x ** 2 + center_y ** 2) ** 0.5

# darken image radially
dark = copy.deepcopy(original)
for i in range(dimensions[HEIGHT]):
    for j in range(dimensions[WIDTH]):

        dark_factor = ((((i - center_y) ** 2 + (j - center_x) ** 2) ** 0.5) / max_radius) ** GAMMA

        for k in range(CHANNEL_COUNT):
            dark[i][j][k] -= round(dark_factor * dark[i][j][k])  # darken pixel

cv2.imshow('original', original)
cv2.imshow('darkened', dark)

cv2.waitKey(0)
cv2.destroyAllWindows()
