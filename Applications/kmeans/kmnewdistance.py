import os
import numpy as np
from Applications.kmeans.kmeansfunctions import HistoryMean, CalculateDistanceD, CalculateCenterListD, \
    CalculateDistanceD2
from CutAndExport.Histogram import HistogramWithMinMaxList

#################################################################
k = 50
centercount = 200
dim = 12

#################################################################
os.chdir("../../")

for ener in ["1500", "5000", "7000", "15000"]:
    centerData = np.loadtxt("_DataFolder/kmeans/kmeans/SMCenters/SM-{0}.csv".format(ener, k), delimiter=',')
    for fthead in ["FT9"]:
        for n in range(0, 21):
            data = np.loadtxt("_DataFolder/kmeans/cs/E{0}/{1}/{1}-{0}-{2}.csv".format(ener, fthead, n), delimiter=',')
            distanceAll = []
            for i in range(0, 200):
                distanceAll.append(CalculateDistanceD2(data, dim, k, centerData[(i*k):((i+1)*k), :]))
                print("{1}-{0}-{2}-{3}-{4} finished".format(ener, fthead, k, n, i))
            distanceAllArray = np.array(distanceAll)
            allMean = np.mean(distanceAllArray, axis=0)
            np.savetxt("_DataFolder/kmeans/newdistances/E{0}/{1}/{1}-{0}-{2}-{3}-meandist.csv".format(ener, fthead, k, n), allMean, delimiter=',', fmt='%f')
            print("{1}-{0}-{2}-{3}-meandist.csv saved!".format(ener, fthead, k, n))
            # res1 = HistogramWithMinMaxList(allMean, [2000, 20000], 50)
            # print(res1.listCount)

