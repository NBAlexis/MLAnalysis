import os

import numpy as np
from matplotlib import pyplot as plt

ite = 287
kcount = 64
coeffnamelst = [0, 5]
filename = "FT0-1500-"
coefficient = 0

os.chdir("../../")

centers = np.loadtxt("_DataFolder/kmeans/qkmeans/C{0}/{1}{0}_c_{2}.csv".format(coeffnamelst[coefficient], filename, 1), delimiter=',')

disthist = []
for i in range(2, ite):
    centers2 = np.loadtxt("_DataFolder/kmeans/qkmeans/C{0}/{1}{0}_c_{2}.csv".format(coeffnamelst[coefficient], filename, i), delimiter=',')
    distlst = (centers[:, 0] - centers2[:, 0]) ** 2 \
              + (centers[:, 1] - centers2[:, 1]) ** 2 \
              + (centers[:, 2] - centers2[:, 2]) ** 2 \
              + (centers[:, 3] - centers2[:, 3]) ** 2 \
              + (centers[:, 4] - centers2[:, 4]) ** 2 \
              + (centers[:, 5] - centers2[:, 5]) ** 2 \
              + (centers[:, 6] - centers2[:, 6]) ** 2
    dist = np.sum(distlst)
    disthist.append(dist)
    # centers = centers2

print(disthist)
plt.plot(disthist)
plt.show()
