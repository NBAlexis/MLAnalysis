import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent, LoadLargeLesHouchesEvent


def Export(eventSetLHCO, eventSetLHE, startIndex, endIndex, applyCut, dataType, file):
    normalizer = 1000.0
    # result_f.write("j1x,j1y,j1z,j2x,j2y,j2z,l1x,l1y,l1z,l2x,l2y,l2z,mx,my,shat\n")
    for i in range(startIndex, endIndex):
        oneEvent = eventSetLHCO.events[i]
        lepton1 = LorentzVector(0, 0, 0, 0)
        lepton2 = LorentzVector(0, 0, 0, 0)
        jet1 = LorentzVector(0, 0, 0, 0)
        jet2 = LorentzVector(0, 0, 0, 0)
        missing = LorentzVector(0, 0, 0, 0)
        largestJetIndex1 = 0
        largestJetM1 = 0.0
        largestJetIndex2 = 0
        largestJetM2 = 0.0
        leptonIdx1 = 0
        leptonIdx2 = 0
        largestLepton1 = 0
        largestLepton2 = 0
        hasMissing = False
        for oneParticle in oneEvent.particles:
            if ParticleStatus.Outgoing == oneParticle.status \
                    and ParticleType.Jet == oneParticle.particleType:
                momentum = oneParticle.momentum.Momentum()
                if momentum > largestJetM1:
                    largestJetM2 = largestJetM1
                    largestJetIndex2 = largestJetIndex1
                    largestJetM1 = momentum
                    largestJetIndex1 = oneParticle.index
                elif momentum > largestJetM2:
                    largestJetM2 = momentum
                    largestJetIndex2 = oneParticle.index
            elif ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
                momentumLepton = oneParticle.momentum.Momentum()
                if oneParticle.PGDid > 0 and momentumLepton > largestLepton1:
                    leptonIdx1 = oneParticle.index
                    largestLepton1 = momentumLepton
                elif oneParticle.PGDid < 0 and momentumLepton > largestLepton2:
                    leptonIdx2 = oneParticle.index
                    largestLepton2 = momentumLepton
            elif ParticleType.Missing == oneParticle.particleType:
                hasMissing = True
                missing = missing + oneParticle.momentum
        if not (leptonIdx1 > 0 and leptonIdx2 > 0):
            continue
        if not (largestJetIndex1 > 0 and largestJetIndex2 > 0):
            continue
        if not hasMissing:
            print(oneEvent.DebugPrint())
            continue
        lepton1 = oneEvent.particles[leptonIdx1 - 1].momentum
        lepton2 = oneEvent.particles[leptonIdx2 - 1].momentum
        jet1 = oneEvent.particles[largestJetIndex1 - 1].momentum
        jet2 = oneEvent.particles[largestJetIndex2 - 1].momentum
        if applyCut:
            if lepton1.values[1] * lepton1.values[1] + lepton1.values[2] * lepton1.values[2] < 1.0e2:
                continue
            if lepton2.values[1] * lepton2.values[1] + lepton2.values[2] * lepton2.values[2] < 1.0e2:
                continue
            if missing.values[1] * missing.values[1] + missing.values[2] * missing.values[2] < 1.0e2:
                continue
            lepX = lepton1.values[1] + lepton2.values[1]
            lepY = lepton1.values[2] + lepton2.values[2]
            if lepX * lepX + lepY * lepY < 100:
                continue
            lengthLep = math.sqrt(lepX * lepX + lepY * lepY)
            lengthM = math.sqrt(missing.values[1] * missing.values[1] + missing.values[2] * missing.values[2])
            dotLM = (lepX * missing.values[1] + lepY * missing.values[2]) / (lengthLep * lengthM)
            if abs(dotLM) < 0.8:
                continue
            lengthL1 = math.sqrt(lepton1.values[1] * lepton1.values[1]
                                 + lepton1.values[2] * lepton1.values[2]
                                 + lepton1.values[3] * lepton1.values[3])
            lengthL2 = math.sqrt(lepton2.values[1] * lepton2.values[1]
                                 + lepton2.values[2] * lepton2.values[2]
                                 + lepton2.values[3] * lepton2.values[3])
            dotLL = (lepton1.values[1] * lepton2.values[1]
                     + lepton1.values[2] * lepton2.values[2]
                     + lepton1.values[3] * lepton2.values[3]) / (lengthL1 * lengthL2)
            if dotLL > -0.5:
                continue
        realShat = SHatWWReal(eventSetLHE.events[i])
        if 0 == dataType:
            paramLst = [jet1.values[0] / normalizer,
                        jet1.values[1] / normalizer,
                        jet1.values[2] / normalizer,
                        jet1.values[3] / normalizer,
                        jet2.values[0] / normalizer,
                        jet2.values[1] / normalizer,
                        jet2.values[2] / normalizer,
                        jet2.values[3] / normalizer,
                        lepton1.values[0] / normalizer,
                        lepton1.values[1] / normalizer,
                        lepton1.values[2] / normalizer,
                        lepton1.values[3] / normalizer,
                        lepton2.values[0] / normalizer,
                        lepton2.values[1] / normalizer,
                        lepton2.values[2] / normalizer,
                        lepton2.values[3] / normalizer,
                        missing.values[1] / normalizer,
                        missing.values[2] / normalizer]
            strW = ""
            for x in range(0, 18):
                strW = "{}{:.5e},".format(strW, paramLst[x])
            strW = "{}{:.5e}\n".format(strW, math.sqrt(realShat) / normalizer)
            file.write(strW)
        elif 1 == dataType:
            paramLst = [jet1.values[0] / normalizer,
                        jet1.values[1] / normalizer,
                        jet1.values[2] / normalizer,
                        jet1.values[3] / normalizer,
                        jet2.values[0] / normalizer,
                        jet2.values[1] / normalizer,
                        jet2.values[2] / normalizer,
                        jet2.values[3] / normalizer,
                        lepton1.values[0] / normalizer,
                        lepton1.values[1] / normalizer,
                        lepton1.values[2] / normalizer,
                        lepton1.values[3] / normalizer,
                        lepton2.values[0] / normalizer,
                        lepton2.values[1] / normalizer,
                        lepton2.values[2] / normalizer,
                        lepton2.values[3] / normalizer,
                        missing.values[1] / normalizer,
                        missing.values[2] / normalizer]
            strW = ""
            for x in range(0, 18):
                for y in range(x + 1, 18):
                    strW = "{}{:.5e},".format(strW, paramLst[x] * paramLst[y])
            strW = "{}{:.5e}\n".format(strW, realShat / (normalizer * normalizer))
            file.write(strW)
        if 2 == dataType:
            paramLst = [lepton1.values[0] / normalizer,
                        lepton1.values[1] / normalizer,
                        lepton1.values[2] / normalizer,
                        lepton1.values[3] / normalizer,
                        lepton2.values[0] / normalizer,
                        lepton2.values[1] / normalizer,
                        lepton2.values[2] / normalizer,
                        lepton2.values[3] / normalizer,
                        missing.values[1] / normalizer,
                        missing.values[2] / normalizer]
            strW = ""
            for x in range(0, 10):
                strW = "{}{:.5e},".format(strW, paramLst[x])
            strW = "{}{:.5e}\n".format(strW, realShat / (normalizer * normalizer))
            file.write(strW)
        if 3 == dataType:
            paramLst = [jet1.values[0] / normalizer,
                        jet1.values[1] / normalizer,
                        jet1.values[2] / normalizer,
                        jet1.values[3] / normalizer,
                        jet2.values[0] / normalizer,
                        jet2.values[1] / normalizer,
                        jet2.values[2] / normalizer,
                        jet2.values[3] / normalizer,
                        missing.values[1] / normalizer,
                        missing.values[2] / normalizer]
            strW = ""
            for x in range(0, 10):
                strW = "{}{:.5e},".format(strW, paramLst[x])
            strW = "{}{:.5e}\n".format(strW, realShat / (normalizer * normalizer))
            file.write(strW)


