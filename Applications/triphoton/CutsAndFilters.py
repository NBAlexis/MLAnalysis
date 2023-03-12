import math

from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType


def GetD4(ecm: float, event: EventSample) -> float:
    pa = LorentzVector(ecm, 0, 0, ecm)
    pb = LorentzVector(ecm, 0, 0, -ecm)
    largest1 = LorentzVector(0, 0, 0, 0)
    largest2 = LorentzVector(0, 0, 0, 0)
    largest3 = LorentzVector(0, 0, 0, 0)
    for particle in event.particles:
        if ParticleType.Photon == particle.particleType:
            if particle.momentum.values[0] > largest1.values[0]:
                largest3 = largest2
                largest2 = largest1
                largest1 = particle.momentum
            elif particle.momentum.values[0] > largest2.values[0]:
                largest3 = largest2
                largest2 = particle.momentum
            elif particle.momentum.values[0] > largest3.values[0]:
                largest3 = particle.momentum
    s1 = (largest1 + largest2).MassSq() * 0.000001
    s2 = (largest2 + largest3).MassSq() * 0.000001
    t1 = (pa - largest1).MassSq() * 0.000001
    t2 = (pb - largest3).MassSq() * 0.000001
    s = (4 * ecm * ecm) * 0.000001
    return abs((-(s1 * s1 * (s2 - t1) * (s2 - t1)) - (s * (t1 - t2) + s2 * t2) * (s * (t1 - t2) + s2 * t2)
                - 2 * s1 * (s * (s2 - t1) * t1 + s2 * (-s2 + t1) * t2 + s * (s2 + t1) * t2)) / 16)


def GetD43(event: EventSample) -> float:
    return GetD4(1500, event) / (3 ** 8)


def GetD410(event: EventSample) -> float:
    return GetD4(5000, event) / (10 ** 8)


def GetD414(event: EventSample) -> float:
    return GetD4(7000, event) / (14 ** 8)


def GetD416(event: EventSample) -> float:
    return GetD4(8000, event) / (16 ** 8)


def GetD430(event: EventSample) -> float:
    return GetD4(15000, event) / (30 ** 8)


def SmallestTheta(event: EventSample) -> float:
    largest1 = LorentzVector(0, 0, 0, 0)
    largest2 = LorentzVector(0, 0, 0, 0)
    largest3 = LorentzVector(0, 0, 0, 0)
    for particle in event.particles:
        if ParticleType.Photon == particle.particleType:
            if particle.momentum.values[0] > largest1.values[0]:
                largest3 = largest2
                largest2 = largest1
                largest1 = particle.momentum
            elif particle.momentum.values[0] > largest2.values[0]:
                largest3 = largest2
                largest2 = particle.momentum
            elif particle.momentum.values[0] > largest3.values[0]:
                largest3 = particle.momentum
    return math.cos(min(largest1.Theta(), largest2.Theta(), largest3.Theta()))


def SmallestPta(event: EventSample) -> float:
    largest1 = LorentzVector(0, 0, 0, 0)
    largest2 = LorentzVector(0, 0, 0, 0)
    largest3 = LorentzVector(0, 0, 0, 0)
    for particle in event.particles:
        if ParticleType.Photon == particle.particleType:
            if particle.momentum.values[0] > largest1.values[0]:
                largest3 = largest2
                largest2 = largest1
                largest1 = particle.momentum
            elif particle.momentum.values[0] > largest2.values[0]:
                largest3 = largest2
                largest2 = particle.momentum
            elif particle.momentum.values[0] > largest3.values[0]:
                largest3 = particle.momentum
    return min(largest1.Pt(), largest2.Pt(), largest3.Pt())


def InvarientMissing(event: EventSample) -> float:
    missing = LorentzVector(0, 0, 0, 0)
    for particle in event.particles:
        if ParticleType.Missing == particle.particleType:
            missing = missing + particle.momentum
    return missing.Mass()


class MissingInvMassCut:

    def Cut(self, eventSample: EventSample) -> bool:
        return InvarientMissing(eventSample) < 100


def SmallPTA3(event: EventSample) -> float:
    return SmallestPta(event) / 1500


def SmallPTA10(event: EventSample) -> float:
    return SmallestPta(event) / 5000


def SmallPTA14(event: EventSample) -> float:
    return SmallestPta(event) / 7000


def SmallPTA30(event: EventSample) -> float:
    return SmallestPta(event) / 15000


class SmallPTACut:

    def __init__(self, ecm: float, cutV: float):
        self.ecm = ecm
        self.cutV = cutV

    def Cut(self, eventSample: EventSample) -> bool:
        pta = SmallestPta(eventSample) / self.ecm
        if pta < self.cutV:
            return True
        return False


class D4Cut:

    def __init__(self, ecm: float, cutV: float):
        self.ecm = ecm
        self.shatsq = 2 * ecm * 0.001
        self.cutV = cutV

    def Cut(self, eventSample: EventSample) -> bool:
        d4 = GetD4(self.ecm, eventSample) / (self.shatsq ** 8)
        if d4 < self.cutV:
            return True
        return False
