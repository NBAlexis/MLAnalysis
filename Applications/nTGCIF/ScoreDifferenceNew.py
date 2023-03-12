import numpy as np

from Interfaces.UsefulFunctions import HistogramStrict

counts = [88030, 87965, 87439, 87699, 87155, 87122, 87730, 87402, 87528, 87588, 87662, 87642]
crosses = [8.275856, 8.272363, 8.267634, 8.274874, 8.271893, 8.276281, 8.269379, 8.273171, 8.266279, 8.269903, 8.280688]

leftV = -0.03
rightV = 0.06
anomV = 0.58
distV = 400
leftAll = []
rightAll = []
anomalAll = []
distAll = []
sumAll = []
crossAll = []
fileName2 = "G:\\nTGCIF\\nTrees\\bs025-11-std.csv"
scoreData2 = np.loadtxt(fileName2, delimiter=',')
cn2 = 21.91647396799364
scorefunc2 = lambda a: 2 ** (-a / cn2)
vscorefunc2 = np.vectorize(scorefunc2)
for i in range(0, 11):
    fileName1 = "G:\\nTGCIF\\nTrees\\bs025-{}-std.csv".format(i)
    mapFileName = "G:\\nTGCIF\\nMaps\\bs25-{}-idx.csv".format(i)
    mapdistFileName = "G:\\nTGCIF\\nMaps\\bs25-{}-dist.csv".format(i)
    denorm = [21.92530857845518, 21.92383127208561, 21.91183613906857, 21.917774283993392,
              21.90532964689008, 21.90457223630713, 21.91848111863564, 21.910989660521036,
              21.91387079701002, 21.915241309349707, 21.91693031550424, 21.91647396799364]
    cn1 = denorm[i]
    scoreData1 = np.loadtxt(fileName1, delimiter=',')
    mapdData = np.loadtxt(mapFileName, delimiter=',').astype(int)
    mapddstData = np.loadtxt(mapdistFileName, delimiter=',')
    print("csv loaded :", i)
    scorefunc1 = lambda a: 2 ** (-a / cn1)
    vscorefunc1 = np.vectorize(scorefunc1)
    smallp = mapdData[mapddstData > distV]
    print("dist > ", distV, " :", len(smallp))
    distAll.append(len(smallp))
    score1 = vscorefunc1(scoreData1[:, 1])
    score2 = vscorefunc2(scoreData2[:, 1])
    anSrc1 = score1[score1 > anomV]
    print(len(anSrc1))
    # anSrc2 = score2[score2 > 0.65]
    # print(len(anSrc2))
    anomalAll.append(len(anSrc1))
    diff = []
    for j in range(0, len(score1)):
        # print("{}/{}", i, len(score1))
        scoreMap = score1[j] - score2[mapdData[j]]
        diff.append(scoreMap)
    # binmin = -0.1
    # binmax = 0.1
    # binsep = 40
    # histres1 = HistogramStrict(diff, binmin, binmax, binsep)
    # print(histres1.minMax)
    # print(histres1.listCount)
    # print(len(diff))
    diffar = np.array(diff)
    print(np.mean(diffar))
    leftC = diffar[diffar < leftV]
    rightC = diffar[diffar > rightV]
    print(len(leftC), len(rightC))
    leftAll.append(len(leftC))
    rightAll.append(len(rightC))
    sumAll.append(len(leftC) + len(rightC))
    crossAll.append(1000.0 * len(leftC) * crosses[i] / 1000000.0)

print("left ", leftAll)
print("right ", rightAll)
print("anomal ", anomalAll)
# print(sumAll)
print("dist ", distAll)
print(crossAll)

"""
7:
107
[-0.1, 0.1]
[0, 0, 1, 2, 4, 7, 9, 22, 42, 93, 143, 288, 594, 1158, 2476, 5450, 12524, 26759, 48429, 67320, 65648, 46679, 26865, 13809, 6877, 3403, 1900, 1052, 613, 380, 258, 151, 125, 89, 66, 50, 27, 10, 12, 11]
333365
0.0005116911809309878
2 17

8:
134
[-0.1, 0.1]
[0, 0, 2, 4, 2, 11, 6, 26, 44, 72, 140, 245, 480, 1019, 2085, 4671, 10632, 23686, 44905, 65602, 67884, 49934, 29898, 15650, 7544, 3798, 1979, 1070, 610, 423, 257, 157, 96, 83, 51, 43, 28, 23, 7, 9]
333196
0.0013281873016066665
1 19

9:
126
[-0.1, 0.1]
[0, 1, 0, 2, 3, 6, 10, 19, 44, 68, 135, 276, 474, 963, 1944, 4253, 9898, 22244, 43404, 64312, 68730, 51876, 31291, 16206, 7952, 4007, 2047, 1127, 656, 407, 288, 197, 117, 90, 55, 42, 24, 26, 15, 10]
333238
0.001716688202654305
1 18

sm:
139
[-0.1, 0.1]
[0, 1, 0, 1, 6, 7, 7, 13, 51, 66, 134, 279, 511, 1006, 2207, 4920, 11528, 25388, 47363, 67088, 66136, 48098, 28163, 14512, 7069, 3647, 1909, 1136, 677, 433, 267, 181, 106, 79, 53, 37, 29, 23, 16, 8]
333177
0.0009169533716780992
0 22

11:
137
136
[-0.1, 0.1]
[1, 1, 1, 1, 1, 2, 14, 26, 42, 69, 142, 242, 493, 960, 1975, 4242, 9869, 22065, 42742, 63953, 68806, 52642, 31697, 16309, 7856, 3932, 2013, 1185, 673, 452, 292, 196, 126, 93, 51, 47, 33, 24, 17, 7]
333308
0.0017866285897602207
1 15

12:
125
136
[-0.1, 0.1]
[0, 1, 0, 1, 5, 2, 11, 31, 53, 77, 121, 250, 521, 1026, 2048, 4706, 10848, 23766, 44976, 65284, 67172, 50536, 29663, 15153, 7537, 3794, 2121, 1187, 770, 470, 274, 202, 146, 97, 59, 50, 33, 27, 15, 6]
333059
0.0013686778452680541
1 19

13:
123
136
[-0.1, 0.1]
[0, 0, 0, 3, 5, 7, 6, 21, 31, 56, 158, 281, 492, 984, 2103, 4557, 10775, 24076, 45166, 65416, 67133, 49843, 29900, 15825, 7485, 3805, 2086, 1099, 677, 423, 254, 188, 130, 72, 48, 39, 28, 21, 17, 11]
333233
0.0013340571148983738
1 11

"""
