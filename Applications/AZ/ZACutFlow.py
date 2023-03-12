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

#jjjll=94335 fb
#sm=3214fb
#fm2=2.811
#fm3=6.791
#fm4=2.884
#fm5=10.87
#ft5=4.455
#ft6=4.462
#ft7=4.420
#ft8=6.250
#ft9=10.33

os.chdir("../../")
testEventsm = LoadLHCOlympics("_DataFolder/za/features/smallsm.lhco")
testEventj3 = LoadLHCOlympics("_DataFolder/za/features/smalljjjll.lhco")
testEventm3 = LoadLHCOlympics("_DataFolder/za/features/smallm3.lhco")
testEventm4 = LoadLHCOlympics("_DataFolder/za/features/smallm4.lhco")
testEventm5 = LoadLHCOlympics("_DataFolder/za/features/smallm5.lhco")
testEventt5 = LoadLHCOlympics("_DataFolder/za/features/smallt5.lhco")
testEventt6 = LoadLHCOlympics("_DataFolder/za/features/smallt6.lhco")
testEventt7 = LoadLHCOlympics("_DataFolder/za/features/smallt7.lhco")
testEventt9 = LoadLHCOlympics("_DataFolder/za/features/smallt9.lhco")

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
testEventj35 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll5.lhco")
testEventj3.AddEventSet(testEventj32)
testEventj3.AddEventSet(testEventj33)
testEventj3.AddEventSet(testEventj35)
# testEventm2 = LoadLHCOlympics("_DataFolder/za/features/azsignalm2.lhco")
testEventm3 = LoadLHCOlympics("_DataFolder/za/features/azsignalm3.lhco")
testEventm3.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-fm3.lhco"))
testEventm4 = LoadLHCOlympics("_DataFolder/za/features/azsignalm4.lhco")
testEventm4.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-fm4.lhco"))
testEventm5 = LoadLHCOlympics("_DataFolder/za/features/azsignalm5.lhco")
testEventm5.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-fm5.lhco"))
testEventt5 = LoadLHCOlympics("_DataFolder/za/features/azsignalt5.lhco")
testEventt5.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-ft5.lhco"))
testEventt6 = LoadLHCOlympics("_DataFolder/za/features/azsignalt6.lhco")
testEventt6.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-ft6.lhco"))
testEventt7 = LoadLHCOlympics("_DataFolder/za/features/azsignalt7.lhco")
testEventt7.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-ft7.lhco"))
# testEventt8 = LoadLHCOlympics("_DataFolder/za/features/azsignalt8.lhco")
testEventt9 = LoadLHCOlympics("_DataFolder/za/features/azsignalt9.lhco")
testEventt9.AddEventSet(LoadLHCOlympics("_DataFolder/za/features/signal-n-ft9.lhco"))

particleNumberCut = ParticleNumberZA()
"""
vbsCut = StandardVBFCut(True, 100.0, 0.0)
vbsCut2 = StandardVBFCut(True, 0.0, 0.8)
invllCut = EllInvMass(25, 91.1876)
ellDotCut = DeltaRCutM(0.8)
rCut = RZACut(0.08, -1)
mzaCut1 = SHatZACut(1000, -1)
mzaCut2 = SHatZACut(1000, -1)
"""
deltaRCut = DeltaRCut(0.2)

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())

CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventj3, particleNumberCut)
CutEvents(testEventm3, particleNumberCut)
CutEvents(testEventm4, particleNumberCut)
CutEvents(testEventm5, particleNumberCut)
CutEvents(testEventt5, particleNumberCut)
CutEvents(testEventt6, particleNumberCut)
CutEvents(testEventt7, particleNumberCut)
CutEvents(testEventt9, particleNumberCut)

print("============== before DeltaR ===============")
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())

CutEvents(testEventm3, deltaRCut)
CutEvents(testEventm4, deltaRCut)
CutEvents(testEventm5, deltaRCut)
CutEvents(testEventt5, deltaRCut)
CutEvents(testEventt6, deltaRCut)
CutEvents(testEventt7, deltaRCut)
CutEvents(testEventt9, deltaRCut)

print("============== after partical number ===============")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())


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
ubcutfm4 = SHatZACut(-1, mzam4)
ubcutfm5 = SHatZACut(-1, mzam5)
ubcutft5 = SHatZACut(-1, mzat5)
ubcutft6 = SHatZACut(-1, mzat6)
ubcutft7 = SHatZACut(-1, mzat7)
ubcutft9 = SHatZACut(-1, mzat9)

