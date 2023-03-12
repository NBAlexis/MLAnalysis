import os
import numpy as np

from Applications.kmeans.kmeansfunctions import KMeans, CalculateDistance
from CutAndExport.Histogram import HistogramWithMinMaxList

#################################################################
k = 50
saveStart = 124
saveEnd = 125
readfileName = "SM-7000"


#################################################################

os.chdir("../../")
dim = 12
data = np.loadtxt("_DataFolder/kmeans/cs/SM/{0}.csv".format(readfileName), delimiter=',')

averageDistance = []
for i in range(0, saveEnd - saveStart + 1):
    succeed = False
    while not succeed:
        succeed = KMeans(data, dim, k, 600)
        if not succeed:
            print("zero type encountered, give up")
    np.savetxt("_DataFolder/kmeans/{0}-{1}-{2}.csv".format(readfileName, k, i + saveStart),
               data[:, dim].astype(int), delimiter=',', fmt='%i')
    distance = CalculateDistance(data, dim, k)
    averageDistance.append(distance)
    print(i + saveStart, " finished({0}/{1})".format(i + 1, saveEnd - saveStart + 1))

"""
npAllDistance = np.array(averageDistance)
npAllDistance = np.transpose(npAllDistance)
npAverageDistance = np.mean(npAllDistance, axis=1)

smDistance = npAverageDistance[0:600000]
npDistance = npAverageDistance[600000:630000]

print(np.max(smDistance))
print(np.max(npDistance))
res1 = HistogramWithMinMaxList(smDistance, [2000, 20000], 50)
print(res1.listCount)
res2 = HistogramWithMinMaxList(npDistance, [2000, 20000], 50)
print(res2.listCount)
"""