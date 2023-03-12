import os

from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../_DataFolder")

fileHeader = "ft7"
iYjjType = 1
bAdd = True
unicutIndex = 6

testEvent1 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-n-0.lhco")
testEvent2 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-n-5.lhco")
testEvent3 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-n-1.lhco")
testEvent4 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-n-6.lhco")
testEvent5 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-n-7.lhco")
testEvent6 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-n-3.lhco")
testEvent7 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-n-8.lhco")
testEvent8 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-n-4.lhco")

if bAdd:
    addEvent1 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-m-0.lhco")
    testEvent1.AddEventSet(addEvent1)
    addEvent2 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-m-1.lhco")
    testEvent2.AddEventSet(addEvent2)
    addEvent3 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-m-3.lhco")
    testEvent3.AddEventSet(addEvent3)
    addEvent4 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-m-4.lhco")
    testEvent4.AddEventSet(addEvent4)
    addEvent5 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-m-5.lhco")
    testEvent5.AddEventSet(addEvent5)
    addEvent6 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-m-6.lhco")
    testEvent6.AddEventSet(addEvent6)
    addEvent7 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-m-7.lhco")
    testEvent7.AddEventSet(addEvent7)
    addEvent8 = LoadLHCOlympics("wa/fittings2/" + fileHeader + "/" + fileHeader + "-m-8.lhco")
    testEvent8.AddEventSet(addEvent8)


print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())
print(testEvent8.GetEventCount())

jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)
lmCut = PhiLeptonMissingCut(1, False, 0.95)
leptonPTCut = LeptonPtCut(80.0)
ptMissingCut = PtMissing(1, 50.0)

mw = 80.379
mz = 91.1876
cw = 0.876801
sw = 0.480853
vev = 246
e2 = 0.0934761  # sqrt{ 4 pi alpha} for alpha = 1/134

uniFM2 = [math.sqrt(256 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * abs(fm2))) * 1.0e6 for fm2 in [-8.2, -6.15, -4.15, -2.05, 2.0, 3.95, 6.0, 8.0]]
uniFM3 = [math.sqrt(384 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * abs(fm3))) * 1.0e6 for fm3 in [-21, -15.75, -10.5, -5.25, 5.25, 10.5, 15.75, 21]]
uniFM4 = [math.sqrt(512 * math.pi * sw * sw * mw * mz / (e2 * vev * vev * abs(fm4))) * 1.0e6 for fm4 in [-15, -11.25, -7.5, -3.75, 4, 8, 12, 16]]
uniFM5 = [math.sqrt(384 * math.pi * sw * mw * mz / (cw * e2 * vev * vev * abs(fm5))) * 1.0e6 for fm5 in [-25, -18.75, -12.5, -6.25, 6, 12, 18, 24]]
uniFT5 = [math.sqrt(40 * math.pi / (cw * cw * abs(ft5))) * 1.0e6 for ft5 in [-0.7, -0.525, -0.35, -0.175, 0.185, 0.37, 0.555, 0.74]]
uniFT6 = [math.sqrt(32 * math.pi / (cw * cw * abs(ft6))) * 1.0e6 for ft6 in [-1.6, -1.2, -0.8, -0.4, 0.425, 0.85, 1.275, 1.7]]
uniFT7 = [math.sqrt(64 * math.pi / (cw * cw * abs(ft7))) * 1.0e6 for ft7 in [-2.6, -1.95, -1.3, -0.65, 0.7, 1.4, 2.1, 2.8]]
uniCut = [uniFM2, uniFM3, uniFM4, uniFM5, uniFT5, uniFT6, uniFT7]

yjjCutM = StandardVBFCut(True, 0.0, 1.5)

r1Cut = RadiusACut(1, 0.05, 1)

shatCut2 = SHatCut2(1, 4.0e5)

CutEvents(testEvent1, jetNumberCut)
CutEvents(testEvent1, leptonNumberCut)
CutEvents(testEvent1, photonNumberCut)
CutEvents(testEvent2, jetNumberCut)
CutEvents(testEvent2, leptonNumberCut)
CutEvents(testEvent2, photonNumberCut)
CutEvents(testEvent3, jetNumberCut)
CutEvents(testEvent3, leptonNumberCut)
CutEvents(testEvent3, photonNumberCut)
CutEvents(testEvent4, jetNumberCut)
CutEvents(testEvent4, leptonNumberCut)
CutEvents(testEvent4, photonNumberCut)
CutEvents(testEvent5, jetNumberCut)
CutEvents(testEvent5, leptonNumberCut)
CutEvents(testEvent5, photonNumberCut)
CutEvents(testEvent6, jetNumberCut)
CutEvents(testEvent6, leptonNumberCut)
CutEvents(testEvent6, photonNumberCut)
CutEvents(testEvent7, jetNumberCut)
CutEvents(testEvent7, leptonNumberCut)
CutEvents(testEvent7, photonNumberCut)
CutEvents(testEvent8, jetNumberCut)
CutEvents(testEvent8, leptonNumberCut)
CutEvents(testEvent8, photonNumberCut)

CutEvents(testEvent1, lmCut)
CutEvents(testEvent2, lmCut)
CutEvents(testEvent3, lmCut)
CutEvents(testEvent4, lmCut)
CutEvents(testEvent5, lmCut)
CutEvents(testEvent6, lmCut)
CutEvents(testEvent7, lmCut)
CutEvents(testEvent8, lmCut)

