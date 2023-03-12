import os

from Applications.triphoton.CutsAndFilters import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut
from CutAndExport.Histogram import HistogramWithMinMax
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../")
testEventSM3 = LoadLHCOlympics("_DataFolder/triphoton/SM-1500.lhco")
testEventT03 = LoadLHCOlympics("_DataFolder/triphoton/FT0-1500.lhco")
testEventSM10 = LoadLHCOlympics("_DataFolder/triphoton/SM-5000.lhco")
testEventT010 = LoadLHCOlympics("_DataFolder/triphoton/FT0-5000.lhco")
testEventSM14 = LoadLHCOlympics("_DataFolder/triphoton/SM-7000.lhco")
testEventT014 = LoadLHCOlympics("_DataFolder/triphoton/FT0-7000.lhco")
testEventSM30 = LoadLHCOlympics("_DataFolder/triphoton/SM-15000.lhco")
testEventT030 = LoadLHCOlympics("_DataFolder/triphoton/FT0-15000.lhco")

"""
testEventT1 = LoadLHCOlympics("_DataFolder/triphoton/AfterPhotonNumber/FT1-1500.lhco")
testEventT2 = LoadLHCOlympics("_DataFolder/triphoton/AfterPhotonNumber/FT2-1500.lhco")
testEventT5 = LoadLHCOlympics("_DataFolder/triphoton/AfterPhotonNumber/FT5-1500.lhco")
testEventT6 = LoadLHCOlympics("_DataFolder/triphoton/AfterPhotonNumber/FT6-1500.lhco")
testEventT7 = LoadLHCOlympics("_DataFolder/triphoton/AfterPhotonNumber/FT7-1500.lhco")
testEventT8 = LoadLHCOlympics("_DataFolder/triphoton/AfterPhotonNumber/FT8-1500.lhco")
testEventT9 = LoadLHCOlympics("_DataFolder/triphoton/AfterPhotonNumber/FT9-1500.lhco")
"""

# """
threePhotn = PhotonNumberCut(1, [3])
CutEvents(testEventSM3, threePhotn)
CutEvents(testEventT03, threePhotn)
CutEvents(testEventSM10, threePhotn)
CutEvents(testEventT010, threePhotn)
CutEvents(testEventSM14, threePhotn)
CutEvents(testEventT014, threePhotn)
CutEvents(testEventSM30, threePhotn)
CutEvents(testEventT030, threePhotn)
# """

"""
CutEvents(testEventT1, threePhotn)
CutEvents(testEventT2, threePhotn)
CutEvents(testEventT5, threePhotn)
CutEvents(testEventT6, threePhotn)
CutEvents(testEventT7, threePhotn)
CutEvents(testEventT8, threePhotn)
CutEvents(testEventT9, threePhotn)
"""

# """
print(testEventSM3.GetEventCount())
print(testEventT03.GetEventCount())
print(testEventSM10.GetEventCount())
print(testEventT010.GetEventCount())
print(testEventSM14.GetEventCount())
print(testEventT014.GetEventCount())
print(testEventSM30.GetEventCount())
print(testEventT030.GetEventCount())
# """

"""
print(testEventT1.GetEventCount())
print(testEventT2.GetEventCount())
print(testEventT5.GetEventCount())
print(testEventT6.GetEventCount())
print(testEventT7.GetEventCount())
print(testEventT8.GetEventCount())
print(testEventT9.GetEventCount())
"""

# """
testSM3 = HistogramWithMinMax(testEventSM3, GetD43, [0, 0.001], 40)
print(testSM3.listCount)
testT03 = HistogramWithMinMax(testEventT03, GetD43, [0, 0.001], 40)
print(testT03.listCount)
testSM10 = HistogramWithMinMax(testEventSM10, GetD410, [0, 0.001], 40)
print(testSM10.listCount)
testT010 = HistogramWithMinMax(testEventT010, GetD410, [0, 0.001], 40)
print(testT010.listCount)
testSM14 = HistogramWithMinMax(testEventSM14, GetD414, [0, 0.001], 40)
print(testSM14.listCount)
testT014 = HistogramWithMinMax(testEventT014, GetD414, [0, 0.001], 40)
print(testT014.listCount)
testSM30 = HistogramWithMinMax(testEventSM30, GetD430, [0, 0.001], 40)
print(testSM30.listCount)
testT030 = HistogramWithMinMax(testEventT030, GetD430, [0, 0.001], 40)
print(testT030.listCount)
# """

