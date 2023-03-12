import numpy as np

from Interfaces.UsefulFunctions import HistogramStrict

meanData = np.loadtxt("G:\\ifres\\comb\\a4-mean.csv", delimiter=',')

print("csv loaded")

cond1 = meanData[:, 0] < 0.5
smData = meanData[cond1, 1]
otherData = meanData[~cond1, :]
cond2 = otherData[:, 0] < 1.5
ttData = otherData[cond2, 1]
npData = otherData[~cond2, 1]

print("point seperated")

# cn = 27.019 # a0
# cn = 27.017 # a1
# cn = 27.01728080 # a2
# cn = 27.01675175 # a3
cn = 27.01663060 # a4
scorefunc = lambda a: 2 ** (-a / cn)
vscorefunc = np.vectorize(scorefunc)

scoreSM = vscorefunc(smData)
scoreTT = vscorefunc(ttData)
scoreNP = vscorefunc(npData)

print("score calculated")

binmin = 0.14
binmax = 0.84
binsep = 35
histres1 = HistogramStrict(list(scoreSM), binmin, binmax, binsep)
print(histres1.minMax)
print(histres1.listCount)
print(len(list(scoreSM)))

histres2 = HistogramStrict(list(scoreTT), binmin, binmax, binsep)
print(histres2.minMax)
print(histres2.listCount)
print(len(list(scoreTT)))

histres3 = HistogramStrict(list(scoreNP), binmin, binmax, binsep)
print(histres3.minMax)
print(histres3.listCount)
print(len(list(scoreNP)))
