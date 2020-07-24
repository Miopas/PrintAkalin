from PIL import Image
import numpy as np
import os
import sys
import string
import random

def generate_sym():
    sym = random.choice(string.punctuation)
    return random.choice(['|', sym])

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print ("usage: python run.py [image_file]")
        exit()
    img_file = sys.argv[1]

    '''
    Define the background pixel and the symbol for the background and the outline.
    Notice: the default background pixcel is white
    '''
    bg_pix = np.array([255, 255, 255])
    backgroud_sym = ' '

    # The parameter to control the size of the output. The larger alpha is, the smaller the result is.
    alpha = 5
    beta = 0.9

    # Load image.
    ori_img = Image.open(img_file)

    # Zoom in image as double width of the origin image.
    # `height * 0.5` is because that characters's height is usually larger than the widths.
    width = ori_img.size[0]
    height = ori_img.size[1]
    new_img = ori_img.transform((width, int(height*0.5)), Image.EXTENT, [0, 0, width, height])

    # Transform image into a mattix.
    img = np.array(new_img)

    # Get the window size and threshold according to the image size and the terminal window size
    new_w = new_img.size[0]
    new_h = new_img.size[1]
    terminal_h, terminal_w = os.popen('stty size', 'r').read().split() # get width and height of the terminal
    terminal_w = int(terminal_w)
    if (new_w > terminal_w):
        window_size = int(new_w/terminal_w) + alpha
    threshold = int(window_size * window_size * beta) # half of the window region should be filled
    #print("new_w:%d, terminal_w:%d, window_size:%d, threshold:%d" % (new_w, terminal_w, window_size, threshold))

    # Start print.
    for i in range(0, img.shape[0], window_size):
        for j in range(0, img.shape[1], window_size):
            # Get how many pix in window origin
            px_count = 0
            for delta_x in range(window_size):
                for delta_y in range(window_size):
                    x_pos = i + delta_x
                    y_pos = j + delta_y
                    if (x_pos >= img.shape[0] or y_pos >= img.shape[1]):
                        break
                    if ((img[x_pos][y_pos] == bg_pix).all() == False):
                        px_count += 1
            if (px_count > threshold):
                print(generate_sym(), end='')
            else:
                print(backgroud_sym, end='')
        print('\n', end='')
