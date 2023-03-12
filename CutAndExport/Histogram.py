import math

from DataStructure import Constants
from DataStructure.EventSet import EventSet


class HistogramResult:
    def __init__(self, count: int, minMax, listCount):
        self.count = count
        self.minMax = minMax
        self.listCount = listCount


def GatherNumbers(eventSet: EventSet, filterFunc, groupCount: int = 100):
    valueList = []
    minValue = 0.0
    maxValue = 0.0
    minMaxSet = False
    for eventSample in eventSet.events:
        eventValue = filterFunc(eventSample)
        if eventValue < minValue or (not minMaxSet):
            minValue = eventValue
        if eventValue > maxValue or (not minMaxSet):
            maxValue = eventValue
        minMaxSet = True
        valueList.append(eventValue)
    separate = (maxValue - minValue) / groupCount
    listCount = [0 for i in range(groupCount)]
    for v in valueList:
        lstIdx = math.floor((v - minValue) / separate)
        if lstIdx < 0:
            lstIdx = 0
        if lstIdx >= groupCount:
            lstIdx = groupCount - 1
        listCount[lstIdx] += 1
    return HistogramResult(groupCount, [minValue, maxValue], listCount)


def Histogram(eventSet: EventSet, filterFunc, groupCount: int = 100):
    import matplotlib.pyplot as plt
    valueList = []
    minValue = 0.0
    maxValue = 0.0
    minMaxSet = False
    for eventSample in eventSet.events:
        eventValue = filterFunc(eventSample)
        if eventValue < minValue or (not minMaxSet):
            minValue = eventValue
        if eventValue > maxValue or (not minMaxSet):
            maxValue = eventValue
        minMaxSet = True
        valueList.append(eventValue)
    separate = (maxValue - minValue) / groupCount
    listCount = [0 for i in range(groupCount)]
    for v in valueList:
        lstIdx = 0 if separate < Constants.minFloat else math.floor((v - minValue) / separate)
        if lstIdx < 0:
            lstIdx = 0
        if lstIdx >= groupCount:
            lstIdx = groupCount - 1
        listCount[lstIdx] += 1
    plt.hist(valueList, groupCount)
    plt.show()
    return HistogramResult(groupCount, [minValue, maxValue], listCount)


def HistogramWithMinMax(eventSet: EventSet, filterFunc, minMax, groupCount: int = 100):
    import matplotlib.pyplot as plt
    valueList = []
    valueListAll = []
    for eventSample in eventSet.events:
        eventValue = filterFunc(eventSample)
        if minMax[1] > eventValue > minMax[0]:
            valueList.append(eventValue)
        valueListAll.append(eventValue)
    separate = (minMax[1] - minMax[0]) / groupCount
    listCount = [0 for i in range(groupCount)]
    for v in valueList:
        lstIdx = 0 if separate < Constants.minFloat else math.floor((v - minMax[0]) / separate)
        if lstIdx < 0:
            lstIdx = 0
        if lstIdx >= groupCount:
            lstIdx = groupCount - 1
        listCount[lstIdx] += 1
    plt.hist(valueListAll, groupCount)
    plt.show()
    return HistogramResult(groupCount, minMax, listCount)


def HistogramWithMinMaxList(dataList, minMax, groupCount: int = 100):
    import matplotlib.pyplot as plt
    valueList = []
    valueListAll = []
    for eventValue in dataList:
        if minMax[1] > eventValue > minMax[0]:
            valueList.append(eventValue)
        valueListAll.append(eventValue)
    separate = (minMax[1] - minMax[0]) / groupCount
    listCount = [0 for i in range(groupCount)]
    for v in valueList:
        lstIdx = 0 if separate < Constants.minFloat else math.floor((v - minMax[0]) / separate)
        if lstIdx < 0:
            lstIdx = 0
        if lstIdx >= groupCount:
            lstIdx = groupCount - 1
        listCount[lstIdx] += 1
    plt.hist(valueListAll, groupCount)
    plt.show()
    return HistogramResult(groupCount, minMax, listCount)
