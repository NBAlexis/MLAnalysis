import os

import numpy as np

from Applications.kmeans.kmeansfunctions import KMeansQ

os.chdir("../../")

# data = np.loadtxt("_DataFolder/kmeans/cs/csq/FT0-1500-{0}.csv".format(0), delimiter=',')
# succeed, kValueList = KMeansQ(data, 32, 600)
# np.savetxt("_DataFolder/kmeans/kmeans/csq/FT0-1500-{0}.csv".format(0), kValueList.astype(int), delimiter=',', fmt='%i')

# """
averageDistance = []
for i in range(0, 21):
    data = np.loadtxt("_DataFolder/kmeans/cs/csq2/FT0-1500-{0}.csv".format(i), delimiter=',')
    for j in range(0, 3):
        succeed, kValueList = KMeansQ(data, 64, 1000)
        np.savetxt("_DataFolder/kmeans/kmeans/csq2/FT0-1500-{0}-{1}.csv".format(i, j + 1), kValueList.astype(int), delimiter=',', fmt='%i')
        print(i, " finished({0}/20)".format(j + 1))
# """