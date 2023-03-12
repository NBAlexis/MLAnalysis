import os

from Applications.triphoton.CutsAndFilters import InvarientMissing, MissingInvMassCut
from CutAndExport.CutEvent import CutEvents
from CutAndExport.Histogram import HistogramWithMinMax
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../")
m2 = LoadLesHouchesEvent("_DataFolder/triphoton/llvvaa/m2.lhe")
t5 = LoadLesHouchesEvent("_DataFolder/triphoton/llvvaa/t5.lhe")
t8 = LoadLesHouchesEvent("_DataFolder/triphoton/llvvaa/t8.lhe")

testm2 = HistogramWithMinMax(m2, InvarientMissing, [0, 25000], 50)
print(testm2.listCount)
testt5 = HistogramWithMinMax(t5, InvarientMissing, [0, 25000], 50)
print(testt5.listCount)
testt8 = HistogramWithMinMax(t8, InvarientMissing, [0, 25000], 50)
print(testt8.listCount)

invcut = MissingInvMassCut()
CutEvents(t5, invcut)

print(t5.GetEventCount())

"""

[9, 43, 127, 277, 496, 727, 1007, 1335, 1740, 1993, 2374, 2799, 2936, 3338, 3620, 3788, 3925, 4051, 4270, 4262, 4271, 4263, 4143, 4054, 3857, 3656, 3511, 3428, 3126, 2785, 2660, 2401, 2180, 1992, 1756, 1537, 1380, 1120, 978, 815, 695, 578, 439, 339, 273, 212, 137, 94, 84, 54]
[25882, 800, 934, 1338, 1520, 1760, 2045, 2275, 2382, 2635, 2793, 2909, 2923, 3052, 2983, 3013, 3019, 3070, 2944, 2813, 2741, 2583, 2499, 2275, 2190, 2014, 1887, 1654, 1566, 1347, 1222, 1092, 987, 866, 706, 623, 534, 419, 384, 308, 249, 195, 172, 110, 85, 71, 46, 28, 24, 18]
[96188, 1134, 584, 418, 299, 248, 161, 144, 115, 98, 86, 71, 63, 54, 35, 35, 32, 29, 23, 30, 24, 21, 17, 20, 9, 8, 12, 7, 5, 8, 2, 2, 5, 3, 3, 1, 3, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

vbs
76382
tri-photon
100000-76382

"""