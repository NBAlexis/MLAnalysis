import os
import random

import numpy as np
from matplotlib import pyplot as plt

from Applications.qkmeans.qkmeansFunc import ChooseEventWithStrategeQ, NormalizeVArray2
from CutAndExport.CutEvent import CutEvents
from Interfaces.LHCOlympics import LoadLHCOlympics
from CutAndExport.CutFunctions import PhotonNumberCut

#iterations = 100000
fac = 1.3
os.chdir("../../")
headList = ["FT0"]
energyList = ["1500"]
PhotonNumberCut = PhotonNumberCut(1, [3])
testEvent1 = LoadLHCOlympics("_DataFolder/triphoton/cs/SM-1500.lhco")
CutEvents(testEvent1, PhotonNumberCut)
vectors1 = ChooseEventWithStrategeQ(testEvent1, len(testEvent1.events))

for i in range(0, 21):
    testEvent2 = LoadLHCOlympics("_DataFolder/triphoton/cs/FT0/FT0-1500-{0}.lhco".format(i))
    CutEvents(testEvent2, PhotonNumberCut)
    vectors2 = ChooseEventWithStrategeQ(testEvent2, len(testEvent2.events))
    cv2, cv1 = NormalizeVArray2(vectors2, vectors1, fac)
    if 0 == i:
        np.savetxt("_DataFolder/qkmeans/vec/E1500/FT0/SM-1500-{0}.csv".format(i), cv1, "%f", delimiter=',')
    np.savetxt("_DataFolder/qkmeans/vec/E1500/FT0/FT0-1500-{0}.csv".format(i), cv2, "%f", delimiter=',')


