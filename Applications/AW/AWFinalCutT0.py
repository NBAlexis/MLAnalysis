import os

from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("F:/PyworkingFolder/CutExperiment/_DataFolder")

testEventsm0 = LoadLHCOlympics("wa/features/bgsm2.lhco")
testEventsm = LoadLHCOlympics("wa/features/bgsm.lhco")
testEventsm.AddEventSet(testEventsm0)
testEventt0 = LoadLHCOlympics("wa/features/ft0.lhco")
testEventt5 = LoadLHCOlympics("wa/features/ft5.lhco")

jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)

CutEvents(testEventt0, jetNumberCut)
CutEvents(testEventt0, leptonNumberCut)
CutEvents(testEventt0, photonNumberCut)
CutEvents(testEventt5, jetNumberCut)
CutEvents(testEventt5, leptonNumberCut)
CutEvents(testEventt5, photonNumberCut)

print(testEventsm.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt5.GetEventCount())

raCut = RadiusACut(1, 0.15, 2)

CutEvents(testEventsm, raCut)
CutEvents(testEventt0, raCut)
CutEvents(testEventt5, raCut)

print(testEventsm.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt5.GetEventCount())

ptMissingCut = PtMissing(1, 75)

CutEvents(testEventsm, ptMissingCut)
CutEvents(testEventt0, ptMissingCut)
CutEvents(testEventt5, ptMissingCut)

print(testEventsm.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt5.GetEventCount())

megammaCut = MeGammaCut(1, False, 800)

CutEvents(testEventsm, megammaCut)
CutEvents(testEventt0, megammaCut)
CutEvents(testEventt5, megammaCut)

print(testEventsm.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt5.GetEventCount())

thetaGammaLepton = ThetaGammaLeptonCut(0, False, 0)

CutEvents(testEventsm, thetaGammaLepton)
CutEvents(testEventt0, thetaGammaLepton)
CutEvents(testEventt5, thetaGammaLepton)

print(testEventsm.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt5.GetEventCount())

"""
vbfCut = StandardVBFCut(True, 0.0, 1.0)

CutEvents(testEventsm, vbfCut)
CutEvents(testEventt0, vbfCut)
CutEvents(testEventt5, vbfCut)

print(testEventsm.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt5.GetEventCount())
"""

"""
phiGammaMissing = PhiGammaMissingCut(0, -0.5)

CutEvents(testEventsm, phiGammaMissing)
CutEvents(testEventt0, phiGammaMissing)
CutEvents(testEventt5, phiGammaMissing)

print(testEventsm.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt5.GetEventCount())

lmCut = PhiLeptonMissingCut(1, False, 0)

CutEvents(testEventsm, lmCut)
CutEvents(testEventt0, lmCut)
CutEvents(testEventt5, lmCut)


print(testEventsm.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt5.GetEventCount())
"""

