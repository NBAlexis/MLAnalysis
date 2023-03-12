import numpy as np

from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType


def ChooseEventWithStrategePCAAD(allEvents: EventSet, count: int):
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
            """
            E1, E2
            Pt1, Pt2
            |eta1|, |eta2|
            InvMass2
            |Delta eta|
            |Delta R|
            """
            p1 = theEvent.particles[largestPhotonIndex].momentum
            p2 = theEvent.particles[secondPhotonIndex].momentum
            p = p1 + p2
            toAdd = [p1.values[0],
                     p2.values[0],
                     p1.Pt(),
                     p2.Pt(),
                     abs(p1.PseudoRapidity()),
                     abs(p2.PseudoRapidity()),
                     p.Mass(),
                     abs(p1.PseudoRapidity() - p2.PseudoRapidity()),
                     LorentzVector.DeltaR(p1, p2)]
            result.append(toAdd)
        idx = idx + 1
    return result

def ZScoreStandardize(dataset1, dataset2):
    means = np.mean(dataset1, axis=0)
    stds = np.std(dataset1, axis=0)
    for i in range(0, len(dataset1[0])):
        dataset1[:, i] = (dataset1[:, i] - means[i]) / stds[i]
        if dataset2 is not None:
            dataset2[:, i] = (dataset2[:, i] - means[i]) / stds[i]
    return [dataset1, dataset2]


def ManualPCA(dataset1, dataset2, k):
    scatt = np.dot(np.transpose(dataset1), dataset1)
    eig_val, eig_vec = np.linalg.eig(scatt)
    eig_pair = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(0, len(dataset1[0]))]
    eig_pair.sort(reverse=True)
    features = np.array([eig[1] for eig in eig_pair[:k]])
    dataset1 = np.dot(dataset1, np.transpose(features))
    if dataset2 is not None:
        dataset2 = np.dot(dataset2, np.transpose(features))
    return [dataset1, dataset2]


def ManualPCAData(dataset1, k):
    means = np.mean(dataset1, axis=0)
    stds = np.std(dataset1, axis=0)
    for i in range(0, len(dataset1[0])):
        dataset1[:, i] = (dataset1[:, i] - means[i]) / stds[i]
    scatt = np.dot(np.transpose(dataset1), dataset1)
    eig_val, eig_vec = np.linalg.eig(scatt)
    eig_pair = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(0, len(dataset1[0]))]
    features = np.array([eig[1] for eig in eig_pair[:k]])
    return [means, stds, features]


def ManualPCATransform(dataset2, means, stds, features):
    for i in range(0, len(dataset2[0])):
        dataset2[:, i] = (dataset2[:, i] - means[i]) / stds[i]
    dataset2 = np.dot(dataset2, np.transpose(features))
    return dataset2
