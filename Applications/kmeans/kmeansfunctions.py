import random
import numpy as np

from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType


def ChooseEventWithStratege(allEvents: EventSet, count: int, tag: int):
    result = []
    idx = 0
    while len(result) < count:
        theEvent = allEvents.events[idx]
        largestPhotonIndex = -1
        largestPhotonEnergy = 0
        secondPhotonIndex = -1
        secondPhotonEnergy = 0
        thirdPhotonIndex = -1
        thirdPhotonEnergy = 0
        for theParticle in theEvent.particles:
            if theParticle.particleType == ParticleType.Photon:
                PhotonEnergy = theParticle.momentum.Momentum()
                if PhotonEnergy > largestPhotonEnergy:
                    thirdPhotonIndex = secondPhotonIndex
                    thirdPhotonEnergy = secondPhotonEnergy
                    secondPhotonIndex = largestPhotonIndex
                    secondPhotonEnergy = largestPhotonEnergy
                    largestPhotonIndex = theParticle.index - 1
                    largestPhotonEnergy = PhotonEnergy
                elif PhotonEnergy > secondPhotonEnergy:
                    thirdPhotonIndex = secondPhotonIndex
                    thirdPhotonEnergy = secondPhotonEnergy
                    secondPhotonIndex = theParticle.index - 1
                    secondPhotonEnergy = PhotonEnergy
                elif PhotonEnergy > thirdPhotonEnergy:
                    thirdPhotonIndex = theParticle.index - 1
                    thirdPhotonEnergy = PhotonEnergy
        if largestPhotonIndex >= 0 and secondPhotonIndex >= 0 and thirdPhotonIndex >= 0:
            toAdd = theEvent.particles[largestPhotonIndex].momentum.values
            toAdd = toAdd + theEvent.particles[secondPhotonIndex].momentum.values
            toAdd = toAdd + theEvent.particles[thirdPhotonIndex].momentum.values
            toAdd = toAdd + [tag]
            result.append(toAdd)
        idx = idx + 1
    return result


def SaveCSVFile(fileName: str, content: list):
    with open(fileName, 'w') as f:
        for line in content:
            for i in range(0, 13):
                if i == 12:
                    f.write(str(line[i]) + "\n")
                else:
                    f.write(str(line[i]) + ", ")


def InitialClassify(dataList, dimension: int, typeCount: int):
    dataList[:, dimension] = np.random.randint(0, typeCount, len(dataList))


def SplitLargestClass(dataList, dimension: int, largestClass: int, missingClasses):
    oldClasses = dataList[:, dimension]
    newClasses = np.copy(oldClasses)
    newClasses[newClasses == largestClass] = -1
    newClasses[newClasses >= 0] = 0
    splitClasses = np.random.randint(0, len(missingClasses), len(dataList))
    splitClasses = missingClasses[splitClasses]
    newClasses = -newClasses * splitClasses + (1 + newClasses) * oldClasses
    dataList[:, dimension] = newClasses


def RandomCenterPoints(dataList, dimension: int, typeCount: int):
    minValue = np.min(dataList, axis=1)[0:dimension]
    maxValue = np.max(dataList, axis=1)[0:dimension]
    centerPoints = []
    for i in range(0, typeCount):
        onePoint = []
        for j in range(0, dimension):
            onePoint.append(random.uniform(minValue[j], maxValue[j]))
        centerPoints.append(onePoint)
    return np.array(centerPoints)


def CalculateCenter(dataList, dimension: int, classIndex: int):
    points = dataList[dataList[:, dimension] == classIndex]
    if 0 == len(points):
        return 0, None
    return len(points), np.mean(points, axis=0)[0:dimension]


def CalculateCenterList(dataList, dimension: int, typeCount: int):
    result = []
    newSplit = []
    maximalCount = 0
    maximalClass = -1
    for ii in range(0, typeCount):
        countOfK, centerForK = CalculateCenter(dataList, dimension, ii)
        if centerForK is None:
            newSplit.append(ii)
        else:
            result.append(centerForK.tolist())
        if countOfK > maximalCount:
            maximalCount = countOfK
            maximalClass = ii
    if len(newSplit) > 0:
        while len(newSplit) > 0:
            newSplit.append(maximalClass)
            SplitLargestClass(dataList, dimension, maximalClass, np.array(newSplit))
            result = []
            newSplit = []
            maximalCount = 0
            maximalClass = -1
            for ii in range(0, typeCount):
                countOfK, centerForK = CalculateCenter(dataList, dimension, ii)
                if centerForK is None:
                    newSplit.append(ii)
                else:
                    result.append(centerForK.tolist())
                if countOfK > maximalCount:
                    maximalCount = countOfK
                    maximalClass = ii
    return np.array(result)


