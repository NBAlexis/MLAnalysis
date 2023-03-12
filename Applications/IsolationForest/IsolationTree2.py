import sys
from random import randint, uniform
import numpy as np

Loop = 100
fileName = "a0.csv"
saveCol = [18, 19]
saveName = "a0-hist6-"
L = 18


# Expecting N = len(-)
# data[:, 0] is order
# data[:, 1-N] is attribute
# data[:, N+1] is tag
# data[:, N+2] is tree depth
def OneSplit(theArray, length: int):
    if len(theArray) < 3:
        print("Error: length < 3")
        return
    depth = theArray[0, length + 2]
    l = 0
    while 0 == l:
        idx = 1 + randint(0, length - 1)
        minV = np.min(theArray[:, idx])
        maxV = np.max(theArray[:, idx])
        midV = uniform(minV, maxV)
        array1 = theArray[theArray[:, idx] > midV]
        array2 = theArray[theArray[:, idx] <= midV]
        array1[:, length + 2] = depth + 1
        array2[:, length + 2] = depth + 1
        l = len(array1) * len(array2)
        # print("retry: {} to {} {} idx:{} v:{} min:{} max:{}".format(len(theArray), len(array1), len(array2), idx, midV, minV, maxV))
        # print(theArray)
    # print("Split {} to {} {} with idx:{} v:{} depth:{}".format(len(theArray), len(array1), len(array2), idx, midV, depth))
    return [array1, array2]


