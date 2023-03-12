import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import HistogramWithMinMax
from Interfaces.LHCOlympics import LoadLHCOlympics, SaveToLHCO

os.chdir("../../")

m0triboson30ee = LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30eetb.lhco")
m0vbs30ee = LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30eevbs.lhco")
m0triboson30em = LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30emtb.lhco")
m0vbs30em = LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30emvbs.lhco")
t0triboson30ee = LoadLHCOlympics("_DataFolder/WWWW/LHE/t0at30eetb.lhco")
t0vbs30ee = LoadLHCOlympics("_DataFolder/WWWW/LHE/t0at30eevbs.lhco")
t0triboson30em = LoadLHCOlympics("_DataFolder/WWWW/LHE/t0at30emtb.lhco")
t0vbs30em = LoadLHCOlympics("_DataFolder/WWWW/LHE/t0at30emvbs.lhco")


def ThetaMissing(eventSample: EventSample) -> float:
    for particle in eventSample.particles:
        if ParticleType.Missing == particle.particleType:
            return math.cos(particle.momentum.Theta())
    return 0


def MuonTheta(eventSample: EventSample) -> float:
    for particle in eventSample.particles:
        if ParticleType.Muon == particle.particleType:
            return math.cos(particle.momentum.Theta())
    return 0


class ThetaMissingCut:

    def __init__(self, v):
        self.v = v

    def Cut(self, eventSample: EventSample) -> bool:
        thetaMissing = abs(ThetaMissing(eventSample))
        if thetaMissing < self.v:
            return True
        return False


class ThetaMuonCut:

    def __init__(self, v):
        self.v = v

    def Cut(self, eventSample: EventSample) -> bool:
        thetaMuon = abs(MuonTheta(eventSample))
        if thetaMuon > self.v:
            return True
        return False


thetaMissingCut = ThetaMissingCut(0.8)
thetaMuoningCut = ThetaMuonCut(0.75)

print("=========== before cut ===========")

print(m0triboson30ee.GetEventCount())
print(m0vbs30ee.GetEventCount())
print(m0triboson30em.GetEventCount())
print(m0vbs30em.GetEventCount())
print(t0triboson30ee.GetEventCount())
print(t0vbs30ee.GetEventCount())
print(t0triboson30em.GetEventCount())
print(t0vbs30em.GetEventCount())

CutEvents(m0triboson30ee, thetaMissingCut)
CutEvents(m0vbs30ee, thetaMissingCut)
CutEvents(m0triboson30em, thetaMissingCut)
CutEvents(m0vbs30em, thetaMissingCut)
CutEvents(t0triboson30ee, thetaMissingCut)
CutEvents(t0vbs30ee, thetaMissingCut)
CutEvents(t0triboson30em, thetaMissingCut)
CutEvents(t0vbs30em, thetaMissingCut)

print("=========== theta missing cut ===========")

print(m0triboson30ee.GetEventCount())
print(m0vbs30ee.GetEventCount())
print(m0triboson30em.GetEventCount())
print(m0vbs30em.GetEventCount())
print(t0triboson30ee.GetEventCount())
print(t0vbs30ee.GetEventCount())
print(t0triboson30em.GetEventCount())
print(t0vbs30em.GetEventCount())

"""
print("=========== theta muon cut ===========")

CutEvents(m0triboson30em, thetaMuoningCut)
CutEvents(m0vbs30em, thetaMuoningCut)
CutEvents(t0triboson30em, thetaMuoningCut)
CutEvents(t0vbs30em, thetaMuoningCut)

print(m0triboson30em.GetEventCount())
print(m0vbs30em.GetEventCount())
print(t0triboson30em.GetEventCount())
print(t0vbs30em.GetEventCount())
"""

"""
SaveToLHCO("_DataFolder/WWWW/LHE/m0at30eetbA.lhco", m0triboson30ee)
SaveToLHCO("_DataFolder/WWWW/LHE/m0at30eevbsA.lhco", m0vbs30ee)
SaveToLHCO("_DataFolder/WWWW/LHE/m0at30emtbA.lhco", m0triboson30em)
SaveToLHCO("_DataFolder/WWWW/LHE/m0at30emvbsA.lhco", m0vbs30em)
SaveToLHCO("_DataFolder/WWWW/LHE/t0at30eetbA.lhco", t0triboson30ee)
SaveToLHCO("_DataFolder/WWWW/LHE/t0at30eevbsA.lhco", t0vbs30ee)
SaveToLHCO("_DataFolder/WWWW/LHE/t0at30emtbA.lhco", t0triboson30em)
SaveToLHCO("_DataFolder/WWWW/LHE/t0at30emvbsA.lhco", t0vbs30em)
"""

"""
s0 int:
0.001005
at 5.5e-3: 2.04722 ab

s1 int:
-0.0002141
at 4.4e-3: -0.277 ab

s2 int:
-8.066e-5
at 4.4e-3: -0.355 ab

m0 int:
9.784e-5
at 0.48e-3: 6.70903*10^-8

m1 int:
0.009715
at 0.1e-3: 4.62619*10^-7

m7 int:
-0.008146
at 2.0e-3: -4.79176*10^-6

t0 int:
0.02621
at 0.048e-3: 0.0000114371

t1 int:
0.03316
at 0.06e-3: 0.0000153046

t2 int:
0.05184
at 0.09e-3: 16.7 ab

"""
