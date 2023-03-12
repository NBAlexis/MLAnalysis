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

# ft5-new-0 has problem

os.chdir("../../_DataFolder/za/newfittings")
eventfileNameA = "ft9/ft9-s"
# eventfileNameB = "ft9/ft9-n"
usercut = True

particleNumberCut = ParticleNumberZA()
vbsCut = StandardVBFCut(True, 100.0, 0.0)
vbsCut2 = StandardVBFCut(True, 0.0, 0.8)
invllCut = EllInvMass(25, 91.1876)
drCut = DeltaRCutM(0.8)
rCut = RZACut(0.08, -1)
mazCut1 = SHatZACut(1000, -1)
mazCut2 = SHatZACut(1000, -1)

mw = 80.379
# 80.385 at z pole, 79.9534?
mz = 91.1876
cw = 0.876801
sw = 0.480853
vev = 246.22
# 246.22
e2 = 0.0982177 # 0.0934761  # sqrt{ 4 pi alpha} for alpha = 1/134
# 0.0982177 at z pole
# smbg = 11.75 if usercut else 14.25

# cefm2 = [-8.2e-12, -6.15e-12, -4.1e-12, -2.05e-12, 2.0e-12, 4.0e-12, 6.0e-12, 8.0e-12]
cefm3 = [-21.0e-12, -15.75e-12, -10.5e-12, -5.25e-12, 5.25e-12, 10.5e-12, 15.75e-12, 21.0e-12]
cefm4 = [-15.0e-12, -11.25e-12, -7.5e-12, -3.75e-12, 4.0e-12, 8.0e-12, 12.0e-12, 16.0e-12]
cefm5 = [-25.0e-12, -18.75e-12, -12.5e-12, -6.25e-12, 6.0e-12, 12.0e-12, 18.0e-12, 24.0e-12]
# ceft2 = [-0.28e-12, -0.21e-12, -0.14e-12, -0.07e-12, 0.07e-12, 0.14e-12, 0.21e-12, 0.28e-12]
ceft5 = [-0.7e-12, -0.525e-12, -0.35e-12, -0.175e-12, 0.185e-12, 0.37e-12, 0.555e-12, 0.74e-12]
ceft6 = [-1.6e-12, -1.2e-12, -0.8e-12, -0.4e-12, 0.425e-12, 0.85e-12, 1.275e-12, 1.7e-12]
ceft7 = [-2.6e-12, -1.95e-12, -1.3e-12, -0.65e-12, 0.7e-12, 1.4e-12, 2.1e-12, 2.8e-12]
# ceft8 = [-0.47e-12, -0.3525e-12, -0.235e-12, -0.1175e-12, 0.1175e-12, 0.235e-12, 0.3525e-12, 0.47e-12]
ceft9 = [-1.3e-12, -0.975e-12, -0.65e-12, -0.325e-12, 0.325e-12, 0.65e-12, 0.975e-12, 1.3e-12]

mzam3 = [math.sqrt(math.sqrt(32 * math.sqrt(2.0) * 3.14159265359 * cw * sw * mz * mz / (abs(cefm3[i]) * e2 * vev * vev))) for i in range(0, 8)]
mzam4 = [math.sqrt(math.sqrt(
    64 * math.sqrt(2.0) * 3.14159265359 * cw * cw * sw * sw * mz * mz / (abs(cefm4[i]) * (cw * cw - sw * sw) * e2 * vev * vev))) for i in range(0, 8)]
mzam5 = [math.sqrt(math.sqrt(192 * 3.14159265359 * sw * sw * mw * mz / (abs(cefm5[i]) * e2 * vev * vev))) for i in range(0, 8)]

mzat5 = [math.sqrt(math.sqrt(3.14159265359 / (abs(ceft5[i]) * cw * cw * sw * sw))) for i in range(0, 8)]
mzat6 = [math.sqrt(math.sqrt(4 * 3.14159265359 / (abs(ceft6[i]) * (cw * cw - sw * sw)))) for i in range(0, 8)]
mzat7 = [math.sqrt(math.sqrt(8 * math.sqrt(2.0) * 3.14159265359 / (3 * abs(ceft7[i]) * (cw * cw - sw * sw) * cw * sw))) for i in range(0, 8)]

