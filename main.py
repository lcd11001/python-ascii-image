# This is a sample Python script.
from image_2_ascii import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    img_input = read_image_gray('assets/bj.png')
    img_h, img_w = img_input.shape
    print(f"Image size: {img_w}x{img_h}")

    # show_image(img_input)

    rows, cols, cell_w, cell_h = split_image(img_input, 80)
    print(f"rows: {rows}, cols: {cols}, cell_w: {cell_w}, cell_h: {cell_h}")

    # style = 'GRAYSCALE'
    style = 'MINIMALIST'
    for i in range(rows):
        print()
        for j in range(cols):
            cell_image = get_cell(img_input, i, j, cell_w, cell_h)
            mean = get_mean_intensity(cell_image)
            index = int(mean / 255 * (len(ASCII_STYLES[style]) - 1))
            print(ASCII_STYLES[style][index], end='')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
