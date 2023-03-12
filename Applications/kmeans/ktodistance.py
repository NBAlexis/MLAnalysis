import os
import numpy as np

#################################################################
from Applications.kmeans.kmeansfunctions import HistoryMean, CalculateDistanceD, CalculateCenterListD, \
    CalculateDistanceD2
from CutAndExport.Histogram import HistogramWithMinMaxList

k = 50
readfileNameSM = "SM-1500"
readfileNameFT0 = "FT0-1500"
historyCheck = [0, 1]

#################################################################
os.chdir("../../")
dim = 12
dataSM = np.loadtxt("_DataFolder/kmeans/cs/SM/{0}.csv".format(readfileNameSM), delimiter=',')
dataFT0 = np.loadtxt("_DataFolder/kmeans/cs/FT0/{0}.csv".format(readfileNameFT0), delimiter=',')
kmeansData = np.loadtxt("_DataFolder/kmeans/kmeans/SM/{0}-{1}-all.csv".format(readfileNameSM, k), delimiter=',')


distanceAllSM = []
distanceAllFT0 = []
for i in range(0, len(kmeansData)):
    dataSM[:, dim] = kmeansData[i, :]
    centersAll = CalculateCenterListD(dataSM, dim, k)
    distanceAllSM.append(CalculateDistanceD(dataSM, dim, centersAll))
    distanceAllFT0.append(CalculateDistanceD2(dataFT0, dim, k, centersAll))
    print(i, " finished")

distanceAllSMArray = np.array(distanceAllSM)
distanceAllFT0Array = np.array(distanceAllFT0)

allMeanSM = np.mean(distanceAllSMArray, axis=0)
np.savetxt("_DataFolder/kmeans/distances/SM/{0}-{1}-meandist.csv".format(readfileNameSM, k), allMeanSM, delimiter=',', fmt='%f')
allMeanFT0 = np.mean(distanceAllFT0Array, axis=0)
np.savetxt("_DataFolder/kmeans/distances/FT0/{0}-{1}-meandist.csv".format(readfileNameFT0, k), allMeanFT0, delimiter=',', fmt='%f')
allStdSM = np.std(distanceAllSMArray, axis=0)
allStdFT0 = np.std(distanceAllFT0Array, axis=0)
relativeErrorSM = allStdSM / allMeanSM / np.sqrt(200.0)
relativeErrorFT0 = allStdFT0 / allMeanFT0 / np.sqrt(200.0)

np.savetxt("_DataFolder/kmeans/distances/SM/{0}-{1}-relativeerr.csv".format(readfileNameSM, k), relativeErrorSM, delimiter=',', fmt='%f')
np.savetxt("_DataFolder/kmeans/distances/FT0/{0}-{1}-relativeerr.csv".format(readfileNameFT0, k), relativeErrorFT0, delimiter=',', fmt='%f')

print("min and max error of SM:")
print(np.min(relativeErrorSM))
print(np.max(relativeErrorSM))
print(np.mean(relativeErrorSM))
print("min and max error of FT0:")
print(np.min(relativeErrorFT0))
print(np.max(relativeErrorFT0))
print(np.mean(relativeErrorFT0))

historyList = []
for idx in historyCheck:
    oneLineSM = distanceAllSMArray[:, idx]
    historyList.append(HistoryMean(oneLineSM))

for idx in historyCheck:
    oneLineFT0 = distanceAllFT0Array[:, idx]
    historyList.append(HistoryMean(oneLineFT0))

historyArray = np.array(historyList)
np.savetxt("_DataFolder/kmeans/distances/SM/{0}-{1}-hist.csv".format(readfileNameSM, k), historyArray, delimiter=',', fmt='%f')

print(np.max(allMeanSM))
print(np.max(allMeanFT0))
res1 = HistogramWithMinMaxList(allMeanSM, [1000, 6000], 50)
print(res1.listCount)
res2 = HistogramWithMinMaxList(allMeanFT0, [1000, 6000], 50)
print(res2.listCount)

"""
==================================================================
k=2

-----------------
E=1500
min and max error of SM:
2.2760602312498263e-07
2.646471582156895e-05
1.345308823013409e-05
min and max error of FT0:
2.670779604351927e-07
2.445729347671596e-05
8.044945218294027e-06

-----------------
E=5000
min and max error of SM:
2.1471596674384433e-07
2.7847221383284876e-05
1.2404062419583242e-05
min and max error of FT0:
2.0095611366491457e-07
2.2643298685504284e-05
6.874057399474505e-06

-----------------
E=7000
min and max error of SM:
2.06608357330886e-07
3.0454891032136387e-05
1.4588048591976535e-05
min and max error of FT0:
3.4659336094829806e-07
2.816735639236983e-05
7.907149076918528e-06

-----------------
E=15000
min and max error of SM:
1.7480199380438368e-07
2.512896470955166e-05
1.1531147617601768e-05
min and max error of FT0:
1.3991508939714492e-07
1.9560201449308826e-05
6.065907907965431e-06

==================================================================
k=10

-----------------
E=1500
min and max error of SM:
0.0009977647842772525
0.03543202230782215
0.014067986969387136
min and max error of FT0:
0.0010698944992604954
0.029027395829476547
0.00836941244518964

-----------------
E=5000
min and max error of SM:
0.0012971476422045495
0.03646525486204744
0.01508790824922793
min and max error of FT0:
0.0013435138474222894
0.03495908526784626
0.008068131760604757

-----------------
E=7000
min and max error of SM:
0.0013132377036568544
0.03637130174953626
0.015484843916610837
min and max error of FT0:
0.0012912438924629998
0.02846678540985113
0.008074198589576701

-----------------
E=15000
min and max error of SM:
0.00136669192694088
0.036978928765416044
0.015984191313575917
min and max error of FT0:
0.001360072277049899
0.03226781076707819
0.00795259864594101

==================================================================
k=50

-----------------
E=1500
min and max error of SM:
0.001215084833118347
0.043874484056559394
0.014897237178022302
min and max error of FT0:
0.0013314090673131487
0.03034809711328204
0.008970032778331971

-----------------
E=5000
min and max error of SM:
0.0011677609161193632
0.04321387303655331
0.01642194199677601
min and max error of FT0:
0.001349433894687232
0.03128202823442869
0.009022336800875977

-----------------
E=7000
min and max error of SM:
0.0013673568858533422
0.03970107875271931
0.01670182370161456
min and max error of FT0:
0.001677638432001235
0.036175787561363186
0.008991038687100559

-----------------
E=15000
min and max error of SM:
0.0014342854535418627
0.04091758425424098
0.01727041846980621
min and max error of FT0:
0.0017413556673483298
0.031118151718157846
0.009077482481867849

"""