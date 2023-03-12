from CutAndExport.FilterFunctions import *
from DataStructure import Constants
from DataStructure.EventSet import *
from DataStructure.Constants import *
from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Matrix4x4 import Matrix4x4
from DataStructure.Particles import ParticleStatus, ParticleType


def InvMass(eventSample: EventSample) -> float:
    largestLM1 = 0
    largestLM2 = 0
    largestLIndex1 = 0
    largestLIndex2 = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestLM1:
                largestLM2 = largestLM1
                largestLIndex2 = largestLIndex1
                largestLM1 = momentum
                largestLIndex1 = particle.index
            elif momentum > largestLM2:
                largestLM2 = momentum
                largestLIndex2 = particle.index
    p41 = eventSample.particles[largestLIndex1 - 1].momentum
    p42 = eventSample.particles[largestLIndex2 - 1].momentum
    momentumEll = p41 + p42
    return momentumEll.Mass()


def LeptonDotZA(eventSample: EventSample) -> float:
    largestLM1 = 0
    largestLM2 = 0
    largestLIndex1 = 0
    largestLIndex2 = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestLM1:
                largestLM2 = largestLM1
                largestLIndex2 = largestLIndex1
                largestLM1 = momentum
                largestLIndex1 = particle.index
            elif momentum > largestLM2:
                largestLM2 = momentum
                largestLIndex2 = particle.index
    p41 = eventSample.particles[largestLIndex1 - 1].momentum
    p42 = eventSample.particles[largestLIndex2 - 1].momentum
    return dot3d(normalize3d(p41.V3d()), normalize3d(p42.V3d()))


def SHatZA(eventSample: EventSample) -> float:
    largestLM1 = 0
    largestLM2 = 0
    largestLIndex1 = 0
    largestLIndex2 = 0
    largestPhotonM = 0
    largestPhotonIndex = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestLM1:
                largestLM2 = largestLM1
                largestLIndex2 = largestLIndex1
                largestLM1 = momentum
                largestLIndex1 = particle.index
            elif momentum > largestLM2:
                largestLM2 = momentum
                largestLIndex2 = particle.index
        if ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhotonM:
                largestPhotonM = momentum
                largestPhotonIndex = particle.index
    p41 = eventSample.particles[largestLIndex1 - 1].momentum
    p42 = eventSample.particles[largestLIndex2 - 1].momentum
    p43 = eventSample.particles[largestPhotonIndex - 1].momentum
    momentumAll = p41 + p42 + p43
    return momentumAll.Mass()


def LeptonPZ(eventSample: EventSample) -> float:
    largestLM1 = 0
    largestLM2 = 0
    largestLIndex1 = 0
    largestLIndex2 = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestLM1:
                largestLM2 = largestLM1
                largestLIndex2 = largestLIndex1
                largestLM1 = momentum
                largestLIndex1 = particle.index
            elif momentum > largestLM2:
                largestLM2 = momentum
                largestLIndex2 = particle.index
    p41 = eventSample.particles[largestLIndex1 - 1].momentum
    p42 = eventSample.particles[largestLIndex2 - 1].momentum
    pZ = p41 + p42
    pL = p41
    if eventSample.particles[largestLIndex2 - 1].PGDid > 0:
        pL = p42
    rotMtr = Matrix4x4.MakeRotationFromTo(pZ.V3d(), [0, 0, 1])
    pZDir = rotMtr.MultiplyVector(pZ)
    pLDir = rotMtr.MultiplyVector(pL)
    v3dz = pZDir.V3d()
    vsq = Constants.dot3d(v3dz, v3dz)
    if vsq > 0.9999999999 or vsq < 0:
        return 1000
    boostMtr = Matrix4x4.MakeBoost(pZDir.V3d())
    # pZRest = boostMtr.MultiplyVector(pZDir)
    pLRest = boostMtr.MultiplyVector(pLDir)
    return math.cos(pLRest.Theta())


def LeptonPZAndGammaTheta(eventSample: EventSample) -> float:
    lpz = LeptonPZ(eventSample)
    gammaDegree = abs(PhotonDegreeCS(eventSample))
    return (1 - gammaDegree) * (1 - gammaDegree) + lpz * lpz * 0.25


def DeltaRMin(eventSample: EventSample) -> float:
    minR = 10000.0
    etaList = []
    phiList = []
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            etaList.append(particle.momentum.PseudoRapidity())
            phiList.append(particle.momentum.Azimuth())
    for a in range(0, len(etaList)):
        for b in range(a + 1, len(etaList)):
            thisDeltaR = (etaList[a] - etaList[b]) * (etaList[a] - etaList[b]) + (phiList[a] - phiList[b]) * (phiList[a] - phiList[b])
            thisDeltaR = 0 if thisDeltaR < 0 else math.sqrt(thisDeltaR)
            if minR > thisDeltaR:
                minR = thisDeltaR
    return minR


