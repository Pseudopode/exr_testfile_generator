import pyexr
import numpy as np

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

rgbArray = np.zeros((256,256,3), np.float16)

# Generate 3 arrays of 256 pixels height X 256 pixels width dimensions
#horizontal gradient from 0 to 1.0 (left to right), yellow color
arr_R = get_gradient_2d(0,1.0, 256,256,True)
arr_G = get_gradient_2d(0,1.0, 256,256,True)
arr_B = get_gradient_2d(0,0.0, 256,256,True)


arr_R = arr_R.astype(np.float16)
arr_G = arr_G.astype(np.float16)
arr_B = arr_B.astype(np.float16)

rgbArray[..., 0] = arr_R
rgbArray[..., 1] = arr_G
rgbArray[..., 2] = arr_B

pyexr.write("out_pyexr_32bits.exr", rgbArray)