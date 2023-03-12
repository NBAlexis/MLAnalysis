import numpy as np

pointset1 = "G:\\nTGCIF\\sm-025-0.csv"
pointset2 = "G:\\nTGCIF\\sm-025-1.csv"
testMax = -1
saveIdx = "G:\\nTGCIF\\Maps\\sm-025-0b-idx.csv"
saveDist = "G:\\nTGCIF\\Maps\\sm-025-0b-dist.csv"
bSaveDist = True


dataSet1 = np.loadtxt(pointset1, delimiter=',')
dataSet2 = np.loadtxt(pointset2, delimiter=',')
print("file loaded")
testMax = testMax if testMax > 0 else len(dataSet1)
mapList = []
distList = []
for i in range(0, testMax):
    arrayCopy = dataSet2 - dataSet1[i]
    arrayCopy = np.square(arrayCopy)
    sumres = np.sum(arrayCopy, 1)
    minIdx = np.argmin(sumres)
    dist = sumres[minIdx]
    print("{}/{} {}".format(i, testMax, dist))
    # print("p1:", dataSet1[i])
    # print("p2:", dataSet2[minIdx])
    mapList.append(minIdx)
    distList.append(dist)

np.savetxt(saveIdx, np.transpose(np.array(mapList).astype(int)), delimiter=',', fmt='%i')
if bSaveDist:
    np.savetxt(saveDist, np.transpose(np.array(distList)), delimiter=',')
