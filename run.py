from PIL import Image
import numpy as np
import os
import sys
import pdb

'''
Print the outline of a image in shell
'''

if (len(sys.argv) < 2):
    print ("usage: ./run.py [image_file]")
    exit()
img_file = sys.argv[1]

'''
Define the background pixel and the symbol for the background and outline
Notice: the default background pixcel is white
'''
bg_pix = np.array([255, 255, 255])
backgroud_sym = '0'
outline_sym = '1'
alpha = 8 # the parameter to control the size of final result. The bigget alpha is, the smaller the result is.

# Load image
ori_img = Image.open(img_file)

# Zoom in image as double width of the origin image
##img.size[0] is weight, img.size[1] is height 
zoom_rate = 0.25
new_img = ori_img.transform((int(ori_img.size[0] * 2 * zoom_rate), int(ori_img.size[1] * zoom_rate)), Image.EXTENT, [0, 0, ori_img.size[0], ori_img.size[1]])

# Transform image into a mattix
img=np.array(new_img) 

# Get window size and threshold according to the image size and shell size
img_w = new_img.size[0]
img_h = new_img.size[1] # get width and height of the image
shell_h, shell_w = os.popen('stty size', 'r').read().split() # get width and height of the shell
shell_w = int(shell_w)
window_w = 1
if (img_w > shell_w):
    window_size = int(img_w/shell_w) + alpha
threshold = int(window_size * window_size / 2) # half of the window region should be filled
print ("img_w:%d, shell_w:%d, window_size:%d, threshold:%d" % (img_w, shell_w, window_size, threshold))

# Start print 
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
            print (outline_sym, end='')
        else:
            print (backgroud_sym, end='')
    print ('\n', end='')
