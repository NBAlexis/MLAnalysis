from Applications.AZ.ZGammaCuts import ParticleNumberZA, DeltaRCut
from CutAndExport.CutEvent import CutEvents
from UsefulFunctions import *

#########################################################
# 我们从bgsm.lhco里选 n1 个事例, 从jjjll里选 n2 个事例
# 然后我们从 m3,4,5 t5,6,7,9 里选出100个事例
#########################################################
n1 = [49351, 105094, 82718, 70231, 14046, 79738, 34781]
n2 = [53932, 114849, 33398, 90396, 76750, 87140, 38010]

# testEventsm = LoadLHCOlympics("../../_DataFolder/za/newbackgrounds/azsm1.lhco")
testEventjjjll = LoadLHCOlympics("../../_DataFolder/za/newbackgrounds/jjjll4.lhco")
# testEventjjjll.AddEventSet(LoadLHCOlympics("../../_DataFolder/za/newbackgrounds/jjjll2.lhco"))
# testEventjjjll.AddEventSet(LoadLHCOlympics("../../_DataFolder/za/newbackgrounds/jjjll3.lhco"))
# testEventjjjll.AddEventSet(LoadLHCOlympics("../../_DataFolder/za/newbackgrounds/jjjll4.lhco"))
# testEventjjjll.AddEventSet(LoadLHCOlympics("../../_DataFolder/za/newbackgrounds/jjjll5.lhco"))

"""
testEventm3 = LoadLHCOlympics("../../_DataFolder/za/features/azsignalm3.lhco")
testEventm4 = LoadLHCOlympics("../../_DataFolder/za/features/azsignalm4.lhco")
testEventm5 = LoadLHCOlympics("../../_DataFolder/za/features/azsignalm5.lhco")
testEventt5 = LoadLHCOlympics("../../_DataFolder/za/features/azsignalt5.lhco")
testEventt6 = LoadLHCOlympics("../../_DataFolder/za/features/azsignalt6.lhco")
testEventt7 = LoadLHCOlympics("../../_DataFolder/za/features/azsignalt7.lhco")
testEventt9 = LoadLHCOlympics("../../_DataFolder/za/features/azsignalt9.lhco")
"""

particleNumberCut = ParticleNumberZA()
deltaRCut = DeltaRCut(0.2)

CutEvents(testEventjjjll, particleNumberCut)
print(testEventjjjll.GetEventCount())

"""
CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventm3, particleNumberCut)
CutEvents(testEventm4, particleNumberCut)
CutEvents(testEventm5, particleNumberCut)
CutEvents(testEventt5, particleNumberCut)
CutEvents(testEventt6, particleNumberCut)
CutEvents(testEventt7, particleNumberCut)
CutEvents(testEventt9, particleNumberCut)

CutEvents(testEventsm, deltaRCut)
CutEvents(testEventm3, deltaRCut)
CutEvents(testEventm4, deltaRCut)
CutEvents(testEventm5, deltaRCut)
CutEvents(testEventt5, deltaRCut)
CutEvents(testEventt6, deltaRCut)
CutEvents(testEventt7, deltaRCut)
CutEvents(testEventt9, deltaRCut)

resultList = ChooseEventsAZ(testEventsm, 10000, 0)
resultList = resultList + ChooseEventsAZ(testEventm3, 20, 1)
resultList = resultList + ChooseEventsAZ(testEventm4, 20, 2)
resultList = resultList + ChooseEventsAZ(testEventm5, 20, 3)
resultList = resultList + ChooseEventsAZ(testEventt5, 20, 4)
resultList = resultList + ChooseEventsAZ(testEventt6, 20, 5)
resultList = resultList + ChooseEventsAZ(testEventt7, 20, 6)
resultList = resultList + ChooseEventsAZ(testEventt9, 20, 7)


SaveCSVFile("datamixedAZ.txt", resultList, 0, 12)
"""

print("Finished")
