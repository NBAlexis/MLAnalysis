import os

from CutAndExport.CorrelationFunctions import CorrelationData, LpTest, CorrelationDataAndSave
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../")

testEventsm = LoadLHCOlympics("_DataFolder/wa/features/bgsm.lhco")
testEventsm2 = LoadLHCOlympics("_DataFolder/wa/features/bgsm2.lhco")
testEventsm3 = LoadLHCOlympics("_DataFolder/wa/features/bgsm3.lhco")
testEventsm.AddEventSet(testEventsm2)
testEventsm.AddEventSet(testEventsm3)
testEventm2 = LoadLHCOlympics("_DataFolder/wa/features2/fm2.lhco")
# testEventm3 = LoadLHCOlympics("_DataFolder/wa/features2/fm3.lhco")
# testEventm4 = LoadLHCOlympics("_DataFolder/wa/features2/fm4.lhco")
# testEventm5 = LoadLHCOlympics("_DataFolder/wa/features2/fm5.lhco")
testEventt5 = LoadLHCOlympics("_DataFolder/wa/features2/ft5.lhco")
# testEventt6 = LoadLHCOlympics("_DataFolder/wa/features2/ft6.lhco")
# testEventt7 = LoadLHCOlympics("_DataFolder/wa/features2/ft7.lhco")


# testEventm2r = LoadLesHouchesEvent("F:/PyworkingFolder/CutExperiment/_DataFolder/wa/features2/fm2.lhe")
# testEventm2 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wa/features2/ft5.lhco")
# testEventm2r = LoadLesHouchesEvent("F:/PyworkingFolder/CutExperiment/_DataFolder/wa/features2/ft5.lhe")