def ExportOnlyLHCO(eventSetLHCO, startIndex, endIndex, file):
    normalizer = 1000.0
    # result_f.write("j1x,j1y,j1z,j2x,j2y,j2z,l1x,l1y,l1z,l2x,l2y,l2z,mx,my,shat\n")
    for i in range(startIndex, endIndex):
        oneEvent = eventSetLHCO.events[i]
        lepton1 = LorentzVector(0, 0, 0, 0)
        lepton2 = LorentzVector(0, 0, 0, 0)
        jet1 = LorentzVector(0, 0, 0, 0)
        jet2 = LorentzVector(0, 0, 0, 0)
        missing = LorentzVector(0, 0, 0, 0)
        largestJetIndex1 = 0
        largestJetM1 = 0.0
        largestJetIndex2 = 0
        largestJetM2 = 0.0
        leptonIdx1 = 0
        leptonIdx2 = 0
        largestLepton1 = 0
        largestLepton2 = 0
        hasMissing = False
        numberOfJet = oneEvent.GetJetCount()
        if numberOfJet < 2 or numberOfJet > 5:
            continue
        for oneParticle in oneEvent.particles:
            if ParticleStatus.Outgoing == oneParticle.status \
                    and ParticleType.Jet == oneParticle.particleType:
                momentum = oneParticle.momentum.Momentum()
                if momentum > largestJetM1:
                    largestJetM2 = largestJetM1
                    largestJetIndex2 = largestJetIndex1
                    largestJetM1 = momentum
                    largestJetIndex1 = oneParticle.index
                elif momentum > largestJetM2:
                    largestJetM2 = momentum
                    largestJetIndex2 = oneParticle.index
            elif ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
                momentumLepton = oneParticle.momentum.Momentum()
                if oneParticle.PGDid > 0 and momentumLepton > largestLepton1:
                    leptonIdx1 = oneParticle.index
                    largestLepton1 = momentumLepton
                elif oneParticle.PGDid < 0 and momentumLepton > largestLepton2:
                    leptonIdx2 = oneParticle.index
                    largestLepton2 = momentumLepton
            elif ParticleType.Missing == oneParticle.particleType:
                hasMissing = True
                missing = missing + oneParticle.momentum
        if not (leptonIdx1 > 0 and leptonIdx2 > 0):
            continue
        if not (largestJetIndex1 > 0 and largestJetIndex2 > 0):
            continue
        if not hasMissing:
            print(oneEvent.DebugPrint())
            continue
        lepton1 = oneEvent.particles[leptonIdx1 - 1].momentum
        lepton2 = oneEvent.particles[leptonIdx2 - 1].momentum
        jet1 = oneEvent.particles[largestJetIndex1 - 1].momentum
        jet2 = oneEvent.particles[largestJetIndex2 - 1].momentum
        paramLst = [jet1.values[0] / normalizer,
                    jet1.values[1] / normalizer,
                    jet1.values[2] / normalizer,
                    jet1.values[3] / normalizer,
                    jet2.values[0] / normalizer,
                    jet2.values[1] / normalizer,
                    jet2.values[2] / normalizer,
                    jet2.values[3] / normalizer,
                    lepton1.values[0] / normalizer,
                    lepton1.values[1] / normalizer,
                    lepton1.values[2] / normalizer,
                    lepton1.values[3] / normalizer,
                    lepton2.values[0] / normalizer,
                    lepton2.values[1] / normalizer,
                    lepton2.values[2] / normalizer,
                    lepton2.values[3] / normalizer,
                    missing.values[1] / normalizer,
                    missing.values[2] / normalizer]
        strW = ""
        for x in range(0, 18):
            strW = "{}{:.5e}{}".format(strW, paramLst[x], "" if 17 == x else ",")
        strW = strW + "\n"
        file.write(strW)


