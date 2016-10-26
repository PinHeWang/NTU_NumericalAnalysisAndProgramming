
## Using python library

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
#pi2 = np.pi * 2.0

################### Read image #################

img = plt.imread('lisa.png')
global M, N
global P, Q
global RGBmatrix
M = img.shape[0]
N = img.shape[1]
P = 2*M
Q = 2*N
RGBmatrix = np.zeros((P,Q))
#print M
#print N
#print img.shape
#print img


############### Functions ######################


## Testing Gaussian LP Filter
def makeGaussian(size, fwhm =10, center=None):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]
    #print x
    #print y

    if center is None:
        x0 = y0 = size // 2
        #print x0
        #print y0
    else:
        x0 = center[0]
        y0 = center[1]

    return np.exp(-4*np.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)


## Butterworth LP Filter
def BLPF(D0, n, center=None):

	#P = size[0]
	#Q = size[1]

	if center is None:
		u0 = P/2
		v0 = Q/2
	else:
		u0 = center[0]
		v0 = center[1]


	H = np.zeros((P,Q))
	for u in range(P):
		for v in range(Q):
			D = ((u-u0)**2 + (v-v0)**2)**0.5
			H[u,v] = 1/(1+((D/D0)**(2*n)))

	return H


## Gaussian LP Filter 
def GLPF(D0, center=None):

	if center is None:
		u0 = P/2
		v0 = Q/2
	else:
		u0 = center[0]
		v0 = center[1]

	H = np.zeros((P,Q))
	for u in range(P):
		for v in range(Q):
			D = ((u-u0)**2 + (v-v0)**2)**0.5
			H[u,v] = np.exp(-(D**2)/(2*(D0**2)))
	return H


def ILPF(D0):
    h=np.ones((P,Q))
    center1=P/2
    center2=Q/2
    for i in range(P):
        for j in range(Q):
            r1=(i-center1)**2+(j-center2)**2
            r=r1**0.5
            
            if r>D0:
                h[i,j]=0.0
    return h

## Gaussian HP Filter
def GHPF(D0):

	return 1 - GLPF(D0)

## Butterworth HP Filter
def BHPF(D0, n, center=None):

	if center is None:
		u0 = P/2
		v0 = Q/2
	else:
		u0 = center[0]
		v0 = center[1]


	H = np.zeros((P,Q))
	for u in range(P):
		for v in range(Q):
			D = ((u-u0)**2 + (v-v0)**2)**0.5
			if D == 0:
				H[u,v] = 0
			else:
				H[u,v] = 1/(1+((D0/D)**(2*n)))

	return H

def IHPF(D0):
    h=np.ones((P,Q))
    center1=P/2
    center2=Q/2
    for i in range(1,P):
        for j in range(1,Q):
            r1=(i-center1)**2+(j-center2)**2
            r=r1**0.5
            
            if 0<r<D0:
                h[i,j]=0.0
    return h




########## padding & shifting ##############

imgp = np.zeros((P,Q,3))
imgp[0:M,0:N,:] = img[0:M,0:N,:]

#print np.ndarray.max(img[:,:,0])
#print np.ndarray.min(img[:,:,0])
#print np.ndarray.max(img[:,:,1])
#print np.ndarray.min(img[:,:,1])
#print np.ndarray.max(img[:,:,2])
#print np.ndarray.min(img[:,:,2])




#for m in range(P):
#	for n in range(Q):
#		if (m+n)%2!=0:
#			imgp[m,n,:] *= -1

#print imgp
#print img.shape

###############################

red = RGBmatrix.copy()
red = imgp[:,:,0]
grn = RGBmatrix.copy()
grn = imgp[:,:,1]
blu = RGBmatrix.copy()
blu = imgp[:,:,2]

redf = np.log((np.fft.fft2(red)))
grnf = np.log((np.fft.fft2(grn)))
bluf = np.log((np.fft.fft2(blu)))


redf = np.fft.fftshift(redf)
grnf = np.fft.fftshift(grnf)
bluf = np.fft.fftshift(bluf)

#print np.ndarray.max(grn)
#print np.ndarray.min(grn)
#print red
#print redf.shape
#plt.imshow(redf)
#plt.show()

#print np.ndarray.max(redf)
#print np.ndarray.min(redf)
##################### FILTER ######################
HorL = 0 ## HP=1 LP=0
FILTER = np.zeros((P,Q))

#FILTER = BLPF(460, 20)
#FILTER = makeGaussian(P, fwhm =100, center=None)
#FILTER = GLPF(60)
#FILTER = ILPF(460)
#FILTER = GHPF(10)
#FILTER = BHPF(60,1)
FILTER = IHPF(160)


#print FILTER
#print FILTER.shape
#print np.ndarray.max(FILTER)

redff = np.exp(redf * FILTER)
grnff = np.exp(grnf * FILTER)
bluff = np.exp(bluf * FILTER)

#print np.ndarray.max(redf)
#print np.ndarray.min(redf)
#print np.ndarray.max(FILTER)
#print np.ndarray.min(FILTER)

#plt.imshow(FILTER)
#plt.show()
#plt.imshow(abs(redf))
#plt.show()
#plt.imshow(abs(redff))
#plt.show()

###################### IFFT ######################

#redf = np.fft.ifftshift(redf)
#grnf = np.fft.ifftshift(grnf)
#blu = np.fft.ifftshift(bluf)

newred = (np.fft.ifft2(redff))
newgrn = (np.fft.ifft2(grnff))
newblu = (np.fft.ifft2(bluff))

#print newred
#print type(newred)

#plt.imshow(abs(newred))
#plt.show()


newimg = np.zeros((P,Q,3))

newimg[:,:,0] = abs(newred)
newimg[:,:,1] = abs(newgrn)
newimg[:,:,2] = abs(newblu)

#print np.ndarray.max(abs(newred))
#print np.ndarray.min(abs(newred))

#print newimg.shape


newimg1=np.zeros((P/2,Q/2,3))
newimg1[:,:,:] = newimg[0:P/2,0:Q/2,:]

if HorL == 1:
	newimg1 += img
	plt.imshow(newimg1)
	plt.show()
elif HorL == 0:
	plt.imshow(newimg1)
	plt.show()






