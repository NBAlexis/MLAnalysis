import numpy as np

dataSet = np.loadtxt("G:\\ifres\\comb\\a0-hist.csv", delimiter=',')

line1 = dataSet[0 + 1]
line2 = dataSet[654610 + 1]
line3 = dataSet[654610 + 467895 + 1]
all = np.array([line1, line2, line3]).astype(int)
np.savetxt("G:\\ifres\\comb\\a0-history.csv", all, delimiter=',', fmt='%i')