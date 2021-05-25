# exr_testfile_generator
Python scripts to generate exr test files. Imageio &amp; pyexr.

The test file is a yellow gradient from left to right (yellow to black).
Imageio outputs a HALF (16 bit float) EXR file, while Pyexr output by default a 32 bit EXR file.

#PYEXR
To test pyexr, run `test_pyexr.py`

#Imageio
To test pyexr, run `test_imageio_exr.py`.
You'll need perhaps to install some imageio binaries: <https://imageio.readthedocs.io/en/latest/format_exr-fi.html#exr-fi>