def Reclassify(dataList, centers, dimension: int, typeCount: int) -> int:
    changedCount = 0
    for i in range(0, len(dataList)):
        classIndexOfThisPoint = 0
        v = dataList[i, 0:dimension]
        delta = centers[0] - v
        distance0 = np.sqrt(np.dot(delta, delta))
        for classIndex in range(1, typeCount):
            deltaThisPoint = centers[classIndex] - v
            distanceThisPoint = np.sqrt(np.dot(deltaThisPoint, deltaThisPoint))
            if distanceThisPoint < distance0:
                distance0 = distanceThisPoint
                classIndexOfThisPoint = classIndex
        if classIndexOfThisPoint != dataList[i, dimension]:
            dataList[i, dimension] = classIndexOfThisPoint
            changedCount = changedCount + 1
    return changedCount


def KMeans(dataList, dimension: int, typeCount: int, stopWhenNoChange: int = 0) -> bool:
    # centers0 = RandomCenterPoints(dataList, dimension, typeCount)
    InitialClassify(dataList, dimension, typeCount)
    centers0 = CalculateCenterList(dataList, dimension, typeCount)
    changedCount = Reclassify(dataList, centers0, dimension, typeCount)
    while changedCount > stopWhenNoChange:
        centers0 = CalculateCenterList(dataList, dimension, typeCount)
        if centers0 is None:
            return False
        changedCount = Reclassify(dataList, centers0, dimension, typeCount)
        print(changedCount)
    return True


def CalculateDistance(dataList, dimension: int, typeCount: int):
    centers0 = CalculateCenterList(dataList, dimension, typeCount)
    distanceList = []
    for p in range(0, len(dataList)):
        center = centers0[int(np.round(dataList[p, dimension]))]
        delta = center - dataList[p, 0:dimension]
        distanceList.append(np.sqrt(np.dot(delta, delta)))
    return distanceList


def CalculateCenterD(dataList, dimension: int, classIndex: int):
    points = dataList[dataList[:, dimension] == classIndex]
    return np.mean(points, axis=0)[0:dimension]


def CalculateCenterListD(dataList, dimension: int, typeCount: int):
    result = []
    for ii in range(0, typeCount):
        centerForK = CalculateCenterD(dataList, dimension, ii)
        result.append(centerForK.tolist())
    return np.array(result)


def CalculateDistanceD(dataList, dimension: int, centers):
    distanceList = []
    for p in range(0, len(dataList)):
        center = centers[int(np.round(dataList[p, dimension]))]
        delta = center - dataList[p, 0:dimension]
        distanceList.append(np.sqrt(np.dot(delta, delta)))
    return distanceList


def CalculateDistanceD2(dataList, dimension: int, typeCount: int, centers):
    """
    similar as CalculateDistanceD
    but calculate the nearest center before calculate distance
    """
    distanceList = []
    for p in range(0, len(dataList)):
        v = dataList[p, 0:dimension]
        delta = centers[0] - v
        distance0 = np.sqrt(np.dot(delta, delta))
        for classIndex in range(1, typeCount):
            deltaThisPoint = centers[classIndex] - v
            distanceThisPoint = np.sqrt(np.dot(deltaThisPoint, deltaThisPoint))
            if distanceThisPoint < distance0:
                distance0 = distanceThisPoint
        distanceList.append(distance0)
    return distanceList


def HistoryMean(lst):
    ret = [lst[0]]
    for ii in range(1, len(lst)):
        ret.append(np.mean(lst[0:ii + 1]))
    return ret


"""
There are only 6 independent variables.
We only list the px,py,pz of the hardest two photons
"""