"""
# total cut flow
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
cfm2 = 8.0
cfm3 = 21
cfm4 = 16
cfm5 = 24
cft5 = 0.74
cft6 = 1.7
cft7 = 2.8
uniFM2 = math.sqrt(256 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * cfm2)) * 1.0e6
uniFM3 = math.sqrt(384 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * cfm3)) * 1.0e6
uniFM4 = math.sqrt(512 * math.pi * sw * sw * mw * mz / (e2 * vev * vev * cfm4)) * 1.0e6
uniFM5 = math.sqrt(384 * math.pi * sw * mw * mz / (cw * e2 * vev * vev * cfm5)) * 1.0e6
uniFT5 = math.sqrt(40 * math.pi / (cw * cw * cft5)) * 1.0e6
uniFT6 = math.sqrt(32 * math.pi / (cw * cw * cft6)) * 1.0e6
uniFT7 = math.sqrt(64 * math.pi / (cw * cw * cft7)) * 1.0e6

shatCutFM2 = SHatCut2(0, uniFM2)
shatCutFM3 = SHatCut2(0, uniFM3)
shatCutFM4 = SHatCut2(0, uniFM4)
shatCutFM5 = SHatCut2(0, uniFM5)
shatCutFT5 = SHatCut2(0, uniFT5)
shatCutFT6 = SHatCut2(0, uniFT6)
shatCutFT7 = SHatCut2(0, uniFT7)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)

CutEvents(testEventm2, jetNumberCut)
CutEvents(testEventm2, leptonNumberCut)
CutEvents(testEventm2, photonNumberCut)
CutEvents(testEventm3, jetNumberCut)
CutEvents(testEventm3, leptonNumberCut)
CutEvents(testEventm3, photonNumberCut)
CutEvents(testEventm4, jetNumberCut)
CutEvents(testEventm4, leptonNumberCut)
CutEvents(testEventm4, photonNumberCut)
CutEvents(testEventm5, jetNumberCut)
CutEvents(testEventm5, leptonNumberCut)
CutEvents(testEventm5, photonNumberCut)
CutEvents(testEventt5, jetNumberCut)
CutEvents(testEventt5, leptonNumberCut)
CutEvents(testEventt5, photonNumberCut)
CutEvents(testEventt6, jetNumberCut)
CutEvents(testEventt6, leptonNumberCut)
CutEvents(testEventt6, photonNumberCut)
CutEvents(testEventt7, jetNumberCut)
CutEvents(testEventt7, leptonNumberCut)
CutEvents(testEventt7, photonNumberCut)

CutEvents(testEventsm, lmCut)
CutEvents(testEventm2, lmCut)
CutEvents(testEventm3, lmCut)
CutEvents(testEventm4, lmCut)
CutEvents(testEventm5, lmCut)
CutEvents(testEventt5, lmCut)
CutEvents(testEventt6, lmCut)
CutEvents(testEventt7, lmCut)

CutEvents(testEventsm, leptonPTCut)
CutEvents(testEventm2, leptonPTCut)
CutEvents(testEventm3, leptonPTCut)
CutEvents(testEventm4, leptonPTCut)
CutEvents(testEventm5, leptonPTCut)
CutEvents(testEventt5, leptonPTCut)
CutEvents(testEventt6, leptonPTCut)
CutEvents(testEventt7, leptonPTCut)

CutEvents(testEventsm, ptMissingCut)
CutEvents(testEventm2, ptMissingCut)
CutEvents(testEventm3, ptMissingCut)
CutEvents(testEventm4, ptMissingCut)
CutEvents(testEventm5, ptMissingCut)
CutEvents(testEventt5, ptMissingCut)
CutEvents(testEventt6, ptMissingCut)
CutEvents(testEventt7, ptMissingCut)

CutEvents(testEventm2, shatCutFM2)
CutEvents(testEventm3, shatCutFM3)
CutEvents(testEventm4, shatCutFM4)
CutEvents(testEventm5, shatCutFM5)
CutEvents(testEventt5, shatCutFT5)
CutEvents(testEventt6, shatCutFT6)
CutEvents(testEventt7, shatCutFT7)

print("================s hat U===================")

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

yjjCutM = StandardVBFCut(True, 0.0, 1.5)
yjjCutT = StandardVBFCut(True, 0.0, 0.8)

rCut = RadiusACut(1, 0.05, 1)
# CutEvents(testEventsm, r1Cut)
# CutEvents(testEventt5, r1Cut)
# CutEvents(testEventt6, r2Cut)
# CutEvents(testEventt7, r2Cut)

shatCut2 = SHatCut2(1, 4.0e5)

CutEvents(testEventsm, shatCut2)
CutEvents(testEventm2, shatCut2)
CutEvents(testEventm3, shatCut2)
CutEvents(testEventm4, shatCut2)
CutEvents(testEventm5, shatCut2)
CutEvents(testEventt5, shatCut2)
CutEvents(testEventt6, shatCut2)
CutEvents(testEventt7, shatCut2)

print("=================s hat c==================")

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

meac = MeGammaCut(1, False, 300)
dupliSmr = EventSet()
meaSmr2 = EventSet()
dupliSmr.AddEventSet(testEventsm)
meaSmr2.AddEventSet(testEventsm)
CutEvents(testEventsm, yjjCutM)
CutEvents(dupliSmr, rCut)
CutEvents(meaSmr2, meac)
CutEvents(testEventm2, yjjCutM)
CutEvents(testEventm3, yjjCutM)
CutEvents(testEventm4, yjjCutM)
CutEvents(testEventm5, yjjCutM)
CutEvents(testEventt5, rCut)
CutEvents(testEventt6, rCut)
CutEvents(testEventt7, rCut)

print("=============== yjj, r1 r2 ====================")


print(testEventsm.GetEventCount())
print(dupliSmr.GetEventCount())
print(meaSmr2.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

"""

