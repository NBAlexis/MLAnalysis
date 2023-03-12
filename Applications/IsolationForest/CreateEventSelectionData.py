from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import JetNumberCut, LeptonPMCut
from CutAndExport.FilterFunctions import *
from UsefulFunctions import *


def ChooseEventWithStratege(allEvents: EventSet, count: int, tag: int):
    result = []
    idx = 0
    while len(result) < count:
        theEvent = allEvents.events[idx]
        largestJetIndex = -1  # 对于一个list, list[i] 这个i通常叫index
        largestJetEnergy = 0
        secondJetIndex = -1  # 对于一个list, list[i] 这个i通常叫index
        secondJetEnergy = 0
        largestLeptonIndex = -1
        largestLeptonEnergy = 0
        largestAntiLeptonIndex = -1
        largestAntiLeptonEnergy = 0
        for theParticle in theEvent.particles:
            if theParticle.particleType == ParticleType.Jet:
                jetEnergy = theParticle.momentum.Momentum()
                if jetEnergy > largestJetEnergy:
                    secondJetIndex = largestJetIndex
                    secondJetEnergy = largestJetEnergy
                    largestJetIndex = theParticle.index - 1
                    largestJetEnergy = jetEnergy
                elif jetEnergy > secondJetEnergy:
                    secondJetIndex = theParticle.index - 1
                    secondJetEnergy = jetEnergy
            elif theParticle.particleType == ParticleType.Electron or theParticle.particleType == ParticleType.Muon:
                if theParticle.PGDid > 0:
                    leptonEnergy = theParticle.momentum.Momentum()
                    if leptonEnergy > largestLeptonEnergy:
                        largestLeptonEnergy = leptonEnergy
                        largestLeptonIndex = theParticle.index - 1
                else:
                    antielLeptonEnergy = theParticle.momentum.Momentum()
                    if antielLeptonEnergy > largestAntiLeptonEnergy:
                        largestAntiLeptonEnergy = antielLeptonEnergy
                        largestAntiLeptonIndex = theParticle.index - 1
        if largestJetIndex >= 0 and secondJetIndex >= 0 \
                and largestLeptonIndex >= 0 and largestAntiLeptonIndex >= 0:
            mjj = Mjj2Filter(theEvent)
            yjj = Yjj2Filter(theEvent)
            cosLM = PhiLLM(theEvent)
            cosLL = LeptonDot(theEvent)
            mol = PTLandPTMissing(theEvent)
            shatWW = SHatWW(theEvent)
            if mjj > 150 and yjj > 1.2 and cosLM > 0.3 and cosLL < 0.0 and mol > 600 and shatWW > 1.5e6:
                toAdd = [tag, 1]
                result = result + [toAdd]
            else:
                toAdd = [tag, 0]
                result = result + [toAdd]
        idx = idx + 1
    return result


lst1 = [16846, 37390]
lst2 = [23654, 52500]
fileNamelst = ["essdatav0.csv", "essdatav3.csv"]

smEvent = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/bgsm.lhco")
ttEvent = LoadLHCOlympics("../../_DataFolder/wwaa/ttbar/ttbar.lhco")
ttEvent.AddEventSet(LoadLHCOlympics("../../_DataFolder/wwaa/ttbar/ttbar2.lhco"))

v0Event = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhco")
v3Event = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha3.lhco")

jetNumberCut = JetNumberCut(2, [2, 3, 4, 5])
leptonNumberCut = LeptonPMCut(False, 1, 1)

CutEvents(smEvent, jetNumberCut)
CutEvents(smEvent, leptonNumberCut)
CutEvents(ttEvent, jetNumberCut)
CutEvents(ttEvent, leptonNumberCut)
CutEvents(v0Event, jetNumberCut)
CutEvents(v0Event, leptonNumberCut)
CutEvents(v3Event, jetNumberCut)
CutEvents(v3Event, leptonNumberCut)

signalSamples = [v0Event, v3Event]

for i in range(0, 2):
    resultList = ChooseEventWithStratege(smEvent, lst1[i], 0)
    resultList = resultList + ChooseEventWithStratege(ttEvent, lst2[i], 1)
    resultList = resultList + ChooseEventWithStratege(signalSamples[i], 50, 2)
    SaveCSVFile(fileNamelst[i], resultList, 0, 1)
    print(fileNamelst[i], " saved!")

print("Finished")
