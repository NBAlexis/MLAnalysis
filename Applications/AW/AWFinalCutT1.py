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
testEventt1 = LoadLHCOlympics("wa/features/ft1.lhco")
testEventt2 = LoadLHCOlympics("wa/features/ft2.lhco")
testEventt6 = LoadLHCOlympics("wa/features/ft6.lhco")
testEventt7 = LoadLHCOlympics("wa/features/ft7.lhco")

jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)

CutEvents(testEventt1, jetNumberCut)
CutEvents(testEventt1, leptonNumberCut)
CutEvents(testEventt1, photonNumberCut)
CutEvents(testEventt2, jetNumberCut)
CutEvents(testEventt2, leptonNumberCut)
CutEvents(testEventt2, photonNumberCut)
CutEvents(testEventt6, jetNumberCut)
CutEvents(testEventt6, leptonNumberCut)
CutEvents(testEventt6, photonNumberCut)
CutEvents(testEventt7, jetNumberCut)
CutEvents(testEventt7, leptonNumberCut)
CutEvents(testEventt7, photonNumberCut)

print(testEventsm.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

raCut = RadiusACut(1, 0.15, 3)

CutEvents(testEventsm, raCut)
CutEvents(testEventt1, raCut)
CutEvents(testEventt2, raCut)
CutEvents(testEventt6, raCut)
CutEvents(testEventt7, raCut)

print(testEventsm.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

ptMissingCut = PtMissing(1, 75)

CutEvents(testEventsm, ptMissingCut)
CutEvents(testEventt1, ptMissingCut)
CutEvents(testEventt2, ptMissingCut)
CutEvents(testEventt6, ptMissingCut)
CutEvents(testEventt7, ptMissingCut)

print(testEventsm.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

megammaCut = MeGammaCut(1, False, 800)

CutEvents(testEventsm, megammaCut)
CutEvents(testEventt1, megammaCut)
CutEvents(testEventt2, megammaCut)
CutEvents(testEventt6, megammaCut)
CutEvents(testEventt7, megammaCut)

print(testEventsm.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

"""
thetaGammaLepton = ThetaGammaLeptonCut(0, False, 0)

CutEvents(testEventsm, thetaGammaLepton)
CutEvents(testEventt1, thetaGammaLepton)
CutEvents(testEventt2, thetaGammaLepton)
CutEvents(testEventt6, thetaGammaLepton)
CutEvents(testEventt7, thetaGammaLepton)

print(testEventsm.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

"""

"""
phiGammaMissing = PhiGammaMissingCut(0, 0)

CutEvents(testEventsm, phiGammaMissing)
CutEvents(testEventt1, phiGammaMissing)
CutEvents(testEventt2, phiGammaMissing)
CutEvents(testEventt6, phiGammaMissing)
CutEvents(testEventt7, phiGammaMissing)

print(testEventsm.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

"""


lmCut = PhiLeptonMissingCut(1, False, 0)

CutEvents(testEventsm, lmCut)
CutEvents(testEventt1, lmCut)
CutEvents(testEventt2, lmCut)
CutEvents(testEventt6, lmCut)
CutEvents(testEventt7, lmCut)


print(testEventsm.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())


vbfCut = StandardVBFCut(True, 0.0, 1.0)

CutEvents(testEventsm, vbfCut)
CutEvents(testEventt1, vbfCut)
CutEvents(testEventt2, vbfCut)
CutEvents(testEventt6, vbfCut)
CutEvents(testEventt7, vbfCut)

print(testEventsm.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

