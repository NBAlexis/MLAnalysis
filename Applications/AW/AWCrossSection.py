import os

from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("F:/PyworkingFolder/CutExperiment/_DataFolder")

cutType = 2
jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)
vbfCut = StandardVBFCut(True, 300.0, 3.0)
# ptMissingCutM = PtMissing(1, 0.1)
megammaCut = MeGammaCut(1, False, 600)
# thetaGammaLeptonCut = ThetaGammaLeptonCut(0, False, 0.99)
# phiGammaMissingCut = PhiGammaMissingCut(0, 0.99)
lmCut = PhiLeptonMissingCut(1, False, 0.98)
# ptMissingCutT = PtMissing(1, 75)
r2Cut = RadiusACut(1, 0.15, 3)
r1Cut = RadiusACut(1, 0.15, 2)
r0Cut = RadiusACut(1, 1.0, 1)

# fileHeader = "wa/fittings/fm0/fm0-"
fileHeader = "wa/fittings2/ft5/ft5-n-"

event0 = LoadLHCOlympics("{}0.lhco".format(fileHeader))
event1 = LoadLHCOlympics("{}1.lhco".format(fileHeader))
event2 = LoadLHCOlympics("{}3.lhco".format(fileHeader))
event3 = LoadLHCOlympics("{}4.lhco".format(fileHeader))

lstCSfm2 = [9.525456, 9.527458, 9.521693, 9.523754]
# lstCSfm3 = [9.528, 9.512, 9.490, 9.480, 9.458, 9.467, 9.459, 9.467, 9.480, 9.508, 9.537]
# lstCSfm4 = [9.494640, 9.487761, 9.484158, 9.471298, 9.450375, 9.467428, 9.457633, 9.461426, 9.469377, 9.490119, 9.501709]
# lstCSfm5 = [9.598661, 9.528272, 9.514946, 9.495662, 9.452598, 9.467065, 9.462070, 9.481284, 9.497909, 9.553497, 9.597163]
lstCSft5 = [9.518368, 9.524209, 9.519024, 9.519816]
# lstCSft6 = [9.482633, 9.488846, 9.475363, 9.464999, 9.467833, 9.458731, 9.467364, 9.475578, 9.466784, 9.486712, 9.492641]
# lstCSft7 = [9.477430, 9.483161, 9.476230, 9.453199, 9.467709, 9.472897, 9.448550, 9.475297, 9.465846, 9.481408, 9.487982]

lstCoeff_fm2 = [-8.2, -4.15, 3.95, 8.0]
# lstCoeff_fm3 = [-43 + 8.7 * i for i in range(0, 11)]
# lstCoeff_fm4 = [-40 + 8 * i for i in range(0, 11)]
# lstCoeff_fm5 = []
lstCoeff_ft5 = [-0.7, -0.35, 0.37, 0.74]
# lstCoeff_ft6 = [-2.8 + 0.58 * i for i in range(0, 11)]
# lstCoeff_ft7 = [-7.3 + 1.5 * i for i in range(0, 11)]

lstEventN = [event0.GetEventCount(),
             event1.GetEventCount(),
             event2.GetEventCount(),
             event3.GetEventCount()]

print(lstEventN)

eventLst = [event0, event1, event2, event3]

if 1 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        # CutEvents(eventSet, vbfCut)
        CutEvents(eventSet, r0Cut)
        CutEvents(eventSet, megammaCut)
        CutEvents(eventSet, lmCut)
elif 2 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        CutEvents(eventSet, r1Cut)
        CutEvents(eventSet, megammaCut)
        CutEvents(eventSet, lmCut)
elif 3 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        CutEvents(eventSet, r2Cut)

lstEventN2 = [event0.GetEventCount(),
              event1.GetEventCount(),
              event2.GetEventCount(),
              event3.GetEventCount()]

print("===========================================")

for i in range(0, 4):
    print(lstEventN2[i] * lstCSft5[i] / lstEventN[i])

print("===========================================")

mw = 80.379
mz = 91.1876
cw = 0.876801
sw = 0.480853
vev = 246
e2 = 0.0934761  # sqrt{ 4 pi alpha} for alpha = 1/134

# apply the s hat cut
epsz = 0.0
cutListm2 = [math.sqrt(256.0 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * abs(fm + epsz))) * 1.0e6
             for fm in lstCoeff_fm2]
# cutListm3 = [math.sqrt(384.0 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * math.fabs(fm + epsz))) * 1.0e6
#             for fm in lstCoeff_fm3]
# cutListm4 = [math.sqrt(512.0 * math.pi * mw * mz * sw * sw / (e2 * vev * vev * math.fabs(fm + epsz))) * 1.0e6 for fm in
#              lstCoeff_fm4]
# cutListm5 = [math.sqrt(384.0 * math.pi * mw * mz * sw / (cw * e2 * vev * vev * math.fabs(fm + epsz))) * 1.0e6 for fm in
#              lstCoeff_fm5]
cutListt5 = [math.sqrt(40.0 * math.pi / (cw * cw * abs(fm + epsz))) * 1.0e6 for fm in lstCoeff_ft5]
# cutListt6 = [math.sqrt(32.0 * math.pi / (cw * cw * math.fabs(fm + epsz))) * 1.0e6 for fm in lstCoeff_ft6]
# cutListt7 = [math.sqrt(64.0 * math.pi / (cw * cw * math.fabs(fm + epsz))) * 1.0e6 for fm in lstCoeff_ft7]

print("============= s cut =================")
print(cutListt5)
print("=====================================")

shatCutList = [SHatCut2(cutV) for cutV in cutListt5]
for i in range(0, 4):
    CutEvents(eventLst[i], shatCutList[i])

lstEventN3 = [event0.GetEventCount(),
              event1.GetEventCount(),
              event2.GetEventCount(),
              event3.GetEventCount()]
for i in range(0, 4):
    print(lstEventN3[i] * lstCSft5[i] / lstEventN[i])

print("===========================================")
