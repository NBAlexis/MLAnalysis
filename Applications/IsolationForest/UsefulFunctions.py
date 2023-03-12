from DataStructure.EventSet import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from DataStructure.Particles import *


def ReadCSVFile(fileName: str, startIdx: int, endIdx: int) -> list:
    dataSample = []
    with open(fileName) as f:
        for lines in f.readlines():
            strList = lines.split(',')
            if len(strList) > endIdx:
                numberList = []
                for j in range(startIdx, endIdx + 1):
                    numberList = numberList + [float(strList[j])]
                dataSample = dataSample + [numberList]
    return dataSample


def SaveCSVFile(fileName: str, content: list, startIdx: int, endIdx: int):
    with open(fileName, 'w') as f:
        for line in content:
            if len(line) > endIdx:
                for i in range(startIdx, endIdx + 1):
                    if i == endIdx:
                        f.write(str(line[i]) + "\n")
                    else:
                        f.write(str(line[i]) + ", ")


#########################################################
# 选事例的标准：两个jet，1个l+，一个l-
#########################################################
def ChooseEvents(allEvents: EventSet, count: int, tag: int) -> list:
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
        missingIndex = -1
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
            elif theParticle.particleType == ParticleType.Missing:
                missingIndex = theParticle.index - 1
        if largestJetIndex >= 0 and secondJetIndex >= 0 \
                and largestLeptonIndex >= 0 and largestAntiLeptonIndex >= 0:
            p1 = theEvent.particles[largestJetIndex].momentum
            p2 = theEvent.particles[secondJetIndex].momentum
            p3 = theEvent.particles[largestLeptonIndex].momentum
            p4 = theEvent.particles[largestAntiLeptonIndex].momentum
            ptMissing = theEvent.particles[missingIndex].momentum
            # 列表是4个动量的点乘(6个结果) + type1 + length1 + length2
            # type1 = 0, 1, 2, 3, 4, 5 对应SM, alpha0, 1, 2, 3, 4
            # length1是一次isolate forest的长度
            # length2是n次isolate forest的平均长度
            # momentumList = [ptMissing, p1 * p2, p1 * p3, p1 * p4, p2 * p3, p2 * p4, p3 * p4] + [tag, 0, 0]
            momentumList = [ptMissing.values[1], ptMissing.values[2]] + p1.values + p2.values + p3.values + p4.values + [tag, 0, 0]
            result = result + [momentumList]
        idx = idx + 1
    return result


def ChooseEvents3D(allEvents: EventSet, count: int, tag: int) -> list:
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
        missingIndex = -1
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
            elif theParticle.particleType == ParticleType.Missing:
                missingIndex = theParticle.index - 1
        if largestJetIndex >= 0 and secondJetIndex >= 0 \
                and largestLeptonIndex >= 0 and largestAntiLeptonIndex >= 0:
            p1 = theEvent.particles[largestJetIndex].momentum
            p2 = theEvent.particles[secondJetIndex].momentum
            p3 = theEvent.particles[largestLeptonIndex].momentum
            p4 = theEvent.particles[largestAntiLeptonIndex].momentum
            ptMissing = theEvent.particles[missingIndex].momentum
            # 列表是4个动量的点乘(6个结果) + type1 + length1 + length2
            # type1 = 0, 1, 2, 3, 4, 5 对应SM, alpha0, 1, 2, 3, 4
            # length1是一次isolate forest的长度
            # length2是n次isolate forest的平均长度
            # momentumList = [ptMissing, p1 * p2, p1 * p3, p1 * p4, p2 * p3, p2 * p4, p3 * p4] + [tag, 0, 0]
            momentumList = [ptMissing.Pt(), p1 * p2, p3 * p4] + [tag, 0, 0]
            result = result + [momentumList]
        idx = idx + 1
    return result


def ChooseEvents2D(allEvents: EventSet, count: int, tag: int) -> list:
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
        missingIndex = -1
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
            elif theParticle.particleType == ParticleType.Missing:
                missingIndex = theParticle.index - 1
        if largestJetIndex >= 0 and secondJetIndex >= 0 \
                and largestLeptonIndex >= 0 and largestAntiLeptonIndex >= 0:
            p1 = theEvent.particles[largestJetIndex].momentum
            p2 = theEvent.particles[secondJetIndex].momentum
            p3 = theEvent.particles[largestLeptonIndex].momentum
            p4 = theEvent.particles[largestAntiLeptonIndex].momentum
            ptMissing = theEvent.particles[missingIndex].momentum
            # 列表是4个动量的点乘(6个结果) + type1 + length1 + length2
            # type1 = 0, 1, 2, 3, 4, 5 对应SM, alpha0, 1, 2, 3, 4
            # length1是一次isolate forest的长度
            # length2是n次isolate forest的平均长度
            # momentumList = [ptMissing, p1 * p2, p1 * p3, p1 * p4, p2 * p3, p2 * p4, p3 * p4] + [tag, 0, 0]
            momentumList = [ptMissing.Pt(), p3 * p4] + [tag, 0, 0]
            result = result + [momentumList]
        idx = idx + 1
    return result


