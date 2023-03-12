import os

from Applications.nTGC.nTGCCuts import *
from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../_DataFolder/nTGC/")

testEventsm1 = LoadLHCOlympics("sm-025-0.lhco")
testEventsm1.AddEventSet(LoadLHCOlympics("sm-025-1.lhco"))
testEventsm2 = LoadLHCOlympics("ILC/sm-05-0.lhco")
testEventsm2.AddEventSet(LoadLHCOlympics("ILC/sm-05-1.lhco"))
testEventsm3 = LoadLHCOlympics("ILC/sm-1-0.lhco")
testEventsm3.AddEventSet(LoadLHCOlympics("ILC/sm-1-1.lhco"))
testEventsm4 = LoadLHCOlympics("CLIC/sm-3-0.lhco")
testEventsm4.AddEventSet(LoadLHCOlympics("CLIC/sm-3-1.lhco"))
testEventsm5 = LoadLHCOlympics("CLIC/sm-5-0.lhco")
testEventsm5.AddEventSet(LoadLHCOlympics("CLIC/sm-5-1.lhco"))

testEventSig1 = LoadLHCOlympics("sig-025.lhco")
testEventSig2 = LoadLHCOlympics("ILC/sig-05.lhco")
testEventSig3 = LoadLHCOlympics("ILC/sig-1.lhco")
testEventSig4 = LoadLHCOlympics("CLIC/sig-3.lhco")
testEventSig5 = LoadLHCOlympics("CLIC/sig-5.lhco")

print(testEventsm1.GetEventCount())
print(testEventsm2.GetEventCount())
print(testEventsm3.GetEventCount())
print(testEventsm4.GetEventCount())
print(testEventsm5.GetEventCount())

print(testEventSig1.GetEventCount())
print(testEventSig2.GetEventCount())
print(testEventSig3.GetEventCount())
print(testEventSig4.GetEventCount())
print(testEventSig5.GetEventCount())

particleNumberCut = ParticleNumberNTGC()
drminCut = DeltaRllMin(0.2)


CutEvents(testEventsm1, particleNumberCut)
CutEvents(testEventsm2, particleNumberCut)
CutEvents(testEventsm3, particleNumberCut)
CutEvents(testEventsm4, particleNumberCut)
CutEvents(testEventsm5, particleNumberCut)

CutEvents(testEventSig1, particleNumberCut)
CutEvents(testEventSig2, particleNumberCut)
CutEvents(testEventSig3, particleNumberCut)
CutEvents(testEventSig4, particleNumberCut)
CutEvents(testEventSig5, particleNumberCut)
CutEvents(testEventSig1, drminCut)
CutEvents(testEventSig2, drminCut)
CutEvents(testEventSig3, drminCut)
CutEvents(testEventSig4, drminCut)
CutEvents(testEventSig5, drminCut)

print(testEventsm1.GetEventCount())
print(testEventsm2.GetEventCount())
print(testEventsm3.GetEventCount())
print(testEventsm4.GetEventCount())
print(testEventsm5.GetEventCount())

print(testEventSig1.GetEventCount())
print(testEventSig2.GetEventCount())
print(testEventSig3.GetEventCount())
print(testEventSig4.GetEventCount())
print(testEventSig5.GetEventCount())

# """
# PhotonPZ lepton pz in Z rest frame
testSM1 = HistogramWithMinMax(testEventsm1, PhotonPZ, [0, 1], 50)
testSM2 = HistogramWithMinMax(testEventsm2, PhotonPZ, [0, 1], 50)
testSM3 = HistogramWithMinMax(testEventsm3, PhotonPZ, [0, 1], 50)
testSM4 = HistogramWithMinMax(testEventsm4, PhotonPZ, [0, 1], 50)
testSM5 = HistogramWithMinMax(testEventsm5, PhotonPZ, [0, 1], 50)
print(testSM1.listCount)
print(testSM2.listCount)
print(testSM3.listCount)
print(testSM4.listCount)
print(testSM5.listCount)

testSig1 = HistogramWithMinMax(testEventSig1, PhotonPZ, [0, 1], 50)
testSig2 = HistogramWithMinMax(testEventSig2, PhotonPZ, [0, 1], 50)
testSig3 = HistogramWithMinMax(testEventSig3, PhotonPZ, [0, 1], 50)
testSig4 = HistogramWithMinMax(testEventSig4, PhotonPZ, [0, 1], 50)
testSig5 = HistogramWithMinMax(testEventSig5, PhotonPZ, [0, 1], 50)