def ExportOnlyLHCONoCut(eventSetLHCO, startIndex, endIndex, file):
    normalizer = 1000.0
    # result_f.write("j1x,j1y,j1z,j2x,j2y,j2z,l1x,l1y,l1z,l2x,l2y,l2z,mx,my,shat\n")
    for i in range(startIndex, endIndex):
        oneEvent = eventSetLHCO.events[i]
        lepton1 = LorentzVector(0, 0, 0, 0)
        lepton2 = LorentzVector(0, 0, 0, 0)
        jet1 = LorentzVector(0, 0, 0, 0)
        jet2 = LorentzVector(0, 0, 0, 0)
        missing = LorentzVector(0, 0, 0, 0)
        largestJetIndex1 = 0
        largestJetM1 = 0.0
        largestJetIndex2 = 0
        largestJetM2 = 0.0
        leptonIdx1 = 0
        leptonIdx2 = 0
        largestLepton1 = 0
        largestLepton2 = 0
        hasMissing = False
        for oneParticle in oneEvent.particles:
            if ParticleStatus.Outgoing == oneParticle.status \
                    and ParticleType.Jet == oneParticle.particleType:
                momentum = oneParticle.momentum.Momentum()
                if momentum > largestJetM1:
                    largestJetM2 = largestJetM1
                    largestJetIndex2 = largestJetIndex1
                    largestJetM1 = momentum
                    largestJetIndex1 = oneParticle.index
                elif momentum > largestJetM2:
                    largestJetM2 = momentum
                    largestJetIndex2 = oneParticle.index
            elif ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
                momentumLepton = oneParticle.momentum.Momentum()
                if oneParticle.PGDid > 0 and momentumLepton > largestLepton1:
                    leptonIdx1 = oneParticle.index
                    largestLepton1 = momentumLepton
                elif oneParticle.PGDid < 0 and momentumLepton > largestLepton2:
                    leptonIdx2 = oneParticle.index
                    largestLepton2 = momentumLepton
            elif ParticleType.Missing == oneParticle.particleType:
                hasMissing = True
                missing = missing + oneParticle.momentum
        if not (leptonIdx1 > 0 and leptonIdx2 > 0):
            continue
        if not (largestJetIndex1 > 0 and largestJetIndex2 > 0):
            continue
        if not hasMissing:
            print(oneEvent.DebugPrint())
            continue
        lepton1 = oneEvent.particles[leptonIdx1 - 1].momentum
        lepton2 = oneEvent.particles[leptonIdx2 - 1].momentum
        jet1 = oneEvent.particles[largestJetIndex1 - 1].momentum
        jet2 = oneEvent.particles[largestJetIndex2 - 1].momentum
        paramLst = [jet1.values[0] / normalizer,
                    jet1.values[1] / normalizer,
                    jet1.values[2] / normalizer,
                    jet1.values[3] / normalizer,
                    jet2.values[0] / normalizer,
                    jet2.values[1] / normalizer,
                    jet2.values[2] / normalizer,
                    jet2.values[3] / normalizer,
                    lepton1.values[0] / normalizer,
                    lepton1.values[1] / normalizer,
                    lepton1.values[2] / normalizer,
                    lepton1.values[3] / normalizer,
                    lepton2.values[0] / normalizer,
                    lepton2.values[1] / normalizer,
                    lepton2.values[2] / normalizer,
                    lepton2.values[3] / normalizer,
                    missing.values[1] / normalizer,
                    missing.values[2] / normalizer]
        strW = ""
        for x in range(0, 18):
            strW = "{}{:.5e}{}".format(strW, paramLst[x], "" if 17 == x else ",")
        strW = strW + "\n"
        file.write(strW)

