import os

from Applications.kmeans.kmeansfunctions import ChooseEventWithStrategeQ, NormalizeVArray, SaveCSVFileQ
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../")

PhotonNumberCut = PhotonNumberCut(1, [3])

for ener in ["5000", "7000", "15000"]:
    testEvent = LoadLHCOlympics("_DataFolder/triphoton/cs/SM-{0}.lhco".format(ener))
    CutEvents(testEvent, PhotonNumberCut)
    resultList = NormalizeVArray(ChooseEventWithStrategeQ(testEvent, len(testEvent.events), 0), 1.0)
    toSave = "_DataFolder/kmeans/cs/csq3/SM-{0}.csv".format(ener)
    SaveCSVFileQ(toSave, resultList, 7)
    print(toSave, " saved! with events: ", len(testEvent.events))
