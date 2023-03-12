###################################
# data are orgnized as
# data[point1, point2, point3, ...]
# point = [x1, x2, x3, ... ,xN]
# or point = [x1, x2, x3, ... ,xN, type1]
###################################
from Applications.IsolationForest.IsolateTree import IsolateTree
from UsefulFunctions import *

# =============== WW 用这个 ===============
N = 18
csvFileName = "a4.csv"
saveCSVFileName = "historya4-1.csv"

dataSample = ReadCSVFile(csvFileName, 0, N + 2)
print(len(dataSample))
loopCount = 10
histList = [[0 for i in range(0, loopCount + 1)] for j in range(0, len(dataSample))]
for n in range(0, loopCount):
    if 0 == n:
        for i in range(0, len(dataSample)):
            histList[i][0] = dataSample[i][N]
    print("==================={}===================\n".format(n))
    rootTree = IsolateTree(dataSample, N, -1)
    while rootTree.canSplit:
        rootTree.Split()
    rootTree.SetDepth(dataSample, N + 2, 0)
    for i in range(0, len(dataSample)):
        histList[i][n + 1] = dataSample[i][N + 2]

SaveCSVFile(saveCSVFileName, histList, 0, loopCount)
