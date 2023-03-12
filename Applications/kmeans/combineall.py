import os
import numpy as np

#################################################################

k = 50
saveStart = 1
saveEnd = 200
energy = "5000"
readfileName = "FT9"


#################################################################

os.chdir("../../")

for n in range(0, 21):
    allList = []
    filehead = "_DataFolder/kmeans/{0}-{1}-{2}".format(readfileName, energy, n)
    for i in range(0, saveEnd - saveStart + 1):
        oneLine = np.loadtxt("{0}/{1}-{2}-{3}-{4}-{5}.csv".format(filehead, readfileName, energy, k, n, i + saveStart), delimiter=',')
        allList.append(oneLine.tolist())
    print(n, " finished")
    allArray = np.array(allList)
    np.savetxt("_DataFolder/kmeans/kmeans/E{0}/{1}/{1}-{0}-{2}-{3}-all.csv".format(energy, readfileName, k, n), allArray.astype(int), delimiter=',', fmt='%i')
