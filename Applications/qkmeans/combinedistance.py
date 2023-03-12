import numpy as np

coefflist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
startn = 1
endn = 256
k = 256
ft = 0
energy = 1500
measure = 1

for coef in coefflist:
    tosave = []
    for i in range(startn, endn + 1):
        dists = np.loadtxt("../../_DataFolder/qkmeans/distance/E{0}/FT{1}/{2}/FT{1}-{0}-{2}_{3}_{4}_{5}.csv".format(energy, ft, coef, k, measure, i), delimiter=',')
        tosave.append(dists.tolist())
    np.savetxt("../../_DataFolder/qkmeans/distance/E{0}/FT{1}/FT{1}-{0}-{2}_{3}_{4}_mean.csv".format(energy, ft, coef, k, measure), np.mean(np.array(tosave), axis=0), "%f", delimiter=',')
    np.savetxt("../../_DataFolder/qkmeans/distance/E{0}/FT{1}/FT{1}-{0}-{2}_{3}_{4}_max.csv".format(energy, ft, coef, k, measure), np.max(np.array(tosave), axis=0), "%f", delimiter=',')
    print("FT{1}-{0}-{2}_{3}_{4}_mean.csv".format(energy, ft, coef, k, measure), " saved")
