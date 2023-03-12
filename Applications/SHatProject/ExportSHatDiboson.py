import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import *
from Interfaces.LesHouchesEvent import *


def Export(eventSetLHCO, eventSetLHE, startIndex, endIndex, file):
    normalizer = 1000.0
    # result_f.write("j1x,j1y,j1z,j2x,j2y,j2z,l1x,l1y,l1z,l2x,l2y,l2z,mx,my,shat\n")
    for i in range(startIndex, endIndex):
        oneEvent = eventSetLHCO.events[i]
        other1 = LorentzVector(0, 0, 0, 0)
        other2 = LorentzVector(0, 0, 0, 0)
        otherParticleCount = 0
        missing = LorentzVector(0, 0, 0, 0)
        leptonIdx1 = 0
        leptonIdx2 = 0
        leptonCount1 = 0
        leptonCount2 = 0
        hasMissing = False
        for oneParticle in oneEvent.particles:
            if ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
                if oneParticle.PGDid > 0:
                    leptonCount1 = leptonCount1 + 1
                    leptonIdx1 = oneParticle.index
                else:
                    leptonCount2 = leptonCount2 + 1
                    leptonIdx2 = oneParticle.index
            elif ParticleType.Missing == oneParticle.particleType:
                if hasMissing:
                    print(oneEvent.DebugPrint())
                hasMissing = True
                missing = missing + oneParticle.momentum
            else:
                otherParticleCount = otherParticleCount + 1
                if 1 == otherParticleCount:
                    other1 = oneParticle.momentum
                elif 2 == otherParticleCount:
                    other2 = oneParticle.momentum
        if 1 != leptonCount1 or 1 != leptonCount2:
            continue
        if otherParticleCount > 2:
            continue
        if not hasMissing:
            print(oneEvent.DebugPrint())
            continue
            # all good
        realShat = SHatWWReal(eventSetLHE.events[i])
        lepton1 = oneEvent.particles[leptonIdx1 - 1].momentum
        lepton2 = oneEvent.particles[leptonIdx2 - 1].momentum
        if lepton1.values[1] * lepton1.values[1] + lepton1.values[2] * lepton1.values[2] < 2500:
            continue
        if lepton2.values[1] * lepton2.values[1] + lepton2.values[2] * lepton2.values[2] < 2500:
            continue
        if missing.values[1] * missing.values[1] + missing.values[2] * missing.values[2] < 2500:
            continue
        # Why this?
        # lepX = lepton1.values[1] + lepton2.values[1]
        # lepY = lepton1.values[2] + lepton2.values[2]
        # if lepX * lepX + lepY * lepY < 100:
        #     continue
        # lengthLep = math.sqrt(lepX * lepX + lepY * lepY)
        # lengthM = math.sqrt(missing.values[1] * missing.values[1] + missing.values[2] * missing.values[2])
        # dotLM = (lepX * missing.values[1] + lepY * missing.values[2]) / (lengthLep * lengthM)
        # if abs(dotLM) < 0.8:
        #     continue
        # lengthL1 = math.sqrt(lepton1.values[1] * lepton1.values[1]
        #                      + lepton1.values[2] * lepton1.values[2]
        #                      + lepton1.values[3] * lepton1.values[3])
        # lengthL2 = math.sqrt(lepton2.values[1] * lepton2.values[1]
        #                      + lepton2.values[2] * lepton2.values[2]
        #                      + lepton2.values[3] * lepton2.values[3])
        # dotLL = (lepton1.values[1] * lepton2.values[1]
        #          + lepton1.values[2] * lepton2.values[2]
        #          + lepton1.values[3] * lepton2.values[3]) / (lengthL1 * lengthL2)
        # if dotLL > -0.5:
        #     continue
        # print(missing.PseudoRapidity(), missing.Azimuth(), missing.Pt())
        paramLst = [lepton1.values[1] / normalizer,
                    lepton1.values[2] / normalizer,
                    lepton1.values[3] / normalizer,
                    lepton2.values[1] / normalizer,
                    lepton2.values[2] / normalizer,
                    lepton2.values[3] / normalizer,
                    other1.values[0] / normalizer,
                    other1.values[1] / normalizer,
                    other1.values[2] / normalizer,
                    other1.values[3] / normalizer,
                    other2.values[0] / normalizer,
                    other2.values[1] / normalizer,
                    other2.values[2] / normalizer,
                    other2.values[3] / normalizer,
                    missing.values[1] / normalizer,
                    missing.values[2] / normalizer]
        strW = ""
        for i in range(0, 16):
            strW = "{}{:.5e},".format(strW, paramLst[i])
        # for x in range(0, 14):
        #    for y in range(x, 14):
        #        strW = "{}{:.5e},".format(strW, paramLst[x] * paramLst[y])
        strW = "{}{:.5e}\n".format(strW, realShat / (normalizer * normalizer))
        file.write(strW)

# """
trainFile = "../../_DataFolder/wwdiboson/train.csv"
trainFile = open(trainFile, 'w')
exportEventLHCO = LoadLHCOlympics("../../_DataFolder/wwdiboson/sample.lhco")
exportEventLHE = LoadLargeLesHouchesEvent("../../_DataFolder/wwdiboson/sample.lhe", True)
Export(exportEventLHCO, exportEventLHE, 0, 1000000, trainFile)
trainFile.close()
# """

# """
testFile = "../../_DataFolder/wwdiboson/test.csv"
testFile = open(testFile, 'w')
exportEventLHCO = LoadLHCOlympics("../../_DataFolder/wwdiboson/check.lhco")
exportEventLHE = LoadLargeLesHouchesEvent("../../_DataFolder/wwdiboson/check.lhe", False)
Export(exportEventLHCO, exportEventLHE, 0, 1000000, testFile)
testFile.close()
# """

print("========== done ===============")
