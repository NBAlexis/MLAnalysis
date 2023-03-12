import os

from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType
import matplotlib.pyplot as plt

from Interfaces.LHCOlympics import LoadLHCOlympics


def GetS1S2T1T2(ecm: float, event: EventSample, bPrint: bool = False) -> [float, float, float, float, float]:
    pa = LorentzVector(ecm, 0, 0, ecm)
    pb = LorentzVector(ecm, 0, 0, -ecm)
    largest1 = LorentzVector(0, 0, 0, 0)
    largestidx1 = -1
    largest2 = LorentzVector(0, 0, 0, 0)
    largestidx2 = -1
    largest3 = LorentzVector(0, 0, 0, 0)
    largestidx3 = -1
    for particle in event.particles:
        if ParticleType.Photon == particle.particleType:
            if particle.momentum.values[0] > largest1.values[0]:
                largest3 = largest2
                largestidx3 = largestidx2
                largest2 = largest1
                largestidx2 = largestidx1
                largest1 = particle.momentum
                largestidx1 = particle.index
            elif particle.momentum.values[0] > largest2.values[0]:
                largest3 = largest2
                largestidx3 = largestidx2
                largest2 = particle.momentum
                largestidx2 = particle.index
            elif particle.momentum.values[0] > largest3.values[0]:
                largest3 = particle.momentum
                largestidx3 = particle.index
    s1 = (largest1 + largest2).MassSq() * 0.000001
    s2 = (largest2 + largest3).MassSq() * 0.000001
    t1 = (pa - largest1).MassSq() * 0.000001
    t2 = (pb - largest3).MassSq() * 0.000001
    s = (4 * ecm * ecm) * 0.000001
    d4 = (-(s1*s1*(s2 - t1)*(s2 - t1)) - (s*(t1 - t2) + s2*t2)*(s*(t1 - t2) + s2*t2)
          - 2*s1*(s*(s2 - t1)*t1 + s2*(-s2 + t1)*t2 + s*(s2 + t1)*t2))/4
    if bPrint:
        print([s1, s2, t1, t2, d4])
    return [s1, s2, t1, t2, d4]


def GetDistributin(ecm: float, events: EventSet, printCount: int) -> [list, list, list, list, list]:
    s1 = []
    s2 = []
    t1 = []
    t2 = []
    d4 = []
    iHasPrint = 0
    for event in events.events:
        [s1e, s2e, t1e, t2e, d4e] = GetS1S2T1T2(ecm, event, iHasPrint < printCount)
        s1.append(s1e)
        s2.append(s2e)
        t1.append(t1e)
        t2.append(t2e)
        d4.append(d4e)
        iHasPrint = iHasPrint + 1
    return [s1, s2, t1, t2, d4]


os.chdir("../../")
testEvent = LoadLHCOlympics("_DataFolder/triphoton/AfterPhotonNumber/SM-1500.lhco")
[s1l, s2l, t1l, t2l, d4l] = GetDistributin(1500, testEvent, 10)
plt.hist(s1l, 50)
plt.show()
plt.hist(s2l, 50)
plt.show()
plt.hist(t1l, 50)
plt.show()
plt.hist(t2l, 50)
plt.show()
plt.hist(d4l, 50)
plt.show()