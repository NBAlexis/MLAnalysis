import os

from Applications.triphoton.CutsAndFilters import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut
from CutAndExport.Histogram import HistogramWithMinMax
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../")
testEventSM3 = LoadLHCOlympics("_DataFolder/triphoton/SM-1500.lhco")
testEventT03 = LoadLHCOlympics("_DataFolder/triphoton/FT0-1500.lhco")
testEventT23 = LoadLHCOlympics("_DataFolder/triphoton/FT2-1500.lhco")
testEventT53 = LoadLHCOlympics("_DataFolder/triphoton/FT5-1500.lhco")
testEventT73 = LoadLHCOlympics("_DataFolder/triphoton/FT7-1500.lhco")
testEventT83 = LoadLHCOlympics("_DataFolder/triphoton/FT8-1500.lhco")
testEventT93 = LoadLHCOlympics("_DataFolder/triphoton/FT9-1500.lhco")
testEventSM10 = LoadLHCOlympics("_DataFolder/triphoton/SM-5000.lhco")
testEventT010 = LoadLHCOlympics("_DataFolder/triphoton/FT0-5000.lhco")
testEventT210 = LoadLHCOlympics("_DataFolder/triphoton/FT2-5000.lhco")
testEventT510 = LoadLHCOlympics("_DataFolder/triphoton/FT5-5000.lhco")
testEventT710 = LoadLHCOlympics("_DataFolder/triphoton/FT7-5000.lhco")
testEventT810 = LoadLHCOlympics("_DataFolder/triphoton/FT8-5000.lhco")
testEventT910 = LoadLHCOlympics("_DataFolder/triphoton/FT9-5000.lhco")
testEventSM14 = LoadLHCOlympics("_DataFolder/triphoton/SM-7000.lhco")
testEventT014 = LoadLHCOlympics("_DataFolder/triphoton/FT0-7000.lhco")
testEventT214 = LoadLHCOlympics("_DataFolder/triphoton/FT2-7000.lhco")
testEventT514 = LoadLHCOlympics("_DataFolder/triphoton/FT5-7000.lhco")
testEventT714 = LoadLHCOlympics("_DataFolder/triphoton/FT7-7000.lhco")
testEventT814 = LoadLHCOlympics("_DataFolder/triphoton/FT8-7000.lhco")
testEventT914 = LoadLHCOlympics("_DataFolder/triphoton/FT9-7000.lhco")
testEventSM30 = LoadLHCOlympics("_DataFolder/triphoton/SM-15000.lhco")
testEventT030 = LoadLHCOlympics("_DataFolder/triphoton/FT0-15000.lhco")
testEventT230 = LoadLHCOlympics("_DataFolder/triphoton/FT2-15000.lhco")
testEventT530 = LoadLHCOlympics("_DataFolder/triphoton/FT5-15000.lhco")
testEventT730 = LoadLHCOlympics("_DataFolder/triphoton/FT7-15000.lhco")
testEventT830 = LoadLHCOlympics("_DataFolder/triphoton/FT8-15000.lhco")
testEventT930 = LoadLHCOlympics("_DataFolder/triphoton/FT9-15000.lhco")

threePhotn = PhotonNumberCut(1, [3])
CutEvents(testEventSM3, threePhotn)
CutEvents(testEventT03, threePhotn)
CutEvents(testEventT23, threePhotn)
CutEvents(testEventT53, threePhotn)
CutEvents(testEventT73, threePhotn)
CutEvents(testEventT83, threePhotn)
CutEvents(testEventT93, threePhotn)
CutEvents(testEventSM10, threePhotn)
CutEvents(testEventT010, threePhotn)
CutEvents(testEventT210, threePhotn)
CutEvents(testEventT510, threePhotn)
CutEvents(testEventT710, threePhotn)
CutEvents(testEventT810, threePhotn)
CutEvents(testEventT910, threePhotn)
CutEvents(testEventSM14, threePhotn)
CutEvents(testEventT014, threePhotn)
CutEvents(testEventT214, threePhotn)
CutEvents(testEventT514, threePhotn)
CutEvents(testEventT714, threePhotn)
CutEvents(testEventT814, threePhotn)
CutEvents(testEventT914, threePhotn)
CutEvents(testEventSM30, threePhotn)
CutEvents(testEventT030, threePhotn)
CutEvents(testEventT230, threePhotn)
CutEvents(testEventT530, threePhotn)
CutEvents(testEventT730, threePhotn)
CutEvents(testEventT830, threePhotn)
CutEvents(testEventT930, threePhotn)

