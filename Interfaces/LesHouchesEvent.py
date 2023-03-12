from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
import xml.etree.ElementTree as ElementTree

from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import Particle, ParticleStatus, ParticleType


def GetParticleType(PDGid: int) -> ParticleType:
    absId = abs(PDGid)
    if 1 <= absId <= 8:  # quarks
        return ParticleType.Jet
    if 12 == absId or 14 == absId or 16 == absId or 18 == absId:  # neutrino
        return ParticleType.Missing
    if 11 == absId:
        return ParticleType.Electron
    if 13 == absId:
        return ParticleType.Muon
    if 15 == absId:
        return ParticleType.Tau
    if 22 == absId:
        return ParticleType.Photon
    return ParticleType.Intermediate


# the format is:
# <event>
# NUP IDPRUP XWGTUP SCALUP AQEDUP AQCDUP
# IDUP(1) ISTUP(1) MOTHUP(1,1) MOTHUP(2,1) ICOLUP(1,1) ICOLUP(2,1) PUP(1,1) PUP(2,1) PUP(3,1) PUP(4,1) PUP(5,1) VTIMUP SPINUP
# IDUP(2) ISTUP(2) MOTHUP(1,2) MOTHUP(2,2) ICOLUP(1,2) ICOLUP(2,2) PUP(1,2) PUP(2,2) PUP(3,2) PUP(4,2) PUP(5,2) VTIMUP SPINUP
# ...
# In total 1+NUP lines after the <event> tag
# Additional
# information
# </event>
# ------------------------------------
# NUP = is number of particle
# IDPRUP = A single process identifier (always 1?)
# XWGTUP = event weight (same for all?)
# SCALUP = (energy?) scale of the event in GeV, as used for calculation of PDFs
# AQEDUP = coupling constant of QED
# AQCDUP = coupling constant of QCD
# ------------------------------------
# IDUP = using the standard PDG numbering
# ISTUP = status code
#   –1 Incoming particle
#   +1 Outgoing final state particle
#   –2 Intermediate space-like propagator defining an x and Q2 which should be preserved
#   +2 Intermediate resonance, Mass should be preserved
#   +3 Intermediate resonance, for documentation only4
#   –9 Incoming beam particles at time t = −INFINITY
# MOTHUP(2) = two mother(s), it seems only particle from MadSpin will have mothers
# ICOLIP(2) = integer tag for the color flow line passing through the color of the particle
#      To avoid confusion it is recommended that integer tags larger than MAXNUP (i.e. 500) are
#      used. The actual value of the tag has no meaning beyond distinguishing the lines in a given
#      process.
# PUP(5) = lab frame momentum (Px, Py, Pz, E, M) of particle in GeV
# VTIMUP = invariant lifetime cτ (distance from production to decay) in mm (only none zero with T.O.F.)
# SPINUP = cosine of the angle between the spin-vector of particle I and the 3-momentum of the decaying particle, specified in the lab frame
# ------------------------------------
# An example:
# <event>
# 10      1 +1.0631935e-01 1.54148500e+02 7.54677100e-03 1.19546600e-01
#         2 -1    0    0  502    0 +0.00000000000e+00 +0.00000000000e+00 +5.06195596080e+02  5.06195596080e+02  0.00000000000e+00 0.0000e+00 -1.0000e+00
#        -2 -1    0    0    0  501 +0.00000000000e+00 +0.00000000000e+00 -9.18941519700e+01  9.18941519700e+01  0.00000000000e+00 0.0000e+00 1.0000e+00
#         1  1    1    2  502    0 -3.25610199539e+01 +2.78859698866e+01 +1.04436913544e+01  4.41238940491e+01  0.00000000000e+00 0.0000e+00 1.0000e+00
#        -1  1    1    2    0  501 -4.19730837895e+01 -8.43890807914e+00 +8.78535352555e+00  4.37051183380e+01  0.00000000000e+00 0.0000e+00 -1.0000e+00
#        24  2    1    2    0    0 +6.05686503397e+01 -1.35988776738e+02 +2.78724441182e+02  3.26198715508e+02  8.09739407687e+01 0.0000e+00 0.0000e+00
#       -11  1    5    5    0    0 +1.56214611745e+01 -1.54470714120e+00 +2.73839975178e+00  1.59347106211e+01  0.00000000000e+00 0.0000e+00 1.0000e+00
#        12  1    5    5    0    0 +4.49471891653e+01 -1.34444069597e+02 +2.75986041431e+02  3.10264004886e+02  0.00000000000e+00 0.0000e+00 -1.0000e+00
#       -24  2    1    2    0    0 +1.39654534036e+01 +1.16541714931e+02 +1.16347958048e+02  1.84062020155e+02  8.10245315572e+01 0.0000e+00 0.0000e+00
#        13  1    8    8    0    0 -7.72086439890e+00 +1.03281655382e+02 +1.19852642754e+02  1.58402550676e+02  0.00000000000e+00 0.0000e+00 -1.0000e+00
#       -14  1    8    8    0    0 +2.16863178025e+01 +1.32600595486e+01 -3.50468470660e+00  2.56594694792e+01  0.00000000000e+00 0.0000e+00 1.0000e+00
# <mgrwt>
# <rscale>  2 0.15414845E+03</rscale>
# <asrwt>0</asrwt>
# <pdfrwt beam="1">  1        2 0.77876244E-01 0.15414845E+03</pdfrwt>
# <pdfrwt beam="2">  1       -2 0.14137562E-01 0.15414845E+03</pdfrwt>
# <totfact> 0.22799232E+03</totfact>
# </mgrwt>
# </event>


