import cv2


def read_image(image_path):
    # read image from file
    return cv2.imread(image_path)


def read_image_gray(image_path):
    # read image from file
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


def show_image(image):
    # get image size
    dimensions = image.shape
    w = dimensions[1]
    h = dimensions[0]

    # detect image is gray scale or color
    is_gray = len(dimensions) == 2

    # create title for the window
    title = f"PREVIEW IMAGE {'gray_scale' if is_gray else 'color'} {w}x{h}"

    # display image in a window
    cv2.imshow(title, image)
    # wait for any key to close the window
    cv2.waitKey(0)
    # close the window
    cv2.destroyAllWindows()
