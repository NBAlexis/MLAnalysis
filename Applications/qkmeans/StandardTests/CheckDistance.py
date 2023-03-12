import random

import matplotlib.pyplot as plt
import numpy as np

pointOfCount = 100000
numOfPair = 30000
pts = np.loadtxt("../../../_DataFolder/qkmeans/standard/p30.csv", delimiter=',')
fact = 4.0

def dist1(v1, v2):
    deltav = v1 - v2
    return np.sqrt(np.dot(deltav, deltav))

def dist2(v1, v2):
    return np.abs(np.dot(np.conjugate(v1), v2))

def RealVToComplexV(v, fac):
    lst = [fac]
    for i in range(0, len(v) // 2):
        lst.append(v[2 * i] + v[2 * i + 1] * 1j)
    arr = np.array(lst)
    arr = arr / np.sqrt(np.dot(np.conjugate(arr), arr))
    return arr

dst = []

for pa in range(0, numOfPair):
    c1 = random.randint(0, pointOfCount - 1)
    c2 = random.randint(0, pointOfCount - 1)
    v1 = pts[c1]
    v2 = pts[c2]
    d1 = dist1(v1, v2)
    d2 = dist2(RealVToComplexV(v1, fact), RealVToComplexV(v2, fact))
    dst.append([d1, d2])

dstarray = np.array(dst)
plt.scatter(dstarray[:, 0], dstarray[:, 1], s=0.1)
plt.show()

np.savetxt("../../../_DataFolder/qkmeans/standard/pair30.csv", dstarray, delimiter=',')