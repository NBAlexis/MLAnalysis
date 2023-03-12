import os

import numpy as np

from Applications.kmeans.kmeansfunctions import ChooseEventWithStratege, SaveCSVFile, ChooseEventWithStrategeQ, \
    NormalizeVArray, SaveCSVFileQ
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut
from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../")


headList = ["FT0"]
energyList = ["1500"]
PhotonNumberCut = PhotonNumberCut(1, [2])
fac = 1.0

for he in headList:
    for en in energyList:
        for i in range(0, 21):
            testEvent = LoadLHCOlympics("_DataFolder/triphoton/cs/{0}/{0}-{1}-{2}.lhco".format(he, en, i))
            CutEvents(testEvent, PhotonNumberCut)
            resultList = NormalizeVArray(ChooseEventWithStrategeQ(testEvent, len(testEvent.events), 0), fac)
            toSave = "_DataFolder/kmeans/cs/csq/{1}-{0}-{2}.csv".format(en, he, i)
            SaveCSVFileQ(toSave, resultList, 7)
            print(toSave, " saved! with events: ", len(testEvent.events))
