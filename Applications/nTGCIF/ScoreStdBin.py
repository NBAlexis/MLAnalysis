import math

import numpy as np

from Interfaces.UsefulFunctions import HistogramStrict

denorm = [25.969640777214963, 25.966857059555114, 25.967450240984157, 25.966718524845717,
          25.965823841419194, 25.965224149397233, 25.96659504016832, 25.968085382368656,
          25.967892754159756, 25.96685404803303, 25.965887115014223, 25.966332986449945]

counts = [665041, 664116, 664313, 664070,
          663773, 663574, 664029, 664524,
          664460, 664115, 663794, 663942]

cn = 24.59307099967978
scoreData = np.loadtxt("G:\\nTGCIF\\Trees\\s025-18-std.csv", delimiter=',')
print("csv loaded, length=", len(scoreData))

factor = math.log(2) / cn / math.sqrt(2000)
scorefunc = lambda a, b: math.sqrt(2 ** (-a / cn)) * b
vscorefunc = np.vectorize(scorefunc)
right = factor * vscorefunc(scoreData[:, 1], scoreData[:, 2])
binmin = 0.0021
binmax = 0.0036
binsep = 50
histres1 = HistogramStrict(list(right), binmin, binmax, binsep)
print(histres1.minMax)
print(histres1.listCount)
print(len(list(right)))
