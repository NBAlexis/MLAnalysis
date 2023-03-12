import numpy as np
from matplotlib import pyplot as plt

coefflist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k = 256
ft = 0
energy = 1500
measure = 1
threshhold = 0.7

pointCount = []
for coef in coefflist:
    meanDist = np.loadtxt("../../_DataFolder/qkmeans/distance/E{0}/FT{1}/FT{1}-{0}-{2}_{3}_{4}_mean.csv".format(energy, ft, coef, k, measure), delimiter=',')
    pointCount.append(len(meanDist[meanDist < threshhold]))

print(pointCount)
plt.plot(coefflist, pointCount)
plt.show()
