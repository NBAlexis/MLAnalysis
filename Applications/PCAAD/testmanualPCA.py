import numpy as np
from matplotlib import pyplot as plt

from Applications.PCAAD.pcaadfunctions import ZScoreStandardize, ManualPCA
from CutAndExport.Histogram import HistogramWithMinMaxList

energy = 1500
data1 = np.loadtxt("../../_DataFolder/kmeans/cs/SM/SM-{0}.csv".format(energy), delimiter=',')
data1 = data1[:, 0:12]
data2 = np.loadtxt("../../_DataFolder/kmeans/cs/FT0/FT0-{0}.csv".format(energy), delimiter=',')
data2 = data2[:, 0:12]

data1, data2 = ZScoreStandardize(data1, data2)
data1, data2 = ManualPCA(data1, data2, 12)

# plt.hist(data1[:, 0], 50)
# plt.show()
# plt.hist(data2[:, 0], 50)
# plt.show()

# plt.hist(data1[:, 1], 50)
# plt.show()
# plt.hist(data2[:, 1], 50)
# plt.show()

# plt.hist(data1[:, 2], 50)
# plt.show()
# plt.hist(data2[:, 2], 50)
# plt.show()

res1 = HistogramWithMinMaxList(data1[:, 0].tolist(), [-2, 6], 40)
print(res1.listCount)
res2 = HistogramWithMinMaxList(data2[:, 0].tolist(), [-2, 6], 40)
print(res2.listCount)

stds = np.std(data1, axis=0)
sumstds = np.sum(stds * stds)
plt.bar([i for i in range(0, len(data1[0]))], stds * stds / sumstds)
plt.show()
