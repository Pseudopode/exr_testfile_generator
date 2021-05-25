import numpy as np
import imageio
# needed : https://imageio.readthedocs.io/en/latest/format_exr-fi.html#exr-fi
# https://stackoverflow.com/questions/45482307/save-float-array-to-image-with-exr-format
# https://stackoverflow.com/questions/55556277/read-process-and-show-the-pixels-in-exr-format-images

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

rgbArray = np.zeros((256,256,3), np.float32)

# Generate 3 arrays of 256 pixels height X 256 pixels width dimensions
#horizontal gradient from 0 to 1.0 (left to right), yellow color
arr_R = get_gradient_2d(0,1.0, 256,256,True)
arr_G = get_gradient_2d(0,1.0, 256,256,True)
arr_B = get_gradient_2d(0,0.0, 256,256,True)

arr_R = arr_R.astype(np.float32)
arr_G = arr_G.astype(np.float32)
arr_B = arr_B.astype(np.float32)

rgbArray[..., 0] = arr_R
rgbArray[..., 1] = arr_G
rgbArray[..., 2] = arr_B

# Write to disk
imageio.imwrite('out_imageio_16bits.exr', rgbArray)

# Read created exr from disk
img = imageio.imread('out_imageio_16bits.exr')

assert img.dtype == np.float32