def ChooseEventWithStrategeQ(allEvents: EventSet, count: int, tag: int):
    result = []
    idx = 0
    while len(result) < count:
        theEvent = allEvents.events[idx]
        largestPhotonIndex = -1
        largestPhotonEnergy = 0
        secondPhotonIndex = -1
        secondPhotonEnergy = 0
        # thirdPhotonIndex = -1
        # thirdPhotonEnergy = 0
        for theParticle in theEvent.particles:
            if theParticle.particleType == ParticleType.Photon:
                PhotonEnergy = theParticle.momentum.Momentum()
                if PhotonEnergy > largestPhotonEnergy:
                    # thirdPhotonIndex = secondPhotonIndex
                    # thirdPhotonEnergy = secondPhotonEnergy
                    secondPhotonIndex = largestPhotonIndex
                    secondPhotonEnergy = largestPhotonEnergy
                    largestPhotonIndex = theParticle.index - 1
                    largestPhotonEnergy = PhotonEnergy
                elif PhotonEnergy > secondPhotonEnergy:
                    # thirdPhotonIndex = secondPhotonIndex
                    # thirdPhotonEnergy = secondPhotonEnergy
                    secondPhotonIndex = theParticle.index - 1
                    secondPhotonEnergy = PhotonEnergy
                # elif PhotonEnergy > thirdPhotonEnergy:
                #     thirdPhotonIndex = theParticle.index - 1
                #     thirdPhotonEnergy = PhotonEnergy
        if largestPhotonIndex >= 0 and secondPhotonIndex >= 0:
            toAdd = theEvent.particles[largestPhotonIndex].momentum.values[1:4]
            toAdd = toAdd + theEvent.particles[secondPhotonIndex].momentum.values[1:4]
            # toAdd = toAdd + theEvent.particles[thirdPhotonIndex].momentum.values
            # toAdd = toAdd + [tag]
            result.append(toAdd)
        idx = idx + 1
    return result


def ChooseEventWithStrategeQ2(allEvents: EventSet, count: int, tag: int):
    result = []
    idx = 0
    while len(result) < count:
        theEvent = allEvents.events[idx]
        largestPhotonIndex = -1
        largestPhotonEnergy = 0
        secondPhotonIndex = -1
        secondPhotonEnergy = 0
        thirdPhotonIndex = -1
        thirdPhotonEnergy = 0
        for theParticle in theEvent.particles:
            if theParticle.particleType == ParticleType.Photon:
                PhotonEnergy = theParticle.momentum.Momentum()
                if PhotonEnergy > largestPhotonEnergy:
                    thirdPhotonIndex = secondPhotonIndex
                    thirdPhotonEnergy = secondPhotonEnergy
                    secondPhotonIndex = largestPhotonIndex
                    secondPhotonEnergy = largestPhotonEnergy
                    largestPhotonIndex = theParticle.index - 1
                    largestPhotonEnergy = PhotonEnergy
                elif PhotonEnergy > secondPhotonEnergy:
                    thirdPhotonIndex = secondPhotonIndex
                    thirdPhotonEnergy = secondPhotonEnergy
                    secondPhotonIndex = theParticle.index - 1
                    secondPhotonEnergy = PhotonEnergy
                elif PhotonEnergy > thirdPhotonEnergy:
                    thirdPhotonIndex = theParticle.index - 1
                    thirdPhotonEnergy = PhotonEnergy
        if largestPhotonIndex >= 0 and secondPhotonIndex >= 0:
            pt1 = theEvent.particles[largestPhotonIndex].momentum.Pt()
            eta1 = theEvent.particles[largestPhotonIndex].momentum.PseudoRapidity()
            pt2 = theEvent.particles[secondPhotonIndex].momentum.Pt()
            eta2 = theEvent.particles[secondPhotonIndex].momentum.PseudoRapidity()
            pt3 = theEvent.particles[thirdPhotonIndex].momentum.Pt()
            eta3 = theEvent.particles[thirdPhotonIndex].momentum.PseudoRapidity()
            toAdd = [pt1, pt2, pt3, eta1, eta2, eta3]
            result.append(toAdd)
        idx = idx + 1
    return result


def NormalizeVArray(lstData, fact) -> list:
    arrData = np.array(lstData)
    maxOfEachDim = np.max(np.abs(arrData), axis=0)
    datacount = np.shape(arrData)[0]
    rows = np.shape(arrData)[1]
    for i in range(0, rows):
        arrData[:, i] = arrData[:, i] / maxOfEachDim[i]
    lenv = fact * fact * np.ones(datacount)
    for i in range(0, rows):
        lenv = lenv + arrData[:, i] * arrData[:, i]
    lenv = np.sqrt(lenv)
    print(lenv[0])
    retlist = [(fact * np.ones(datacount) / lenv).tolist()]
    for i in range(0, rows):
        retlist.append((arrData[:, i] / lenv).tolist())
    retarray = np.array(retlist)
    retarray = np.transpose(retarray)
    return retarray.tolist()


