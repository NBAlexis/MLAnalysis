from Interfaces.LHCOlympics import *
from CutAndExport.CutEvent import *
from CutAndExport.Histogram import *
from CutAndExport.CutFunctions import *

testEventSet_lowmass = LoadLHCOlympics("ma10_e-4_2.lhco")
testEventSet_bg = LoadLHCOlympics("ee2aaa_bg.lhco")
print("ee2aaa_ma10.lhco", len(testEventSet_lowmass.events))
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

def MAllP(eventSample: EventSample) -> float:
    mPP = LorentzVector(0, 0, 0, 0)
    for particle in eventSample.particles:
        if ParticleType.Photon == particle.particleType:
             mPP = mPP + particle.momentum
    return mPP.Mass()
'''
result = HistogramWithMinMax(testEventSet_lowmass, MAllP, [0, 250], 250)
print(result.minMax)
print(result.listCount)
result = HistogramWithMinMax(testEventSet_bg, MAllP, [0, 250], 250)
print(result.minMax)
print(result.listCount)
'''


class MAllPCut:
    def __init__(self, cutValue: float):
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        if MAllP(eventSample) > self.cutValue:
            return True
        return False





def PTA1Momentum(eventSample: EventSample) -> float:
    largestPhotonM1 = 0
    largestPhotonIndex1 = 0
    for particle in eventSample.particles:
        if ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhotonM1:
                largestPhotonM1 = momentum
                largestPhotonIndex1 = particle.index

    p1 = eventSample.particles[largestPhotonIndex1 - 1].momentum
    return p1.Pt()
'''
result = HistogramWithMinMax(testEventSet_lowmass, PTA1Momentum, [0, 140], 140)
print(result.minMax)
print(result.listCount)
result = HistogramWithMinMax(testEventSet_bg, PTA1Momentum, [0, 140], 140)
print(result.minMax)
print(result.listCount)
'''
class PTA1MomentumCut:
    def __init__(self, cutValue: float):
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        if PTA1Momentum(eventSample) < self.cutValue:
            return True
        return False






############################################################################################

photonNumberCut = PhotonNumberCut(1, [1])
CutEvents(testEventSet_lowmass, photonNumberCut)
CutEvents(testEventSet_bg, photonNumberCut)
print(len(testEventSet_lowmass.events))
print(len(testEventSet_bg.events))

mppCut = MAllPCut(20)
CutEvents(testEventSet_lowmass, mppCut)
CutEvents(testEventSet_bg, mppCut)
print("ma7_cutmpp", len(testEventSet_lowmass.events))
print("bg_cutmpp", len(testEventSet_bg.events))

pTA1Cut = PTA1MomentumCut(20)
CutEvents(testEventSet_lowmass, pTA1Cut)
CutEvents(testEventSet_bg, pTA1Cut)
print("ma7_cutPTA1", len(testEventSet_lowmass.events))
print("bg_cutPTA1", len(testEventSet_bg.events))
















