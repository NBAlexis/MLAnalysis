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

os.chdir("../../_DataFolder/za/newnew")
eventfileNameA = "fm4/fm4"
usercut = False

particleNumberCut = ParticleNumberZA()
# vbsCut = StandardVBFCut(True, 100.0, 0.0)
vbsCut2 = StandardVBFCut(True, 0.0, 0.8)
# invllCut = EllInvMass(10, 91.1876)
# drCut = DeltaRCutM(0.8)
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

cefm4 = [-1.5e-11, -1.3125e-11, -1.125e-11, -9.375e-12, -7.5e-12, -5.625e-12, -3.75e-12, -1.875e-12, 1.0e-22, 2e-12, 4e-12, 6e-12, 8e-12, 1e-11, 1.2e-11, 1.4e-11, 1.6e-11]

cefm5 = [-2.5e-11, -2.1875e-11, -1.875e-11, -1.5625e-11, -1.25e-11, -9.375e-12, -6.25e-12, -3.125e-12, 1.0e-22, 3e-12, 6e-12, 9e-12, 1.2e-11, 1.5e-11, 1.8e-11, 2.1e-11, 2.4e-11]

# ceft2 = [-0.28e-12, -0.21e-12, -0.14e-12, -0.07e-12, 0.07e-12, 0.14e-12, 0.21e-12, 0.28e-12]

ceft5 = [-7e-13, -6.125e-13, -5.25e-13, -4.375e-13, -3.5e-13, 2.625e-13, -1.75e-13, -8.75e-14, 1.0e-22, 9.25e-14, 1.85e-13, 2.775e-13, 3.7e-13, 4.625e-13, 5.55e-13, 6.475e-13, 7.4e-13]

ceft6 = [-1.6e-12, -1.4e-12, -1.2e-12, -1.0e-12, -0.8e-12, -0.6e-12, -0.4e-12, -0.2e-12, 1.0e-22, 0.2125e-12, 0.425e-12, 0.6375e-12, 0.85e-12, 1.0625e-12, 1.275e-12, 1.4875e-12, 1.7e-12]

ceft7 = [-2.6e-12, -2.275e-12, -1.95e-12, -1.625e-12, -1.3e-12, -0.975e-12, -0.65e-12, -0.325e-12, 1.0e-22, 0.35e-12, 0.7e-12, 1.05e-12, 1.40e-12, 1.75e-12, 2.1e-12, 2.45e-12, 2.8e-12]

# ceft8 = [-0.47e-12, -0.3525e-12, -0.235e-12, -0.1175e-12, 0.1175e-12, 0.235e-12, 0.3525e-12, 0.47e-12]
ceft9 = [-1.3e-12, -1.1375e-12, -0.975e-12, -0.8125e-12, -0.65e-12, -0.4875e-12, -0.325e-12, -0.1625e-12, 1.0e-22, 0.1625e-12, 0.325e-12, 0.4875e-12, 0.65e-12, 0.8125e-12, 0.975e-12, 1.1375e-12, 1.3e-12]

mzam3 = [math.sqrt(math.sqrt(32 * math.sqrt(2.0) * 3.14159265359 * cw * sw * mz * mz / (abs(cefm3[i]) * e2 * vev * vev))) for i in range(0, 8)]

mzam4 = [math.sqrt(math.sqrt(
    64 * math.sqrt(2.0) * 3.14159265359 * cw * cw * sw * sw * mz * mz / (abs(cefm4[i]) * (cw * cw - sw * sw) * e2 * vev * vev))) for i in range(0, 17)]
mzam4h = [math.sqrt(math.sqrt(
    2.0 * 64 * math.sqrt(2.0) * 3.14159265359 * cw * cw * sw * sw * mz * mz / (abs(cefm4[i]) * (cw * cw - sw * sw) * e2 * vev * vev))) for i in range(0, 17)]
mzam4d = [math.sqrt(math.sqrt(
    0.5 * 64 * math.sqrt(2.0) * 3.14159265359 * cw * cw * sw * sw * mz * mz / (abs(cefm4[i]) * (cw * cw - sw * sw) * e2 * vev * vev))) for i in range(0, 17)]