"""
for i in range(0, 5):
    exportEventLHCO = LoadLHCOlympics("G://ww/samplea{}.lhco".format(i))
    exportEventLHE = LoadLargeLesHouchesEvent("G://ww/samplea{}.lhe".format(i), False)
    datafile = open("../../_DataFolder/shat/a{}trainsq.csv".format(i), 'w')
    Export(exportEventLHCO, exportEventLHE, 0, 1000000, False, 0, datafile)
    datafile.close()
    print("========== done sample {}===============".format(i))
    exportEventLHCO = LoadLHCOlympics("G://ww/checka{}.lhco".format(i))
    exportEventLHE = LoadLargeLesHouchesEvent("G://ww/checka{}.lhe".format(i), False)
    datafile = open("../../_DataFolder/shat/a{}testsq.csv".format(i), 'w')
    Export(exportEventLHCO, exportEventLHE, 0, 1000000, False, 0, datafile)
    datafile.close()
    print("========== done check {}===============".format(i))
"""

"""
exportEventLHCOsm1 = LoadLHCOlympics("G://ww/a0-14-1.lhco")
exportEventLHEsm1 = LoadLargeLesHouchesEvent("G://ww/a0-14-1.lhe", False)
exportEventLHCOsm2 = LoadLHCOlympics("G://ww/a0-14-2.lhco")
exportEventLHEsm2 = LoadLargeLesHouchesEvent("G://ww/a0-14-2.lhe", False)
exportEventLHCOsm1.AddEventSet(exportEventLHCOsm2)
exportEventLHEsm1.AddEventSet(exportEventLHEsm2)

exportEventLHCOsm3 = LoadLHCOlympics("G://ww/a0-14-3.lhco")
exportEventLHEsm3 = LoadLargeLesHouchesEvent("G://ww/a0-14-3.lhe", False)
exportEventLHCOsm4 = LoadLHCOlympics("G://ww/a0-14-4.lhco")
exportEventLHEsm4 = LoadLargeLesHouchesEvent("G://ww/a0-14-4.lhe", False)
exportEventLHCOsm3.AddEventSet(exportEventLHCOsm4)
exportEventLHEsm3.AddEventSet(exportEventLHEsm4)

datafile1 = open("../../_DataFolder/shat/a014trainsq.csv", 'w')
Export(exportEventLHCOsm1, exportEventLHEsm1, 0, 1000000, False, 0, datafile1)
datafile1.close()

datafile1 = open("../../_DataFolder/shat/a014testsq.csv", 'w')
Export(exportEventLHCOsm1, exportEventLHEsm1, 0, 1000000, False, 0, datafile1)
datafile1.close()
"""