"""
testSM3 = HistogramWithMinMax(testEventSM3, SmallPTA3, [0, 0.64], 40)
print(testSM3.listCount)
testT03 = HistogramWithMinMax(testEventT03, SmallPTA3, [0, 0.64], 40)
print(testT03.listCount)
testSM10 = HistogramWithMinMax(testEventSM10, SmallPTA10, [0, 0.64], 40)
print(testSM10.listCount)
testT010 = HistogramWithMinMax(testEventT010, SmallPTA10, [0, 0.64], 40)
print(testT010.listCount)
testSM14 = HistogramWithMinMax(testEventSM14, SmallPTA14, [0, 0.64], 40)
print(testSM14.listCount)
testT014 = HistogramWithMinMax(testEventT014, SmallPTA14, [0, 0.64], 40)
print(testT014.listCount)
testSM30 = HistogramWithMinMax(testEventSM30, SmallPTA30, [0, 0.64], 40)
print(testSM30.listCount)
testT030 = HistogramWithMinMax(testEventT030, SmallPTA30, [0, 0.64], 40)
print(testT030.listCount)
"""

# testSM = HistogramWithMinMax(testEventSM, SmallestTheta, [0, 1], 40)
# print(testSM.listCount)
# testT0 = HistogramWithMinMax(testEventT0, SmallestTheta, [0, 1], 40)
# print(testT0.listCount)

"""
testT1 = HistogramWithMinMax(testEventT1, SmallestTheta, [0, 1.6], 40)
print(testT1.listCount)
testT2 = HistogramWithMinMax(testEventT2, SmallestTheta, [0, 1.6], 40)
print(testT2.listCount)
testT5 = HistogramWithMinMax(testEventT5, SmallestTheta, [0, 1.6], 40)
print(testT5.listCount)
testT6 = HistogramWithMinMax(testEventT6, SmallestTheta, [0, 1.6], 40)
print(testT6.listCount)
testT7 = HistogramWithMinMax(testEventT7, SmallestTheta, [0, 1.6], 40)
print(testT7.listCount)
testT8 = HistogramWithMinMax(testEventT8, SmallestTheta, [0, 1.6], 40)
print(testT8.listCount)
testT9 = HistogramWithMinMax(testEventT9, SmallestTheta, [0, 1.6], 40)
print(testT9.listCount)
"""

