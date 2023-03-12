import numpy as np

saveNames = ["G:\\nTGCIF\\Trees\\sm-0\\sm-025-0-hist-"]
LoopStart = 0
Loop = 2000
fileNames = []
saveMean = True
saveScoreStd = True

for saveName in saveNames:
    for i in range(LoopStart, Loop):
        fileNames.append(saveName + str(i) + ".csv")

toSave = None

# """
# history
for i in range(0, len(fileNames)):
    print("adding {} : {} / {}".format(fileNames[i], i, len(fileNames)))
    dataSet = np.loadtxt(fileNames[i], delimiter=',')
    if toSave is None:
        toSave = dataSet
    else:
        toSave = np.append(toSave, dataSet[:, 1:dataSet.shape[1]], 1)

if saveMean and saveScoreStd:
    typeOfPoints = toSave[:, 0].astype(float)
    depthOfPoints = toSave[:, 1:toSave.shape[1]].astype(float)
    depthMean = np.mean(depthOfPoints, 1)
    depthStd = np.std(depthOfPoints, 1).astype(float)
    toSaveArray = np.transpose(np.array([typeOfPoints.tolist(), depthMean.tolist(), depthStd.tolist()]))
    np.savetxt("G:\\nTGCIF\\Trees\\sm-025-0-std.csv", toSaveArray, delimiter=',')
elif saveMean:
    typeOfPoints = toSave[:, 0].astype(float)
    depthOfPoints = toSave[:, 1:toSave.shape[1]].astype(float)
    depthMean = np.mean(depthOfPoints, 1)
    meanArray = np.transpose(np.array([typeOfPoints.tolist(), depthMean.tolist()]))
    np.savetxt("G:\\nTGCIF\\Trees\\sm-025-0-mean.csv", meanArray, delimiter=',')

np.savetxt("G:\\nTGCIF\\Trees\\sm-025-0-hist.csv", toSave.astype(int), delimiter=',', fmt='%i')

# """

# """
# mean


# “”“