mzat9 = [math.sqrt(math.sqrt(2 * 3.14159265359 / (3 * abs(ceft9[i]) * cw * cw * sw * sw))) for i in range(0, 8)]

# csm2 = [3.215410e+00, 3.217469e+00, 3.213814e+00, 3.212588e+00, 3.212947e+00, 3.212922e+00, 3.213983e+00,
#         3.213225e+00, 3.214454e+00, 3.215051e+00, 3.215380e+00]

csm3 = [3.300413, 3.303718, 3.301809, 3.301382, 3.303433, 3.303993, 3.301815, 3.304791]

csm4 = [3.302168, 3.302694, 3.303989, 3.303423, 3.302925, 3.304942, 3.303569, 3.302564]

csm5 = [3.305420, 3.305494, 3.303532, 3.302692, 3.303199, 3.301171, 3.304708, 3.304336]

cst5 = [3.303495, 3.302399, 3.302841, 3.302790, 3.302627, 3.302287, 3.302630, 3.301742]

cst6 = [3.302495, 3.304344, 3.302963, 3.301411, 3.302572, 3.304112, 3.301829, 3.305289]

cst7 = [3.302869, 3.301668, 3.304165, 3.303329, 3.304152, 3.304350, 3.302971, 3.302536]

cst9 = [3.304434, 3.302627, 3.301188, 3.301484, 3.302339, 3.302326, 3.301592, 3.302570]

cs = cst9
mzaub = mzat9
print(mzaub)
mzaCut2 = [SHatZACut(-1, mzaub[i]) for i in range(0, 8)]

testEvent0 = LoadLHCOlympics(eventfileNameA + "-0.lhco")
testEvent1 = LoadLHCOlympics(eventfileNameA + "-1.lhco")
testEvent2 = LoadLHCOlympics(eventfileNameA + "-2.lhco")
testEvent3 = LoadLHCOlympics(eventfileNameA + "-3.lhco")
testEvent4 = LoadLHCOlympics(eventfileNameA + "-4.lhco")
testEvent5 = LoadLHCOlympics(eventfileNameA + "-5.lhco")
testEvent6 = LoadLHCOlympics(eventfileNameA + "-6.lhco")
testEvent7 = LoadLHCOlympics(eventfileNameA + "-7.lhco")

"""
testEvent0.AddEventSet(LoadLHCOlympics(eventfileNameB + "-0.lhco"))
testEvent1.AddEventSet(LoadLHCOlympics(eventfileNameB + "-1.lhco"))
testEvent2.AddEventSet(LoadLHCOlympics(eventfileNameB + "-2.lhco"))
testEvent3.AddEventSet(LoadLHCOlympics(eventfileNameB + "-3.lhco"))
testEvent4.AddEventSet(LoadLHCOlympics(eventfileNameB + "-4.lhco"))
testEvent5.AddEventSet(LoadLHCOlympics(eventfileNameB + "-5.lhco"))
testEvent6.AddEventSet(LoadLHCOlympics(eventfileNameB + "-6.lhco"))
testEvent7.AddEventSet(LoadLHCOlympics(eventfileNameB + "-7.lhco"))
"""

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

evnm0 = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]
# evnm0 = [1000000, 1000000, 999936, 1000000, 1000000, 1000000, 999962, 1000000]

# CutEvents(testEvent0, particleNumberCut)
# CutEvents(testEvent1, particleNumberCut)
# CutEvents(testEvent2, particleNumberCut)
# CutEvents(testEvent3, particleNumberCut)
# CutEvents(testEvent4, particleNumberCut)
# CutEvents(testEvent5, particleNumberCut)
# CutEvents(testEvent6, particleNumberCut)
# CutEvents(testEvent7, particleNumberCut)