mzam5 = [math.sqrt(math.sqrt(192 * 3.14159265359 * sw * sw * mw * mz / (abs(cefm5[i]) * e2 * vev * vev))) for i in range(0, 17)]
mzam5h = [math.sqrt(math.sqrt(2.0 * 192 * 3.14159265359 * sw * sw * mw * mz / (abs(cefm5[i]) * e2 * vev * vev))) for i in range(0, 17)]
mzam5d = [math.sqrt(math.sqrt(0.5 * 192 * 3.14159265359 * sw * sw * mw * mz / (abs(cefm5[i]) * e2 * vev * vev))) for i in range(0, 17)]

mzat5 = [math.sqrt(math.sqrt(3.14159265359 / (abs(ceft5[i]) * cw * cw * sw * sw))) for i in range(0, 17)]
mzat5h = [math.sqrt(math.sqrt(2.0 * 3.14159265359 / (abs(ceft5[i]) * cw * cw * sw * sw))) for i in range(0, 17)]
mzat5d = [math.sqrt(math.sqrt(0.5 * 3.14159265359 / (abs(ceft5[i]) * cw * cw * sw * sw))) for i in range(0, 17)]

mzat6 = [math.sqrt(math.sqrt(4 * 3.14159265359 / (abs(ceft6[i]) * (cw * cw - sw * sw)))) for i in range(0, 17)]
mzat6h = [math.sqrt(math.sqrt(2.0 * 4 * 3.14159265359 / (abs(ceft6[i]) * (cw * cw - sw * sw)))) for i in range(0, 17)]
mzat6d = [math.sqrt(math.sqrt(0.5 * 4 * 3.14159265359 / (abs(ceft6[i]) * (cw * cw - sw * sw)))) for i in range(0, 17)]

mzat7 = [math.sqrt(math.sqrt(8 * math.sqrt(2.0) * 3.14159265359 / (3 * abs(ceft7[i]) * (cw * cw - sw * sw) * cw * sw))) for i in range(0, 17)]
mzat7h = [math.sqrt(math.sqrt(2.0 * 8 * math.sqrt(2.0) * 3.14159265359 / (3 * abs(ceft7[i]) * (cw * cw - sw * sw) * cw * sw))) for i in range(0, 17)]
mzat7d = [math.sqrt(math.sqrt(0.5 * 8 * math.sqrt(2.0) * 3.14159265359 / (3 * abs(ceft7[i]) * (cw * cw - sw * sw) * cw * sw))) for i in range(0, 17)]

mzat9 = [math.sqrt(math.sqrt(2 * 3.14159265359 / (3 * abs(ceft9[i]) * cw * cw * sw * sw))) for i in range(0, 17)]
mzat9h = [math.sqrt(math.sqrt(2.0 * 2 * 3.14159265359 / (3 * abs(ceft9[i]) * cw * cw * sw * sw))) for i in range(0, 17)]
mzat9d = [math.sqrt(math.sqrt(0.5 * 2 * 3.14159265359 / (3 * abs(ceft9[i]) * cw * cw * sw * sw))) for i in range(0, 17)]

# csm2 = [3.215410e+00, 3.217469e+00, 3.213814e+00, 3.212588e+00, 3.212947e+00, 3.212922e+00, 3.213983e+00,
#         3.213225e+00, 3.214454e+00, 3.215051e+00, 3.215380e+00]

csm3 = [3.300413, 3.303718, 3.301809, 3.301382, 3.303433, 3.303993, 3.301815, 3.304791]

csm4 = [0.01920333, 0.01903318, 0.01889238, 0.01886421, 0.01888804, 0.01880008, 0.01871418, 0.01861723, 0.01875862, 0.01876711, 0.01881069, 0.01880306, 0.01895656, 0.0189422, 0.01913988, 0.01912938, 0.01923554]

