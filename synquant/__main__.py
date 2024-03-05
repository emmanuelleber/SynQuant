import os, sys
import read_lif
import matplotlib.pylab as plt
import numpy as np

if len(sys.argv)<2:
    filename = os.path.join('data', '240228_#313.lif')
else:
    filename = sys.argv[-1]

reader = read_lif.Reader(filename)
headers = reader.getSeriesHeaders()
series = reader.getSeries()

iSerie = 2
# print(dir(headers[iSerie]))

# dimensions
dims = headers[iSerie].getDimensions()
DIMS = []
for dim in dims:
    d0 = float(dim.getAttribute('Origin'))
    length = float(dim.getAttribute('Length'))
    N = int(dim.getAttribute('NumberOfElements'))
    print(d0, length, N)
    DIMS.append(np.linspace(d0, d0+length, N))

X, Y, Z = np.meshgrid(*DIMS, indexing='ij')

# Series 004, 24/02/28 #313 --> series[2].getFrame(channel=1)
# channel 0 -> TdTomato
# channel 1 -> GFP
TdTomato_img = series[iSerie].getFrame(channel=0,
                                       dtype=np.uint16).T # NEED TO RESHAPE HERE
GFP_img = series[iSerie].getFrame(channel=1, dtype=np.uint16)

# threshold the TdTomato image
factor = 20.
thresh = np.median(TdTomato_img.flatten())+factor*np.std(TdTomato_img.flatten())

cond = TdTomato_img>thresh

# X, Y, Z = np.meshgrid(
# # plot
# plt.imshow(np.std(img[:,:,:], axis=0), interpolation=None, cmap=plt.cm.binary)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(121, projection='3d')
ax.scatter(X[cond], Y[cond], Z[cond], 'k.', s=0.1)
ax2 = fig.add_subplot(122)
ax2.plot(X[cond].flatten(), Y[cond].flatten(), '.', ms=0.1)

plt.show()