def Split(dataArray, length: int, maxSplit: int):
    dataArrayPrepared = np.insert(dataArray, 0, np.arange(0, len(dataArray)), 1)
    dataArrayPrepared[:, length + 2] = 0
    arrayLst = [dataArrayPrepared]
    resArray = None
    step = 1
    emptyArray = np.array([])
    while len(arrayLst) > 0 and (maxSplit < 0 or step < maxSplit):
        if 0 == (step % 20):
            print("-----------step:{} remaining:{} finished:{}-----------".format(step, len(arrayLst),
                                                                                  0 if resArray is None else len(
                                                                                      resArray)))
        nextArrayLst = []
        for toSplitArray in arrayLst:
            splitList = OneSplit(toSplitArray, length)
            if 2 == len(splitList):
                for retArray in splitList:
                    if len(retArray) > 5:
                        nextArrayLst.append(retArray)
                        retArray = emptyArray
                        # """
                    elif len(retArray) == 5:
                        depth = retArray[0, length + 2]
                        idx = 1 + randint(0, length - 1)
                        minV = np.min(retArray[:, idx])
                        maxV = np.max(retArray[:, idx])
                        midV = uniform(minV, maxV)
                        array1 = retArray[retArray[:, idx] > midV]
                        array2 = retArray[retArray[:, idx] <= midV]
                        if 1 == len(array1):
                            array1[0, length + 2] = depth + 1
                            array2[0, length + 2] = depth + 1
                            retArray = array2
                            if resArray is None:
                                resArray = array1
                            else:
                                resArray = np.append(resArray, array1, 0)
                        elif 2 == len(array1):
                            array1[0, length + 2] = depth + 2
                            array2[0, length + 2] = depth + 1
                            retArray = array2
                            if resArray is None:
                                resArray = array1
                            else:
                                resArray = np.append(resArray, array1, 0)
                        elif 3 == len(array1):
                            array1[0, length + 2] = depth + 1
                            array2[0, length + 2] = depth + 2
                            retArray = array1
                            if resArray is None:
                                resArray = array2
                            else:
                                resArray = np.append(resArray, array2, 0)
                        elif 4 == len(array1):
                            array1[0, length + 2] = depth + 1
                            array2[0, length + 2] = depth + 1
                            retArray = array1
                            if resArray is None:
                                resArray = array2
                            else:
                                resArray = np.append(resArray, array2, 0)
                        else:
                            nextArrayLst.append(retArray)
                            retArray = emptyArray
                    if len(retArray) == 4:
                        depth = retArray[0, length + 2]
                        idx = 1 + randint(0, length - 1)
                        minV = np.min(retArray[:, idx])
                        maxV = np.max(retArray[:, idx])
                        midV = uniform(minV, maxV)
                        array1 = retArray[retArray[:, idx] > midV]
                        array2 = retArray[retArray[:, idx] <= midV]
                        if 1 == len(array1):
                            array1[0, length + 2] = depth + 1
                            array2[0, length + 2] = depth + 1
                            retArray = array2
                            if resArray is None:
                                resArray = array1
                            else:
                                resArray = np.append(resArray, array1, 0)
                        elif 2 == len(array1):
                            array1[0, length + 2] = depth + 2
                            array2[0, length + 2] = depth + 2
                            if resArray is None:
                                resArray = array1
                                resArray = np.append(resArray, array2, 0)
                            else:
                                resArray = np.append(resArray, array1, 0)
                                resArray = np.append(resArray, array2, 0)
                            retArray = emptyArray
                        elif 3 == len(array1):
                            array1[0, length + 2] = depth + 1
                            array2[0, length + 2] = depth + 1
                            retArray = array1
                            if resArray is None:
                                resArray = array2
                            else:
                                resArray = np.append(resArray, array2, 0)
                        else:
                            nextArrayLst.append(retArray)
                            retArray = emptyArray
                    if len(retArray) == 3:
                        depth = retArray[0, length + 2]
                        idx = 1 + randint(0, length - 1)
                        minV = np.min(retArray[:, idx])
                        maxV = np.max(retArray[:, idx])
                        midV = uniform(minV, maxV)
                        splited = False
                        if (retArray[0, idx] > midV >= retArray[1, idx] and retArray[2, idx] <= midV) \
                                or (retArray[0, idx] <= midV < retArray[1, idx] and retArray[2, idx] > midV):
                            retArray[0, length + 2] = depth + 1
                            retArray[1, length + 2] = depth + 2
                            retArray[2, length + 2] = depth + 2
                            splited = True
                        elif (retArray[1, idx] > midV >= retArray[2, idx] and retArray[0, idx] <= midV) \
                                or (retArray[1, idx] <= midV < retArray[2, idx] and retArray[0, idx] > midV):
                            retArray[0, length + 2] = depth + 2
                            retArray[1, length + 2] = depth + 1
                            retArray[2, length + 2] = depth + 2
                            splited = True
                        elif (retArray[2, idx] > midV >= retArray[0, idx] and retArray[1, idx] <= midV) \
                                or (retArray[2, idx] <= midV < retArray[0, idx] and retArray[1, idx] > midV):
                            retArray[0, length + 2] = depth + 2
                            retArray[1, length + 2] = depth + 2
                            retArray[2, length + 2] = depth + 1
                            splited = True
                        if splited:
                            if resArray is None:
                                resArray = retArray
                            else:
                                resArray = np.append(resArray, retArray, 0)
                        else:
                            nextArrayLst.append(retArray)
                        # """
                    elif len(retArray) == 2:
                        depth = retArray[0, length + 2]
                        retArray[0, length + 2] = depth + 1
                        retArray[1, length + 2] = depth + 1
                        if resArray is None:
                            resArray = retArray
                        else:
                            resArray = np.append(resArray, retArray, 0)
                    elif len(retArray) == 1:
                        if resArray is None:
                            resArray = retArray
                        else:
                            resArray = np.append(resArray, retArray, 0)
            else:
                print("Error: return of OneSplit is not 2")
        arrayLst = nextArrayLst
        step = step + 1
    for leftArray in arrayLst:
        resArray = np.append(resArray, leftArray, 0)
    orders = np.argsort(resArray[:, 0])
    resArray = resArray[orders]
    return np.delete(resArray, 0, 1)


dataSet = np.loadtxt(fileName, delimiter=',')
for i in range(0, Loop):
    print("======== loop {} ==========".format(i + 1))
    resSet = Split(dataSet, L, -1)
    np.savetxt(saveName + str(i) + ".csv", resSet[saveCol].astype(int), delimiter=',')
