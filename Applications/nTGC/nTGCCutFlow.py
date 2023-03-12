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

os.chdir("../../_DataFolder/nTGC/CLIC")
energyHead = "5"

testEventsm = LoadLHCOlympics("sm-" + energyHead + "-0.lhco")
testEventsm.AddEventSet(LoadLHCOlympics("sm-" + energyHead + "-1.lhco"))

testEventSig = LoadLHCOlympics("sig-" + energyHead + ".lhco")

print(testEventsm.GetEventCount())
print(testEventSig.GetEventCount())

particleNumberCut = ParticleNumberNTGC()
drminCut = DeltaRllMin(0.2)

mzcut = MllMZCut(15, 91.1876)

"""
# ========== 025 =========
thetaGammaCut = ThetaGammaCut(0.9)
thetaPZCut = ThetaPLeptonZ(0.8)
deltaRCut = DeltaRllMinMax(5, 6)
hasDeltaRCut = False
"""

"""
# ========== 05 =========
thetaGammaCut = ThetaGammaCut(0.9)
thetaPZCut = ThetaPLeptonZ(0.8)
deltaRCut = DeltaRllMinMax(3, 4)
hasDeltaRCut = False
"""


"""
# ========== 1 =========
thetaGammaCut = ThetaGammaCut(0.9)
thetaPZCut = ThetaPLeptonZ(0.8)
deltaRCut = DeltaRllMinMax(1.5, 5.5)
hasDeltaRCut = True
"""

"""
# ========== 3 =========
thetaGammaCut = ThetaGammaCut(0.95)
thetaPZCut = ThetaPLeptonZ(0.9)
deltaRCut = DeltaRllMinMax(0.7, 6.0)
hasDeltaRCut = True
"""

# """
# ========== 5 =========
thetaGammaCut = ThetaGammaCut(1)
thetaPZCut = ThetaPLeptonZ(0.95)
deltaRCut = DeltaRllMinMax(0.5, 6.0)
hasDeltaRCut = True
# """

CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventSig, particleNumberCut)
CutEvents(testEventSig, drminCut)

print(testEventsm.GetEventCount())
print(testEventSig.GetEventCount())

print("=========== MZ ==============")
CutEvents(testEventsm, mzcut)
CutEvents(testEventSig, mzcut)
print(testEventsm.GetEventCount())
print(testEventSig.GetEventCount())

print("=========== theta gamma ==============")
CutEvents(testEventsm, thetaGammaCut)
CutEvents(testEventSig, thetaGammaCut)
print(testEventsm.GetEventCount())
print(testEventSig.GetEventCount())

print("=========== theta pz ==============")
CutEvents(testEventsm, thetaPZCut)
CutEvents(testEventSig, thetaPZCut)
print(testEventsm.GetEventCount())
print(testEventSig.GetEventCount())

print("=========== delta R ==============")
if hasDeltaRCut:
    CutEvents(testEventsm, deltaRCut)
    CutEvents(testEventSig, deltaRCut)
    print(testEventsm.GetEventCount())
    print(testEventSig.GetEventCount())