def DeltaR(eventSample: EventSample) -> float:
    largestLM1 = 0
    largestLM2 = 0
    largestLIndex1 = 0
    largestLIndex2 = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestLM1:
                largestLM2 = largestLM1
                largestLIndex2 = largestLIndex1
                largestLM1 = momentum
                largestLIndex1 = particle.index
            elif momentum > largestLM2:
                largestLM2 = momentum
                largestLIndex2 = particle.index
    y1 = eventSample.particles[largestLIndex1 - 1].momentum.PseudoRapidity()
    y2 = eventSample.particles[largestLIndex2 - 1].momentum.PseudoRapidity()
    phi1 = eventSample.particles[largestLIndex1 - 1].momentum.Azimuth()
    phi2 = eventSample.particles[largestLIndex2 - 1].momentum.Azimuth()
    beforeSqrt = (y1 - y2) * (y1 - y2) + (phi1 - phi2) * (phi1 - phi2)
    return 0 if beforeSqrt < 0 else math.sqrt(beforeSqrt)


def ZpAndGammaDirTest(eventSet: EventSet):
    xList = []
    # smallXlist = []
    yList = []
    # result_f = open(fileName, 'a')
    for eventSample in eventSet.events:
        largestPhotonIdx = -1
        largestEa = -1.0
        for i in range(len(eventSample.particles)):
            if 0 == eventSample.particles[i].particleType:
                if eventSample.particles[i].momentum.values[0] > largestEa:
                    largestEa = eventSample.particles[i].momentum.values[0]
                    largestPhotonIdx = i
        momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
        lp = LeptonPZ(eventSample)
        yList.append(lp)
        xList.append(math.cos(momentumPhoton.Theta()))
        # smallXlist.append(lp)
    # result_f.close()
    import matplotlib.pyplot as plt
    plt.scatter(xList, yList, s=1)
    plt.show()


class ParticleNumberZA:
    """
    Nj >= 2
    Nell+ >= 1
    Nell- >= 1
    Na >= 1
    and hardest are e+e- or mu+mu-
    """
    def Cut(self, eventSample: EventSample) -> bool:
        jetCount = 0
        photonCount = 0
        largestLM1 = 0
        largestLM2 = 0
        largestLIndex1 = 0
        largestLIndex2 = 0
        for particle in eventSample.particles:
            if ParticleType.Jet == particle.particleType:
                jetCount += 1
            if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
                momentum = particle.momentum.Momentum()
                if momentum > largestLM1:
                    largestLM2 = largestLM1
                    largestLIndex2 = largestLIndex1
                    largestLM1 = momentum
                    largestLIndex1 = particle.index
                elif momentum > largestLM2:
                    largestLM2 = momentum
                    largestLIndex2 = particle.index
            if ParticleType.Photon == particle.particleType:
                photonCount += 1
        if jetCount < 2:  # or jetCount > 4:
            return True
        if photonCount < 1:
            return True
        if 0 == largestLIndex1 or 0 == largestLIndex2:
            return True
        if eventSample.particles[largestLIndex1 - 1].PGDid != -eventSample.particles[largestLIndex2 - 1].PGDid:
            return True
        return False


class EllInvMass:
    def __init__(self, mdiva: float, mz: float):
        self.mdiva = mdiva
        self.mz = mz

    def Cut(self, eventSample: EventSample) -> bool:
        return abs(InvMass(eventSample) - self.mz) > self.mdiva


class DotEllCut:
    def __init__(self, dotValue: float):
        self.dotValue = dotValue

    def Cut(self, eventSample: EventSample) -> bool:
        return LeptonDotZA(eventSample) < self.dotValue


class SHatZACut:
    def __init__(self, minV: float, maxV: float):
        self.minV = minV
        self.maxV = maxV

    def Cut(self, eventSample: EventSample) -> bool:
        if self.minV > 0:
            return SHatZA(eventSample) < self.minV
        return SHatZA(eventSample) > self.maxV


class RZACut:
    def __init__(self, minV: float, maxV: float):
        self.minV = minV
        self.maxV = maxV

    def Cut(self, eventSample: EventSample) -> bool:
        if self.minV > 0:
            return LeptonPZAndGammaTheta(eventSample) < self.minV
        return LeptonPZAndGammaTheta(eventSample) > self.maxV


class DeltaRCut:
    def __init__(self, rValue: float):
        self.rValue = rValue

    def Cut(self, eventSample: EventSample) -> bool:
        return DeltaRMin(eventSample) < self.rValue


class DeltaRCutM:
    def __init__(self, rValue: float):
        self.rValue = rValue

    def Cut(self, eventSample: EventSample) -> bool:
        return DeltaR(eventSample) > self.rValue
