from Interfaces.LHCOlympics import *
from CutAndExport.CutEvent import *
from CutAndExport.Histogram import *
from CutAndExport.CutFunctions import *
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

testEventSet_ma160 = LoadLHCOlympics("ma160_e-4.lhco")
testEventSet_bg = LoadLHCOlympics("ee2aaa_bg.lhco")
print("ee2aaa_ma160.lhco", len(testEventSet_ma160.events))
print("ee2aaa_bg.lhco", len(testEventSet_bg.events))


# e+ e- > a a a
class PhotonNumberCut:
    """
    If cutType = 0, cut all with photons > parameters[0]
    If cutType = 1, cut all with photons < parameters[0]
    If cutType = 2, cut all with photons not in parameters
    """

    def __init__(self, cutType: int, parameters):
        self.cutType = cutType
        self.parameters = parameters

    def Cut(self, eventSample: EventSample) -> bool:
        photonCount = 0
        for particle in eventSample.particles:
            if 0 == particle.particleType:
                photonCount += 1
        if 0 == self.cutType:
            return photonCount > self.parameters[0]
        if 1 == self.cutType:
            return photonCount < self.parameters[0]
        return photonCount not in self.parameters


def InvMassA1A2(eventSample: EventSample) -> float:
    largestAM1 = 0
    largestAM2 = 0
    largestAIndex1 = 0
    largestAIndex2 = 0
    for particle in eventSample.particles:
        if ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestAM1:
                largestAM2 = largestAM1
                largestAIndex2 = largestAIndex1
                largestAM1 = momentum
                largestAIndex1 = particle.index
            elif momentum > largestAM2:
                largestAM2 = momentum
                largestAIndex2 = particle.index
    p41 = eventSample.particles[largestAIndex1 - 1].momentum
    p42 = eventSample.particles[largestAIndex2 - 1].momentum
    momentumEAA = p41 + p42
    if largestAIndex1 > 0 and largestAIndex2 > 0:
        return momentumEAA.Mass()
    return 0.0
'''
result1 = HistogramWithMinMax(testEventSet_ma160, InvMassA1A2, [0,250], 100)
print(result1.minMax)
print(result1.listCount)
result2 = HistogramWithMinMax(testEventSet_bg, InvMassA1A2, [0,250], 100)
print(result2.minMax)
print(result2.listCount)
'''
class InvMassA1A2Cut:
    def __init__(self, min: float, max: float):
        self.min = min
        self.max = max

    def Cut(self, eventSample: EventSample) -> bool:
        invMassA1A2 = InvMassA1A2(eventSample)
        if self.min < invMassA1A2 < self.max:
            return False
        return True


def TET(eventSample: EventSample) -> float:
    tet = LorentzVector(0, 0, 0, 0).Et()
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status:
            tet = tet + particle.momentum.Et()
    return tet

#result = HistogramWithMinMax(exportEventLHE_sig, TET, [0, 250], 100)
#print(result.minMax)
#print(result.listCount)
'''
result5 = HistogramWithMinMax(testEventSet_ma160, TET, [0,270], 100)
resultbg = HistogramWithMinMax(testEventSet_bg, TET, [0,270], 100)
print(result5.minMax)
print(result5.listCount)
print(resultbg.minMax)
print(resultbg.listCount)
'''
class TETCut:
    def __init__(self, cutValue: float):
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        if TET(eventSample) < self.cutValue:
            return True
        return False



def YPhoton1(eventSample: EventSample) -> float:
    largestPhotonIndex1 = 0
    largestPhotonM1 = 0.0
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status \
                and ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhotonM1:
                largestPhotonM1 = momentum
                largestPhotonIndex1 = particle.index
    p1 = eventSample.particles[largestPhotonIndex1 - 1].momentum
    if largestPhotonIndex1 > 0:
        return p1.PseudoRapidity()
    return 0.0
