import os

from Applications.kmeans.kmeansfunctions import ChooseEventWithStratege, SaveCSVFile
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut
from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../")


headList = ["FT0", "FT2", "FT5", "FT7", "FT8", "FT9"]
energyList = ["1500", "5000", "7000", "15000"]
PhotonNumberCut = PhotonNumberCut(1, [3])

for he in headList:
    for en in energyList:
        for i in range(0, 11):
            testEvent = LoadLHCOlympics("_DataFolder/triphoton/cs/{0}/{0}-{1}-{2}.lhco".format(he, en, i))
            CutEvents(testEvent, PhotonNumberCut)
            resultList = ChooseEventWithStratege(testEvent, len(testEvent.events), 0)
            toSave = "_DataFolder/kmeans/cs/E{0}/{1}/{1}-{0}-{2}.csv".format(en, he, i)
            SaveCSVFile(toSave, resultList)
            print(toSave, " saved! with events: ", len(testEvent.events))
