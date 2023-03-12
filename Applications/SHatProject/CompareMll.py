import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent, LoadLargeLesHouchesEvent

def ExportMll(eventSetLHCO, eventSetLHE, startIndex, endIndex, applyCut, dataType, file):
    msq = 0
    msqCount = 0
    for i in range(startIndex, endIndex):
        oneEventA = eventSetLHCO.events[i]
        oneEventB = eventSetLHE.events[i]
        Alepton1 = LorentzVector(0, 0, 0, 0)
        Alepton2 = LorentzVector(0, 0, 0, 0)
        Blepton1 = LorentzVector(0, 0, 0, 0)
        Blepton2 = LorentzVector(0, 0, 0, 0)
        AleptonIdx1 = 0
        AleptonIdx2 = 0
        AlargestLepton1 = 0
        AlargestLepton2 = 0
        BleptonIdx1 = 0
        BleptonIdx2 = 0
        BlargestLepton1 = 0
        BlargestLepton2 = 0
        for oneParticle in oneEventA.particles:
            if ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
                momentumLepton = oneParticle.momentum.Momentum()
                if oneParticle.PGDid > 0 and momentumLepton > AlargestLepton1:
                    AleptonIdx1 = oneParticle.index
                    AlargestLepton1 = momentumLepton
                elif oneParticle.PGDid < 0 and momentumLepton > AlargestLepton2:
                    AleptonIdx2 = oneParticle.index
                    AlargestLepton2 = momentumLepton
        for oneParticle in oneEventB.particles:
            if ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
                momentumLepton = oneParticle.momentum.Momentum()
                if oneParticle.PGDid > 0 and momentumLepton > BlargestLepton1:
                    BleptonIdx1 = oneParticle.index
                    BlargestLepton1 = momentumLepton
                elif oneParticle.PGDid < 0 and momentumLepton > BlargestLepton2:
                    BleptonIdx2 = oneParticle.index
                    BlargestLepton2 = momentumLepton
        if not (AleptonIdx1 > 0 and AleptonIdx2 > 0):
            continue
        if not (BleptonIdx1 > 0 and BleptonIdx2 > 0):
            continue
        Alepton1 = oneEventA.particles[AleptonIdx1 - 1].momentum
        Alepton2 = oneEventA.particles[AleptonIdx2 - 1].momentum
        Blepton1 = oneEventB.particles[BleptonIdx1 - 1].momentum
        Blepton2 = oneEventB.particles[BleptonIdx2 - 1].momentum
        mass1 = (Alepton1 + Alepton2).Mass()
        mass2 = (Blepton1 + Blepton2).Mass()
        deltaM = mass1 - mass2
        msqOne = 0.000001 * (mass1 * mass1 - mass2 * mass1)
        msqOne = msqOne * msqOne
        file.write("{}, {}, {}\n".format(mass2, deltaM, msqOne))
        msq = msq + msqOne
        msqCount = msqCount + 1
    print("msq = {}".format(msq / msqCount))


exportEventLHCO = LoadLHCOlympics("G://ww/samplea0.lhco")
exportEventLHE = LoadLargeLesHouchesEvent("G://ww/samplea0.lhe", False)

datafile = open("../../_DataFolder/shat/a0deltaM.csv", 'w')
ExportMll(exportEventLHCO, exportEventLHE, 0, 1000000, False, 0, datafile)
datafile.close()

print("========== done ===============")
