from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import Particle, ParticleStatus, ParticleType


def GetPGDIdByType(particleType: int, nTrack: float) -> int:
    if 0 == particleType:
        return 22
    if 6 == particleType:
        return 12
    if nTrack > 0.0:
        if 1 == particleType:
            return -11
        if 2 == particleType:
            return -13
        if 3 == particleType:
            return -15
    else:
        if 1 == particleType:
            return 11
        if 2 == particleType:
            return 13
        if 3 == particleType:
            return 15
    return 1


def LoadLHCOlympics(fileName: str) -> EventSet:
    ret = EventSet()
    oneEvent = None
    particleIndex = 0
    with open(fileName) as f:
        for lines in f.readlines():
            if lines.strip()[0] == "#":  # this is a comment line
                continue
            valueList = lines.split()
            if 3 == len(valueList):
                if oneEvent is None:  # first record
                    oneEvent = EventSample()
                    particleIndex = 0
                else:
                    ret.AddEvent(oneEvent)
                    oneEvent = EventSample()
                    particleIndex = 0
            elif 11 == len(valueList):
                if oneEvent is None:
                    print("File {} has problem! The first line should be a start record!\n".format(fileName))
                    oneEvent = EventSample()
                    particleIndex = 0
                particleIndex += 1
                if particleIndex != int(valueList[0]):
                    print("File {} has problem! he particle Index is wrong!\n".format(fileName))
                nTrack = float(valueList[6])
                particleType = int(valueList[1])
                oneParticle = Particle(
                    particleIndex,  # index
                    GetPGDIdByType(particleType, nTrack),  # PGD
                    ParticleType(particleType),  # Particle Type
                    ParticleStatus.Invisible if 6 == particleType else ParticleStatus.Outgoing,  # Status
                    LorentzVector.MakeWithRapidity(float(valueList[2]), float(valueList[3]), float(valueList[4]), float(valueList[5])),  # Momentum
                    float(valueList[5]),  # Mass
                    0.0,  # Decay Length
                    0.0  # Hecility
                )
                oneParticle.SetLHCOOtherInfo(float(valueList[6]), float(valueList[7]), float(valueList[8]))
                oneEvent.AddParticle(oneParticle)
            else:
                print("File {} has problem! This line is either 3 value nor 11 value: {}\n".format(fileName, lines))
        if not (oneEvent is None):
            ret.AddEvent(oneEvent)
    return ret


def LHCOPutSpaces(contents: str, length: int) -> str:
    for i in range(len(contents), length):
        contents = " " + contents
    return contents


def LHCOParticleTypeNumber(particleType: ParticleType) -> int:
    if particleType == ParticleType.Electron:
        return 1
    elif particleType == ParticleType.Photon:
        return 0
    elif particleType == ParticleType.Muon:
        return 2
    elif particleType == ParticleType.Jet:
        return 4
    elif particleType == ParticleType.Tau:
        return 3
    elif particleType == ParticleType.Intermediate:
        return 5
    # Missing
    return 6


def SaveToLHCO(fileName: str, event: EventSet, realLHCO: bool = True):
    result_f = open(fileName, 'w')
    columnLength = [4, 6, 9, 9, 9, 9, 7, 7, 8, 7, 7]
    line = LHCOPutSpaces("#", columnLength[0])
    line = line + LHCOPutSpaces("typ", columnLength[1])
    line = line + LHCOPutSpaces("eta", columnLength[2])
    line = line + LHCOPutSpaces("phi", columnLength[3])
    line = line + LHCOPutSpaces("pt", columnLength[4])
    line = line + LHCOPutSpaces("jmas", columnLength[5])
    line = line + LHCOPutSpaces("ntrk", columnLength[6])
    line = line + LHCOPutSpaces("btag", columnLength[7])
    line = line + LHCOPutSpaces("had/em", columnLength[8])
    line = line + LHCOPutSpaces("dum1", columnLength[9])
    line = line + LHCOPutSpaces("dum2", columnLength[10])
    result_f.write("{}\n".format(line))
    eventIdx: int = 0
    for eventSample in event.events:
        line = LHCOPutSpaces("0", columnLength[0])
        line = line + LHCOPutSpaces(str(eventIdx), columnLength[1] + columnLength[2])
        line = line + LHCOPutSpaces("0", columnLength[3])
        result_f.write("{}\n".format(line))
        eventIdx = eventIdx + 1
        particleIdx: int = 1
        missingMomentum = LorentzVector(0, 0, 0, 0)
        for particle in eventSample.particles:
            if realLHCO:
                if particle.status != ParticleStatus.Outgoing:
                    if particle.status == ParticleStatus.Invisible:
                        missingMomentum = missingMomentum + particle.momentum
                    continue
            line = LHCOPutSpaces(str(particleIdx), columnLength[0])
            particleIdx = particleIdx + 1
            line = line + LHCOPutSpaces(str(LHCOParticleTypeNumber(particle.particleType)), columnLength[1])
            line = line + LHCOPutSpaces('{:.3f}'.format(particle.momentum.PseudoRapidity()), columnLength[2])
            line = line + LHCOPutSpaces('{:.3f}'.format(particle.momentum.Azimuth()), columnLength[3])
            line = line + LHCOPutSpaces('{:.2f}'.format(particle.momentum.Pt()), columnLength[4])
            line = line + LHCOPutSpaces('{:.2f}'.format(particle.momentum.Mass()), columnLength[5])
            line = line + LHCOPutSpaces('{:.1f}'.format(particle.nTrack), columnLength[6])
            line = line + LHCOPutSpaces('{:.1f}'.format(particle.bTag), columnLength[7])
            line = line + LHCOPutSpaces('{:.2f}'.format(particle.hadEm), columnLength[8])
            line = line + LHCOPutSpaces('0.0', columnLength[9])
            line = line + LHCOPutSpaces('0.0', columnLength[10])
            result_f.write("{}\n".format(line))
        if realLHCO:
            line = LHCOPutSpaces(str(particleIdx), columnLength[0])
            line = line + LHCOPutSpaces(str(LHCOParticleTypeNumber(ParticleType.Missing)), columnLength[1])
            line = line + LHCOPutSpaces('{:.3f}'.format(missingMomentum.PseudoRapidity()), columnLength[2])
            line = line + LHCOPutSpaces('{:.3f}'.format(missingMomentum.Azimuth()), columnLength[3])
            line = line + LHCOPutSpaces('{:.2f}'.format(missingMomentum.Pt()), columnLength[4])
            line = line + LHCOPutSpaces('{:.2f}'.format(missingMomentum.Mass()), columnLength[5])
            line = line + LHCOPutSpaces('{:.1f}'.format(0), columnLength[6])
            line = line + LHCOPutSpaces('{:.1f}'.format(0), columnLength[7])
            line = line + LHCOPutSpaces('{:.2f}'.format(0), columnLength[8])
            line = line + LHCOPutSpaces('0.0', columnLength[9])
            line = line + LHCOPutSpaces('0.0', columnLength[10])
            result_f.write("{}\n".format(line))
    result_f.close()

