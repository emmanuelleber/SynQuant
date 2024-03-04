import sys
import read_lif
import matplotlib.pylab as plt
import numpy as np

filename = sys.argv[-1]

reader = read_lif.Reader(filename)
series = reader.getSeries()

# import matplotlib.pylab as plt
# plt.imshow(series[2].getFrame(T=0, channel=0)[0,:,:])
# plt.show()

img = series[2].getFrame(channel=1)[:,::10,::10]
print(img.shape)
