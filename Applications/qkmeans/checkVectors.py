import os
import random

import numpy as np
from matplotlib import pyplot as plt

from Applications.qkmeans.qkmeansFunc import ChooseEventWithStrategeQ, NormalizeVArray, StateVectorDot3, \
    NormalizeVArray2
from CutAndExport.CutEvent import CutEvents
from Interfaces.LHCOlympics import LoadLHCOlympics
from CutAndExport.CutFunctions import PhotonNumberCut

iterations = 100000
fac = 1.3
os.chdir("../../")
headList = ["FT0"]
energyList = ["1500"]
PhotonNumberCut = PhotonNumberCut(1, [3])
testEvent1 = LoadLHCOlympics("_DataFolder/triphoton/cs/SM-1500.lhco")
CutEvents(testEvent1, PhotonNumberCut)
testEvent2 = LoadLHCOlympics("_DataFolder/triphoton/cs/FT0/FT0-1500-0.lhco")
CutEvents(testEvent2, PhotonNumberCut)
vectors1 = ChooseEventWithStrategeQ(testEvent1, len(testEvent1.events))
vectors2 = ChooseEventWithStrategeQ(testEvent2, len(testEvent2.events))
cv2, cv1 = NormalizeVArray2(vectors2, vectors1, fac)

print(len(vectors1))
print(len(vectors2))

d1 = []
d2 = []

for i in range(0, iterations):
    p1 = int(random.uniform(0.0, 1.0) * len(vectors1))
    p2 = int(random.uniform(0.0, 1.0) * len(vectors2))
    v1 = np.array(vectors1[p1])
    v2 = np.array(vectors2[p2])
    delta = v1 - v2
    d1.append(np.sqrt(np.dot(delta, delta)))
    w1 = cv1[p1]
    w2 = cv2[p2]
    d2.append(StateVectorDot3(w1, w2))

plt.scatter(d1, d2, s=0.01)
plt.show()
plt.hist(d1, 50)
plt.show()
plt.hist(d2, 50)
plt.show()
