import os
import numpy as np
from Applications.kmeans.kmeansfunctions import HistoryMean, CalculateDistanceD, CalculateCenterListD, \
    CalculateCenterListDQ, CalculateDistanceDQ
from CutAndExport.Histogram import HistogramWithMinMaxList

#################################################################
k = 32
energy = "1500"
readfileName = "FT0"

#################################################################
os.chdir("../../")
dim = 12

for n in range(0, 21):
    data = np.loadtxt("_DataFolder/kmeans/cs/csq/{1}-{0}-{2}.csv".format(energy, readfileName, n), delimiter=',')
    kmeansData = np.loadtxt("_DataFolder/kmeans/kmeans/csq/{1}-{0}-{2}-all.csv".format(energy, readfileName, n), delimiter=',').astype(int)
    distanceAll = []
    for i in range(0, len(kmeansData)):
        centersAll = CalculateCenterListDQ(data, kmeansData[i], k)
        distanceAll.append(CalculateDistanceDQ(data, kmeansData[i], centersAll))
    distanceAllArray = np.array(distanceAll)
    allMean = np.mean(distanceAllArray, axis=0)
    np.savetxt("_DataFolder/kmeans/distances/csq/{1}-{0}-{2}-meandist.csv".format(energy, readfileName, n), allMean, delimiter=',', fmt='%f')
    res1 = HistogramWithMinMaxList(allMean, [2000, 20000], 50)
    print(res1.listCount)
