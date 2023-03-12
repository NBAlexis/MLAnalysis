###########################################
# 1 - generate the event list
###########################################
from Applications.IsolationForest.IsolateTree import IsolateTree
from Applications.IsolationForest.UsefulFunctions import *

alphaIdx = 2
fileCount = 11
N = 6
loopCount = 10
for fileIdx in range(fileCount):
    dataSample = ChooseEventsAll("../../_DataFolder/wwaa/a" + alphaIdx + "/alpha" + alphaIdx + "-" + str(fileIdx) + ".lhco")
    for n in range(0, loopCount):
        print("==============={} - {}==============\n".format(fileIdx, n))
        rootTree = IsolateTree(dataSample, N)
        while rootTree.canSplit:
            rootTree.Split()
        rootTree.SetDepth(dataSample, N + 1, 0)
        for point in dataSample:
            point[N] = point[N] + point[N + 1]
    for point in dataSample:
        point[N] = point[N] / loopCount
        # if 0 == fileIdx:


SaveCSVFile("alpha2.csv", dataSample, N, N)
