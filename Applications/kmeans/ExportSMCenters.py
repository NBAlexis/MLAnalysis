import numpy as np

energies = [1500, 5000, 7000, 15000]

for ener in energies:
    # kfile = np.loadtxt("../../_DataFolder/kmeans/kmeans/E{0}/FT0/FT0-{0}-50-10-all.csv".format(ener), delimiter=',').astype(int)
    # pfile = np.loadtxt("../../_DataFolder/kmeans/cs/E{0}/FT0/FT0-{0}-10.csv".format(ener), delimiter=',')
    pfile = np.loadtxt("../../_DataFolder/kmeans/cs/SM/SM-{0}.csv".format(ener), delimiter=',')
    for kk in [2, 10, 50]:
        kfile = np.loadtxt("../../_DataFolder/kmeans/kmeans/SM/SM-{0}-{1}-all.csv".format(ener, kk), delimiter=',').astype(int)
        tosave = []
        for ite in range(0, 200):
            for k in range(0, kk):
                tosave.append(np.mean(pfile[kfile[ite, :] == k], axis=0)[0:12].tolist())
        np.savetxt("../../_DataFolder/kmeans/kmeans/SMCenters/SM-{0}-k{1}.csv".format(ener, kk), tosave, "%f", delimiter=',')