# """
# Cut experiment
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
cfm2 = 8.0
cfm3 = 21
cfm4 = 16
cfm5 = 24
cft5 = 0.74
cft6 = 1.7
cft7 = 2.8
uniFM2 = math.sqrt(256 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * cfm2)) * 1.0e6
uniFT5 = math.sqrt(40 * math.pi / (cw * cw * cft5)) * 1.0e6
uniFT6 = math.sqrt(32 * math.pi / (cw * cw * cft6)) * 1.0e6
uniFT7 = math.sqrt(64 * math.pi / (cw * cw * cft7)) * 1.0e6
shatCutFM2 = SHatCut2(0, uniFM2)
shatCutFT5 = SHatCut2(0, uniFT5)
shatCutFT6 = SHatCut2(0, uniFT6)
shatCutFT7 = SHatCut2(0, uniFT7)

shatCut2 = SHatCut2(1, 4.0e5)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)
CutEvents(testEventm2, jetNumberCut)
CutEvents(testEventm2, leptonNumberCut)
CutEvents(testEventm2, photonNumberCut)
CutEvents(testEventt5, jetNumberCut)
CutEvents(testEventt5, leptonNumberCut)
CutEvents(testEventt5, photonNumberCut)
# CutEvents(testEventt7, jetNumberCut)
# CutEvents(testEventt7, leptonNumberCut)
# CutEvents(testEventt7, photonNumberCut)

CutEvents(testEventsm, lmCut)
CutEvents(testEventm2, lmCut)
CutEvents(testEventt5, lmCut)
# CutEvents(testEventt7, lmCut)

CutEvents(testEventsm, leptonPTCut)
CutEvents(testEventm2, leptonPTCut)
CutEvents(testEventt5, leptonPTCut)
# CutEvents(testEventt7, leptonPTCut)

CutEvents(testEventsm, ptMissingCut)
CutEvents(testEventm2, ptMissingCut)
CutEvents(testEventt5, ptMissingCut)
# CutEvents(testEventt7, ptMissingCut)

CutEvents(testEventm2, shatCutFM2)
CutEvents(testEventt5, shatCutFT5)
# CutEvents(testEventt7, shatCutFT7)

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())
# print(testEventt7.GetEventCount())

# testYjjSM = HistogramWithMinMax(testEventsm, Mjj2Filter, [0, 2000], 50)
# testYjjM2 = HistogramWithMinMax(testEventm2, Mjj2Filter, [0, 2000], 50)
# testYjjT5 = HistogramWithMinMax(testEventt5, Mjj2Filter, [0, 2000], 50)

CutEvents(testEventsm, shatCut2)
CutEvents(testEventm2, shatCut2)
CutEvents(testEventt5, shatCut2)
# CutEvents(testEventt7, shatCut2)

testYjjSM = HistogramWithMinMax(testEventsm, Mjj2Filter, [0, 2000], 50)
testYjjM2 = HistogramWithMinMax(testEventm2, Mjj2Filter, [0, 2000], 50)
testYjjT5 = HistogramWithMinMax(testEventt5, Mjj2Filter, [0, 2000], 50)

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())
# print(testEventt7.GetEventCount())

# testYjjSM = HistogramWithMinMax(testEventsm, RadiusA, [0, 1.25], 50)
# testYjjM2 = HistogramWithMinMax(testEventm2, LpFilter, [0, 1], 50)
# testYjjT5 = HistogramWithMinMax(testEventt5, RadiusA, [0, 1.25], 50)
# testYjjT7 = HistogramWithMinMax(testEventt7, RadiusA, [0, 1.25], 50)

# testYjjSM = HistogramWithMinMax(testEventsm, RadiusA, [0, 1], 50)
# testYjjM2 = HistogramWithMinMax(testEventm2, LpFilter, [0, 1], 50)
print(testYjjSM.listCount)
print(testYjjM2.listCount)
# testYjjSM = HistogramWithMinMax(testEventsm, RadiusC, [0, 2], 50)
# testYjjSM2 = HistogramWithMinMax(testEventm2, RadiusC, [0, 2], 50)
# testYjjT5 = HistogramWithMinMax(testEventt5, RadiusB, [0, 2], 50)
# testYjjT7 = HistogramWithMinMax(testEventt7, RadiusC, [0, 2], 50)
# print(testYjjSM.listCount)
# print(testYjjM2.listCount)
print(testYjjT5.listCount)
# print(testYjjSM2.listCount)
# print(testYjjT5.listCount)
# print(testYjjT7.listCount)

