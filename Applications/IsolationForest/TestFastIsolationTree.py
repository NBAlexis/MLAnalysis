
##################################
# Generate test data
##################################
import math
from random import uniform, randint

import numpy as np

from Applications.IsolationForest.IsolateTree import IsolateTree
from Interfaces.UsefulFunctions import HistogramStrict

datasetCount = 800
loopCount = 10000
testList = []
for i in range(0, datasetCount):
    r = uniform(-1.0, 1.0)
    phi = uniform(0.0, 2 * math.pi)
    x = r * math.sin(phi)
    y = r * math.cos(phi)
    testList.append([x, y, 0, 0, 0])

##################################
# 1000 trees for 1
##################################
depthtable1 = [[0 for _ in range(0, loopCount)] for _ in range(0, datasetCount)]
for i in range(0, loopCount):
    print("old tree ", i)
    tree = IsolateTree(testList, 2, -2)
    while tree.canSplit:
        tree.Split()
    tree.SetDepth(depthtable1, i, 0)

deptharray1 = np.array(depthtable1)
avearray1 = np.mean(deptharray1, 1)
# print(avearray1)


##################################
class IsolationTree2:

    def __init__(self, dataArray, length: int, depth: int, limits: list):
        self.data = dataArray
        self.count = len(dataArray)
        self.len = length
        self.limits = limits
        self.depth = depth

    # Expecting N = len(-)
    # data[:, 0] is order
    # data[:, 1-N] is attribute
    # data[:, N+1] is tag
    # data[:, N+2] is tree depth
    def OneSplit(self):
        if self.count < 3:
            print("Error: length < 3")
            return [None, None]
        l = 0
        while 0 == l:
            idx = 1 + randint(0, self.len - 1)
            if self.limits[idx - 1] is None:
                minV = np.min(self.data[:, idx])
                maxV = np.max(self.data[:, idx])
                self.limits[idx - 1] = [minV, maxV]
            else:
                minV = self.limits[idx - 1][0]
                maxV = self.limits[idx - 1][1]
            midV = uniform(minV, maxV)
            cond = self.data[:, idx] > midV
            array1 = self.data[cond]
            array2 = self.data[~cond]
            l = len(array1) * len(array2)
            # print("retry: {} to {} {} idx:{} v:{} min:{} max:{}".format(len(theArray), len(array1), len(array2), idx, midV, minV, maxV))
            # print(theArray)
        # print("Split {} to {} {} with idx:{} v:{} depth:{}".format(len(theArray), len(array1), len(array2), idx, midV, depth))
        newlim1 = [np.min(array1[:, idx]), maxV]
        newlim2 = [minV, np.max(array2[:, idx])]
        list1 = self.limits.copy()
        list1[idx - 1] = newlim1
        list2 = self.limits.copy()
        list2[idx - 1] = newlim2
        return [IsolationTree2(array1, self.len, self.depth + 1, list1),
                IsolationTree2(array2, self.len, self.depth + 1, list2)]

    def MinMax(self, idx: int):
        if self.limits[idx - 1] is None:
            self.limits[idx - 1] = [np.min(self.data[:, idx]), np.max(self.data[:, idx])]
        return self.limits[idx - 1]


def Split(dataArray, length: int, maxSplit: int):
    dataArrayPrepared = np.insert(dataArray, 0, np.arange(0, len(dataArray)), 1)
    limits = []
    for i in range(0, length):
        limits.append(None)
    arrayLst = [IsolationTree2(dataArrayPrepared, length, 0, limits)]
    resArray = None
    step = 1
    while len(arrayLst) > 0 and (maxSplit < 0 or step < maxSplit):
        if 0 == (step % 20):
            print("-----------step:{} remaining:{} finished:{}-----------".format(step, len(arrayLst),
                                                                                  0 if resArray is None else len(
                                                                                      resArray)))
        nextArrayLst = []
        thisRun = None
        for toSplitArray in arrayLst:
            splitList = toSplitArray.OneSplit()
            if 2 == len(splitList):
                for retArray in splitList:
                    if retArray.count > 3:
                        nextArrayLst.append(retArray)
                        continue
                    if retArray.count == 3:
                        depth = retArray.depth
                        idx = 1 + randint(0, length - 1)
                        [minV, maxV] = retArray.MinMax(idx)
                        midV = uniform(minV, maxV)
                        splited = False
                        data3 = retArray.data
                        if (data3[0, idx] > midV >= data3[1, idx] and data3[2, idx] <= midV) \
                                or (data3[0, idx] <= midV < data3[1, idx] and data3[2, idx] > midV):
                            data3[0, length + 2] = depth + 1
                            data3[1, length + 2] = depth + 2
                            data3[2, length + 2] = depth + 2
                            splited = True
                        elif (data3[1, idx] > midV >= data3[2, idx] and data3[0, idx] <= midV) \
                                or (data3[1, idx] <= midV < data3[2, idx] and data3[0, idx] > midV):
                            data3[0, length + 2] = depth + 2
                            data3[1, length + 2] = depth + 1
                            data3[2, length + 2] = depth + 2
                            splited = True
                        elif (data3[2, idx] > midV >= data3[0, idx] and data3[1, idx] <= midV) \
                                or (data3[2, idx] <= midV < data3[0, idx] and data3[1, idx] > midV):
                            data3[0, length + 2] = depth + 2
                            data3[1, length + 2] = depth + 2
                            data3[2, length + 2] = depth + 1
                            splited = True
                        if splited:
                            if thisRun is None:
                                thisRun = data3
                            else:
                                thisRun = np.append(thisRun, data3, 0)
                        else:
                            nextArrayLst.append(retArray)
                        # """
                    elif retArray.count == 2:
                        retArray.data[:, length + 2] = retArray.depth + 1
                        if thisRun is None:
                            thisRun = retArray.data
                        else:
                            thisRun = np.append(thisRun, retArray.data, 0)
                    elif retArray.count == 1:
                        retArray.data[0, length + 2] = retArray.depth
                        if thisRun is None:
                            thisRun = retArray.data
                        else:
                            thisRun = np.append(thisRun, retArray.data, 0)
            else:
                print("Error: return of OneSplit is not 2")
        arrayLst = nextArrayLst
        if thisRun is not None:
            if resArray is None:
                resArray = thisRun
            else:
                resArray = np.append(resArray, thisRun, 0)
        step = step + 1
    for leftArray in arrayLst:
        resArray = np.append(resArray, leftArray.data, 0)
    orders = np.argsort(resArray[:, 0])
    resArray = resArray[orders]
    return np.delete(resArray, 0, 1)
##################################

##################################
# 1000 trees for 2
##################################
testArray = np.array(testList)
depthtable2 = [[0 for _ in range(0, loopCount)] for _ in range(0, datasetCount)]
deptharrray2 = np.array(depthtable2)
for i in range(0, loopCount):
    print("new tree ", i)
    resSet = Split(testArray, 2, -1)
    deptharrray2[:, i] = resSet[:, 3]

avearray2 = np.mean(deptharrray2, 1)

print(avearray1)
print(avearray2)
print(np.average(avearray1 - avearray2))
HistogramStrict(list(avearray1 - avearray2), -0.2, 0.2, 50)
print(np.max(np.abs(avearray1 - avearray2)))

