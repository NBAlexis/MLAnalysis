import random
import numpy as np

dataCount = 100000

p6 = [[random.uniform(-1.0, 1.0) for d in range(0, 6)] for k in range(0, dataCount)]
p14 = [[random.uniform(-1.0, 1.0) for d in range(0, 14)] for k in range(0, dataCount)]
p30 = [[random.uniform(-1.0, 1.0) for d in range(0, 30)] for k in range(0, dataCount)]

np.savetxt("../../../_DataFolder/qkmeans/standard/p6.csv", np.array(p6), delimiter=',')
np.savetxt("../../../_DataFolder/qkmeans/standard/p14.csv", np.array(p14), delimiter=',')
np.savetxt("../../../_DataFolder/qkmeans/standard/p30.csv", np.array(p30), delimiter=',')
