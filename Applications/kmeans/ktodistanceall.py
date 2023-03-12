import os
import numpy as np
from Applications.kmeans.kmeansfunctions import HistoryMean, CalculateDistanceD, CalculateCenterListD
from CutAndExport.Histogram import HistogramWithMinMaxList

#################################################################
k = 50
energy = "5000"
readfileName = "FT9"

#################################################################
os.chdir("../../")
dim = 12

for n in range(0, 21):
    data = np.loadtxt("_DataFolder/kmeans/cs/E{0}/{1}/{1}-{0}-{2}.csv".format(energy, readfileName, n), delimiter=',')
    kmeansData = np.loadtxt("_DataFolder/kmeans/kmeans/E{0}/{1}/{1}-{0}-{2}-{3}-all.csv".format(energy, readfileName, k, n), delimiter=',')
    distanceAll = []
    for i in range(0, len(kmeansData)):
        data[:, dim] = kmeansData[i, :]
        centersAll = CalculateCenterListD(data, dim, k)
        distanceAll.append(CalculateDistanceD(data, dim, centersAll))
    distanceAllArray = np.array(distanceAll)
    allMean = np.mean(distanceAllArray, axis=0)
    np.savetxt("_DataFolder/kmeans/distances/E{0}/{1}/{1}-{0}-{2}-{3}-meandist.csv".format(energy, readfileName, k, n), allMean, delimiter=',', fmt='%f')
    res1 = HistogramWithMinMaxList(allMean, [2000, 20000], 50)
    print(res1.listCount)
