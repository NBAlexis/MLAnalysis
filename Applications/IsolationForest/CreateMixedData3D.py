from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import JetNumberCut, LeptonPMCut
from UsefulFunctions import *

#########################################################
# 这个是 p p > l+ l- j j 事例。
# 我们从bgsm.lhco里选2000个事例
# 然后我们从alpha0,1,2,3,4里各选出20个事例
#########################################################
lst1 = [16846, 37390]
lst2 = [23654, 52500]
fileNamelst = ["v0event.csv", "v3event.csv"]

smEvent = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/bgsm.lhco")
ttEvent = LoadLHCOlympics("../../_DataFolder/wwaa/ttbar/ttbar.lhco")
ttEvent.AddEventSet(LoadLHCOlympics("../../_DataFolder/wwaa/ttbar/ttbar2.lhco"))

v0Event = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhco")

jetNumberCut = JetNumberCut(2, [2, 3, 4, 5])
leptonNumberCut = LeptonPMCut(False, 1, 1)

CutEvents(smEvent, jetNumberCut)
CutEvents(smEvent, leptonNumberCut)
CutEvents(ttEvent, jetNumberCut)
CutEvents(ttEvent, leptonNumberCut)
CutEvents(v0Event, jetNumberCut)
CutEvents(v0Event, leptonNumberCut)

resultList = ChooseEvents2D(smEvent, 16846, 0)
resultList = resultList + ChooseEvents2D(ttEvent, 23654, 1)
resultList = resultList + ChooseEvents2D(v0Event, 50, 2)
SaveCSVFile("v0event2d.csv", resultList, 0, 2 + 2)
print("v0event2d.csv", " saved!")

print("Finished")
