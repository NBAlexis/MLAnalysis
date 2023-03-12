import os
import random

import numpy as np
from matplotlib import pyplot as plt

from Applications.kmeans.kmeansfunctions import ChooseEventWithStrategeQ, NormalizeVArrayOnlyRescal, NormalizeVTest, \
    StateVectorDot3
from CutAndExport.CutEvent import CutEvents
from Interfaces.LHCOlympics import LoadLHCOlympics
from CutAndExport.CutFunctions import PhotonNumberCut

iterations = 10000
fac = 1.0


os.chdir("../../")
headList = ["FT0"]
energyList = ["1500"]
PhotonNumberCut = PhotonNumberCut(1, [2])
testEvent = LoadLHCOlympics("_DataFolder/triphoton/cs/FT0/FT0-1500-0.lhco")
CutEvents(testEvent, PhotonNumberCut)
vectors1 = ChooseEventWithStrategeQ(testEvent, len(testEvent.events), 0)
vectors2 = NormalizeVArrayOnlyRescal(vectors1)

print(len(vectors1))

d1 = []
d2 = []

for i in range(0, 100000):
    p1 = int(random.uniform(0.0, 1.0) * len(vectors1))
    p2 = int(random.uniform(0.0, 1.0) * len(vectors1))
    v1 = np.array(vectors1[p1])
    v2 = np.array(vectors1[p2])
    delta = v1 - v2
    d1.append(np.sqrt(np.dot(delta, delta)))
    w1 = NormalizeVTest(vectors2[p1], fac)
    w2 = NormalizeVTest(vectors2[p2], fac)
    d2.append(StateVectorDot3(w1, w2))

plt.scatter(d1, d2, s=0.1)
plt.show()
plt.hist(d1, 50)
plt.show()
plt.hist(d2, 50)
plt.show()
