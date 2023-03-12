import os
import numpy as np

#################################################################

k = 32
saveStart = 1
saveEnd = 3
energy = "1500"
readfileName = "FT0"


#################################################################

os.chdir("../../")

for n in range(0, 21):
    allList = []
    filehead = "_DataFolder/kmeans/kmeans/csq/{0}-{1}-{2}".format(readfileName, energy, n)
    for i in range(0, saveEnd - saveStart + 1):
        oneLine = np.loadtxt("{0}-{1}.csv".format(filehead, i + saveStart), delimiter=',')
        allList.append(oneLine.tolist())
    print(n, " finished")
    allArray = np.array(allList)
    np.savetxt("_DataFolder/kmeans/kmeans/csq/{1}-{0}-{2}-all.csv".format(energy, readfileName, n), allArray.astype(int), delimiter=',', fmt='%i')
