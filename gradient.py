import cv2


class Image:
    # region Constants
    DEFAULT_IMAGE_TITLE = 'Image'
    BASE_IMAGE_UNITS = 'uint8'

    BLUE = 0
    GREEN = 1
    RED = 2

    HEIGHT = 0
    WIDTH = 1

    # endregion

    def __init__(self, path):
        self.path = path

        # get image
        self.img = cv2.imread(IMAGE_PATH)
        self.dimensions = self.img.shape

        #  Get center coordinates
        self.center_x = self.img.shape[self.WIDTH] // 2
        self.center_y = self.img.shape[self.HEIGHT] // 2

    def darken(self, gauss_sigma):
        # get 2D Gaussian kernel
        kernel_x = cv2.getGaussianKernel(self.img.shape[self.WIDTH], gauss_sigma)
        kernel_y = cv2.getGaussianKernel(self.img.shape[self.HEIGHT], gauss_sigma)

        kernel = kernel_x.T * kernel_y

        # normalize kernel
        beta = kernel[0][0]  # beta subtraction
        kernel -= beta

        alpha = 1 / (kernel[self.center_y][self.center_x])  # alpha factoring
        kernel = alpha * kernel

        # darken image by kernel
        split = cv2.split(self.img.copy())
        split[self.BLUE] = split[self.BLUE] * kernel
        split[self.GREEN] = split[self.GREEN] * kernel
        split[self.RED] = split[self.RED] * kernel

        self.img = (cv2.merge(split)).astype(self.BASE_IMAGE_UNITS)

    def show(self, title=None):
        if title is None:
            title = self.DEFAULT_IMAGE_TITLE
        cv2.imshow(title, self.img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


#  region Constants
IMAGE_PATH = 'images/monkey.jpeg'

KERNEL_SIGMA = 80
#  endregion

image = Image(IMAGE_PATH)
image.darken(KERNEL_SIGMA)
image.show()
