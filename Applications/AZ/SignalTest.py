import os

from Applications.AZ.ZGammaCuts import *
from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../")
"""
testEventsm = LoadLHCOlympics("_DataFolder/za/newbackgrounds/azsm1.lhco")
testEventsm2 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/azsm2.lhco")
testEventsm3 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/azsm3.lhco")
testEventsm4 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/azsm4.lhco")
testEventsm.AddEventSet(testEventsm2)
testEventsm.AddEventSet(testEventsm3)
testEventsm.AddEventSet(testEventsm4)
testEventj3 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll1.lhco")
testEventj32 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll2.lhco")
testEventj33 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll3.lhco")
# testEventj34 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll4.lhco")
testEventj35 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll5.lhco")
testEventj3.AddEventSet(testEventj32)
testEventj3.AddEventSet(testEventj33)
# testEventj3.AddEventSet(testEventj34)
testEventj3.AddEventSet(testEventj35)
testEventm4 = LoadLHCOlympics("_DataFolder/za/features/azsignalm4.lhco")
testEventm4.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-fm4.lhco"))
testEventt5 = LoadLHCOlympics("_DataFolder/za/features/azsignalt5.lhco")
testEventt5.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-ft5.lhco"))

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventt5.GetEventCount())

particleNumberCut = ParticleNumberZA()
deltaRCut = DeltaRCut(0.2)

CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventj3, particleNumberCut)
CutEvents(testEventm4, particleNumberCut)
CutEvents(testEventt5, particleNumberCut)

print("============ after partical number ==============")

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventt5.GetEventCount())

CutEvents(testEventm4, deltaRCut)
CutEvents(testEventt5, deltaRCut)

print("============ after Delta R ==============")
"""

testEventsm = LoadLHCOlympics("_DataFolder/za/features/smallsm.lhco")
testEventj3 = LoadLHCOlympics("_DataFolder/za/features/smalljjjll.lhco")
testEventm5 = LoadLHCOlympics("_DataFolder/za/features/smallm5.lhco")
testEventt5 = LoadLHCOlympics("_DataFolder/za/features/smallt5.lhco")

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
"""

mw = 80.379
# 80.385 at z pole, 79.9534?
mz = 91.1876
cw = 0.876801
sw = 0.480853
vev = 246.22
# 246.22
e2 = 0.0982177 # 0.0934761  # sqrt{ 4 pi alpha} for alpha = 1/134
# 0.0982177 at z pole

cefm3 = 21.0e-12
cefm4 = 16.0e-12
cefm5 = 24.0e-12
ceft5 = 0.74e-12
ceft6 = 1.7e-12
ceft7 = 2.8e-12
ceft9 = 1.3e-12

mzam3 = math.sqrt(math.sqrt(32 * math.sqrt(2.0) * 3.14159265359 * cw * sw * mz * mz / (abs(cefm3 + 1.0e-22) * e2 * vev * vev)))
mzam4 = math.sqrt(math.sqrt(
    64 * math.sqrt(2.0) * 3.14159265359 * cw * cw * sw * sw * mz * mz / (abs(cefm4) * (cw * cw - sw * sw) * e2 * vev * vev)))
mzam5 = math.sqrt(math.sqrt(192 * 3.14159265359 * sw * sw * mw * mz / (abs(cefm5) * e2 * vev * vev)))

mzat5 = math.sqrt(math.sqrt(3.14159265359 / (abs(ceft5) * cw * cw * sw * sw)))
mzat6 = math.sqrt(math.sqrt(4 * 3.14159265359 / (abs(ceft6) * (cw * cw - sw * sw))))
mzat7 = math.sqrt(math.sqrt(8 * math.sqrt(2.0) * 3.14159265359 / (3 * abs(ceft7) * (cw * cw - sw * sw) * cw * sw)))

mzat9 = math.sqrt(math.sqrt(2 * 3.14159265359 / (3 * abs(ceft9) * cw * cw * sw * sw)))

ubcutfm4 = SHatZACut(-1, mzam4)
ubcutft5 = SHatZACut(-1, mzat5)

testEventsm1 = testEventsm.GetCopy()
testEventsm2 = testEventsm.GetCopy()
testEventsmj31 = testEventj3.GetCopy()
testEventsmj32 = testEventj3.GetCopy()
CutEvents(testEventsm1, ubcutfm4)
CutEvents(testEventsmj31, ubcutfm4)
CutEvents(testEventsm2, ubcutft5)
CutEvents(testEventsmj32, ubcutft5)
CutEvents(testEventm4, ubcutfm4)
CutEvents(testEventt5, ubcutft5)

print("============ after unitarity bound ==============")

print(testEventsm1.GetEventCount())
print(testEventsmj31.GetEventCount())
print(testEventsm2.GetEventCount())
print(testEventsmj32.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventt5.GetEventCount())
"""

# ===================================================
# Here starts the cut flow

# testDeltaRm2 = HistogramWithMinMax(testEventm2, DeltaR, [0, 1], 40)
# testDeltaRt5 = HistogramWithMinMax(testEventt5, DeltaR, [0, 1], 40)

"""
# Invariant mass of l+l-
testTlSM = HistogramWithMinMax(testEventsm, InvMass, [0, 120], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, InvMass, [0, 120], 40)
testTlM4 = HistogramWithMinMax(testEventm4, InvMass, [0, 120], 40)
testTlT5 = HistogramWithMinMax(testEventt5, InvMass, [0, 120], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM4.listCount)
print(testTlT5.listCount)
"""

"""
# Yjj
testTlSM = HistogramWithMinMax(testEventsm, Yjj2Filter, [0, 8], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, Yjj2Filter, [0, 8], 40)
testTlM3 = HistogramWithMinMax(testEventm4, Yjj2Filter, [0, 8], 40)
testTlT5 = HistogramWithMinMax(testEventt5, Yjj2Filter, [0, 8], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# Mjj
testTlSM = HistogramWithMinMax(testEventsm, Mjj2Filter, [0, 2000], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, Mjj2Filter, [0, 2000], 40)
testTlM3 = HistogramWithMinMax(testEventm4, Mjj2Filter, [0, 2000], 40)
testTlT5 = HistogramWithMinMax(testEventt5, Mjj2Filter, [0, 2000], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# theta ll
testTlSM = HistogramWithMinMax(testEventsm, DeltaR, [0.2, 1], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, DeltaR, [0.2, 1], 40)
testTlM3 = HistogramWithMinMax(testEventm4, DeltaR, [0.2, 1], 40)
testTlT5 = HistogramWithMinMax(testEventt5, DeltaR, [0.2, 1], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# shat
testTlSM = HistogramWithMinMax(testEventsm, SHatZA, [0, 2400], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, SHatZA, [0, 2400], 40)
testTlM3 = HistogramWithMinMax(testEventm4, SHatZA, [0, 2400], 40)
testTlT5 = HistogramWithMinMax(testEventt5, SHatZA, [0, 2400], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# Polarization
testTlSM = HistogramWithMinMax(testEventsm, LeptonPZAndGammaTheta, [0, 1.2], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, LeptonPZAndGammaTheta, [0, 1.2], 40)
# testTlM2 = HistogramWithMinMax(testEventm2, LeptonPZAndGammaTheta, [0, 1.25], 40)
testTlT5 = HistogramWithMinMax(testEventt5, LeptonPZAndGammaTheta, [0, 1.2], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
# print(testTlM2.listCount)
print(testTlT5.listCount)
"""


