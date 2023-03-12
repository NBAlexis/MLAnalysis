import math

import numpy as np

from Interfaces.UsefulFunctions import HistogramStrict

meanData = np.loadtxt("G:\\ifres\\comb\\a0-mean.csv", delimiter=',')
cn = 27.019 # a0
# cn = 27.017 # a1
# cn = 27.01728080 # a2
# cn = 27.01675175 # a3
cssm = 308.63 / 467895
cstt = 431.79 / 654610
csa = 0.91 / 1380 # a0
# csa = 0.16 / 243 # a1
# csa = 0.26 / 394 # a2
# csa = 0.064 / 97 # a2
scorefunc = lambda a: 2 ** (-a / cn)
vscorefunc = np.vectorize(scorefunc)
scores = vscorefunc(meanData[:, 1])

print("csv loaded")
csData = []
scorestart = 0.4
for i in range(0, 701):
    tags = meanData[scores > scorestart + i * 0.0005, 0].astype(int)
    sm = tags[tags == 0]
    tt = tags[tags == 1]
    np = tags[tags == 2]
    lsm = len(sm)
    ltt = len(tt)
    lnp = len(np)
    print(scorestart + i * 0.0005, lsm, ltt, lnp)
    sig = lnp * csa
    dinom = math.sqrt(lsm * cssm + ltt * cstt + lnp * csa)
    csData.append(sig / dinom)

print(csData)




