import numpy as np
from matplotlib import pyplot as plt

from Applications.PCAAD.pcaadfunctions import ManualPCAData, ManualPCATransform

"""
critiron:

1500: 1.5
15000: 0.5
"""

energy = 15000
ft = 0
critiron = 1.5
datasm = np.loadtxt("../../_DataFolder/kmeans/cs/SM/SM-{0}.csv".format(energy), delimiter=',')
datasm = datasm[:, 0:12]

means, stds, features = ManualPCAData(datasm, 1)

reslst = []

for i in range(0, 21):
    data2 = np.loadtxt("../../_DataFolder/kmeans/cs/E{1}/FT{2}/FT{2}-{1}-{0}.csv".format(i, energy, ft), delimiter=',')
    data2 = data2[:, 0:12]
    res = ManualPCATransform(data2, means, stds, features)
    res = res[:, 0]
    reslst.append(len(res[res > critiron]))

print(reslst)
plt.plot(reslst)
plt.show()






