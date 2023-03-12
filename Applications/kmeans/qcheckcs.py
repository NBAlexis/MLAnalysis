import os
import numpy as np

#################################################################
from matplotlib import pyplot as plt

energy = "1500"
readfileName = "FT0"
cutdist = 0.975
#################################################################

os.chdir("../../")
dim = 12
eventnumber = []

for n in range(0, 21):
    dist = np.loadtxt("_DataFolder/kmeans/distances/csq/{1}-{0}-{2}-meandist.csv".format(energy, readfileName, n), delimiter=',')
    eventnumber.append(len(dist[dist < cutdist]))

print(eventnumber)
plt.plot(eventnumber)
plt.show()