print(testSig1.listCount)
print(testSig2.listCount)
print(testSig3.listCount)
print(testSig4.listCount)
print(testSig5.listCount)
# """

"""
# DeltaR
testSM1 = HistogramWithMinMax(testEventsm1, DeltaR, [0.2, 6.2], 50)
testSM2 = HistogramWithMinMax(testEventsm2, DeltaR, [0.2, 6.2], 50)
testSM3 = HistogramWithMinMax(testEventsm3, DeltaR, [0.2, 6.2], 50)
testSM4 = HistogramWithMinMax(testEventsm4, DeltaR, [0.2, 6.2], 50)
testSM5 = HistogramWithMinMax(testEventsm5, DeltaR, [0.2, 6.2], 50)
print(testSM1.listCount)
print(testSM2.listCount)
print(testSM3.listCount)
print(testSM4.listCount)
print(testSM5.listCount)

testSig1 = HistogramWithMinMax(testEventSig1, DeltaR, [0.2, 6.2], 50)
testSig2 = HistogramWithMinMax(testEventSig2, DeltaR, [0.2, 6.2], 50)
testSig3 = HistogramWithMinMax(testEventSig3, DeltaR, [0.2, 6.2], 50)
testSig4 = HistogramWithMinMax(testEventSig4, DeltaR, [0.2, 6.2], 50)
testSig5 = HistogramWithMinMax(testEventSig5, DeltaR, [0.2, 6.2], 50)

print(testSig1.listCount)
print(testSig2.listCount)
print(testSig3.listCount)
print(testSig4.listCount)
print(testSig5.listCount)

"""

"""
# EllInvMass
testSM1 = HistogramWithMinMax(testEventsm1, EllInvMass, [0, 150], 50)
testSM2 = HistogramWithMinMax(testEventsm2, EllInvMass, [0, 150], 50)
testSM3 = HistogramWithMinMax(testEventsm3, EllInvMass, [0, 150], 50)
testSM4 = HistogramWithMinMax(testEventsm4, EllInvMass, [0, 150], 50)
testSM5 = HistogramWithMinMax(testEventsm5, EllInvMass, [0, 150], 50)
print(testSM1.listCount)
print(testSM2.listCount)
print(testSM3.listCount)
print(testSM4.listCount)
print(testSM5.listCount)

testSig1 = HistogramWithMinMax(testEventSig1, EllInvMass, [0, 150], 50)
testSig2 = HistogramWithMinMax(testEventSig2, EllInvMass, [0, 150], 50)
testSig3 = HistogramWithMinMax(testEventSig3, EllInvMass, [0, 150], 50)
testSig4 = HistogramWithMinMax(testEventSig4, EllInvMass, [0, 150], 50)
testSig5 = HistogramWithMinMax(testEventSig5, EllInvMass, [0, 150], 50)

print(testSig1.listCount)
print(testSig2.listCount)
print(testSig3.listCount)
print(testSig4.listCount)
print(testSig5.listCount)
"""

"""
# LeptonPZ lepton pz in Z rest frame
testSM1 = HistogramWithMinMax(testEventsm1, LeptonPZ, [0, 1], 50)
testSM2 = HistogramWithMinMax(testEventsm2, LeptonPZ, [0, 1], 50)
testSM3 = HistogramWithMinMax(testEventsm3, LeptonPZ, [0, 1], 50)
testSM4 = HistogramWithMinMax(testEventsm4, LeptonPZ, [0, 1], 50)
testSM5 = HistogramWithMinMax(testEventsm5, LeptonPZ, [0, 1], 50)
print(testSM1.listCount)
print(testSM2.listCount)
print(testSM3.listCount)
print(testSM4.listCount)
print(testSM5.listCount)

testSig1 = HistogramWithMinMax(testEventSig1, LeptonPZ, [0, 1], 50)
testSig2 = HistogramWithMinMax(testEventSig2, LeptonPZ, [0, 1], 50)
testSig3 = HistogramWithMinMax(testEventSig3, LeptonPZ, [0, 1], 50)
testSig4 = HistogramWithMinMax(testEventSig4, LeptonPZ, [0, 1], 50)
testSig5 = HistogramWithMinMax(testEventSig5, LeptonPZ, [0, 1], 50)

print(testSig1.listCount)
print(testSig2.listCount)
print(testSig3.listCount)
print(testSig4.listCount)
print(testSig5.listCount)
"""
