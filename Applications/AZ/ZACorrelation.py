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

os.chdir("../../_DataFolder/")

"""
testEventsm = LoadLHCOlympics("za/newbackgrounds/azsm1.lhco")
testEventsm2 = LoadLHCOlympics("za/newbackgrounds/azsm2.lhco")
testEventsm3 = LoadLHCOlympics("za/newbackgrounds/azsm3.lhco")
testEventsm4 = LoadLHCOlympics("za/newbackgrounds/azsm4.lhco")
testEventsm.AddEventSet(testEventsm2)
testEventsm.AddEventSet(testEventsm3)
testEventsm.AddEventSet(testEventsm4)
testEventj3 = LoadLHCOlympics("za/newbackgrounds/jjjll1.lhco")
testEventj32 = LoadLHCOlympics("za/newbackgrounds/jjjll2.lhco")
testEventj33 = LoadLHCOlympics("za/newbackgrounds/jjjll3.lhco")
testEventj35 = LoadLHCOlympics("za/newbackgrounds/jjjll5.lhco")
testEventj3.AddEventSet(testEventj32)
testEventj3.AddEventSet(testEventj33)
testEventj3.AddEventSet(testEventj35)
# testEventm2 = LoadLHCOlympics("za/features/azsignalm2.lhco")
testEventm3 = LoadLHCOlympics("za/features/azsignalm3.lhco")
testEventm3.AddEventSet(LoadLHCOlympics("za/features/signal-n-fm3.lhco"))
# testEventm4 = LoadLHCOlympics("za/features/azsignalm4.lhco")
# testEventm5 = LoadLHCOlympics("za/features/azsignalm5.lhco")
testEventt5 = LoadLHCOlympics("za/features/azsignalt5.lhco")
testEventt5.AddEventSet(LoadLHCOlympics("za/features/signal-n-ft5.lhco"))
# testEventt6 = LoadLHCOlympics("za/features/azsignalt6.lhco")
# testEventt7 = LoadLHCOlympics("za/features/azsignalt7.lhco")
# testEventt8 = LoadLHCOlympics("za/features/azsignalt8.lhco")
# testEventt9 = LoadLHCOlympics("za/features/azsignalt9.lhco")

particleNumberCut = ParticleNumberZA()
# invllCut = EllInvMass(25, 91.1876)
# ellDotCut = DotEllCut(0.7)
# mzaCut = SHatZACut(300, -1)
deltaRCut = DeltaRCut(0.2)

CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventj3, particleNumberCut)
# CutEvents(testEventm2, particleNumberCut)
CutEvents(testEventm3, particleNumberCut)
# CutEvents(testEventm4, particleNumberCut)
# CutEvents(testEventm5, particleNumberCut)
CutEvents(testEventt5, particleNumberCut)
# CutEvents(testEventt6, particleNumberCut)
# CutEvents(testEventt7, particleNumberCut)
# CutEvents(testEventt8, particleNumberCut)
# CutEvents(testEventt9, particleNumberCut)

# CutEvents(testEventm2, deltaRCut)
CutEvents(testEventm3, deltaRCut)
# CutEvents(testEventm4, deltaRCut)
# CutEvents(testEventm5, deltaRCut)
CutEvents(testEventt5, deltaRCut)
# CutEvents(testEventt6, deltaRCut)
# CutEvents(testEventt7, deltaRCut)
# CutEvents(testEventt8, deltaRCut)
# CutEvents(testEventt9, deltaRCut)
"""

"""
CutEvents(testEventsm, invllCut)
CutEvents(testEventj3, invllCut)
CutEvents(testEventm2, invllCut)
CutEvents(testEventm3, invllCut)
CutEvents(testEventm4, invllCut)
CutEvents(testEventm5, invllCut)
CutEvents(testEventt5, invllCut)
CutEvents(testEventt6, invllCut)
CutEvents(testEventt7, invllCut)
CutEvents(testEventt8, invllCut)
CutEvents(testEventt9, invllCut)


CutEvents(testEventsm, ellDotCut)
CutEvents(testEventm2, ellDotCut)
CutEvents(testEventm3, ellDotCut)
CutEvents(testEventm4, ellDotCut)
CutEvents(testEventm5, ellDotCut)
CutEvents(testEventt5, ellDotCut)
CutEvents(testEventt6, ellDotCut)
CutEvents(testEventt7, ellDotCut)
CutEvents(testEventt8, ellDotCut)
CutEvents(testEventt9, ellDotCut)

CutEvents(testEventsm, mzaCut)
CutEvents(testEventm2, mzaCut)
CutEvents(testEventm3, mzaCut)
CutEvents(testEventm4, mzaCut)
CutEvents(testEventm5, mzaCut)
CutEvents(testEventt5, mzaCut)
CutEvents(testEventt6, mzaCut)
CutEvents(testEventt7, mzaCut)
CutEvents(testEventt8, mzaCut)
CutEvents(testEventt9, mzaCut)
"""

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

ubcutfm3 = SHatZACut(-1, mzam3)
ubcutft5 = SHatZACut(-1, mzat5)

CutEvents(testEventm3, ubcutfm3)
CutEvents(testEventt5, ubcutft5)
"""

testEventj3 = LoadLHCOlympics("za/features/smalljjjll.lhco")
# testEventm4 = LoadLHCOlympics("za/features/smallm4.lhco")

# Note: This function save .csv use append, remember to delete the old files
# CorrelationDataAndSave(testEventsm, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zasmpl.csv')
CorrelationDataAndSave(testEventj3, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zaj3pl.csv')
# CorrelationDataAndSave(testEventm2, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zam2pl.csv')
# CorrelationDataAndSave(testEventm3, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zam3pl.csv')
# CorrelationDataAndSave(testEventm4, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zam4pl.csv')
# CorrelationDataAndSave(testEventm5, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zam5pl.csv')
# CorrelationDataAndSave(testEventt5, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat5pl.csv')
# CorrelationDataAndSave(testEventt6, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat6pl.csv')
# CorrelationDataAndSave(testEventt7, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat7pl.csv')
# CorrelationDataAndSave(testEventt8, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat8pl.csv')
# CorrelationDataAndSave(testEventt9, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat9pl.csv')


# print(testEventsm.GetEventCount())
# print(testEventm2.GetEventCount())
# print(testEventt5.GetEventCount())


# testTlSM = HistogramWithMinMax(testEventsm, LeptonPZ, [-1, 1], 50)
# testTlM2 = HistogramWithMinMax(testEventm2, LeptonPZ, [-1, 1], 50)
# testTlT5 = HistogramWithMinMax(testEventt5, LeptonPZ, [-1, 1], 50)

# ZpAndGammaDirTest(testEventsm)
# ZpAndGammaDirTest(testEventm2)
# ZpAndGammaDirTest(testEventt5)

# print(testTlSM.listCount)
# print(testTlM2.listCount)
# print(testTlT5.listCount)