print("after tri-photon cut")

print([testEventSM3.GetEventCount(), testEventT03.GetEventCount(), testEventT23.GetEventCount(), testEventT53.GetEventCount(), testEventT73.GetEventCount(), testEventT83.GetEventCount(), testEventT93.GetEventCount()])
print([testEventSM10.GetEventCount(), testEventT010.GetEventCount(), testEventT210.GetEventCount(), testEventT510.GetEventCount(), testEventT710.GetEventCount(), testEventT810.GetEventCount(), testEventT910.GetEventCount()])
print([testEventSM14.GetEventCount(), testEventT014.GetEventCount(), testEventT214.GetEventCount(), testEventT514.GetEventCount(), testEventT714.GetEventCount(), testEventT814.GetEventCount(), testEventT914.GetEventCount()])
print([testEventSM30.GetEventCount(), testEventT030.GetEventCount(), testEventT230.GetEventCount(), testEventT530.GetEventCount(), testEventT730.GetEventCount(), testEventT830.GetEventCount(), testEventT930.GetEventCount()])

ptacutv = 0.12
ptaCut3 = SmallPTACut(1500, ptacutv)
ptaCut10 = SmallPTACut(5000, ptacutv)
ptaCut14 = SmallPTACut(7000, ptacutv)
ptaCut30 = SmallPTACut(15000, ptacutv)

CutEvents(testEventSM3, ptaCut3)
CutEvents(testEventT03, ptaCut3)
CutEvents(testEventT23, ptaCut3)
CutEvents(testEventT53, ptaCut3)
CutEvents(testEventT73, ptaCut3)
CutEvents(testEventT83, ptaCut3)
CutEvents(testEventT93, ptaCut3)
CutEvents(testEventSM10, ptaCut10)
CutEvents(testEventT010, ptaCut10)
CutEvents(testEventT210, ptaCut10)
CutEvents(testEventT510, ptaCut10)
CutEvents(testEventT710, ptaCut10)
CutEvents(testEventT810, ptaCut10)
CutEvents(testEventT910, ptaCut10)
CutEvents(testEventSM14, ptaCut14)
CutEvents(testEventT014, ptaCut14)
CutEvents(testEventT214, ptaCut14)
CutEvents(testEventT514, ptaCut14)
CutEvents(testEventT714, ptaCut14)
CutEvents(testEventT814, ptaCut14)
CutEvents(testEventT914, ptaCut14)
CutEvents(testEventSM30, ptaCut30)
CutEvents(testEventT030, ptaCut30)
CutEvents(testEventT230, ptaCut30)
CutEvents(testEventT530, ptaCut30)
CutEvents(testEventT730, ptaCut30)
CutEvents(testEventT830, ptaCut30)
CutEvents(testEventT930, ptaCut30)

print("after pta cut")

print([testEventSM3.GetEventCount(), testEventT03.GetEventCount(), testEventT23.GetEventCount(), testEventT53.GetEventCount(), testEventT73.GetEventCount(), testEventT83.GetEventCount(), testEventT93.GetEventCount()])
print([testEventSM10.GetEventCount(), testEventT010.GetEventCount(), testEventT210.GetEventCount(), testEventT510.GetEventCount(), testEventT710.GetEventCount(), testEventT810.GetEventCount(), testEventT910.GetEventCount()])
print([testEventSM14.GetEventCount(), testEventT014.GetEventCount(), testEventT214.GetEventCount(), testEventT514.GetEventCount(), testEventT714.GetEventCount(), testEventT814.GetEventCount(), testEventT914.GetEventCount()])
print([testEventSM30.GetEventCount(), testEventT030.GetEventCount(), testEventT230.GetEventCount(), testEventT530.GetEventCount(), testEventT730.GetEventCount(), testEventT830.GetEventCount(), testEventT930.GetEventCount()])

