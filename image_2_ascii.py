import os
import cv2
import numpy as np

# define ASCII styles use to replace pixels
# https://www.asciiart.eu/image-to-ascii
ASCII_STYLES = {
    'MINIMALIST': "#+-.",
    'NORMAL': "@%#*+=-:.",
    'NORMAL2': "&$Xx+;:.",
    'ALPHABETIC': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'ALPHA_NUMERIC': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz',
    'EXTENDED': "@%#{}[]()<>^*+=~-:.",
    'MATH': "+-\xd7\xf7=≠≈∞√π",
    'ARROW': '↑↗→↘↓↙←↖',
    'GRAYSCALE': "@$BWM#*oahkbdpwmZO0QCJYXzcvnxrjft/|()1{}[]-_+~<>i!lI;:,\"^`'.",
    'MAX': "\xc6\xd1\xcaŒ\xd8M\xc9\xcb\xc8\xc3\xc2WQB\xc5\xe6#N\xc1\xfeE\xc4\xc0HKRŽœXg\xd0\xeaq\xdbŠ\xd5\xd4A€\xdfpm\xe3\xe2G\xb6\xf8\xf0\xe98\xda\xdc$\xebd\xd9\xfd\xe8\xd3\xde\xd6\xe5\xff\xd2b\xa5FD\xf1\xe1ZP\xe4š\xc7\xe0h\xfb\xa7\xddkŸ\xaeS9žUTe6\xb5Oyx\xce\xbef4\xf55\xf4\xfa&a\xfc™2\xf9\xe7w\xa9Y\xa30V\xcdL\xb13\xcf\xcc\xf3C@n\xf6\xf2s\xa2u‰\xbd\xbc‡zJƒ%\xa4Itoc\xeerjv1l\xed=\xef\xec<>i7†[\xbf?\xd7}*{+()/\xbb\xab•\xac|!\xa1\xf7\xa6\xaf—^\xaa„”“~\xb3\xba\xb2–\xb0\xad\xb9‹›;:’‘‚’˜ˆ\xb8…\xb7\xa8\xb4`",
    'CODEPAGE437': "█▓▒░",
    'BLACK_AND_WHITE': " █"
}


def read_image(image_path):
    # read image from file
    return cv2.imread(image_path)


def read_image_gray(image_path):
    # read image from file with gray scale
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


def show_image(image):
    # get image size
    h, w = image.shape

    # detect image is gray scale or color
    is_gray = len(image.shape) == 2

    # create title for the window
    title = f"PREVIEW IMAGE {'gray_scale' if is_gray else 'color'} {w}x{h}"

    # display image in a window
    cv2.imshow(title, image)
    # wait for any key to close the window
    cv2.waitKey(0)
    # close the window
    cv2.destroyAllWindows()


def split_image(image, cols):
    # get image size
    h, w = image.shape

    # calculate cell size
    cell_w = w // cols
    cell_h = cell_w * 2

    # calculate rows
    rows = h // cell_h

    return rows, cols, cell_w, cell_h


def get_cell(image, row, col, cell_w, cell_h):
    # get cell from image
    x = col * cell_w
    y = row * cell_h
    return image[y:y + cell_h, x:x + cell_w]


def get_mean_intensity(cell_image):
    # calculate mean intensity of cell image
    return np.mean(cell_image)


def img_2_ascii(image_path, cols, style):
    img = read_image_gray(image_path)
    rows, cols, cell_w, cell_h = split_image(img, cols)

    for i in range(rows):
        for j in range(cols):
            cell_image = get_cell(img, i, j, cell_w, cell_h)
            mean = get_mean_intensity(cell_image)
            index = 0
            max_index = len(ASCII_STYLES[style]) - 1
            if max_index > 1:
                index = int(mean / 255 * max_index)
            else:
                index = 0 if mean < 128 else 1
            print(ASCII_STYLES[style][index], end='')
        print()


def img_2_file(image_path, cols, style, file_path):
    img = read_image_gray(image_path)
    rows, cols, cell_w, cell_h = split_image(img, cols)

    # get parent directory
    parent_dir = os.path.dirname(file_path)

    # check if parent directory is not exists
    if len(parent_dir) > 0 and not os.path.exists(parent_dir):
        # create parent directory
        os.makedirs(parent_dir)

    with open(file_path, mode='w', encoding='utf-8') as f:
        for i in range(rows):
            for j in range(cols):
                cell_image = get_cell(img, i, j, cell_w, cell_h)
                mean = get_mean_intensity(cell_image)
                index = 0
                max_index = len(ASCII_STYLES[style]) - 1
                if max_index > 1:
                    index = int(mean / 255 * max_index)
                else:
                    index = 0 if mean < 128 else 1
                f.write(ASCII_STYLES[style][index])
            f.write('\n')
