from CutAndExport.FilterFunctions import *
from DataStructure import Constants
from DataStructure.EventSet import *
from DataStructure.Constants import *
from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Matrix4x4 import Matrix4x4
from DataStructure.Particles import ParticleStatus, ParticleType


class ParticleNumberNTGC:
    """
    Nell+ >= 1
    Nell- >= 1
    Na >= 1
    and hardest are e+e- or mu+mu-
    """
    def Cut(self, eventSample: EventSample) -> bool:
        photonCount = 0
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
            if ParticleType.Photon == particle.particleType:
                photonCount += 1
        if photonCount < 1:
            return True
        if 0 == largestLIndex1 or 0 == largestLIndex2:
            return True
        if eventSample.particles[largestLIndex1 - 1].PGDid != -eventSample.particles[largestLIndex2 - 1].PGDid:
            return True
        return False


class ParticleNumberNTGCJJA:
    """
    Nj >= 2
    Na >= 1
    """
    def Cut(self, eventSample: EventSample) -> bool:
        photonCount = 0
        jetCount = 0
        for particle in eventSample.particles:
            if ParticleType.Jet == particle.particleType:
                jetCount += 1
            if ParticleType.Photon == particle.particleType:
                photonCount += 1
        if photonCount < 1 or jetCount < 1:
            return True
        return False


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


def EllInvMass(eventSample: EventSample) -> float:
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
    return abs(math.cos(pLRest.Theta()))


def DeltaRAL(eventSample: EventSample) -> float:
    largestL = 0
    largestPhoton = 0
    largestLIndex = 0
    largestPhotonIndex = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestL:
                largestL = momentum
                largestLIndex = particle.index
        elif ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhoton:
                largestPhoton = momentum
                largestPhotonIndex = particle.index
    y1 = eventSample.particles[largestLIndex - 1].momentum.PseudoRapidity()
    y2 = eventSample.particles[largestPhotonIndex - 1].momentum.PseudoRapidity()
    phi1 = eventSample.particles[largestLIndex - 1].momentum.Azimuth()
    phi2 = eventSample.particles[largestPhotonIndex - 1].momentum.Azimuth()
    beforeSqrt = (y1 - y2) * (y1 - y2) + (phi1 - phi2) * (phi1 - phi2)
    return 0 if beforeSqrt < 0 else math.sqrt(beforeSqrt)


def PhotonPZ(eventSample: EventSample) -> float:
    largestPhoton = 0
    largestPhotonIndex = 0
    for particle in eventSample.particles:
        if ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhoton:
                largestPhoton = momentum
                largestPhotonIndex = particle.index
    return abs(math.cos(eventSample.particles[largestPhotonIndex - 1].momentum.Theta()))


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


def Mjj(eventSample: EventSample) -> float:
    jetIndex = []
    for particle in eventSample.particles:
        if ParticleType.Jet == particle.particleType:
            jetIndex.append(particle.index)
    if 2 == len(jetIndex):
        m1 = eventSample.particles[jetIndex[0] - 1].momentum
        m2 = eventSample.particles[jetIndex[1] - 1].momentum
        mall = m1 + m2
        return mall.Mass()
    closest = -1.0
    for i in range(0, len(jetIndex)):
        for j in range(i + 1, len(jetIndex)):
            m1 = eventSample.particles[jetIndex[0] - 1].momentum
            m2 = eventSample.particles[jetIndex[1] - 1].momentum
            mall = m1 + m2
            mjj = mall.Mass()
            if closest < 0.0 or abs(mjj - 91.1876) < abs(closest - 91.1876):
                closest = mjj
    return closest


def MAllj(eventSample: EventSample) -> float:
    mjj = LorentzVector(0, 0, 0, 0)
    for particle in eventSample.particles:
        if ParticleType.Jet == particle.particleType:
            mjj = mjj + particle.momentum
    return mjj.Mass()


