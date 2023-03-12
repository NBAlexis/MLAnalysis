import numpy as np

from Interfaces.UsefulFunctions import HistogramStrict

meanData = np.loadtxt("G:\\ifres\\comb\\a3-mean.csv", delimiter=',')
# cn = 27.019 # a0
# cn = 27.017 # a1
# cn = 27.01728080 # a2
cn = 27.01675175 # a3
scorefunc = lambda a: 2 ** (-a / cn)
vscorefunc = np.vectorize(scorefunc)
scores = vscorefunc(meanData[:, 1])

print("csv loaded")
countData = []
nplst = []
npttlst = []
scorestart = 0.14
for i in range(0, 661):
    tags = meanData[scores > scorestart + i * 0.001, 0].astype(int)
    sm = tags[tags == 0]
    tt = tags[tags == 1]
    np = tags[tags == 2]
    lsm = len(sm)
    ltt = len(tt)
    lnp = len(np)
    print(scorestart + i * 0.001, lsm, ltt, lnp)
    alllen = lsm + ltt + lnp
    countData.append([lsm / alllen, ltt / alllen, lnp / alllen])
    nplst.append(lnp / alllen)
    npttlst.append((ltt + lnp) / alllen)

print(countData)

print(npttlst)
print(nplst)