CutEvents(testEventm3, ubcutfm3)
CutEvents(testEventm4, ubcutfm4)
CutEvents(testEventm5, ubcutfm5)
CutEvents(testEventt5, ubcutft5)
CutEvents(testEventt6, ubcutft6)
CutEvents(testEventt7, ubcutft7)
CutEvents(testEventt9, ubcutft9)
"""

print("============== after ub ===============")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())


CutEvents(testEventsm, vbsCut)
CutEvents(testEventj3, vbsCut)
CutEvents(testEventm3, vbsCut)
CutEvents(testEventm4, vbsCut)
CutEvents(testEventm5, vbsCut)
CutEvents(testEventt5, vbsCut)
CutEvents(testEventt6, vbsCut)
CutEvents(testEventt7, vbsCut)
CutEvents(testEventt9, vbsCut)

print("============== after vbf ===============")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())



CutEvents(testEventsm, ellDotCut)
CutEvents(testEventj3, ellDotCut)
CutEvents(testEventm3, ellDotCut)
CutEvents(testEventm4, ellDotCut)
CutEvents(testEventm5, ellDotCut)
CutEvents(testEventt5, ellDotCut)
CutEvents(testEventt6, ellDotCut)
CutEvents(testEventt7, ellDotCut)
CutEvents(testEventt9, ellDotCut)

print("============== after theta ll ===============")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())


CutEvents(testEventsm, invllCut)
CutEvents(testEventj3, invllCut)
CutEvents(testEventm3, invllCut)
CutEvents(testEventm4, invllCut)
CutEvents(testEventm5, invllCut)
CutEvents(testEventt5, invllCut)
CutEvents(testEventt6, invllCut)
CutEvents(testEventt7, invllCut)
CutEvents(testEventt9, invllCut)

print("============== after inv ll ===============")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())

testEventsmcpy = testEventsm.GetCopy()
testEventj3cpy = testEventj3.GetCopy()

""" this is for OT """
CutEvents(testEventsm, mzaCut2)
CutEvents(testEventj3, mzaCut2)
""" this is for OM """
CutEvents(testEventsmcpy, mzaCut1)
CutEvents(testEventj3cpy, mzaCut1)
CutEvents(testEventm3, mzaCut1)
CutEvents(testEventm4, mzaCut1)
CutEvents(testEventm5, mzaCut1)
CutEvents(testEventt5, mzaCut2)
CutEvents(testEventt6, mzaCut2)
CutEvents(testEventt7, mzaCut2)
CutEvents(testEventt9, mzaCut2)

print("============== after s hat ===============")
print("sm j3 r")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print("sm j3 vbf")
print(testEventsmcpy.GetEventCount())
print(testEventj3cpy.GetEventCount())
print("om")
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print("os")
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())

""" this is for OT """
CutEvents(testEventsm, rCut)
CutEvents(testEventj3, rCut)
# CutEvents(testEventsm, vbsCut2)
# CutEvents(testEventj3, vbsCut2)
""" this is for OM """
CutEvents(testEventsmcpy, vbsCut2)
CutEvents(testEventj3cpy, vbsCut2)
CutEvents(testEventm3, vbsCut2)
CutEvents(testEventm4, vbsCut2)
CutEvents(testEventm5, vbsCut2)
CutEvents(testEventt5, rCut)
CutEvents(testEventt6, rCut)
CutEvents(testEventt7, rCut)
CutEvents(testEventt9, rCut)
# CutEvents(testEventt5, vbsCut2)
# CutEvents(testEventt6, vbsCut2)
# CutEvents(testEventt7, vbsCut2)
# CutEvents(testEventt9, vbsCut2)

print("============== after r ===============")
print("sm j3 r and mjj200 ")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print("sm mj250 and dy 1.6 ")
print(testEventsmcpy.GetEventCount())
print(testEventj3cpy.GetEventCount())
print("om")
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print("os")
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt9.GetEventCount())

"""
2000000
1843772
600000
600000
600000
600000
600000
600000
600000
============== before DeltaR ===============
308193
293844
313697
289951
285560
288526
282804
============== after partical number ===============
442364
14081
130769
144210
131655
118683
139407
123509
120497
============== after ub ===============
442364
14081
18344
33303
29256
33272
31453
31483
17525
============== after vbf ===============
235764
9035
17154
31247
27384
31487
29778
29833
16457
============== after theta ll ===============
16222
1091
13416
25257
22798
26532
23656
24818
13008
============== after inv ll ===============
3026
424
13255
25028
22600
26230
23372
24507
12877
============== after s hat ===============
sm j3 r
89
1
sm j3 vbf
89
1
om
9688
21067
18788
os
24790
20958
22735
11244
============== after r ===============
sm j3 r
47
0
sm j3 vbf
57
1
om
9238
19827
17694
os
20026
16292
18255
8888

============== after r ===============
sm j3 r
44
0
sm j3 vbf
54
1
om
19750
17612
os
19703
15999
17962
8735

Process finished with exit code 0


Process finished with exit code 0

"""