def ChooseEventsAll(fileName: str) -> list:
    allEvents = LoadLHCOlympics(fileName)
    result = []
    for theEvent in allEvents.events:
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
            p1 = theEvent.particles[largestJetIndex].momentum
            p2 = theEvent.particles[secondJetIndex].momentum
            p3 = theEvent.particles[largestLeptonIndex].momentum
            p4 = theEvent.particles[largestAntiLeptonIndex].momentum
            # 列表是4个动量的点乘(6个结果) + type1 + length1 + length2
            # type1 = 0, 1, 2, 3, 4, 5 对应SM, alpha0, 1, 2, 3, 4
            # length1是一次isolate forest的长度
            # length2是n次isolate forest的平均长度
            momentumList = [p1 * p2, p1 * p3, p1 * p4, p2 * p3, p2 * p4, p3 * p4] + [0, 0]
            result = result + [momentumList]
    print(fileName, "Loaded\n")
    return result


#########################################################
# 选事例的标准：两个 jet e+ e-(or muon+ muon-) and photon
#########################################################
def ChooseEventsAZ(allEvents: EventSet, count: int, tag: int) -> list:
    result = []
    idx = 0
    while len(result) < count:
        theEvent = allEvents.events[idx]
        largestJetIndex = -1  # 对于一个list, list[i] 这个i通常叫index
        largestJetEnergy = 0
        secondJetIndex = -1  # 对于一个list, list[i] 这个i通常叫index
        secondJetEnergy = 0
        largestElectronIndex = -1
        largestElectronEnergy = 0
        largestAntiElectronIndex = -1
        largestAntiElectronEnergy = 0
        largestMuonIndex = -1
        largestMuonEnergy = 0
        largestAntiMuonIndex = -1
        largestAntiMuonEnergy = 0
        largestPhotonIndex = -1
        largestPhotonEnergy = 0
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
                particleEnergy = theParticle.momentum.Momentum()
                if theParticle.PGDid > 0:
                    if theParticle.particleType == ParticleType.Electron:
                        if particleEnergy > largestElectronEnergy:
                            largestElectronEnergy = particleEnergy
                            largestElectronIndex = theParticle.index - 1
                    else:
                        if particleEnergy > largestMuonEnergy:
                            largestMuonEnergy = particleEnergy
                            largestMuonIndex = theParticle.index - 1
                else:
                    if theParticle.particleType == ParticleType.Electron:
                        if particleEnergy > largestAntiElectronEnergy:
                            largestAntiElectronEnergy = particleEnergy
                            largestAntiElectronIndex = theParticle.index - 1
                    else:
                        if particleEnergy > largestAntiMuonEnergy:
                            largestAntiMuonEnergy = particleEnergy
                            largestAntiMuonIndex = theParticle.index - 1
            elif theParticle.particleType == ParticleType.Photon:
                photonEnergy = theParticle.momentum.Momentum()
                if photonEnergy > largestPhotonEnergy:
                    largestPhotonEnergy = photonEnergy
                    largestPhotonIndex = theParticle.index - 1
        if largestJetIndex >= 0 and secondJetIndex >= 0 \
                and largestElectronIndex >= 0 and largestAntiElectronIndex > 0 and largestPhotonIndex >= 0:
            p1 = theEvent.particles[largestJetIndex].momentum
            p2 = theEvent.particles[secondJetIndex].momentum
            p3 = theEvent.particles[largestElectronIndex].momentum
            p4 = theEvent.particles[largestAntiElectronIndex].momentum
            p5 = theEvent.particles[largestPhotonIndex].momentum
            # length1是一次isolate forest的长度
            # length2是n次isolate forest的平均长度
            momentumList = [p1 * p2, p1 * p3, p1 * p4, p1 * p5, p2 * p3, p2 * p4, p2 * p5, p3 * p4, p3 * p5, p4 * p5] + [tag, 0, 0]
            result = result + [momentumList]
        elif largestJetIndex >= 0 and secondJetIndex >= 0 \
                and largestMuonIndex >= 0 and largestAntiMuonIndex > 0 and largestPhotonIndex >= 0:
            p1 = theEvent.particles[largestJetIndex].momentum
            p2 = theEvent.particles[secondJetIndex].momentum
            p3 = theEvent.particles[largestMuonIndex].momentum
            p4 = theEvent.particles[largestAntiMuonIndex].momentum
            p5 = theEvent.particles[largestPhotonIndex].momentum
            # length1是一次isolate forest的长度
            # length2是n次isolate forest的平均长度
            momentumList = [p1 * p2, p1 * p3, p1 * p4, p1 * p5, p2 * p3, p2 * p4, p2 * p5, p3 * p4, p3 * p5, p4 * p5] + [tag, 0, 0]
            result = result + [momentumList]
        idx = idx + 1
    print("ChooseEventsAZ Loaded\n")
    return result



