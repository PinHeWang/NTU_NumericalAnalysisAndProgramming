
## NAP final project

import matplotlib.pyplot as plt
import numpy as np
pi2 = np.pi * 2.0

def DFT(image):
	# imagex, imagey
	global M, N
	M = image.shape[0]
	N = image.shape[1] 

	#inital RGB matrixs
	dft_red = [[0.0 for k in range(M)] for l in range(N)]
	dft_grn = [[0.0 for k in range(M)] for l in range(N)]
	dft_blu = [[0.0 for k in range(M)] for l in range(N)]

	#DFT calculate
	for k in range(M):
		for l in range(N):
			sum_red = 0.0
			sum_grn = 0.0
			sum_blu = 0.0
			for m in range(M):
				for n in range(N):
					red, grn, blu, alpha = image[m, n]
					e = np.exp(-1j * pi2 *(float(k*m)/M + float(l*n)/N))
					sum_red += red * e
					sum_grn += grn * e
					sum_blu += blu * e
			dft_red[l][k] = sum_red / M / N
			dft_grn[l][k] = sum_grn / M / N
			dft_blu[l][k] = sum_blu / M / N
	return (dft_red, dft_grn, dft_blu)



def makeGaussian(size, fwhm = 3, center=None):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]

    return np.exp(-4*np.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)

#TEST
red, green, blue = DFT(plt.imread('Logo_rolling_stones.png'))