def NormalizeVArrayOnlyRescal(lstData) -> list:
    arrData = np.array(lstData)
    maxOfEachDim = np.max(np.abs(arrData), axis=0)
    rows = np.shape(arrData)[1]
    for i in range(0, rows):
        arrData[:, i] = arrData[:, i] / maxOfEachDim[i]
    return arrData.tolist()


def NormalizeVTest(lstData, factor) -> list:
    lenv = factor * factor
    for i in range(0, len(lstData)):
        lenv = lenv + lstData[i] * lstData[i]
    lenv = np.sqrt(lenv)
    retlist = [factor / lenv]
    for i in range(0, len(lstData)):
        retlist.append(lstData[i] / lenv)
    return retlist


"""
def StateVectorDot(pax1, pay1, paz1, pbx1, pby1, pbz1, pax2, pay2, paz2, pbx2, pby2, pbz2) -> float:
    c1_1 = np.cos(pax1)
    s1_1 = np.sin(pax1)
    c2_1 = np.cos(pay1)
    s2_1 = np.sin(pay1)
    c5_1 = np.cos(paz1)
    s5_1 = np.sin(paz1)
    c1_2 = np.cos(pax2)
    s1_2 = np.sin(pax2)
    c2_2 = np.cos(pay2)
    s2_2 = np.sin(pay2)
    c5_2 = np.cos(paz2)
    s5_2 = np.sin(paz2)
    phi1 = c1_1 * c5_1 * np.exp(-1j * (- pbx1 - pbz1)) / 2
    phi2 = s1_1 * c5_1 * np.exp(-1j * (pbx1 - pbz1)) / 2
    phi3 = c2_1 * s5_1 * np.exp(-1j * (-pby1 + pbz1)) / 2
    phi4 = s2_1 * s5_1 * np.exp(-1j * (pby1 + pbz1)) / 2
    psi1 = c1_2 * c5_2 * np.exp(1j * (- pbx2 - pbz2)) / 2
    psi2 = s1_2 * c5_2 * np.exp(1j * (pbx2 - pbz2)) / 2
    psi3 = c2_2 * s5_2 * np.exp(1j * (-pby2 + pbz2)) / 2
    psi4 = s2_2 * s5_2 * np.exp(1j * (pby2 + pbz2)) / 2
    return float(np.abs(phi1 * psi1 + phi2 * psi2 + phi3 * psi3 + phi4 * psi4))


def StateVectorDot2(pax1, pay1, paz1, pbx1, pby1, pbz1, pax2, pay2, paz2, pbx2, pby2, pbz2) -> float:
    c1_1 = np.cos(pax1)
    s1_1 = np.sin(pax1)
    c2_1 = np.cos(pay1)
    s2_1 = np.sin(pay1)
    c3_1 = np.cos(paz1)
    s3_1 = np.sin(paz1)
    c4_1 = np.cos(pbx1)
    s4_1 = np.sin(pbx1)
    c5_1 = np.cos(pby1)
    s5_1 = np.sin(pby1)
    c6_1 = np.cos(pbz1)
    s6_1 = np.sin(pbz1)
    c1_2 = np.cos(pax2)
    s1_2 = np.sin(pax2)
    c2_2 = np.cos(pay2)
    s2_2 = np.sin(pay2)
    c3_2 = np.cos(paz2)
    s3_2 = np.sin(paz2)
    c4_2 = np.cos(pbx2)
    s4_2 = np.sin(pbx2)
    c5_2 = np.cos(pby2)
    s5_2 = np.sin(pby2)
    c6_2 = np.cos(pbz2)
    s6_2 = np.sin(pbz2)
    phi1 = c1_1 * c5_1
    phi2 = s1_1 * c5_1
    phi3 = c2_1 * s5_1
    phi4 = s2_1 * s5_1
    phi5 = c3_1 * c6_1
    phi6 = s3_1 * c6_1
    phi7 = c4_1 * s6_1
    phi8 = s4_1 * s6_1
    psi1 = c1_2 * c5_2
    psi2 = s1_2 * c5_2
    psi3 = c2_2 * s5_2
    psi4 = s2_2 * s5_2
    psi5 = c3_2 * c6_2
    psi6 = s3_2 * c6_2
    psi7 = c4_2 * s6_2
    psi8 = s4_2 * s6_2
    return float(np.abs(phi1 * psi1 + phi2 * psi2 + phi3 * psi3 + phi4 * psi4
                        + phi5 * psi5 + phi6 * psi6 + phi7 * psi7 + phi8 * psi8))

"""


