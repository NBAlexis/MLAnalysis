import os

import numpy as np
from matplotlib import pyplot as plt

checklst = [2, 4, 8, 16, 32, 64, 128, 1024, 2048, 4096]
os.chdir("../../")
averagem = []
averagec = []
averagecm = []
for i in range(0, len(checklst)):
    ms = np.loadtxt("_DataFolder/kmeans/qkmeans/Measures/SM-1500_m_{0}_1.csv".format(checklst[i]),
                    delimiter=',').astype(int)
    cs = np.loadtxt("_DataFolder/kmeans/qkmeans/Measures/SM-1500_p_{0}_1.csv".format(checklst[i]),
                    delimiter=',').astype(float)
    averagem.append(np.mean(ms))
    averagec.append(np.mean(cs))
    averagecm.append(np.mean(ms / cs))
    # plt.hist2d(ms, cs, 50)
    # plt.show()

print([averagem[i + 1] / averagem[i] for i in range(0, len(averagem) - 1)])
print([averagecm[i + 1] / averagecm[i] for i in range(0, len(averagecm) - 1)])
print(averagem)
print(averagec)
print(averagecm)

plt.plot(checklst, averagem)
plt.show()
plt.plot(checklst, averagec)
plt.show()
plt.plot(checklst, averagecm)
plt.show()
