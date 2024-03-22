import cv2


def read_image(image_path):
    # read image from file
    return cv2.imread(image_path)


def show_image(image):
    # get image size
    dimensions = image.shape
    # create title for the window
    w = dimensions[1]
    h = dimensions[0]
    title = f'PREVIEW IMAGE {w}x{h}'
    # display image in a window
    cv2.imshow(title, image)
    # wait for any key to close the window
    cv2.waitKey(0)
    # close the window
    cv2.destroyAllWindows()
