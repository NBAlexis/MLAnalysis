import math
import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.Histogram import HistogramWithMinMax
from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../_DataFolder/")

signalEvent = LoadLHCOlympics("mumuZAA/run_04.lhco")
# smEvent = LoadLHCOlympics("mumuZAA/run_03.lhco")

# EventSet.events
# mu+ mu - > v v~ a a
# mu+ mu- > z/a > zaa
# z > v v~
print(len(signalEvent.events))


class ParticleNumberZAA:

    """
    Every cut class must implement "Cut(self, eventSample: EventSample) -> bool:" function
    """
    def Cut(self, eventSample: EventSample) -> bool:
        photonCount = 0
        for particle in eventSample.particles:
            if ParticleType.Photon == particle.particleType:
                photonCount = photonCount + 1
        if photonCount < 2:
            return True
        return False


def HardestPhoton(event: EventSample) -> float:
    largetPhotonEnergy = -1.0
    for particle in event.particles:
        if ParticleType.Photon == particle.particleType and particle.momentum.values[0] > largetPhotonEnergy:
            largetPhotonEnergy = particle.momentum.values[0]
    return largetPhotonEnergy


def PhotonInvarientMass(event: EventSample) -> float:
    momentumAllPhoton = LorentzVector(0, 0, 0, 0)
    for particle in event.particles:
        if ParticleType.Photon == particle.particleType:
            momentumAllPhoton = momentumAllPhoton + particle.momentum
    return momentumAllPhoton.Mass()


class HardestPhotonEnergyCut:

    def Cut(self, eventSample: EventSample) -> bool:
        hardestPhotonEnergy = HardestPhoton(eventSample)
        if hardestPhotonEnergy < 1500:
            return True
        return False


def ETMissing(event: EventSample) -> float:
    for particle in event.particles:
        if ParticleType.Missing == particle.particleType:
            momentumArray = particle.momentum.values
            # [t, x, y, z]
            return math.sqrt(momentumArray[1] * momentumArray[1] + momentumArray[2] * momentumArray[2])
    return 0.0


particleNumberCut = ParticleNumberZAA()
CutEvents(signalEvent, particleNumberCut)

testETMissingSignal = HistogramWithMinMax(signalEvent, PhotonInvarientMass, [0, 5000], 50)
print(testETMissingSignal.listCount)

# hardestPhotonCut = HardestPhotonEnergyCut()
# CutEvents(smEvent, hardestPhotonCut)
# print(len(smEvent.events))

# testETMissingSignal = HistogramWithMinMax(signalEvent, HardestPhoton, [0, 5000], 50)
# print(testETMissingSignal.listCount)
"""
(174997/200000)*1.7016654800000002
(21124/500000)*0.09778634900000001
signal: 1.5pb
sm: 0.004pb

sqrt(L) * signal / sqrt(signal + sm) 

"""