# """

"""
# Correlation with shat
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
cfm2 = 8.0
cfm3 = 21
cfm4 = 16
cfm5 = 24
cft5 = 0.74
cft6 = 1.7
cft7 = 2.8
uniFM2 = math.sqrt(256 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * cfm2)) * 1.0e6
uniFT5 = math.sqrt(40 * math.pi / (cw * cw * cft5)) * 1.0e6
uniFT6 = math.sqrt(32 * math.pi / (cw * cw * cft6)) * 1.0e6
uniFT7 = math.sqrt(64 * math.pi / (cw * cw * cft7)) * 1.0e6
shatCutFM2 = SHatCut2(0, uniFM2)
shatCutFT5 = SHatCut2(0, uniFT5)
shatCutFT6 = SHatCut2(0, uniFT6)
shatCutFT7 = SHatCut2(0, uniFT7)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)
CutEvents(testEventt5, jetNumberCut)
CutEvents(testEventt5, leptonNumberCut)
CutEvents(testEventt5, photonNumberCut)

CutEvents(testEventsm, lmCut)
CutEvents(testEventt5, lmCut)


CutEvents(testEventsm, leptonPTCut)
CutEvents(testEventt5, leptonPTCut)

CutEvents(testEventsm, ptMissingCut)
CutEvents(testEventt5, ptMissingCut)

CutEvents(testEventt5, shatCutFT5)

print(testEventsm.GetEventCount())
print(testEventt5.GetEventCount())

CorrelationDataAndSave(testEventsm, SHatAW, Megamma, 40, 40, [0, 1e5], [0, 300], 'smmea.csv')
CorrelationDataAndSave(testEventt5, SHatAW, Megamma, 40, 40, [0, 1e7], [0, 3000], 't5mea.csv')
CorrelationDataAndSave(testEventsm, SHatAW, RadiusA, 40, 40, [0, 1e5], [0, 2], 'smr2.csv')
CorrelationDataAndSave(testEventt5, SHatAW, RadiusA, 40, 40, [0, 1e7], [0, 2], 't5r2.csv')

"""

"""
# Correlation Lp
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
cfm2 = 8.0
cfm3 = 21
cfm4 = 16
cfm5 = 24
cft5 = 0.74
cft6 = 1.7
cft7 = 2.8
uniFM2 = math.sqrt(256 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * cfm2)) * 1.0e6
uniFT5 = math.sqrt(40 * math.pi / (cw * cw * cft5)) * 1.0e6
uniFT6 = math.sqrt(32 * math.pi / (cw * cw * cft6)) * 1.0e6
uniFT7 = math.sqrt(64 * math.pi / (cw * cw * cft7)) * 1.0e6
shatCutFM2 = SHatCut2(0, uniFM2)
shatCutFT5 = SHatCut2(0, uniFT5)
shatCutFT6 = SHatCut2(0, uniFT6)
shatCutFT7 = SHatCut2(0, uniFT7)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)
CutEvents(testEventm2, jetNumberCut)
CutEvents(testEventm2, leptonNumberCut)
CutEvents(testEventm2, photonNumberCut)
CutEvents(testEventt5, jetNumberCut)
CutEvents(testEventt5, leptonNumberCut)
CutEvents(testEventt5, photonNumberCut)
CutEvents(testEventt7, jetNumberCut)
CutEvents(testEventt7, leptonNumberCut)
CutEvents(testEventt7, photonNumberCut)

CutEvents(testEventsm, lmCut)
CutEvents(testEventm2, lmCut)
CutEvents(testEventt5, lmCut)
CutEvents(testEventt7, lmCut)

CutEvents(testEventsm, leptonPTCut)
CutEvents(testEventm2, leptonPTCut)
CutEvents(testEventt5, leptonPTCut)
CutEvents(testEventt7, leptonPTCut)

CutEvents(testEventsm, ptMissingCut)
CutEvents(testEventm2, ptMissingCut)
CutEvents(testEventt5, ptMissingCut)
CutEvents(testEventt7, ptMissingCut)

CutEvents(testEventm2, shatCutFM2)
CutEvents(testEventt5, shatCutFT5)
CutEvents(testEventt7, shatCutFT7)

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt7.GetEventCount())

LpTest(testEventsm, "smlp.csv")
LpTest(testEventm2, "m2lp.csv")
LpTest(testEventt5, "t5lp.csv")
LpTest(testEventt7, "t7lp.csv")

"""