# print("============== after particle number ============")

# print(testEvent0.GetEventCount())
# print(testEvent1.GetEventCount())
# print(testEvent2.GetEventCount())
# print(testEvent3.GetEventCount())
# print(testEvent4.GetEventCount())
# print(testEvent5.GetEventCount())
# print(testEvent6.GetEventCount())
# print(testEvent7.GetEventCount())

CutEvents(testEvent0, vbsCut)
CutEvents(testEvent1, vbsCut)
CutEvents(testEvent2, vbsCut)
CutEvents(testEvent3, vbsCut)
CutEvents(testEvent4, vbsCut)
CutEvents(testEvent5, vbsCut)
CutEvents(testEvent6, vbsCut)
CutEvents(testEvent7, vbsCut)

print("============== after vbs cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

CutEvents(testEvent0, invllCut)
CutEvents(testEvent1, invllCut)
CutEvents(testEvent2, invllCut)
CutEvents(testEvent3, invllCut)
CutEvents(testEvent4, invllCut)
CutEvents(testEvent5, invllCut)
CutEvents(testEvent6, invllCut)
CutEvents(testEvent7, invllCut)

print("============== after mll cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

CutEvents(testEvent0, drCut)
CutEvents(testEvent1, drCut)
CutEvents(testEvent2, drCut)
CutEvents(testEvent3, drCut)
CutEvents(testEvent4, drCut)
CutEvents(testEvent5, drCut)
CutEvents(testEvent6, drCut)
CutEvents(testEvent7, drCut)

print("============== after ell cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

if usercut:
    CutEvents(testEvent0, mazCut2)
    CutEvents(testEvent1, mazCut2)
    CutEvents(testEvent2, mazCut2)
    CutEvents(testEvent3, mazCut2)
    CutEvents(testEvent4, mazCut2)
    CutEvents(testEvent5, mazCut2)
    CutEvents(testEvent6, mazCut2)
    CutEvents(testEvent7, mazCut2)
else:
    CutEvents(testEvent0, mazCut1)
    CutEvents(testEvent1, mazCut1)
    CutEvents(testEvent2, mazCut1)
    CutEvents(testEvent3, mazCut1)
    CutEvents(testEvent4, mazCut1)
    CutEvents(testEvent5, mazCut1)
    CutEvents(testEvent6, mazCut1)
    CutEvents(testEvent7, mazCut1)

print("============== after shat cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

if usercut:
    CutEvents(testEvent0, rCut)
    CutEvents(testEvent1, rCut)
    CutEvents(testEvent2, rCut)
    CutEvents(testEvent3, rCut)
    CutEvents(testEvent4, rCut)
    CutEvents(testEvent5, rCut)
    CutEvents(testEvent6, rCut)
    CutEvents(testEvent7, rCut)
else:
    CutEvents(testEvent0, vbsCut2)
    CutEvents(testEvent1, vbsCut2)
    CutEvents(testEvent2, vbsCut2)
    CutEvents(testEvent3, vbsCut2)
    CutEvents(testEvent4, vbsCut2)
    CutEvents(testEvent5, vbsCut2)
    CutEvents(testEvent6, vbsCut2)
    CutEvents(testEvent7, vbsCut2)

print("============== before unitarity bound ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

evnm1 = [testEvent0.GetEventCount(), testEvent1.GetEventCount(), testEvent2.GetEventCount(), testEvent3.GetEventCount(),
         testEvent4.GetEventCount(), testEvent5.GetEventCount(), testEvent6.GetEventCount(), testEvent7.GetEventCount()]


CutEvents(testEvent0, mzaCut2[0])
CutEvents(testEvent1, mzaCut2[1])
CutEvents(testEvent2, mzaCut2[2])
CutEvents(testEvent3, mzaCut2[3])
CutEvents(testEvent4, mzaCut2[4])
CutEvents(testEvent5, mzaCut2[5])
CutEvents(testEvent6, mzaCut2[6])
CutEvents(testEvent7, mzaCut2[7])


print("============== after unitarity bound ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

evnm2 = [testEvent0.GetEventCount(), testEvent1.GetEventCount(), testEvent2.GetEventCount(), testEvent3.GetEventCount(),
         testEvent4.GetEventCount(), testEvent5.GetEventCount(), testEvent6.GetEventCount(), testEvent7.GetEventCount()]

print("[{}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
      1000 * cs[0] * evnm1[0] / evnm0[0],
      1000 * cs[1] * evnm1[1] / evnm0[1],
      1000 * cs[2] * evnm1[2] / evnm0[2],
      1000 * cs[3] * evnm1[3] / evnm0[3],
      0.106 if usercut else 0.140,
      1000 * cs[4] * evnm1[4] / evnm0[4],
      1000 * cs[5] * evnm1[5] / evnm0[5],
      1000 * cs[6] * evnm1[6] / evnm0[6],
      1000 * cs[7] * evnm1[7] / evnm0[7]))

print("[{}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
      1000 * cs[0] * evnm2[0] / evnm0[0],
      1000 * cs[1] * evnm2[1] / evnm0[1],
      1000 * cs[2] * evnm2[2] / evnm0[2],
      1000 * cs[3] * evnm2[3] / evnm0[3],
      0.106 if usercut else 0.140,
      1000 * cs[4] * evnm2[4] / evnm0[4],
      1000 * cs[5] * evnm2[5] / evnm0[5],
      1000 * cs[6] * evnm2[6] / evnm0[6],
      1000 * cs[7] * evnm2[7] / evnm0[7]))


"""

================================ ft5 ===========================


ceft5 = [-0.7e-12, -0.525e-12, -0.35e-12, -0.175e-12, 0.185e-12, 0.37e-12, 0.555e-12, 0.74e-12]

[0.280797075, 0.191539142, 0.15193068599999998, 0.08587254, 0.078, 0.09577618300000001, 0.095766323, 0.17503939000000002, 0.29715677999999995]
[0.16517475, 0.158515152, 0.13211363999999998, 0.08587254, 0.078, 0.09577618300000001, 0.07925488800000001, 0.14531572, 0.204708004]


============================== ft6 =====================================

ceft6 = [-1.6e-12, -1.2e-12, -0.8e-12, -0.4e-12, 0.425e-12, 0.85e-12, 1.275e-12, 1.7e-12]

[0.20475469, 0.208173672, 0.102391853, 0.08913809700000001, 0.078, 0.105682304, 0.11894803200000001, 0.181600595, 0.284254854]
[0.128797305, 0.14869548000000002, 0.08918000100000001, 0.08253527499999999, 0.078, 0.105682304, 0.105731584, 0.135374989, 0.20162262900000003]


============== ft7 ============

ceft7 = [-2.6e-12, -1.95e-12, -1.3e-12, -0.65e-12, 0.7e-12, 1.4e-12, 2.1e-12, 2.8e-12]

[0.32698403099999995, 0.254228436, 0.19826258880568357, 0.181683095, 0.106, 0.14868684, 0.1652175, 0.2642477214134137, 0.290623168]
[0.22459509199999997, 0.201401748, 0.18174070640520995, 0.171773108, 0.106, 0.14538268799999998, 0.14869575, 0.1981857910600603, 0.19154708799999998]

============== ft9 ============

ceft9 = [-1.3e-12, -0.975e-12, -0.65e-12, -0.325e-12, 0.325e-12, 0.65e-12, 0.975e-12, 1.3e-12]
[0.343661136, 0.27411804100000003, 0.20467365599999998, 0.13536084399999998, 0.106, 0.11558186499999999, 0.250976776, 0.28063531999999997, 0.28402101999999996]
[0.20157047400000003, 0.18164448500000002, 0.171661776, 0.125456392, 0.106, 0.09907017, 0.211348864, 0.19479392799999998, 0.14861565]

=========================================================
"""