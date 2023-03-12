import numpy as np

from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType


def ChooseEventWithStrategeQ(allEvents: EventSet, count: int):
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


def NormalizeVArray(lstData1, lstData2, fact) -> [list, list]:
    arrData1 = np.array(lstData1)
    arrData2 = np.array(lstData2)
    maxOfEachDim1 = np.max(np.abs(arrData1), axis=0)
    maxOfEachDim2 = np.max(np.abs(arrData2), axis=0)
    maxOfEachDim = np.max(np.array([maxOfEachDim1.tolist(), maxOfEachDim2.tolist()]), axis=0)
    # maxOfEachDim = np.max(np.abs(arrData1), axis=0)
    # print(maxOfEachDim)
    datacount1 = np.shape(arrData1)[0]
    datacount2 = np.shape(arrData2)[0]
    rows = np.shape(arrData1)[1]
    for i in range(0, rows):
        arrData1[:, i] = arrData1[:, i] / maxOfEachDim[i]
        arrData2[:, i] = arrData2[:, i] / maxOfEachDim[i]
    lenv1 = fact * fact * np.ones(datacount1)
    lenv2 = fact * fact * np.ones(datacount2)
    for i in range(0, rows):
        lenv1 = lenv1 + arrData1[:, i] * arrData1[:, i]
        lenv2 = lenv2 + arrData2[:, i] * arrData2[:, i]
    lenv1 = np.sqrt(lenv1)
    lenv2 = np.sqrt(lenv2)
    print(len(lenv1))
    retlist1 = [(fact * np.ones(datacount1) / lenv1).tolist()]
    retlist2 = [(fact * np.ones(datacount2) / lenv2).tolist()]
    for i in range(0, rows):
        retlist1.append((arrData1[:, i] / lenv1).tolist())
        retlist2.append((arrData2[:, i] / lenv2).tolist())
    retarray1 = np.array(retlist1)
    retarray1 = np.transpose(retarray1)
    retarray2 = np.array(retlist2)
    retarray2 = np.transpose(retarray2)
    return [retarray1.tolist(), retarray2.tolist()]

def NormalizeVArray2(lstData1, lstData2, fact) -> [list, list]:
    arrData1 = np.array(lstData1)
    arrData2 = np.array(lstData2)
    maxOfAllDim = np.max(np.abs(arrData2))
    datacount1 = np.shape(arrData1)[0]
    datacount2 = np.shape(arrData2)[0]
    rows = np.shape(arrData1)[1]
    arrData1 = arrData1 / maxOfAllDim
    arrData2 = arrData2 / maxOfAllDim
    lenv1 = fact * fact * np.ones(datacount1)
    lenv2 = fact * fact * np.ones(datacount2)
    for i in range(0, rows):
        lenv1 = lenv1 + arrData1[:, i] * arrData1[:, i]
        lenv2 = lenv2 + arrData2[:, i] * arrData2[:, i]
    lenv1 = np.sqrt(lenv1)
    lenv2 = np.sqrt(lenv2)
    print(len(lenv1))
    retlist1 = [(fact * np.ones(datacount1) / lenv1).tolist()]
    retlist2 = [(fact * np.ones(datacount2) / lenv2).tolist()]
    for i in range(0, rows):
        retlist1.append((arrData1[:, i] / lenv1).tolist())
        retlist2.append((arrData2[:, i] / lenv2).tolist())
    retarray1 = np.array(retlist1)
    retarray1 = np.transpose(retarray1)
    retarray2 = np.array(retlist2)
    retarray2 = np.transpose(retarray2)
    return [retarray1.tolist(), retarray2.tolist()]

def StateVectorDot3(v1, v2) -> float:
    return float(np.abs(np.dot(np.array([v1[0], v1[1] - v1[4] * 1j, v1[2] - v1[5] * 1j, v1[3] - v1[6] * 1j]),
                               np.array([v2[0], v2[1] + v2[4] * 1j, v2[2] + v2[5] * 1j, v2[3] + v2[6] * 1j]))))
