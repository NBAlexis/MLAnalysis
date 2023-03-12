import os

from Applications.nTGC.nTGCCuts import *
from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("G:\\ntgc\\")

particleNumberCut = ParticleNumberNTGCJJA()
mzcut = MjjMZCut(45, 15, 91.1876)
thetaGammaCut1 = ThetaGammaCut(0.9)
deltaPhi2 = DeltaPhiMax(-0.99)
deltaPhi1 = DeltaPhiMax(-0.9995)

fileNames = ["025", "05", "1", "3", "5"]
cutGroup = [[particleNumberCut, mzcut, thetaGammaCut1],
            [particleNumberCut, mzcut, thetaGammaCut1],
            [particleNumberCut, mzcut, thetaGammaCut1],
            [particleNumberCut, mzcut, deltaPhi2],
            [particleNumberCut, mzcut, deltaPhi1]]
for i in range(0, 5):
    fileSM1 = "sm-{}-0.lhco".format(fileNames[i])
    fileSM2 = "sm-{}-1.lhco".format(fileNames[i])
    sigFileName = "sig-s{}-0.lhco".format(fileNames[i])
    event1Set = LoadLHCOlympics(fileSM1)
    event2Set = LoadLHCOlympics(fileSM2)
    event1Set.AddEventSet(event2Set)
    event3Set = LoadLHCOlympics(sigFileName)
    print("SM Events:", i, " before cut is ", event1Set.GetEventCount())
    print("Sig Events:", i, " before cut is ", event3Set.GetEventCount())
    for cuts in cutGroup[i]:
        CutEvents(event1Set, cuts)
        CutEvents(event3Set, cuts)
        print("SM Events:", i, " after cut {} is ".format(cuts), event1Set.GetEventCount())
        print("Sig Events:", i, " after cut {} is ".format(cuts), event3Set.GetEventCount())