"""
# This is s-cut flow
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
cfm2 = 8.0
cfm3 = 21
cfm4 = 16
cfm5 = 24
cft5 = 0.74
cft6 = 1.7
cft7 = 2.8
uniFM2 = math.sqrt(256 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * cfm2)) * 1.0e6
uniFM3 = math.sqrt(384 * math.pi * sw * sw * mw * mw / (cw * cw * e2 * vev * vev * cfm3)) * 1.0e6
uniFM4 = math.sqrt(512 * math.pi * sw * sw * mw * mz / (e2 * vev * vev * cfm4)) * 1.0e6
uniFM5 = math.sqrt(384 * math.pi * sw * mw * mz / (cw * e2 * vev * vev * cfm5)) * 1.0e6
uniFT5 = math.sqrt(40 * math.pi / (cw * cw * cft5)) * 1.0e6
uniFT6 = math.sqrt(32 * math.pi / (cw * cw * cft6)) * 1.0e6
uniFT7 = math.sqrt(64 * math.pi / (cw * cw * cft7)) * 1.0e6

shatCutFM2 = SHatCut2(uniFM2)
shatCutFM3 = SHatCut2(uniFM3)
shatCutFM4 = SHatCut2(uniFM4)
shatCutFM5 = SHatCut2(uniFM5)
shatCutFT5 = SHatCut2(uniFT5)
shatCutFT6 = SHatCut2(uniFT6)
shatCutFT7 = SHatCut2(uniFT7)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)

CutEvents(testEventm2, jetNumberCut)
CutEvents(testEventm2, leptonNumberCut)
CutEvents(testEventm2, photonNumberCut)
CutEvents(testEventm3, jetNumberCut)
CutEvents(testEventm3, leptonNumberCut)
CutEvents(testEventm3, photonNumberCut)
CutEvents(testEventm4, jetNumberCut)
CutEvents(testEventm4, leptonNumberCut)
CutEvents(testEventm4, photonNumberCut)
CutEvents(testEventm5, jetNumberCut)
CutEvents(testEventm5, leptonNumberCut)
CutEvents(testEventm5, photonNumberCut)
CutEvents(testEventt5, jetNumberCut)
CutEvents(testEventt5, leptonNumberCut)
CutEvents(testEventt5, photonNumberCut)
CutEvents(testEventt6, jetNumberCut)
CutEvents(testEventt6, leptonNumberCut)
CutEvents(testEventt6, photonNumberCut)
CutEvents(testEventt7, jetNumberCut)
CutEvents(testEventt7, leptonNumberCut)
CutEvents(testEventt7, photonNumberCut)

print("===================================")

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

CutEvents(testEventsm, lmCut)
CutEvents(testEventm2, lmCut)
CutEvents(testEventm3, lmCut)
CutEvents(testEventm4, lmCut)
CutEvents(testEventm5, lmCut)
CutEvents(testEventt5, lmCut)
CutEvents(testEventt6, lmCut)
CutEvents(testEventt7, lmCut)

print("===================================")

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

CutEvents(testEventsm, leptonPTCut)
CutEvents(testEventm2, leptonPTCut)
CutEvents(testEventm3, leptonPTCut)
CutEvents(testEventm4, leptonPTCut)
CutEvents(testEventm5, leptonPTCut)
CutEvents(testEventt5, leptonPTCut)
CutEvents(testEventt6, leptonPTCut)
CutEvents(testEventt7, leptonPTCut)

print("===================================")

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

CutEvents(testEventsm, ptMissingCut)
CutEvents(testEventm2, ptMissingCut)
CutEvents(testEventm3, ptMissingCut)
CutEvents(testEventm4, ptMissingCut)
CutEvents(testEventm5, ptMissingCut)
CutEvents(testEventt5, ptMissingCut)
CutEvents(testEventt6, ptMissingCut)
CutEvents(testEventt7, ptMissingCut)

print("===================================")

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

CutEvents(testEventm2, shatCutFM2)
CutEvents(testEventm3, shatCutFM3)
CutEvents(testEventm4, shatCutFM4)
CutEvents(testEventm5, shatCutFM5)
CutEvents(testEventt5, shatCutFT5)
CutEvents(testEventt6, shatCutFT6)
CutEvents(testEventt7, shatCutFT7)

print("===================================")

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())

"""

