from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import JetNumberCut, LeptonPMCut
from Applications.IsolationForest.UsefulFunctions import *


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
v3Event = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha3.lhco")

jetNumberCut = JetNumberCut(2, [2, 3, 4, 5])
leptonNumberCut = LeptonPMCut(False, 1, 1)

CutEvents(smEvent, jetNumberCut)
CutEvents(smEvent, leptonNumberCut)
CutEvents(ttEvent, jetNumberCut)
CutEvents(ttEvent, leptonNumberCut)
CutEvents(v0Event, jetNumberCut)
CutEvents(v0Event, leptonNumberCut)
CutEvents(v3Event, jetNumberCut)
CutEvents(v3Event, leptonNumberCut)

signalSamples = [v0Event, v3Event]

"""
for i in range(0, 2):
    resultList = ChooseEvents(smEvent, lst1[i], 0)
    resultList = resultList + ChooseEvents(ttEvent, lst2[i], 1)
    resultList = resultList + ChooseEvents(signalSamples[i], 50, 2)
    SaveCSVFile(fileNamelst[i], resultList, 0, 18 + 2)
    print(fileNamelst[i], " saved!")
"""

fileNamelst2 = ["v3event-n0.csv", "v3event-n1.csv", "v3event-n2.csv", "v3event-n3.csv", "v3event-n4.csv"]
for i in range(0, 5):
    resultList = ChooseEvents(smEvent, lst1[1], 0)
    resultList = resultList + ChooseEvents(ttEvent, lst2[1], 1)
    resultList = resultList + ChooseEvents(signalSamples[1], 10 * i, 2)
    SaveCSVFile(fileNamelst2[i], resultList, 0, 18 + 2)
    print(fileNamelst2[i], " saved!")

print("Finished")
