import os

from Applications.AZ.ZGammaCuts import *
from CutAndExport.CutEvent import CutEvents
from Interfaces.LHCOlympics import *

"""
# ====================================================================
os.chdir("../../_DataFolder/za")

testEventAll = LoadLHCOlympics("features/azsignalm3.lhco")
testEventAll.AddEventSet(LoadLHCOlympics("features/signal-n-fm3.lhco"))

print(testEventAll.GetEventCount())

particleNumberCut = ParticleNumberZA()
deltaRCut = DeltaRCut(0.2)

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

ubcutfm3 = SHatZACut(-1, mzam3)

CutEvents(testEventAll, particleNumberCut)
CutEvents(testEventAll, deltaRCut)
CutEvents(testEventAll, ubcutfm3)

print(testEventAll.GetEventCount())
SaveToLHCO("features/smallm3.lhco", testEventAll)
"""

# ====================================================================
# """
os.chdir("../../_DataFolder/za/newfittings")
eventfileNameA = "fm3/fm3"
eventfileNameB = "fm3/fm3-n"

testEvent0 = LoadLHCOlympics(eventfileNameA + "-0.lhco")
testEvent1 = LoadLHCOlympics(eventfileNameA + "-1.lhco")
testEvent2 = LoadLHCOlympics(eventfileNameA + "-2.lhco")
testEvent3 = LoadLHCOlympics(eventfileNameA + "-3.lhco")
testEvent4 = LoadLHCOlympics(eventfileNameA + "-4.lhco")
testEvent5 = LoadLHCOlympics(eventfileNameA + "-5.lhco")
testEvent6 = LoadLHCOlympics(eventfileNameA + "-6.lhco")
testEvent7 = LoadLHCOlympics(eventfileNameA + "-7.lhco")

testEvent0.AddEventSet(LoadLHCOlympics(eventfileNameB + "-0.lhco"))
testEvent1.AddEventSet(LoadLHCOlympics(eventfileNameB + "-1.lhco"))
testEvent2.AddEventSet(LoadLHCOlympics(eventfileNameB + "-2.lhco"))
testEvent3.AddEventSet(LoadLHCOlympics(eventfileNameB + "-3.lhco"))
testEvent4.AddEventSet(LoadLHCOlympics(eventfileNameB + "-4.lhco"))
testEvent5.AddEventSet(LoadLHCOlympics(eventfileNameB + "-5.lhco"))
testEvent6.AddEventSet(LoadLHCOlympics(eventfileNameB + "-6.lhco"))
testEvent7.AddEventSet(LoadLHCOlympics(eventfileNameB + "-7.lhco"))

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())


particleNumberCut = ParticleNumberZA()
deltaRCut = DeltaRCut(0.2)

CutEvents(testEvent0, particleNumberCut)
CutEvents(testEvent1, particleNumberCut)
CutEvents(testEvent2, particleNumberCut)
CutEvents(testEvent3, particleNumberCut)
CutEvents(testEvent4, particleNumberCut)
CutEvents(testEvent5, particleNumberCut)
CutEvents(testEvent6, particleNumberCut)
CutEvents(testEvent7, particleNumberCut)

CutEvents(testEvent0, deltaRCut)
CutEvents(testEvent1, deltaRCut)
CutEvents(testEvent2, deltaRCut)
CutEvents(testEvent3, deltaRCut)
CutEvents(testEvent4, deltaRCut)
CutEvents(testEvent5, deltaRCut)
CutEvents(testEvent6, deltaRCut)
CutEvents(testEvent7, deltaRCut)

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

SaveToLHCO(eventfileNameA + "-s-0.lhco", testEvent0)
print(eventfileNameA + "-s-0.lhco saved")
SaveToLHCO(eventfileNameA + "-s-1.lhco", testEvent1)
print(eventfileNameA + "-s-1.lhco saved")
SaveToLHCO(eventfileNameA + "-s-2.lhco", testEvent2)
print(eventfileNameA + "-s-2.lhco saved")
SaveToLHCO(eventfileNameA + "-s-3.lhco", testEvent3)
print(eventfileNameA + "-s-3.lhco saved")
SaveToLHCO(eventfileNameA + "-s-4.lhco", testEvent4)
print(eventfileNameA + "-s-4.lhco saved")
SaveToLHCO(eventfileNameA + "-s-5.lhco", testEvent5)
print(eventfileNameA + "-s-5.lhco saved")
SaveToLHCO(eventfileNameA + "-s-6.lhco", testEvent6)
print(eventfileNameA + "-s-6.lhco saved")
SaveToLHCO(eventfileNameA + "-s-7.lhco", testEvent7)
print(eventfileNameA + "-s-7.lhco saved")
# """

"""
sm: 2000000
jjjll: 2343725
fm4: 600000
fm5: 600000
ft5: 600000
ft6: 600000
ft7: 600000
ft9: 600000

ft5:
[1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]

ft6:
[1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]

ft7:
[1000000, 1000000, 999936, 1000000, 1000000, 1000000, 999962, 1000000]

ft9:
[1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]

"""
