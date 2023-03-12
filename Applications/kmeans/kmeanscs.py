import os
import numpy as np

from Applications.kmeans.kmeansfunctions import KMeans, CalculateDistance
from CutAndExport.Histogram import HistogramWithMinMaxList

#################################################################
k = 50
saveStart = 1
saveEnd = 10


#################################################################

os.chdir("../../")
dim = 12
for n in range(0, 11):
    data = np.loadtxt("_DataFolder/kmeans/cs/E15000/FT0/FT0-15000-{0}.csv".format(n), delimiter=',')
    averageDistance = []
    for i in range(0, saveEnd - saveStart + 1):
        succeed = False
        while not succeed:
            succeed = KMeans(data, dim, k, 1000)
            if not succeed:
                print("zero type encountered, give up")
        np.savetxt("_DataFolder/kmeans/FT0-15000-{0}-{1}-{2}.csv".format(n, k, i + saveStart),
                   data[:, dim].astype(int), delimiter=',', fmt='%i')
        distance = CalculateDistance(data, dim, k)
        averageDistance.append(distance)
        print(i + saveStart, " finished({0}/{1})".format(i + 1, saveEnd - saveStart + 1))
    npAllDistance = np.array(averageDistance)
    npAllDistance = np.transpose(npAllDistance)
    npAverageDistance = np.mean(npAllDistance, axis=1)
    res1 = HistogramWithMinMaxList(npAverageDistance, [2000, 20000], 50)
    print(res1.listCount)