'''
result = HistogramWithMinMax(testEventSet_ma160, YPhoton1, [-3,3], 100)
print(result.minMax)
print(result.listCount)

result = HistogramWithMinMax(testEventSet_bg, YPhoton1, [-3,3], 100)
print(result.minMax)
print(result.listCount)
'''
class YPhoton1Cut:
    def __init__(self, min: float, max: float):
        self.min = min
        self.max = max

    def Cut(self, eventSample: EventSample) -> bool:
        if self.min < YPhoton1(eventSample) < self.max:
            return False
        return True


def Cosa1a2(eventSample: EventSample) -> float:
    largestPhotonM1 = 0
    largestPhotonM2 = 0
    largestPhotonIndex1 = 0
    largestPhotonIndex2 = 0
    for particle in eventSample.particles:
        if ParticleType.Photon == particle.particleType:
                momentum = particle.momentum.Momentum()
                if momentum > largestPhotonM1:
                    largestPhotonM2 = largestPhotonM1
                    largestPhotonIndex2 = largestPhotonIndex1
                    largestPhotonM1 = momentum
                    largestPhotonIndex1 = particle.index
                elif momentum > largestPhotonM2:
                    largestPhotonM2 = momentum
                    largestPhotonIndex2 = particle.index
    a1 = eventSample.particles[largestPhotonIndex1 - 1].momentum + eventSample.particles[largestPhotonIndex2 - 1].momentum
    a2 = eventSample.particles[largestPhotonIndex2 - 1].momentum + eventSample.particles[largestPhotonIndex2 - 1].momentum
    pa1a2 = a1.values[1] * a2.values[1] + a1.values[2] * a2.values[2] + a1.values[3] * a2.values[3]
    pa1mod = math.sqrt(a1.values[1] ** 2 + a1.values[2] ** 2 + a1.values[3] ** 2)
    pa2mod = math.sqrt(a2.values[1] ** 2 + a2.values[2] ** 2 + a2.values[3] ** 2)
    cos = pa1a2 / (pa1mod * pa2mod)
    if largestPhotonIndex1 > 0 and largestPhotonIndex2 > 0:
        return cos
    return 0.0
'''
result1 = HistogramWithMinMax(testEventSet_ma40, Cosaa1a2, [-1,1], 100)
print(result1.minMax)
print(result1.listCount)
result2 = HistogramWithMinMax(testEventSet_bg, Cosaa1a2, [-1,1], 100)
print(result2.minMax)
print(result2.listCount)
'''
class Cosa1a2Cut:
    def __init__(self, cutValue: float):
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        if Cosa1a2(eventSample) < self.cutValue:
            return True
        return False


###########################################################################################################
photonNumberCut = PhotonNumberCut(1, [3])
CutEvents(testEventSet_ma160, photonNumberCut)
CutEvents(testEventSet_bg, photonNumberCut)
print(len(testEventSet_ma160.events))
print(len(testEventSet_bg.events))


yPhotonCut = YPhoton1Cut(-1.7, 1.7)
CutEvents(testEventSet_ma160, yPhotonCut)
CutEvents(testEventSet_bg, yPhotonCut)
print("ma160_cutyPhotonCut", len(testEventSet_ma160.events))
print("bg_cutyPhotonCut", len(testEventSet_bg.events))

tetCut = TETCut(100)
CutEvents(testEventSet_ma160, tetCut)
CutEvents(testEventSet_bg, tetCut)
print("ma160_cutTET", len(testEventSet_ma160.events))
print("bg_cutTET", len(testEventSet_bg.events))

invMassA1A2Cut = InvMassA1A2Cut(155, 165)
CutEvents(testEventSet_ma160, invMassA1A2Cut)
CutEvents(testEventSet_bg, invMassA1A2Cut)
print("ma160_cutinvMassAACut", len(testEventSet_ma160.events))
print("bg_cutinvMassAACut", len(testEventSet_bg.events))