d4cutv = 0.00003
d4Cut3 = D4Cut(1500, d4cutv)
d4Cut10 = D4Cut(5000, d4cutv)
d4Cut14 = D4Cut(7000, d4cutv)
d4Cut30 = D4Cut(15000, d4cutv)

print("after d4 cut")

CutEvents(testEventSM3, d4Cut3)
CutEvents(testEventT03, d4Cut3)
CutEvents(testEventT23, d4Cut3)
CutEvents(testEventT53, d4Cut3)
CutEvents(testEventT73, d4Cut3)
CutEvents(testEventT83, d4Cut3)
CutEvents(testEventT93, d4Cut3)
CutEvents(testEventSM10, d4Cut10)
CutEvents(testEventT010, d4Cut10)
CutEvents(testEventT210, d4Cut10)
CutEvents(testEventT510, d4Cut10)
CutEvents(testEventT710, d4Cut10)
CutEvents(testEventT810, d4Cut10)
CutEvents(testEventT910, d4Cut10)
CutEvents(testEventSM14, d4Cut14)
CutEvents(testEventT014, d4Cut14)
CutEvents(testEventT214, d4Cut14)
CutEvents(testEventT514, d4Cut14)
CutEvents(testEventT714, d4Cut14)
CutEvents(testEventT814, d4Cut14)
CutEvents(testEventT914, d4Cut14)
CutEvents(testEventSM30, d4Cut30)
CutEvents(testEventT030, d4Cut30)
CutEvents(testEventT230, d4Cut30)
CutEvents(testEventT530, d4Cut30)
CutEvents(testEventT730, d4Cut30)
CutEvents(testEventT830, d4Cut30)
CutEvents(testEventT930, d4Cut30)

print([testEventSM3.GetEventCount(), testEventT03.GetEventCount(), testEventT23.GetEventCount(), testEventT53.GetEventCount(), testEventT73.GetEventCount(), testEventT83.GetEventCount(), testEventT93.GetEventCount()])
print([testEventSM10.GetEventCount(), testEventT010.GetEventCount(), testEventT210.GetEventCount(), testEventT510.GetEventCount(), testEventT710.GetEventCount(), testEventT810.GetEventCount(), testEventT910.GetEventCount()])
print([testEventSM14.GetEventCount(), testEventT014.GetEventCount(), testEventT214.GetEventCount(), testEventT514.GetEventCount(), testEventT714.GetEventCount(), testEventT814.GetEventCount(), testEventT914.GetEventCount()])
print([testEventSM30.GetEventCount(), testEventT030.GetEventCount(), testEventT230.GetEventCount(), testEventT530.GetEventCount(), testEventT730.GetEventCount(), testEventT830.GetEventCount(), testEventT930.GetEventCount()])

"""

after tri-photon cut
[753671, 156676, 157566, 156656, 157426, 156559, 157223]
[753365, 156727, 157186, 156580, 157247, 156710, 157026]
[753238, 156674, 157175, 156909, 157100, 156756, 157248]
[753435, 156691, 156999, 157014, 157446, 156845, 157171]
after pta cut
[181913, 147331, 148824, 147058, 148647, 146898, 148503]
[138496, 147305, 148374, 147014, 148385, 147274, 148139]
[129797, 147180, 148279, 147195, 148262, 146934, 148335]
[114118, 147255, 148441, 147509, 148607, 147372, 148401]
after d4 cut
[115065, 128928, 131681, 128686, 131651, 128291, 131300]
[87440, 128303, 131105, 128163, 131141, 128593, 130982]
[82071, 128242, 130897, 128143, 130739, 128161, 130796]
[71935, 128097, 130950, 128397, 130920, 128388, 131096]


"""