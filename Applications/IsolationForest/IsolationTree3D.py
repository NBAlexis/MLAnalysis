###################################
# data are orgnized as
# data[point1, point2, point3, ...]
# point = [x1, x2, x3, ... ,xN]
# or point = [x1, x2, x3, ... ,xN, type1]
###################################
from Applications.IsolationForest.IsolateTree import IsolateTree
from UsefulFunctions import *

# =============== WW 用这个 ===============
N = 2
csvFileName = "v0event2d.csv"
saveCSVFileName = "resultv0-2d.csv"

dataSample = ReadCSVFile(csvFileName, 0, N + 2)

loopCount = 100
for n in range(0, loopCount):
    print("==================={}===================\n".format(n))
    rootTree = IsolateTree(dataSample, N, -1)
    while rootTree.canSplit:
        rootTree.Split()
    rootTree.SetDepth(dataSample, N + 2, 0)
    for point in dataSample:
        point[N + 1] = point[N + 1] + point[N + 2]

for point in dataSample:
    point[N + 1] = point[N + 1] / loopCount

minNor = 0
averageNor = 0
countNor = 0
minAnorm = 0
maxAnorm = 0
averAnorm = 0
countAnorm = 0
for thePoint in dataSample:
    if 0 == thePoint[N] or 1 == thePoint[N]:
        if countNor == 0 or minNor > thePoint[N + 1]:
            minNor = thePoint[N + 1]
        averageNor = averageNor + thePoint[N + 1]
        countNor = countNor + 1
    else:
        if countAnorm == 0 or minAnorm > thePoint[N + 1]:
            minAnorm = thePoint[N + 1]
        if countAnorm == 0 or maxAnorm < thePoint[N + 1]:
            maxAnorm = thePoint[N + 1]
        averAnorm = averAnorm + thePoint[N + 1]
        countAnorm = countAnorm + 1

averageNor = averageNor / countNor
averAnorm = averAnorm / countAnorm
print("Normal", minNor, averageNor, "Anormaly", minAnorm, maxAnorm, averAnorm)
SaveCSVFile(saveCSVFileName, dataSample, 0, N + 1)