"""
# This is to show the phi_ell,m p_T missing and p_{ell}^T cut

jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)
CutEvents(testEventm2, jetNumberCut)
CutEvents(testEventm2, leptonNumberCut)
CutEvents(testEventm2, photonNumberCut)
CutEvents(testEventt5, jetNumberCut)
CutEvents(testEventt5, leptonNumberCut)
CutEvents(testEventt5, photonNumberCut)

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())

testYjjSM = HistogramWithMinMax(testEventsm, Mjj2Filter, [0, 2000], 50)
testYjjM2 = HistogramWithMinMax(testEventm2, Mjj2Filter, [0, 2000], 50)
testYjjT5 = HistogramWithMinMax(testEventt5, Mjj2Filter, [0, 2000], 50)
print(testYjjSM.listCount)
print(testYjjM2.listCount)
print(testYjjT5.listCount)
"""

"""
# This is to show the correlation of s hat and s tilde
particleCount0 = 0
particleCount = 0
lstDelta = []
lstS1 = []
lstRealS = []
particleCount1 = 0
particleCount2 = 0

result_f = open("t5shat.csv", 'a')
for i in range(len(testEventm2.events)):
    # requirements
    bValid = (1 == testEventm2.events[i].GetLeptonCount())
    bValid = bValid and testEventm2.events[i].GetJetCount() > 1
    bValid = bValid and testEventm2.events[i].GetPhotonCount() > 0
    bValid = bValid and LeptonPtFilter(testEventm2.events[i]) >= 80.0
    bValid = bValid and PtSlashFilter(testEventm2.events[i]) >= 50.0
    if bValid:
        particleCount = particleCount + 1
        calcS = SHatAW(testEventm2.events[i])
        realS = SHatAWReal(testEventm2r.events[i])
        if abs(calcS - realS) < 1.0e7:
            particleCount2 = particleCount2 + 1
            lstDelta.append(calcS - realS)
        if 3.0e7 > calcS > 0 and 3.0e7 > realS > 0:
            particleCount1 = particleCount1 + 1
            lstS1.append(calcS)
            lstRealS.append(realS)
            result_f.write("{}, {}\n".format(realS, calcS))

result_f.close()
print(particleCount0)
print(particleCount)
print(particleCount1)
print(particleCount2)
histArray = [0 for i in range(50)]
sep2 = 2.0e7 / 50

for i in range(particleCount2):
    v3 = lstDelta[i]
    idxZ = math.floor((v3 + 1.0e7) / sep2)
    if idxZ >= 40:
        idxZ = 39
    if idxZ < 0:
        idxZ = 0
    histArray[idxZ] = histArray[idxZ] + 1

print(histArray)
import matplotlib.pyplot as plt
plt.hist2d(lstS1, lstRealS, [50, 50])
plt.show()
"""