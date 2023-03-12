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


testEventSig1 = LoadLHCOlympics("sig-025.lhco")
testEventSig2 = LoadLHCOlympics("sig-05.lhco")
testEventSig3 = LoadLHCOlympics("sig-1.lhco")
testEventSig4 = LoadLHCOlympics("sig-3.lhco")
testEventSig5 = LoadLHCOlympics("sig-5.lhco")

particleNumberCut = ParticleNumberNTGC()

CutEvents(testEventSig1, particleNumberCut)
CutEvents(testEventSig2, particleNumberCut)
CutEvents(testEventSig3, particleNumberCut)
CutEvents(testEventSig4, particleNumberCut)
CutEvents(testEventSig5, particleNumberCut)

print(testEventSig1.GetEventCount())
print(testEventSig2.GetEventCount())
print(testEventSig3.GetEventCount())
print(testEventSig4.GetEventCount())
print(testEventSig5.GetEventCount())

drminCut = DeltaRllMin(0.2)

CutEvents(testEventSig1, drminCut)
CutEvents(testEventSig2, drminCut)
CutEvents(testEventSig3, drminCut)
CutEvents(testEventSig4, drminCut)
CutEvents(testEventSig5, drminCut)

print(testEventSig1.GetEventCount())
print(testEventSig2.GetEventCount())
print(testEventSig3.GetEventCount())
print(testEventSig4.GetEventCount())
print(testEventSig5.GetEventCount())
