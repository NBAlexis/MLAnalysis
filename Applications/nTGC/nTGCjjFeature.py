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

os.chdir("G:\\ntgc")

testEventsm1 = LoadLHCOlympics("sm-025-0.lhco")
testEventsm1.AddEventSet(LoadLHCOlympics("sm-025-1.lhco"))
testEventsm2 = LoadLHCOlympics("sm-05-0.lhco")
testEventsm2.AddEventSet(LoadLHCOlympics("sm-05-1.lhco"))
testEventsm3 = LoadLHCOlympics("sm-1-0.lhco")
testEventsm3.AddEventSet(LoadLHCOlympics("sm-1-1.lhco"))
testEventsm4 = LoadLHCOlympics("sm-3-0.lhco")
testEventsm4.AddEventSet(LoadLHCOlympics("sm-3-1.lhco"))
testEventsm5 = LoadLHCOlympics("sm-5-0.lhco")
testEventsm5.AddEventSet(LoadLHCOlympics("sm-5-1.lhco"))

testEventSig1 = LoadLHCOlympics("sig-s025-0.lhco")
testEventSig2 = LoadLHCOlympics("sig-s05-0.lhco")
testEventSig3 = LoadLHCOlympics("sig-s1-0.lhco")
testEventSig4 = LoadLHCOlympics("sig-s3-0.lhco")
testEventSig5 = LoadLHCOlympics("sig-s5-0.lhco")

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

particleNumberCut = ParticleNumberNTGCJJA()

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

"""
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
"""

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
# Mjj
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

# """
# Mjj
testSM1 = HistogramWithMinMax(testEventsm1, MAllj, [0, 150], 50)
testSM2 = HistogramWithMinMax(testEventsm2, MAllj, [0, 150], 50)
testSM3 = HistogramWithMinMax(testEventsm3, MAllj, [0, 150], 50)
testSM4 = HistogramWithMinMax(testEventsm4, MAllj, [0, 150], 50)
testSM5 = HistogramWithMinMax(testEventsm5, MAllj, [0, 150], 50)
print(testSM1.listCount)
print(testSM2.listCount)
print(testSM3.listCount)
print(testSM4.listCount)
print(testSM5.listCount)

testSig1 = HistogramWithMinMax(testEventSig1, MAllj, [0, 150], 50)
testSig2 = HistogramWithMinMax(testEventSig2, MAllj, [0, 150], 50)
testSig3 = HistogramWithMinMax(testEventSig3, MAllj, [0, 150], 50)
testSig4 = HistogramWithMinMax(testEventSig4, MAllj, [0, 150], 50)
testSig5 = HistogramWithMinMax(testEventSig5, MAllj, [0, 150], 50)

print(testSig1.listCount)
print(testSig2.listCount)
print(testSig3.listCount)
print(testSig4.listCount)
print(testSig5.listCount)
# """

"""
# draj
testSM1 = HistogramWithMinMax(testEventsm1, MaxPhiaj, [-1, -0.5], 50)
testSM2 = HistogramWithMinMax(testEventsm2, MaxPhiaj, [-1, -0.5], 50)
testSM3 = HistogramWithMinMax(testEventsm3, MaxPhiaj, [-1, -0.5], 50)
testSM4 = HistogramWithMinMax(testEventsm4, MaxPhiaj, [-1, -0.5], 50)
testSM5 = HistogramWithMinMax(testEventsm5, MaxPhiaj, [-1, -0.5], 50)
print(testSM1.listCount)
print(testSM2.listCount)
print(testSM3.listCount)
print(testSM4.listCount)
print(testSM5.listCount)

testSig1 = HistogramWithMinMax(testEventSig1, MaxPhiaj, [-1, -0.5], 50)
testSig2 = HistogramWithMinMax(testEventSig2, MaxPhiaj, [-1, -0.5], 50)
testSig3 = HistogramWithMinMax(testEventSig3, MaxPhiaj, [-1, -0.5], 50)
testSig4 = HistogramWithMinMax(testEventSig4, MaxPhiaj, [-1, -0.5], 50)
testSig5 = HistogramWithMinMax(testEventSig5, MaxPhiaj, [-1, -0.5], 50)


print(testSig1.listCount)
print(testSig2.listCount)
print(testSig3.listCount)
print(testSig4.listCount)
print(testSig5.listCount)
"""

"""
not very good
and no reason to use
# draj
testSM1 = HistogramWithMinMax(testEventsm1, MaxYaj, [-1, 1], 50)
testSM2 = HistogramWithMinMax(testEventsm2, MaxYaj, [-1, 1], 50)
testSM3 = HistogramWithMinMax(testEventsm3, MaxYaj, [-1, 1], 50)
testSM4 = HistogramWithMinMax(testEventsm4, MaxYaj, [-1, 1], 50)
testSM5 = HistogramWithMinMax(testEventsm5, MaxYaj, [-1, 1], 50)
print(testSM1.listCount)
print(testSM2.listCount)
print(testSM3.listCount)
print(testSM4.listCount)
print(testSM5.listCount)

testSig1 = HistogramWithMinMax(testEventSig1, MaxYaj, [-1, 1], 50)
testSig2 = HistogramWithMinMax(testEventSig2, MaxYaj, [-1, 1], 50)
testSig3 = HistogramWithMinMax(testEventSig3, MaxYaj, [-1, 1], 50)
testSig4 = HistogramWithMinMax(testEventSig4, MaxYaj, [-1, 1], 50)
testSig5 = HistogramWithMinMax(testEventSig5, MaxYaj, [-1, 1], 50)


print(testSig1.listCount)
print(testSig2.listCount)
print(testSig3.listCount)
print(testSig4.listCount)
print(testSig5.listCount)
"""