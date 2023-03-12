import os

from CutAndExport.CorrelationFunctions import CorrelationData
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../_DataFolder")

testEventm2r = LoadLesHouchesEvent("wa/features2/fm2.lhe")
testEventm2 = LoadLHCOlympics("wa/features2/fm2.lhco")

"""
# Check which s hat is better
# It shows SHatAW2 is better


div1 = 0.0
div2 = 0.0

for i in range(len(testEventm2.events)):
    # requirements
    bValid = (1 == testEventm2.events[i].GetLeptonCount())
    bValid = bValid and testEventm2.events[i].GetJetCount() > 1
    bValid = bValid and testEventm2.events[i].GetPhotonCount() > 0
    bValid = bValid and LeptonPtFilter(testEventm2.events[i]) >= 80.0
    bValid = bValid and PtSlashFilter(testEventm2.events[i]) >= 50.0
    if bValid:
        particleCount = particleCount + 1
        calcS = SHatAW(testEventm2.events[i])
        calcS2 = SHatAW2(testEventm2.events[i])
        realS = SHatAWReal(testEventm2r.events[i])
        div1 = div1 + ((calcS - realS) * (calcS - realS) / 1.0e6)
        div2 = div2 + ((calcS2 - realS) * (calcS2 - realS) / 1.0e6)


print(calcS)
print(calcS2)

"""

"""
# To draw s hat correlation plots
particleCount0 = 0
particleCount = 0
lstDelta = []
lstS1 = []
lstRealS = []
particleCount1 = 0
particleCount2 = 0
result_f = open("m2shat.csv", 'w')
for i in range(len(testEventm2.events)):
    # requirements
    bValid = (1 == testEventm2.events[i].GetLeptonCount())
    bValid = bValid and testEventm2.events[i].GetJetCount() > 1
    bValid = bValid and testEventm2.events[i].GetPhotonCount() > 0
    bValid = bValid and LeptonPtFilter(testEventm2.events[i]) >= 80.0
    bValid = bValid and PtSlashFilter(testEventm2.events[i]) >= 50.0
    if bValid:
        particleCount = particleCount + 1
        calcS = SHatAW(testEventm2.events[i])
        realS = SHatAWReal(testEventm2r.events[i])
        if abs(calcS - realS) < 1.0e7:
            particleCount2 = particleCount2 + 1
            lstDelta.append(calcS - realS)
        if 3.0e7 > calcS > 0 and 3.0e7 > realS > 0:
            particleCount1 = particleCount1 + 1
            lstS1.append(calcS)
            lstRealS.append(realS)
            result_f.write("{}, {}\n".format(realS, calcS))

result_f.close()
print(particleCount0)
print(particleCount)
print(particleCount1)
print(particleCount2)
histArray = [0 for i in range(50)]
sep2 = 2.0e7 / 50

for i in range(particleCount2):
    v3 = lstDelta[i]
    idxZ = math.floor((v3 + 1.0e7) / sep2)
    if idxZ >= 40:
        idxZ = 39
    if idxZ < 0:
        idxZ = 0
    histArray[idxZ] = histArray[idxZ] + 1

print(histArray)
import matplotlib.pyplot as plt
plt.hist2d(lstS1, lstRealS, [50, 50])
plt.show()

"""