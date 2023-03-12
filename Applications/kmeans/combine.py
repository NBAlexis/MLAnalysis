import os
import numpy as np

#################################################################

k = 50
saveStart = 1
saveEnd = 200
readfileName = "SM-1500"


#################################################################

os.chdir("../../")

allList = []
for i in range(0, saveEnd - saveStart + 1):
    oneLine = np.loadtxt("_DataFolder/kmeans/{0}-{1}-{2}.csv".format(readfileName, k, i + saveStart), delimiter=',')
    allList.append(oneLine.tolist())
    print(i, " finished")

print("saving...")
allArray = np.array(allList)
np.savetxt("_DataFolder/kmeans/kmeans/SM/{0}-{1}-all.csv".format(readfileName, k), allArray.astype(int), delimiter=',', fmt='%i')