def StateVectorDot3(v1, v2) -> float:
    return float(np.abs(np.dot(np.array([v1[0], v1[1] - v1[4] * 1j, v1[2] - v1[5] * 1j, v1[3] - v1[6] * 1j]),
                               np.array([v2[0], v2[1] + v2[4] * 1j, v2[2] + v2[5] * 1j, v2[3] + v2[6] * 1j]))))


def SaveCSVFileQ(fileName: str, content: list, count: int):
    with open(fileName, 'w') as f:
        for line in content:
            for i in range(0, count):
                if i == (count - 1):
                    f.write(str(line[i]) + "\n")
                else:
                    f.write(str(line[i]) + ", ")


def InitialClassifyQ(dataCount: int, typeCount: int):
    return np.random.randint(0, typeCount, dataCount)


def CalculateCenterQ(dataList, kValueList, classIndex: int):
    points = dataList[kValueList == classIndex]
    if 0 == len(points):
        return 0, None
    return len(points), np.mean(points, axis=0)


def SplitLargestClassQ(kValueList, dataCount: int, largestClass: int, missingClasses):
    oldClasses = kValueList
    newClasses = np.copy(oldClasses)
    newClasses[newClasses == largestClass] = -1
    newClasses[newClasses >= 0] = 0
    splitClasses = np.random.randint(0, len(missingClasses), dataCount)
    splitClasses = missingClasses[splitClasses]
    newClasses = -newClasses * splitClasses + (1 + newClasses) * oldClasses
    return newClasses


def CalculateCenterListQ(dataList, kValueList, typeCount: int):
    result = []
    newSplit = []
    maximalCount = 0
    maximalClass = -1
    for ii in range(0, typeCount):
        countOfK, centerForK = CalculateCenterQ(dataList, kValueList, ii)
        if centerForK is None:
            newSplit.append(ii)
        else:
            result.append(centerForK.tolist())
        if countOfK > maximalCount:
            maximalCount = countOfK
            maximalClass = ii
    if len(newSplit) > 0:
        while len(newSplit) > 0:
            newSplit.append(maximalClass)
            kValueList = SplitLargestClassQ(kValueList, len(kValueList), maximalClass, np.array(newSplit))
            result = []
            newSplit = []
            maximalCount = 0
            maximalClass = -1
            for ii in range(0, typeCount):
                countOfK, centerForK = CalculateCenterQ(dataList, kValueList, ii)
                if centerForK is None:
                    newSplit.append(ii)
                else:
                    result.append(centerForK.tolist())
                if countOfK > maximalCount:
                    maximalCount = countOfK
                    maximalClass = ii
    return np.array(result)


def CalculateCenterListDQ(dataList, kValueList, typeCount: int):
    result = []
    for ii in range(0, typeCount):
        countOfK, centerForK = CalculateCenterQ(dataList, kValueList, ii)
        result.append(centerForK.tolist())
    return np.array(result)


def CalculateDistanceDQ(dataList, kValueList, centers):
    distanceList = []
    for p in range(0, len(dataList)):
        center = centers[kValueList[p]]
        distanceList.append(StateVectorDot3(dataList[p], center))
    return distanceList


def ReclassifyQ(dataList, kValueList, centers, typeCount: int) -> int:
    changedCount = 0
    for i in range(0, len(dataList)):
        classIndexOfThisPoint = 0
        v = dataList[i]
        distance0 = StateVectorDot3(centers[0], v)
        for classIndex in range(1, typeCount):
            distanceThisPoint = StateVectorDot3(centers[classIndex], v)
            if distanceThisPoint > distance0:
                distance0 = distanceThisPoint
                classIndexOfThisPoint = classIndex
        if classIndexOfThisPoint != kValueList[i]:
            kValueList[i] = classIndexOfThisPoint
            changedCount = changedCount + 1
    return changedCount


def KMeansQ(dataList, typeCount: int, stopWhenNoChange: int = 0):
    kValueList = InitialClassifyQ(len(dataList), typeCount)
    centers0 = CalculateCenterListQ(dataList, kValueList, typeCount)
    changedCount = ReclassifyQ(dataList, kValueList, centers0, typeCount)
    while changedCount > stopWhenNoChange:
        centers0 = CalculateCenterListQ(dataList, kValueList, typeCount)
        if centers0 is None:
            return False, None
        changedCount = ReclassifyQ(dataList, kValueList, centers0, typeCount)
        print(changedCount)
    return True, kValueList