def SetLeptonNTrack(pgdid: int) -> float:
    if 11 == pgdid:
        return -1.0
    if 13 == pgdid:
        return -1.0
    if 15 == pgdid:
        return -1.0
    if -11 == pgdid:
        return 1.0
    if -13 == pgdid:
        return 1.0
    if -15 == pgdid:
        return 1.0
    return 0.0

def LoadLesHouchesEvent(fileName: str) -> EventSet:
    ret = EventSet()
    tree = ElementTree.parse(fileName)
    root = tree.getroot()
    for child in root:
        if child.tag == 'event':
            lines = child.text.strip().split('\n')
            event_header = lines[0].strip()
            num_part = int(event_header.split()[0].strip())
            oneEvent = EventSample()
            for i in range(1, num_part + 1):
                part_data = lines[i].strip().split()
                pdgId: int = int(part_data[0])
                statusCode: int = int(part_data[1])
                particleType = ParticleType.Intermediate if -2 == statusCode or 2 == statusCode or -3 == statusCode else GetParticleType(pdgId)
                oneParticle = Particle(
                    i,  # index
                    pdgId,  # PGD
                    particleType,  # Particle Type
                    ParticleStatus.Invisible if ParticleType.Missing == particleType else ParticleStatus(statusCode),  # Status
                    LorentzVector(float(part_data[9]), float(part_data[6]), float(part_data[7]), float(part_data[8])),  # Momentum
                    float(part_data[10]),  # Mass
                    float(part_data[11]),  # Decay Length
                    float(part_data[12])   # Hecility
                )
                oneParticle.nTrack = SetLeptonNTrack(oneParticle.PGDid)
                oneEvent.AddParticle(oneParticle)
            ret.AddEvent(oneEvent)
    return ret


def LoadLargeLesHouchesEvent(fileName: str, debugCount: bool) -> EventSet:
    ret = EventSet()
    fileContent = open(fileName, 'r')
    nextLine = fileContent.readline()
    oneBlock = False
    lines = []
    eventCount = 1
    while nextLine:
        if nextLine.startswith('<event>') and not oneBlock:
            oneBlock = True
            lines = []
        elif nextLine.startswith('</event>') and oneBlock:
            oneBlock = False
            if len(lines) > 0:
                event_header = lines[0].strip()
                num_part = int(event_header.split()[0].strip())
                oneEvent = EventSample()
                if debugCount:
                    print("Add event", eventCount, num_part, "particles")
                    eventCount = eventCount + 1
                for i in range(1, num_part + 1):
                    part_data = lines[i].strip().split()
                    pdgId: int = int(part_data[0])
                    statusCode: int = int(part_data[1])
                    particleType = ParticleType.Intermediate if -2 == statusCode or 2 == statusCode or -3 == statusCode else GetParticleType(pdgId)
                    oneParticle = Particle(
                        i,  # index
                        pdgId,  # PGD
                        particleType,  # Particle Type
                        ParticleStatus.Invisible if ParticleType.Missing == particleType else ParticleStatus(statusCode),  # Status
                        LorentzVector(float(part_data[9]), float(part_data[6]), float(part_data[7]), float(part_data[8])),  # Momentum
                        float(part_data[10]),  # Mass
                        float(part_data[11]),  # Decay Length
                        float(part_data[12])   # Hecility
                    )
                    oneParticle.nTrack = SetLeptonNTrack(oneParticle.PGDid)
                    oneEvent.AddParticle(oneParticle)
                ret.AddEvent(oneEvent)
        elif oneBlock:
            lines.append(nextLine)
        nextLine = fileContent.readline()
    return ret