"""
sourcefolder = "a0"
for i in range(0, 11):
    exportEventLHCO1 = LoadLHCOlympics("G://ww/{}-0-{}.lhco".format(sourcefolder, i))
    exportEventLHCO2 = LoadLHCOlympics("G://ww/{}-1-{}.lhco".format(sourcefolder, i))
    exportEventLHCO1.AddEventSet(exportEventLHCO2)
    print("exporting {} - {}".format(sourcefolder, i))
    datafile1 = open("../../_DataFolder/shat/{}-{}.csv".format(sourcefolder, i), 'w')
    ExportOnlyLHCO(exportEventLHCO1, 0, 1000000, datafile1)
    datafile1.close()
"""

sourcefolder = "a3"
for i in range(0, 11):
    exportEventLHCO1 = LoadLHCOlympics("G:\\ww\\finalcs\\{}-c-{}.lhco".format(sourcefolder, i))
    print("exporting {} - {}".format(sourcefolder, i))
    datafile1 = open("G:\\ww\\finalcsshat\\csv\\{}-{}.csv".format(sourcefolder, i), 'w')
    ExportOnlyLHCONoCut(exportEventLHCO1, 0, exportEventLHCO1.GetEventCount(), datafile1)
    datafile1.close()

"""
exportEventLHCO1 = LoadLHCOlympics("G://ww/ttbar1.lhco")
exportEventLHCO2 = LoadLHCOlympics("G://ww/ttbar2.lhco")
exportEventLHCO3 = LoadLHCOlympics("G://ww/ttbar3.lhco")
exportEventLHCO4 = LoadLHCOlympics("G://ww/ttbar4.lhco")
exportEventLHCO1.AddEventSet(exportEventLHCO2)
exportEventLHCO1.AddEventSet(exportEventLHCO3)
exportEventLHCO1.AddEventSet(exportEventLHCO4)
datafile1 = open("../../_DataFolder/shat/ttbar.csv", 'w')
ExportOnlyLHCO(exportEventLHCO1, 0, 2000000, datafile1)
datafile1.close()
"""

"""
exportEventLHCOsm1 = LoadLHCOlympics("G://ww/sm1.lhco")
exportEventLHCOsm2 = LoadLHCOlympics("G://ww/sm2.lhco")
exportEventLHCOsm3 = LoadLHCOlympics("G://ww/sm3.lhco")
exportEventLHCOsm4 = LoadLHCOlympics("G://ww/sm4.lhco")
exportEventLHCOsm1.AddEventSet(exportEventLHCOsm2)
exportEventLHCOsm1.AddEventSet(exportEventLHCOsm3)
exportEventLHCOsm1.AddEventSet(exportEventLHCOsm4)

datafile1 = open("../../_DataFolder/shat/sm.csv", 'w')
ExportOnlyLHCO(exportEventLHCOsm1, 0, 2000000, datafile1)
datafile1.close()
"""

"""
for i in range(0, 5):
    exportEventLHCO1 = LoadLHCOlympics("G://ww/samplea{}.lhco".format(i))
    exportEventLHCO2 = LoadLHCOlympics("G://ww/checka{}.lhco".format(i))
    exportEventLHCO1.AddEventSet(exportEventLHCO2)
    datafile = open("../../_DataFolder/shat/a{}.csv".format(i), 'w')
    ExportOnlyLHCO(exportEventLHCO1, 0, 2000000, datafile)
    datafile.close()
    print("========== done check {}===============".format(i))
"""