csm5 = [0.02079628, 0.02022477, 0.01977676, 0.01947045, 0.01924135, 0.01905016, 0.01882909, 0.01884689, 0.01875633, 0.0187594, 0.01895182, 0.01897407, 0.01901435, 0.01935937, 0.01968454, 0.02003264, 0.0205372]

cst5 = [0.01953315, 0.01932127, 0.01911402, 0.01903731, 0.01896598, 0.01887025, 0.01872181, 0.01865201, 0.01875921, 0.01877686, 0.01882201, 0.01885801, 0.01902432, 0.01909048, 0.01933879, 0.01939306, 0.01959845]


cst6 = [1.967827e-02, 1.939690e-02, 1.926170e-02, 1.906988e-02, 1.899650e-02,
        1.881397e-02, 1.889446e-02, 1.879877e-02, 1.879831e-02,
        1.873854e-02, 1.884838e-02, 1.898309e-02, 1.897212e-02,
        1.910359e-02, 1.937112e-02, 1.950966e-02, 1.977169e-02]

cst7 = [1.947130e-02, 1.933375e-02, 1.922100e-02, 1.908863e-02,
        1.882178e-02, 1.884216e-02, 1.880014e-02, 1.869239e-02, 1.878274e-02,
        1.871156e-02, 1.883403e-02, 1.885642e-02, 1.900533e-02,
        1.912124e-02, 1.920818e-02, 1.936896e-02, 1.958787e-02]

cst9 = [2.076397e-02, 2.032789e-02, 1.989580e-02, 1.959619e-02, 1.915623e-02,
        1.901480e-02, 1.886301e-02, 1.868098e-02, 1.878334e-02,
        1.870653e-02, 1.889363e-02, 1.906351e-02, 1.930512e-02,
        1.960768e-02, 1.986875e-02, 2.017960e-02, 2.074727e-02]

cs = csm4
mzaub = mzam4
mzaubh = mzam4h
mzaubd = mzam4d
print(mzaub)
mzaCut2 = [SHatZACut(-1, mzaub[i]) for i in range(0, 17)]
mzaCut2h = [SHatZACut(-1, mzaubh[i]) for i in range(0, 17)]
mzaCut2d = [SHatZACut(-1, mzaubd[i]) for i in range(0, 17)]

testEvent0 = LoadLHCOlympics(eventfileNameA + "-0.lhco")
testEvent1 = LoadLHCOlympics(eventfileNameA + "-1.lhco")
testEvent2 = LoadLHCOlympics(eventfileNameA + "-2.lhco")
testEvent3 = LoadLHCOlympics(eventfileNameA + "-3.lhco")
testEvent4 = LoadLHCOlympics(eventfileNameA + "-4.lhco")
testEvent5 = LoadLHCOlympics(eventfileNameA + "-5.lhco")
testEvent6 = LoadLHCOlympics(eventfileNameA + "-6.lhco")
testEvent7 = LoadLHCOlympics(eventfileNameA + "-7.lhco")
testEvent8 = LoadLHCOlympics(eventfileNameA + "-8.lhco")
testEvent9 = LoadLHCOlympics(eventfileNameA + "-9.lhco")
testEvent10 = LoadLHCOlympics(eventfileNameA + "-10.lhco")
testEvent11 = LoadLHCOlympics(eventfileNameA + "-11.lhco")
testEvent12 = LoadLHCOlympics(eventfileNameA + "-12.lhco")
testEvent13 = LoadLHCOlympics(eventfileNameA + "-13.lhco")
testEvent14 = LoadLHCOlympics(eventfileNameA + "-14.lhco")
testEvent15 = LoadLHCOlympics(eventfileNameA + "-15.lhco")
testEvent16 = LoadLHCOlympics(eventfileNameA + "-16.lhco")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())
print(testEvent8.GetEventCount())
print(testEvent9.GetEventCount())
print(testEvent10.GetEventCount())
print(testEvent11.GetEventCount())
print(testEvent12.GetEventCount())
print(testEvent13.GetEventCount())
print(testEvent14.GetEventCount())
print(testEvent15.GetEventCount())
print(testEvent16.GetEventCount())

