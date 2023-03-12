import math
import re

from CutAndExport.Histogram import HistogramResult
from DataStructure.EventSet import EventSet
from Interfaces.LHCOlympics import LoadLHCOlympics, SaveToLHCO


def ReadCSVFile(fileName: str, startIdx: int, endIdx: int) -> list:
    dataSample = []
    with open(fileName) as f:
        for lines in f.readlines():
            strList = lines.split(',')
            if len(strList) > endIdx:
                numberList = []
                for j in range(startIdx, endIdx + 1):
                    numberList = numberList + [float(strList[j])]
                dataSample = dataSample + [numberList]
    return dataSample


def SaveCSVFile(fileName: str, content: list, startIdx: int, endIdx: int):
    with open(fileName, 'w') as f:
        for line in content:
            if len(line) > endIdx:
                for i in range(startIdx, endIdx + 1):
                    if i == endIdx:
                        f.write(str(line[i]) + "\n")
                    else:
                        f.write(str(line[i]) + ", ")


def SaveCSVFileA(fileName: str, content: list, startIdx: int, endIdx: int):
    with open(fileName, 'a') as f:
        for line in content:
            if len(line) > endIdx:
                for i in range(startIdx, endIdx + 1):
                    if i == endIdx:
                        f.write(str(line[i]) + "\n")
                    else:
                        f.write(str(line[i]) + ", ")


def CombineEventsLHCO(fileNames: list, targetFileName: str):
    eventAll = EventSet()
    for fileName in fileNames:
        eventToAdd = LoadLHCOlympics(fileName)
        print("Adding {} ({} events)...".format(fileName, eventToAdd.GetEventCount()))
        eventAll.AddEventSet(eventToAdd)
    SaveToLHCO(targetFileName, eventAll)
    eventVerify = LoadLHCOlympics(targetFileName)
    print("Verify: {} ({} events)...".format(targetFileName, eventVerify.GetEventCount()))


def PrintLogTxt(fileName: str):
    lineNumber = 0
    lstA = []
    lstB = []
    with open(fileName) as f:
        for lines in f.readlines():
            lineNumber = lineNumber + 1
            if 1 == lineNumber:
                continue
            linesrep = re.sub("[\\s]+", " ", lines)
            contentList = linesrep.split(' ')
            if 3 <= len(contentList):
                lstA.append(float(contentList[1]))
                lstB.append(float(contentList[2]))
    print(lstA)
    print(lstB)


def HistogramStrict(valueList: list, minValue: float, maxValue: float, groupCount: int = 100):
    import matplotlib.pyplot as plt
    separate = (maxValue - minValue) / groupCount
    listCount = [0 for i in range(groupCount)]
    for v in valueList:
        lstIdx = 0 if separate < 1.0e-22 else math.floor((v - minValue) / separate)
        if 0 <= lstIdx < groupCount:
            listCount[lstIdx] += 1
    plt.hist(valueList, groupCount)
    plt.show()
    return HistogramResult(groupCount, [minValue, maxValue], listCount)
