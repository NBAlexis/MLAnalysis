import math

import numpy as np

from Interfaces.UsefulFunctions import HistogramStrict

meanData1 = np.loadtxt("G:\\ifres\\newcomb\\a0-n0-mean.csv", delimiter=',')
meanData5 = np.loadtxt("G:\\ifres\\comb\\a0-mean.csv", delimiter=',')
cn0 = 27.019 # a0 27.0166
cn = 27.019 # a0
# cn = 27.017 # a1
# cn = 27.01728080 # a2
# cn = 27.01675175 # a3
cssm = 308.63 / 467895
cstt = 431.79 / 654610
# csa = 0.91 / 1380 # a0
# csa = 0.16 / 243 # a1
# csa = 0.26 / 394 # a2
# csa = 0.064 / 97 # a3
scorefunc0 = lambda a: 2 ** (-a / cn0)
scorefunc = lambda a: 2 ** (-a / cn)
vscorefunc0 = np.vectorize(scorefunc0)
vscorefunc = np.vectorize(scorefunc)
scoressm1 = vscorefunc0(meanData1[0 == meanData1[:, 0], 1])
scorestt1 = vscorefunc0(meanData1[1 == meanData1[:, 0], 1])
scoressm2 = vscorefunc(meanData5[0 == meanData5[:, 0], 1])
scorestt2 = vscorefunc(meanData5[1 == meanData5[:, 0], 1])

# vscorefunc0(meanData1[:, 1])
# scores5 = vscorefunc(meanData5[:, 1])
# scores5cut = scores5[0:len(scores1)]

delta1 = (scoressm1 - scoressm2).tolist()
delta2 = (scorestt1 - scorestt2).tolist()

binmin = -0.004
binmax = 0.142
binsep = 73
histres1 = HistogramStrict(delta1, binmin, binmax, binsep)
print(histres1.minMax)
print(histres1.listCount)
print(len(list(delta1)))

histres2 = HistogramStrict(delta2, binmin, binmax, binsep)
print(histres2.minMax)
print(histres2.listCount)
print(len(list(delta2)))

"""
print("csv loaded")
csData2 = []
csData3 = []
csData4 = []
csData5 = []
scorestart = 0.5
for i in range(0, 601):
    # tags = meanData[scores > scorestart + i * 0.0005, 0].astype(int)
    count1 = cstt * np.count_nonzero(scores1 > scorestart + i * 0.0005)
    count2 = cstt * np.count_nonzero(scores2 > scorestart + i * 0.0005)
    count3 = cstt * np.count_nonzero(scores3 > scorestart + i * 0.0005)
    count4 = cstt * np.count_nonzero(scores4 > scorestart + i * 0.0005)
    count5 = cstt * np.count_nonzero(scores5 > scorestart + i * 0.0005)
    sig2 = math.sqrt(137.1) * (count2 - count1) / math.sqrt(count2)
    sig3 = math.sqrt(137.1) * (count3 - count1) / math.sqrt(count3)
    sig4 = math.sqrt(137.1) * (count4 - count1) / math.sqrt(count4)
    sig5 = math.sqrt(137.1) * (count5 - count1) / math.sqrt(count5)
    print(scorestart + i * 0.0005, sig2, sig3, sig4, sig5)

"""



"""

a0
0.645 1.2680023581514897 1.7187634520305557 1.5387341804835564 1.5619415445932519
# 0.026384564855410093 0.05079028734666443 0.06332295565298422 0.05804604268190221 0.05870565680328746
0.026384564855410093 0.05079028734666443 0.06332295565298422 0.06804604268190221 0.06870565680328746

a1
0.6465 0.7635250448592796 0.9850692742084033 1.1584815795882457 1.2404106771289143
cs: 0.024405722491254337 0.03693839079757413 0.041555689647270896 0.04551337437558241 0.04749221673973816

a2
0.646 0.8541039991738746 1.204970372068088 1.4611992816508612 1.736951931583745
0.02506533661263959 0.03957684728311514 0.04749221673973816 0.05408835795359069 0.06200372741021372

a3
0.7125 0.34098551799521654 0.5705779050672267 0.750644890917924 0.8541039991738746
cs: 0.0026384564855410093 0.004617298849696767 0.006596141213852523 0.00857498357800828 0.009894211820778785


"""