"""

d4:
753671
156676
753365
156727
753238
156674
753435
156691
[536608, 83726, 38623, 22186, 14325, 10001, 7314, 5621, 4456, 3541, 2880, 2504, 2140, 1761, 1659, 1410, 1180, 1103, 961, 909, 844, 716, 665, 633, 607, 488, 479, 389, 399, 348, 344, 301, 303, 267, 264, 262, 243, 191, 203, 191]
[19795, 14272, 11350, 9424, 7979, 6877, 5836, 5311, 4715, 4332, 3905, 3535, 3216, 3001, 2741, 2678, 2526, 2426, 2184, 2128, 1911, 1900, 1766, 1655, 1544, 1587, 1466, 1369, 1286, 1251, 1175, 1111, 994, 993, 960, 961, 921, 816, 826, 783]
[580481, 70781, 30644, 17021, 10664, 7557, 5516, 4076, 3294, 2666, 2281, 1879, 1545, 1321, 1221, 1051, 905, 823, 711, 643, 598, 561, 519, 469, 462, 383, 335, 326, 302, 301, 301, 248, 245, 175, 194, 177, 183, 160, 161, 136]
[20348, 14262, 11257, 9090, 7889, 6760, 5939, 5279, 4749, 4233, 3869, 3598, 3293, 3076, 2858, 2588, 2450, 2328, 2247, 1947, 1990, 1908, 1736, 1653, 1641, 1537, 1501, 1374, 1275, 1217, 1158, 1171, 1056, 1060, 1016, 955, 893, 853, 829, 773]
[588801, 67762, 29313, 16028, 10077, 6864, 5207, 3992, 3198, 2418, 2057, 1748, 1634, 1282, 1112, 977, 850, 789, 707, 665, 562, 527, 438, 414, 397, 383, 350, 276, 291, 298, 255, 240, 238, 199, 178, 183, 157, 136, 148, 151]
[20449, 14208, 11425, 9125, 7673, 6753, 5801, 5214, 4821, 4144, 3962, 3449, 3263, 2994, 2904, 2731, 2481, 2299, 2270, 2061, 2002, 1841, 1732, 1693, 1589, 1454, 1444, 1319, 1264, 1212, 1188, 1134, 1083, 1015, 936, 949, 933, 890, 832, 798]
[604115, 63810, 26370, 14279, 8935, 6093, 4494, 3493, 2744, 2190, 1888, 1529, 1312, 1036, 939, 879, 736, 626, 603, 557, 493, 418, 426, 385, 349, 318, 277, 282, 283, 242, 221, 222, 191, 173, 153, 158, 134, 143, 129, 120]
[20485, 14429, 11131, 9278, 7803, 6611, 5868, 5197, 4627, 4319, 3848, 3549, 3328, 3055, 2825, 2551, 2496, 2271, 2212, 2134, 2000, 1844, 1801, 1688, 1516, 1542, 1398, 1338, 1264, 1227, 1195, 1135, 1105, 1052, 983, 962, 923, 881, 788, 765]

Process finished with exit code 0


PTA
753671
156676
753365
156727
753238
156674
753435
156691
[171375, 136610, 80036, 56709, 44488, 36808, 31560, 27734, 25296, 23290, 19967, 16307, 13467, 11218, 9366, 7879, 6761, 5683, 4851, 4078, 3552, 3053, 2562, 2254, 1838, 1570, 1290, 1041, 873, 641, 463, 339, 254, 167, 120, 68, 55, 27, 11, 9]
[6, 75, 327, 741, 1400, 2120, 2929, 3757, 4760, 5377, 5953, 6336, 6636, 6834, 7330, 7241, 7409, 7419, 7480, 7466, 7232, 7197, 6841, 6452, 6160, 5628, 5146, 4543, 3949, 3140, 2549, 1855, 1367, 1022, 722, 543, 339, 214, 111, 50]
[310205, 103860, 60757, 43553, 33754, 28183, 23560, 21428, 19178, 17734, 15151, 12495, 10167, 8397, 7194, 5978, 5052, 4352, 3794, 3279, 2682, 2284, 1980, 1662, 1361, 1222, 957, 800, 627, 490, 407, 283, 186, 129, 94, 55, 37, 19, 10, 7]
[7, 84, 299, 741, 1391, 2128, 3023, 3770, 4667, 5473, 5857, 6329, 6552, 7065, 7175, 7384, 7417, 7403, 7417, 7439, 7351, 7156, 6827, 6600, 6026, 5634, 4994, 4584, 3887, 3162, 2596, 1933, 1365, 962, 799, 529, 324, 206, 103, 58]
[336811, 97882, 57203, 40577, 31757, 26536, 22475, 19976, 17629, 16503, 14117, 11358, 9728, 8158, 6716, 5715, 4844, 4229, 3480, 3026, 2502, 2188, 1873, 1572, 1326, 1118, 971, 738, 601, 471, 385, 254, 157, 117, 84, 67, 37, 34, 16, 6]
[7, 77, 341, 746, 1426, 2190, 2915, 3861, 4523, 5278, 5910, 6239, 6619, 6907, 7095, 7231, 7546, 7510, 7424, 7448, 7099, 7168, 6956, 6662, 5959, 5717, 5189, 4576, 3882, 3245, 2511, 1903, 1386, 1112, 764, 541, 348, 207, 106, 38]
[385779, 86536, 50742, 35931, 28234, 23029, 19992, 17436, 15922, 14542, 12440, 10268, 8486, 6860, 5882, 5008, 4299, 3632, 3139, 2648, 2254, 1896, 1557, 1372, 1157, 955, 840, 654, 531, 406, 307, 230, 172, 109, 81, 53, 21, 18, 9, 6]
[5, 88, 318, 757, 1367, 2132, 2945, 3842, 4658, 5513, 5891, 6283, 6658, 6965, 7157, 7297, 7456, 7510, 7463, 7448, 7584, 6881, 6727, 6598, 6047, 5637, 5022, 4574, 3905, 3149, 2487, 1807, 1539, 1022, 730, 498, 334, 221, 121, 40]


"""