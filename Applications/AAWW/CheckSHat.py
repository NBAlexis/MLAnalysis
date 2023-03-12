import math

from CutAndExport.FilterFunctions import SHatWWReal, SHatWW
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleStatus, ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

exportEventLHCO = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhco")
exportEventLHE = LoadLesHouchesEvent("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhe")

shatDeltaList = []
mseCount = 0
mseValue = 0

for i in range(0, len(exportEventLHCO.events)):
    oneEvent = exportEventLHCO.events[i]
    lepton1 = LorentzVector(0, 0, 0, 0)
    lepton2 = LorentzVector(0, 0, 0, 0)
    jet1 = LorentzVector(0, 0, 0, 0)
    jet2 = LorentzVector(0, 0, 0, 0)
    jet3 = LorentzVector(0, 0, 0, 0)
    missing = LorentzVector(0, 0, 0, 0)
    largestJetIndex1 = 0
    largestJetM1 = 0.0
    largestJetIndex2 = 0
    largestJetM2 = 0.0
    largestJetIndex3 = 0
    largestJetM3 = 0.0
    leptonIdx1 = 0
    leptonIdx2 = 0
    leptonCount = 0
    lepton1Found = False
    hasMissing = False
    for oneParticle in oneEvent.particles:
        if ParticleStatus.Outgoing == oneParticle.status \
                and ParticleType.Jet == oneParticle.particleType:
            momentum = oneParticle.momentum.Momentum()
            if momentum > largestJetM1:
                largestJetM3 = largestJetM2
                largestJetIndex3 = largestJetIndex2
                largestJetM2 = largestJetM1
                largestJetIndex2 = largestJetIndex1
                largestJetM1 = momentum
                largestJetIndex1 = oneParticle.index
            elif momentum > largestJetM2:
                largestJetM3 = largestJetM2
                largestJetIndex3 = largestJetIndex2
                largestJetM2 = momentum
                largestJetIndex2 = oneParticle.index
            elif momentum > largestJetM3:
                largestJetM3 = momentum
                largestJetIndex3 = oneParticle.index
        elif ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
            leptonCount = leptonCount + 1
            if not lepton1Found:
                lepton1Found = True
                leptonIdx1 = oneParticle.index
            else:
                leptonIdx2 = oneParticle.index
        elif ParticleType.Missing == oneParticle.particleType:
            hasMissing = True
            missing = missing + oneParticle.momentum
    if largestJetIndex1 > 0 and largestJetIndex2 > 0:
        jet1 = oneEvent.particles[largestJetIndex1 - 1].momentum
        jet2 = oneEvent.particles[largestJetIndex2 - 1].momentum
        if largestJetIndex3 > 0:
            jet3 = oneEvent.particles[largestJetIndex3 - 1].momentum
    else:
        continue
    if leptonCount != 2:
        continue
    if leptonIdx1 > 0 and leptonIdx2 > 0:
        lepton1 = oneEvent.particles[leptonIdx1 - 1].momentum
        lepton2 = oneEvent.particles[leptonIdx2 - 1].momentum
    else:
        continue
    if not hasMissing:
        print(oneEvent.DebugPrint())
        continue
        # all good
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
    realShat = 0.000001 * SHatWWReal(exportEventLHE.events[i])
    approxiShat = 0.000001 * SHatWW(oneEvent)
    shatDeltaList.append(realShat - approxiShat)
    mseCount = mseCount + 1
    mseValue = mseValue + (realShat - approxiShat) * (realShat - approxiShat)
    if (realShat - approxiShat) * (realShat - approxiShat) > 10000:
        print(realShat, approxiShat)

print(mseValue)
print(mseCount)
print(mseValue / mseCount)
import matplotlib.pyplot as plt
plt.hist(shatDeltaList, 50, [-200, 200])
plt.show()