evnm0 = [testEvent0.GetEventCount(), testEvent1.GetEventCount(), testEvent2.GetEventCount(), testEvent3.GetEventCount(),
         testEvent4.GetEventCount(), testEvent5.GetEventCount(), testEvent6.GetEventCount(), testEvent7.GetEventCount(),
         testEvent8.GetEventCount(), testEvent9.GetEventCount(), testEvent10.GetEventCount(), testEvent11.GetEventCount(),
         testEvent12.GetEventCount(), testEvent13.GetEventCount(), testEvent14.GetEventCount(), testEvent15.GetEventCount(),
         testEvent16.GetEventCount()]

CutEvents(testEvent0, particleNumberCut)
CutEvents(testEvent1, particleNumberCut)
CutEvents(testEvent2, particleNumberCut)
CutEvents(testEvent3, particleNumberCut)
CutEvents(testEvent4, particleNumberCut)
CutEvents(testEvent5, particleNumberCut)
CutEvents(testEvent6, particleNumberCut)
CutEvents(testEvent7, particleNumberCut)
CutEvents(testEvent8, particleNumberCut)
CutEvents(testEvent9, particleNumberCut)
CutEvents(testEvent10, particleNumberCut)
CutEvents(testEvent11, particleNumberCut)
CutEvents(testEvent12, particleNumberCut)
CutEvents(testEvent13, particleNumberCut)
CutEvents(testEvent14, particleNumberCut)
CutEvents(testEvent15, particleNumberCut)
CutEvents(testEvent16, particleNumberCut)

