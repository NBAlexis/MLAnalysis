import numpy as np

from Interfaces.UsefulFunctions import HistogramStrict
counts = [335921, 335685, 335456, 335308, 334127, 334087, 334122, 333365, 333196, 333238, 333214, 333308, 333059, 333233, 333647, 333347, 334312, 334141, 334981, 335459, 336396, 320828]
crosses = [8.748779, 8.662495, 8.571247, 8.499948, 8.445656, 8.37835, 8.327999, 8.292839, 8.273086, 8.251527, 8.249646, 8.238043, 8.257455, 8.282612, 8.322343, 8.373476, 8.403988, 8.46645, 8.529048, 8.608382, 8.689725]

leftV = -0.05
rightV = 0.05
anomV = 0.65
distV = 1500
leftAll = []
rightAll = []
anomalAll = []
distAll = []
sumAll = []
crossAll = []
acsAll = []
gradientAll = []
leftV1 = [-0.08 + 0.002 * i for i in range(0, 35)]
for i in range(0, 21):
    if i == 10:
        fileName1 = "H:\\nTGCIF\\Trees\\sm-025-1-std.csv"
        fileName2 = "H:\\nTGCIF\\Trees\\s025-10-std.csv"
        mapFileName = "H:\\nTGCIF\\Maps\\sm-025-1-idx.csv"
        mapdistFileName = "H:\\nTGCIF\\Maps\\sm-025-1-dist.csv"
        denorm = [24.6036968911978, 24.602291307219588, 24.60092646932307, 24.60004389493471, 24.59298720108968,
                  24.59274775719783, 24.592957272170857, 24.588420859084493, 24.58740669983976, 24.587658787440535,
                  24.587514741273683, 24.588078862845617, 24.58658419316407, 24.587628778677978, 24.590111980647652,
                  24.588312866589945, 24.594094256351024, 24.59307099967978, 24.598092500607233, 24.600944355317736,
                  24.606522935296173]
        # 24.587292649771754, 24.585280698009036
        cn1 = 24.585280698009036
        cn2 = denorm[10]
    else:
        fileName1 = "H:\\nTGCIF\\Trees\\s025-{}-std.csv".format(i)
        fileName2 = "H:\\nTGCIF\\Trees\\s025-10-std.csv"
        mapFileName = "H:\\nTGCIF\\Maps\\s025-{}-idx.csv".format(i)
        mapdistFileName = "H:\\nTGCIF\\Maps\\s025-{}-dist.csv".format(i)
        denorm = [24.6036968911978, 24.602291307219588, 24.60092646932307, 24.60004389493471, 24.59298720108968,
                  24.59274775719783, 24.592957272170857, 24.588420859084493, 24.58740669983976, 24.587658787440535,
                  24.587514741273683, 24.588078862845617, 24.58658419316407, 24.587628778677978, 24.590111980647652,
                  24.588312866589945, 24.594094256351024, 24.59307099967978, 24.598092500607233, 24.600944355317736,
                  24.606522935296173]
        # 24.587292649771754, 24.585280698009036
        cn1 = denorm[i]
        # cnsm0 = 24.587292649771754
        cn2 = denorm[10]
    scoreData1 = np.loadtxt(fileName1, delimiter=',')
    scoreData2 = np.loadtxt(fileName2, delimiter=',')
    mapdData = np.loadtxt(mapFileName, delimiter=',').astype(int)
    mapddstData = np.loadtxt(mapdistFileName, delimiter=',')
    print("csv loaded :", i)
    scorefunc1 = lambda a: 2 ** (-a / cn1)
    vscorefunc1 = np.vectorize(scorefunc1)
    scorefunc2 = lambda a: 2 ** (-a / cn2)
    vscorefunc2 = np.vectorize(scorefunc2)
    smallp = mapdData[mapddstData > distV]
    print("dist > ", distV, " :", len(smallp))
    distAll.append(len(smallp))
    score1 = vscorefunc1(scoreData1[:, 1])
    score2 = vscorefunc1(scoreData2[:, 1])
    anSrc1 = score1[score1 > anomV]
    print(len(anSrc1))
    # anSrc2 = score2[score2 > 0.65]
    # print(len(anSrc2))
    anomalAll.append(len(anSrc1))
    diff = []
    for j in range(0, len(score1)):
        # print("{}/{}", i, len(score1))
        scoreMap = score1[j] - score2[mapdData[j]]
        diff.append(scoreMap)
    diffar = np.array(diff)
    gradient = []
    for th in leftV1:
        leftv = diffar[diffar < th]
        gradient.append(len(leftv) * 1000 * crosses[i] / 500000.0)
    gradientAll.append(gradient)
    # binmin = -0.1
    # binmax = 0.1
    # binsep = 40
    # histres1 = HistogramStrict(diff, binmin, binmax, binsep)
    # print(histres1.minMax)
    # print(histres1.listCount)
    # print(len(diff))
    print(np.mean(diffar))
    leftC = diffar[diffar < leftV]
    rightC = diffar[diffar > rightV]
    print(len(leftC), len(rightC))
    leftAll.append(len(leftC))
    rightAll.append(len(rightC))
    sumAll.append(len(leftC) + len(rightC))
    crossAll.append(1000.0 * len(leftC) * crosses[i] / 500000.0)
    acsAll.append(1000.0 * len(anSrc1) * crosses[i] / 500000.0)

print(leftAll)
print(rightAll)
# print(anomalAll)
# print(sumAll)
print(distAll)
print(crossAll)
print("anomal cs: ", acsAll)

print(gradientAll)

"""


"""