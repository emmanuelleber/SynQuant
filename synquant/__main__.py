import sys
import read_lif
import matplotlib.pylab as plt
import numpy as np

filename = sys.argv[-1]

reader = read_lif.Reader(filename)
series = reader.getSeries()

print(len(series))
# Series 004, 24/02/28 #313 --> series[2].getFrame(channel=1)
# channel 0 -> TdTomato
# channel 1 -> GFP
img = series[2].getFrame(channel=1, dtype=np.uint16)
print(img.shape)

# plot
fig, AX = plt.subplots(1, 2)

AX[0].set_title('mean')
AX[0].imshow(np.mean(img[:,:,:], axis=0), interpolation=None, cmap=plt.cm.binary)
AX[0].axis('off')

AX[1].set_title('std')
AX[1].imshow(np.std(img[:,:,:], axis=0), interpolation=None, cmap=plt.cm.binary)
AX[1].axis('off')
plt.show()