print("============== after particle number ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())
print(testEvent8.GetEventCount())
print(testEvent9.GetEventCount())
print(testEvent10.GetEventCount())
print(testEvent11.GetEventCount())
print(testEvent12.GetEventCount())
print(testEvent13.GetEventCount())
print(testEvent14.GetEventCount())
print(testEvent15.GetEventCount())
print(testEvent16.GetEventCount())

"""
if not usercut:
    CutEvents(testEvent0, invllCut)
    CutEvents(testEvent1, invllCut)
    CutEvents(testEvent2, invllCut)
    CutEvents(testEvent3, invllCut)
    CutEvents(testEvent4, invllCut)
    CutEvents(testEvent5, invllCut)
    CutEvents(testEvent6, invllCut)
    CutEvents(testEvent7, invllCut)
    CutEvents(testEvent8, invllCut)
    CutEvents(testEvent9, invllCut)
    CutEvents(testEvent10, invllCut)
    CutEvents(testEvent11, invllCut)
    CutEvents(testEvent12, invllCut)
    CutEvents(testEvent13, invllCut)
    CutEvents(testEvent14, invllCut)
    CutEvents(testEvent15, invllCut)
    CutEvents(testEvent16, invllCut)
    print("============== after invllCut ============")
    print(testEvent0.GetEventCount())
    print(testEvent1.GetEventCount())
    print(testEvent2.GetEventCount())
    print(testEvent3.GetEventCount())
    print(testEvent4.GetEventCount())
    print(testEvent5.GetEventCount())
    print(testEvent6.GetEventCount())
    print(testEvent7.GetEventCount())
    print(testEvent8.GetEventCount())
    print(testEvent9.GetEventCount())
    print(testEvent10.GetEventCount())
    print(testEvent11.GetEventCount())
    print(testEvent12.GetEventCount())
    print(testEvent13.GetEventCount())
    print(testEvent14.GetEventCount())
    print(testEvent15.GetEventCount())
    print(testEvent16.GetEventCount())
"""

if usercut:
    CutEvents(testEvent0, mazCut2)
    CutEvents(testEvent1, mazCut2)
    CutEvents(testEvent2, mazCut2)
    CutEvents(testEvent3, mazCut2)
    CutEvents(testEvent4, mazCut2)
    CutEvents(testEvent5, mazCut2)
    CutEvents(testEvent6, mazCut2)
    CutEvents(testEvent7, mazCut2)
    CutEvents(testEvent8, mazCut2)
    CutEvents(testEvent9, mazCut2)
    CutEvents(testEvent10, mazCut2)
    CutEvents(testEvent11, mazCut2)
    CutEvents(testEvent12, mazCut2)
    CutEvents(testEvent13, mazCut2)
    CutEvents(testEvent14, mazCut2)
    CutEvents(testEvent15, mazCut2)
    CutEvents(testEvent16, mazCut2)
else:
    CutEvents(testEvent0, mazCut1)
    CutEvents(testEvent1, mazCut1)
    CutEvents(testEvent2, mazCut1)
    CutEvents(testEvent3, mazCut1)
    CutEvents(testEvent4, mazCut1)
    CutEvents(testEvent5, mazCut1)
    CutEvents(testEvent6, mazCut1)
    CutEvents(testEvent7, mazCut1)
    CutEvents(testEvent8, mazCut1)
    CutEvents(testEvent9, mazCut1)
    CutEvents(testEvent10, mazCut1)
    CutEvents(testEvent11, mazCut1)
    CutEvents(testEvent12, mazCut1)
    CutEvents(testEvent13, mazCut1)
    CutEvents(testEvent14, mazCut1)
    CutEvents(testEvent15, mazCut1)
    CutEvents(testEvent16, mazCut1)

print("============== after shat cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())
print(testEvent8.GetEventCount())
print(testEvent9.GetEventCount())
print(testEvent10.GetEventCount())
print(testEvent11.GetEventCount())
print(testEvent12.GetEventCount())
print(testEvent13.GetEventCount())
print(testEvent14.GetEventCount())
print(testEvent15.GetEventCount())
print(testEvent16.GetEventCount())

if usercut:
    CutEvents(testEvent0, rCut)
    CutEvents(testEvent1, rCut)
    CutEvents(testEvent2, rCut)
    CutEvents(testEvent3, rCut)
    CutEvents(testEvent4, rCut)
    CutEvents(testEvent5, rCut)
    CutEvents(testEvent6, rCut)
    CutEvents(testEvent7, rCut)
    CutEvents(testEvent8, rCut)
    CutEvents(testEvent9, rCut)
    CutEvents(testEvent10, rCut)
    CutEvents(testEvent11, rCut)
    CutEvents(testEvent12, rCut)
    CutEvents(testEvent13, rCut)
    CutEvents(testEvent14, rCut)
    CutEvents(testEvent15, rCut)
    CutEvents(testEvent16, rCut)
else:
    CutEvents(testEvent0, vbsCut2)
    CutEvents(testEvent1, vbsCut2)
    CutEvents(testEvent2, vbsCut2)
    CutEvents(testEvent3, vbsCut2)
    CutEvents(testEvent4, vbsCut2)
    CutEvents(testEvent5, vbsCut2)
    CutEvents(testEvent6, vbsCut2)
    CutEvents(testEvent7, vbsCut2)
    CutEvents(testEvent8, vbsCut2)
    CutEvents(testEvent9, vbsCut2)
    CutEvents(testEvent10, vbsCut2)
    CutEvents(testEvent11, vbsCut2)
    CutEvents(testEvent12, vbsCut2)
    CutEvents(testEvent13, vbsCut2)
    CutEvents(testEvent14, vbsCut2)
    CutEvents(testEvent15, vbsCut2)
    CutEvents(testEvent16, vbsCut2)


print("============== before unitarity bound ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())
print(testEvent8.GetEventCount())
print(testEvent9.GetEventCount())
print(testEvent10.GetEventCount())
print(testEvent11.GetEventCount())
print(testEvent12.GetEventCount())
print(testEvent13.GetEventCount())
print(testEvent14.GetEventCount())
print(testEvent15.GetEventCount())
print(testEvent16.GetEventCount())

evnm1 = [testEvent0.GetEventCount(), testEvent1.GetEventCount(), testEvent2.GetEventCount(), testEvent3.GetEventCount(),
         testEvent4.GetEventCount(), testEvent5.GetEventCount(), testEvent6.GetEventCount(), testEvent7.GetEventCount(),
         testEvent8.GetEventCount(), testEvent9.GetEventCount(), testEvent10.GetEventCount(), testEvent11.GetEventCount(),
         testEvent12.GetEventCount(), testEvent13.GetEventCount(), testEvent14.GetEventCount(), testEvent15.GetEventCount(),
         testEvent16.GetEventCount()]


teh0 = testEvent0.GetCopy()
teh1 = testEvent1.GetCopy()
teh2 = testEvent2.GetCopy()
teh3 = testEvent3.GetCopy()
teh4 = testEvent4.GetCopy()
teh5 = testEvent5.GetCopy()
teh6 = testEvent6.GetCopy()
teh7 = testEvent7.GetCopy()
teh8 = testEvent8.GetCopy()
teh9 = testEvent9.GetCopy()
teh10 = testEvent10.GetCopy()
teh11 = testEvent11.GetCopy()
teh12 = testEvent12.GetCopy()
teh13 = testEvent13.GetCopy()
teh14 = testEvent14.GetCopy()
teh15 = testEvent15.GetCopy()
teh16 = testEvent16.GetCopy()

ted0 = testEvent0.GetCopy()
ted1 = testEvent1.GetCopy()
ted2 = testEvent2.GetCopy()
ted3 = testEvent3.GetCopy()
ted4 = testEvent4.GetCopy()
ted5 = testEvent5.GetCopy()
ted6 = testEvent6.GetCopy()
ted7 = testEvent7.GetCopy()
ted8 = testEvent8.GetCopy()
ted9 = testEvent9.GetCopy()
ted10 = testEvent10.GetCopy()
ted11 = testEvent11.GetCopy()
ted12 = testEvent12.GetCopy()
ted13 = testEvent13.GetCopy()
ted14 = testEvent14.GetCopy()
ted15 = testEvent15.GetCopy()
ted16 = testEvent16.GetCopy()

CutEvents(testEvent0, mzaCut2[0])
CutEvents(testEvent1, mzaCut2[1])
CutEvents(testEvent2, mzaCut2[2])
CutEvents(testEvent3, mzaCut2[3])
CutEvents(testEvent4, mzaCut2[4])
CutEvents(testEvent5, mzaCut2[5])
CutEvents(testEvent6, mzaCut2[6])
CutEvents(testEvent7, mzaCut2[7])
CutEvents(testEvent8, mzaCut2[8])
CutEvents(testEvent9, mzaCut2[9])
CutEvents(testEvent10, mzaCut2[10])
CutEvents(testEvent11, mzaCut2[11])
CutEvents(testEvent12, mzaCut2[12])
CutEvents(testEvent13, mzaCut2[13])
CutEvents(testEvent14, mzaCut2[14])
CutEvents(testEvent15, mzaCut2[15])
CutEvents(testEvent16, mzaCut2[16])

CutEvents(teh0, mzaCut2h[0])
CutEvents(teh1, mzaCut2h[1])
CutEvents(teh2, mzaCut2h[2])
CutEvents(teh3, mzaCut2h[3])
CutEvents(teh4, mzaCut2h[4])
CutEvents(teh5, mzaCut2h[5])
CutEvents(teh6, mzaCut2h[6])
CutEvents(teh7, mzaCut2h[7])
CutEvents(teh8, mzaCut2h[8])
CutEvents(teh9, mzaCut2h[9])
CutEvents(teh10, mzaCut2h[10])
CutEvents(teh11, mzaCut2h[11])
CutEvents(teh12, mzaCut2h[12])
CutEvents(teh13, mzaCut2h[13])
CutEvents(teh14, mzaCut2h[14])
CutEvents(teh15, mzaCut2h[15])
CutEvents(teh16, mzaCut2h[16])

CutEvents(ted0, mzaCut2d[0])
CutEvents(ted1, mzaCut2d[1])
CutEvents(ted2, mzaCut2d[2])
CutEvents(ted3, mzaCut2d[3])
CutEvents(ted4, mzaCut2d[4])
CutEvents(ted5, mzaCut2d[5])
CutEvents(ted6, mzaCut2d[6])
CutEvents(ted7, mzaCut2d[7])
CutEvents(ted8, mzaCut2d[8])
CutEvents(ted9, mzaCut2d[9])
CutEvents(ted10, mzaCut2d[10])
CutEvents(ted11, mzaCut2d[11])
CutEvents(ted12, mzaCut2d[12])
CutEvents(ted13, mzaCut2d[13])
CutEvents(ted14, mzaCut2d[14])
CutEvents(ted15, mzaCut2d[15])
CutEvents(ted16, mzaCut2d[16])



print("============== after unitarity bound ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())
print(testEvent8.GetEventCount())
print(testEvent9.GetEventCount())
print(testEvent10.GetEventCount())
print(testEvent11.GetEventCount())
print(testEvent12.GetEventCount())
print(testEvent13.GetEventCount())
print(testEvent14.GetEventCount())
print(testEvent15.GetEventCount())
print(testEvent16.GetEventCount())

evnm2 = [testEvent0.GetEventCount(), testEvent1.GetEventCount(), testEvent2.GetEventCount(), testEvent3.GetEventCount(),
         testEvent4.GetEventCount(), testEvent5.GetEventCount(), testEvent6.GetEventCount(), testEvent7.GetEventCount(),
         testEvent8.GetEventCount(), testEvent9.GetEventCount(), testEvent10.GetEventCount(), testEvent11.GetEventCount(),
         testEvent12.GetEventCount(), testEvent13.GetEventCount(), testEvent14.GetEventCount(), testEvent15.GetEventCount(),
         testEvent16.GetEventCount()]

evnm3 = [teh0.GetEventCount(), teh1.GetEventCount(), teh2.GetEventCount(), teh3.GetEventCount(),
         teh4.GetEventCount(), teh5.GetEventCount(), teh6.GetEventCount(), teh7.GetEventCount(),
         teh8.GetEventCount(), teh9.GetEventCount(), teh10.GetEventCount(), teh11.GetEventCount(),
         teh12.GetEventCount(), teh13.GetEventCount(), teh14.GetEventCount(), teh15.GetEventCount(),
         teh16.GetEventCount()]

evnm4 = [ted0.GetEventCount(), ted1.GetEventCount(), ted2.GetEventCount(), ted3.GetEventCount(),
         ted4.GetEventCount(), ted5.GetEventCount(), ted6.GetEventCount(), ted7.GetEventCount(),
         ted8.GetEventCount(), ted9.GetEventCount(), ted10.GetEventCount(), ted11.GetEventCount(),
         ted12.GetEventCount(), ted13.GetEventCount(), ted14.GetEventCount(), ted15.GetEventCount(),
         ted16.GetEventCount()]

print("[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
      1000 * cs[0] * evnm1[0] / evnm0[0],
      1000 * cs[1] * evnm1[1] / evnm0[1],
      1000 * cs[2] * evnm1[2] / evnm0[2],
      1000 * cs[3] * evnm1[3] / evnm0[3],
      1000 * cs[4] * evnm1[4] / evnm0[4],
      1000 * cs[5] * evnm1[5] / evnm0[5],
      1000 * cs[6] * evnm1[6] / evnm0[6],
      1000 * cs[7] * evnm1[7] / evnm0[7],
      0.106 if usercut else 0.140,
      1000 * cs[9] * evnm1[9] / evnm0[9],
      1000 * cs[10] * evnm1[10] / evnm0[10],
      1000 * cs[11] * evnm1[11] / evnm0[11],
      1000 * cs[12] * evnm1[12] / evnm0[12],
      1000 * cs[13] * evnm1[13] / evnm0[13],
      1000 * cs[14] * evnm1[14] / evnm0[14],
      1000 * cs[15] * evnm1[15] / evnm0[15],
      1000 * cs[16] * evnm1[16] / evnm0[16]
))

print(1000 * cs[8] * evnm1[8] / evnm0[8])

print("[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
      1000 * cs[0] * evnm2[0] / evnm0[0],
      1000 * cs[1] * evnm2[1] / evnm0[1],
      1000 * cs[2] * evnm2[2] / evnm0[2],
      1000 * cs[3] * evnm2[3] / evnm0[3],
      1000 * cs[4] * evnm2[4] / evnm0[4],
      1000 * cs[5] * evnm2[5] / evnm0[5],
      1000 * cs[6] * evnm2[6] / evnm0[6],
      1000 * cs[7] * evnm2[7] / evnm0[7],
      0.106 if usercut else 0.140,
      1000 * cs[9] * evnm2[9] / evnm0[9],
      1000 * cs[10] * evnm2[10] / evnm0[10],
      1000 * cs[11] * evnm2[11] / evnm0[11],
      1000 * cs[12] * evnm2[12] / evnm0[12],
      1000 * cs[13] * evnm2[13] / evnm0[13],
      1000 * cs[14] * evnm2[14] / evnm0[14],
      1000 * cs[15] * evnm2[15] / evnm0[15],
      1000 * cs[16] * evnm2[16] / evnm0[16]
))


print("[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
      1000 * cs[0] * evnm3[0] / evnm0[0],
      1000 * cs[1] * evnm3[1] / evnm0[1],
      1000 * cs[2] * evnm3[2] / evnm0[2],
      1000 * cs[3] * evnm3[3] / evnm0[3],
      1000 * cs[4] * evnm3[4] / evnm0[4],
      1000 * cs[5] * evnm3[5] / evnm0[5],
      1000 * cs[6] * evnm3[6] / evnm0[6],
      1000 * cs[7] * evnm3[7] / evnm0[7],
      0.106 if usercut else 0.140,
      1000 * cs[9] * evnm3[9] / evnm0[9],
      1000 * cs[10] * evnm3[10] / evnm0[10],
      1000 * cs[11] * evnm3[11] / evnm0[11],
      1000 * cs[12] * evnm3[12] / evnm0[12],
      1000 * cs[13] * evnm3[13] / evnm0[13],
      1000 * cs[14] * evnm3[14] / evnm0[14],
      1000 * cs[15] * evnm3[15] / evnm0[15],
      1000 * cs[16] * evnm3[16] / evnm0[16]
))

print("[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
      1000 * cs[0] * evnm4[0] / evnm0[0],
      1000 * cs[1] * evnm4[1] / evnm0[1],
      1000 * cs[2] * evnm4[2] / evnm0[2],
      1000 * cs[3] * evnm4[3] / evnm0[3],
      1000 * cs[4] * evnm4[4] / evnm0[4],
      1000 * cs[5] * evnm4[5] / evnm0[5],
      1000 * cs[6] * evnm4[6] / evnm0[6],
      1000 * cs[7] * evnm4[7] / evnm0[7],
      0.106 if usercut else 0.140,
      1000 * cs[9] * evnm4[9] / evnm0[9],
      1000 * cs[10] * evnm4[10] / evnm0[10],
      1000 * cs[11] * evnm4[11] / evnm0[11],
      1000 * cs[12] * evnm4[12] / evnm0[12],
      1000 * cs[13] * evnm4[13] / evnm0[13],
      1000 * cs[14] * evnm4[14] / evnm0[14],
      1000 * cs[15] * evnm4[15] / evnm0[15],
      1000 * cs[16] * evnm4[16] / evnm0[16]
))

"""

================================ ft5 ===========================

fm4:sm is 0.1148027544

ceft5 = [-0.7e-12, -0.525e-12, -0.35e-12, -0.175e-12, 0.185e-12, 0.37e-12, 0.555e-12, 0.74e-12]

[0.280797075, 0.191539142, 0.15193068599999998, 0.08587254, 0.078, 0.09577618300000001, 0.095766323, 0.17503939000000002, 0.29715677999999995]
[0.16517475, 0.158515152, 0.13211363999999998, 0.08587254, 0.078, 0.09577618300000001, 0.07925488800000001, 0.14531572, 0.204708004]


=========================================================
"""