CutEvents(testEvent1, leptonPTCut)
CutEvents(testEvent2, leptonPTCut)
CutEvents(testEvent3, leptonPTCut)
CutEvents(testEvent4, leptonPTCut)
CutEvents(testEvent5, leptonPTCut)
CutEvents(testEvent6, leptonPTCut)
CutEvents(testEvent7, leptonPTCut)
CutEvents(testEvent8, leptonPTCut)

CutEvents(testEvent1, ptMissingCut)
CutEvents(testEvent2, ptMissingCut)
CutEvents(testEvent3, ptMissingCut)
CutEvents(testEvent4, ptMissingCut)
CutEvents(testEvent5, ptMissingCut)
CutEvents(testEvent6, ptMissingCut)
CutEvents(testEvent7, ptMissingCut)
CutEvents(testEvent8, ptMissingCut)

if 0 == iYjjType:
    CutEvents(testEvent1, yjjCutM)
    CutEvents(testEvent2, yjjCutM)
    CutEvents(testEvent3, yjjCutM)
    CutEvents(testEvent4, yjjCutM)
    CutEvents(testEvent5, yjjCutM)
    CutEvents(testEvent6, yjjCutM)
    CutEvents(testEvent7, yjjCutM)
    CutEvents(testEvent8, yjjCutM)
elif 1 == iYjjType:
    CutEvents(testEvent1, r1Cut)
    CutEvents(testEvent2, r1Cut)
    CutEvents(testEvent3, r1Cut)
    CutEvents(testEvent4, r1Cut)
    CutEvents(testEvent5, r1Cut)
    CutEvents(testEvent6, r1Cut)
    CutEvents(testEvent7, r1Cut)
    CutEvents(testEvent8, r1Cut)


CutEvents(testEvent1, shatCut2)
CutEvents(testEvent2, shatCut2)
CutEvents(testEvent3, shatCut2)
CutEvents(testEvent4, shatCut2)
CutEvents(testEvent5, shatCut2)
CutEvents(testEvent6, shatCut2)
CutEvents(testEvent7, shatCut2)
CutEvents(testEvent8, shatCut2)

print("=====================")

print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())
print(testEvent8.GetEventCount())

shatCuts = [SHatCut2(0, fm) for fm in uniCut[unicutIndex]]
CutEvents(testEvent1, shatCuts[0])
CutEvents(testEvent2, shatCuts[1])
CutEvents(testEvent3, shatCuts[2])
CutEvents(testEvent4, shatCuts[3])
CutEvents(testEvent5, shatCuts[4])
CutEvents(testEvent6, shatCuts[5])
CutEvents(testEvent7, shatCuts[6])
CutEvents(testEvent8, shatCuts[7])

print("=====================")

print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())
print(testEvent8.GetEventCount())

"""
results:

M2: (-6.15, -2.05, 2, 6)
run_36               -8.200000e-12        9.525456e+00         
run_37               -4.150000e-12        9.527458e+00          
run_39               3.950000e-12         9.521693e+00         
run_40               8.000000e-12         9.523754e+00      
run_17               -6.150000e-12        9.526165e+00         
run_18               -2.050000e-12        9.522944e+00         
run_19               2.000000e-12         9.524413e+00         
run_20               6.000000e-12         9.519525e+00      
=====================
165
113
74
67
62
69
111
164
=====================
83
81
69
66
61
66
82
84

Process finished with exit code 0



M3: (15.75, 5.25)
run_05               -2.100000e-11        9.536763e+00         
run_06               -1.050000e-11        9.529054e+00         
run_07               1.050000e-11         9.526845e+00         
run_08               2.100000e-11         9.539585e+00      
run_02               -1.575000e-11        9.531539e+00         
run_03               -5.250000e-12        9.521418e+00         
run_04               5.250000e-12         9.520109e+00         
run_05               1.575000e-11         9.533204e+00         
=====================
508
289
143
59
74
161
284
492
=====================
132
109
101
57
65
89
121
140

Process finished with exit code 0



M4++: (-11.25, -3.75, 4, 12)
run_01               -1.500000e-11        9.523230e+00         
run_02               -7.500000e-12        9.523658e+00         
run_03               8.000000e-12         9.521536e+00         
run_04               1.600000e-11         9.525901e+00        
=====================
180
57
61
79
=====================
105
49
53
43

T5++: (-5.25 -1.75 1.85, 5.55)
run_01               -7.000000e-13        9.518368e+00         
run_02               -3.500000e-13        9.524209e+00         
run_03               3.700000e-13         9.519024e+00         
run_04               7.400000e-13         9.519816e+00  
=====================
92
65
80
94
=====================
90
64
80
88

T6:
run_09               -1.600000e-12        9.530656e+00         
run_10               -8.000000e-13        9.526409e+00         
run_11               -8.500000e-13        9.529597e+00         
run_12               1.700000e-12         9.532588e+00  
=====================
222
110
100
247
=====================
141
100
84
145


T7++: (-1.95, 0.65, 0.7, 2.1)
run_13               -2.600000e-12        9.525817e+00         
run_14               -1.300000e-12        9.524225e+00         
run_15               1.400000e-12         9.523410e+00         
run_16               2.800000e-12         9.521811e+00  
=====================
106
80
91
95
=====================
85
79
86
77

"""