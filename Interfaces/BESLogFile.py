from DataStructure.EventSet import *
from DataStructure.Particles import *


def LoadBESCIII(fileName: str) -> EventSet:
    bFirstLine = True
    with open(fileName) as f:
        ret = EventSet()
        for lines in f.readlines():
            if bFirstLine:
                bFirstLine = False
                continue
            if 17 != len(lines.split()):
                print("line have no 17 element: " + lines)
                continue
            valueList = lines.split()
            oneEvent = EventSample()
            p1 = LorentzVector(float(valueList[4]), float(valueList[1]), float(valueList[2]), float(valueList[3]))
            p2 = LorentzVector(float(valueList[8]), float(valueList[5]), float(valueList[6]), float(valueList[7]))
            p3 = LorentzVector(float(valueList[12]), float(valueList[9]), float(valueList[10]), float(valueList[11]))
            p4 = LorentzVector(float(valueList[16]), float(valueList[13]), float(valueList[14]), float(valueList[15]))
            proton = Particle(
                0,  # index
                1,  # PGD
                ParticleType.Jet,  # Particle Type
                ParticleStatus.Outgoing,  # Status
                p1,
                p1.Mass(),  # Mass
                0.0,  # Decay Length
                0.0  # Hecility
            )
            antipion = Particle(
                1,  # index
                -2,  # PGD
                ParticleType.Jet,  # Particle Type
                ParticleStatus.Outgoing,  # Status
                p2,
                p2.Mass(),  # Mass
                0.0,  # Decay Length
                0.0  # Hecility
            )
            antiproton = Particle(
                2,  # index
                -1,  # PGD
                ParticleType.Jet,  # Particle Type
                ParticleStatus.Outgoing,  # Status
                p3,
                p3.Mass(),  # Mass
                0.0,  # Decay Length
                0.0  # Hecility
            )
            pion = Particle(
                3,  # index
                2,  # PGD
                ParticleType.Jet,  # Particle Type
                ParticleStatus.Outgoing,  # Status
                p4,
                p4.Mass(),  # Mass
                0.0,  # Decay Length
                0.0  # Hecility
            )
            oneEvent.AddParticle(proton)
            oneEvent.AddParticle(antipion)
            oneEvent.AddParticle(antiproton)
            oneEvent.AddParticle(pion)
            ret.AddEvent(oneEvent)
        return ret