#########################################################
# 选事例的标准：l+ l- and photon
#########################################################
def ChooseEventsNTGC(fileName: str, count: int, tag: int) -> list:
    allEvents = LoadLHCOlympics(fileName)
    result = []
    idx = 0
    while len(result) < count:
        theEvent = allEvents.events[idx]
        largestPhotonIndex = -1
        largestPhotonEnergy = 0
        largestElectronIndex = -1
        largestElectronEnergy = 0
        largestAntiElectronIndex = -1
        largestAntiElectronEnergy = 0
        largestMuonIndex = -1
        largestMuonEnergy = 0
        largestAntiMuonIndex = -1
        largestAntiMuonEnergy = 0
        for theParticle in theEvent.particles:
            if theParticle.particleType == ParticleType.Photon:
                photonEnergy = theParticle.momentum.Momentum()
                if photonEnergy > largestPhotonEnergy:
                    largestPhotonEnergy = photonEnergy
                    largestPhotonIndex = theParticle.index - 1
            elif theParticle.particleType == ParticleType.Electron:
                if theParticle.PGDid > 0:
                    electronEnergy = theParticle.momentum.Momentum()
                    if electronEnergy > largestElectronEnergy:
                        largestElectronEnergy = electronEnergy
                        largestElectronIndex = theParticle.index - 1
                else:
                    antiElectronEnergy = theParticle.momentum.Momentum()
                    if antiElectronEnergy > largestAntiElectronEnergy:
                        largestAntiElectronEnergy = antiElectronEnergy
                        largestAntiElectronIndex = theParticle.index - 1
            elif theParticle.particleType == ParticleType.Muon:
                if theParticle.PGDid > 0:
                    muonEnergy = theParticle.momentum.Momentum()
                    if muonEnergy > largestMuonEnergy:
                        largestMuonEnergy = electronEnergy
                        largestMuonIndex = theParticle.index - 1
                else:
                    antiMuonEnergy = theParticle.momentum.Momentum()
                    if antiMuonEnergy > largestAntiMuonEnergy:
                        largestAntiMuonEnergy = antiMuonEnergy
                        largestAntiMuonIndex = theParticle.index - 1
        p1 = LorentzVector(0, 0, 0, 0)
        p2 = LorentzVector(0, 0, 0, 0)
        p3 = LorentzVector(0, 0, 0, 0)
        foundParticles = True
        if largestPhotonIndex >= 0 and largestElectronIndex >= 0 and largestAntiElectronIndex >= 0:
            if largestMuonIndex >= 0 and largestAntiMuonIndex >= 0:
                if largestElectronEnergy + largestAntiElectronEnergy > largestMuonEnergy + largestAntiMuonEnergy:
                    p1 = theEvent.particles[largestElectronIndex].momentum
                    p2 = theEvent.particles[largestAntiElectronIndex].momentum
                    p3 = theEvent.particles[largestPhotonIndex].momentum
                else:
                    p1 = theEvent.particles[largestMuonIndex].momentum
                    p2 = theEvent.particles[largestAntiMuonIndex].momentum
                    p3 = theEvent.particles[largestPhotonIndex].momentum
            else:
                p1 = theEvent.particles[largestElectronIndex].momentum
                p2 = theEvent.particles[largestAntiElectronIndex].momentum
                p3 = theEvent.particles[largestPhotonIndex].momentum
        elif largestPhotonIndex >= 0 and largestMuonIndex >= 0 and largestAntiMuonIndex >= 0:
            p1 = theEvent.particles[largestMuonIndex].momentum
            p2 = theEvent.particles[largestAntiMuonIndex].momentum
            p3 = theEvent.particles[largestPhotonIndex].momentum
        else:
            foundParticles = False
        if foundParticles:
            momentumList = p1.values + p2.values + p3.values + [tag, 0, 0]
            result = result + [momentumList]
        idx = idx + 1
    print(fileName, "Loaded\n")
    return result