def MinDRaj(eventSample: EventSample) -> float:
    jetIndex = []
    largestPhoton = 0
    largestPhotonIndex = 0
    for particle in eventSample.particles:
        if ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhoton:
                largestPhoton = momentum
                largestPhotonIndex = particle.index
        if ParticleType.Jet == particle.particleType:
            jetIndex.append(particle.index)
    minDRaj = -1.0
    pa = eventSample.particles[largestPhotonIndex - 1].momentum
    for jet in jetIndex:
        pjet = eventSample.particles[jet - 1].momentum
        deltaPhi = pa.Azimuth() - pjet.Azimuth()
        if deltaPhi > 3.1415926536:
            deltaPhi = 2 * 3.1415926536 - deltaPhi
        if deltaPhi < -3.1415926536:
            deltaPhi = deltaPhi + 2 * 3.1415926536
        deltaY = pa.PseudoRapidity() - pjet.PseudoRapidity()
        deltaRaj = math.sqrt(deltaPhi * deltaPhi + deltaY * deltaY)
        if minDRaj < 0.0 or minDRaj > deltaRaj:
            minDRaj = deltaRaj
    return minDRaj


def MaxPhiaj(eventSample: EventSample) -> float:
    jetIndex = []
    largestPhoton = 0
    largestPhotonIndex = 0
    for particle in eventSample.particles:
        if ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhoton:
                largestPhoton = momentum
                largestPhotonIndex = particle.index
        if ParticleType.Jet == particle.particleType:
            jetIndex.append(particle.index)
    maxPhiAJ = -2.0
    pa = eventSample.particles[largestPhotonIndex - 1].momentum
    for jet in jetIndex:
        pjet = eventSample.particles[jet - 1].momentum
        deltaPhi = math.cos(pa.Azimuth() - pjet.Azimuth())
        if deltaPhi > maxPhiAJ:
            maxPhiAJ = deltaPhi
    return maxPhiAJ


def MaxYaj(eventSample: EventSample) -> float:
    jetIndex = []
    largestPhoton = 0
    largestPhotonIndex = 0
    for particle in eventSample.particles:
        if ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhoton:
                largestPhoton = momentum
                largestPhotonIndex = particle.index
        if ParticleType.Jet == particle.particleType:
            jetIndex.append(particle.index)
    maxYAJ = -2.0
    pa = eventSample.particles[largestPhotonIndex - 1].momentum
    for jet in jetIndex:
        pjet = eventSample.particles[jet - 1].momentum
        deltaY = math.cos(pa.PseudoRapidity() - pjet.PseudoRapidity())
        if deltaY > maxYAJ:
            maxYAJ = deltaY
    return maxYAJ


class DeltaRllMin:
    def __init__(self, rValue: float):
        self.rValue = rValue

    def Cut(self, eventSample: EventSample) -> bool:
        return DeltaRMin(eventSample) < self.rValue


class MllMZCut:
    def __init__(self, delta: float, mz: float):
        self.delta = delta
        self.mz = mz

    def Cut(self, eventSample: EventSample) -> bool:
        return abs(EllInvMass(eventSample) - self.mz) > self.delta


class ThetaGammaCut:
    def __init__(self, rValue: float):
        self.rValue = rValue

    def Cut(self, eventSample: EventSample) -> bool:
        return PhotonPZ(eventSample) > self.rValue


class ThetaPLeptonZ:
    def __init__(self, rValue: float):
        self.rValue = rValue

    def Cut(self, eventSample: EventSample) -> bool:
        return LeptonPZ(eventSample) > self.rValue


class DeltaRllMinMax:
    def __init__(self, min: float, max: float):
        self.min = min
        self.max = max

    def Cut(self, eventSample: EventSample) -> bool:
        deltaR = DeltaR(eventSample)
        return self.min < deltaR < self.max


class MjjMZCut:
    def __init__(self, deltaL: float, deltaR: float, mz: float):
        self.deltaL = deltaL
        self.deltaR = deltaR
        self.mz = mz

    def Cut(self, eventSample: EventSample) -> bool:
        mj = MAllj(eventSample)
        return mj > self.mz + self.deltaR or mj < self.mz - self.deltaR


class DeltaAJMinMax:
    def __init__(self, min: float, max: float):
        self.min = min
        self.max = max

    def Cut(self, eventSample: EventSample) -> bool:
        deltaR = MinDRaj(eventSample)
        return not (self.min < deltaR < self.max)


class DeltaPhiMax:
    def __init__(self, max: float):
        self.max = max

    def Cut(self, eventSample: EventSample) -> bool:
        deltaPhi = MaxPhiaj(eventSample)
        return deltaPhi > self.max


def ReadTXTFile(fileName: str) -> list:
    dataSample = []
    bFirstLine = True
    with open(fileName) as f:
        for lines in f.readlines():
            if bFirstLine:
                bFirstLine = False
                continue
            strList = lines.split()
            dataSample = dataSample + [float(strList[2])]
    return dataSample
