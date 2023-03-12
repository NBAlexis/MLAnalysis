import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from Applications.PCAAD.pcaadfunctions import ZScoreStandardize, ManualPCA

data1 = np.loadtxt("../../_DataFolder/kmeans/cs/SM/SM-1500.csv", delimiter=',')
data1 = data1[:, 0:12]

newdata = StandardScaler().fit_transform(data1)
pca = PCA(n_components=12)
newdata = pca.fit_transform(newdata)

data1, _ = ZScoreStandardize(data1, None)
data1, _ = ManualPCA(data1, None, 12)

for i in range(0, 12):
    print(np.max(np.abs(newdata[:,i] - data1[:,i])))

stds = np.std(data1, axis=0)
sumstds = np.sum(stds * stds)
plt.bar([i for i in range(0, len(data1[0]))], stds * stds / sumstds)
plt.show()

plt.bar([i for i in range(0, len(data1[0]))], pca.explained_variance_ratio_)
plt.show()


