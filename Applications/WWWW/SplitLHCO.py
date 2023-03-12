import os

from Applications.WWWW.Filters import NvInvCut
from CutAndExport.CutEvent import CutEvents
from DataStructure import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleStatus, ParticleType
from Interfaces.LHCOlympics import SaveToLHCO
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent


class FinalStateCut:

    def __init__(self, mode: int):
        self.mode = mode

    def Cut(self, eventSample: EventSample) -> bool:
        """
        mode = 0: e+, e-
        mode = 1: e+, mu- or e-, mu+
        mode = 2: mu+, mu-
        """
        lepton1 = 0
        lepton2 = 0
        for particle in eventSample.particles:
            if particle.status == ParticleStatus.Outgoing:
                if particle.particleType == ParticleType.Electron:
                    if 0 == lepton1:
                        lepton1 = 1
                    else:
                        lepton2 = 1
                if particle.particleType == ParticleType.Muon:
                    if 0 == lepton1:
                        lepton1 = 2
                    else:
                        lepton2 = 2
        mode = 0
        if lepton1 != lepton2:
            mode = 1
        elif lepton1 == 2:
            mode = 2
        return mode != self.mode


class VBSTriboson:

    def __init__(self, mode: int):
        self.mode = mode

    def Cut(self, eventSample: EventSample) -> bool:
        for particle in eventSample.particles:
            if particle.status != ParticleStatus.Outgoing and particle.status != ParticleStatus.Incoming:
                if particle.PGDid == 23 or particle.PGDid == -23:
                    return True if 0 == self.mode else False
        return False if 0 == self.mode else True


os.chdir("../../")
# s0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/s0at30.lhe")
# m0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/m0at30.lhe")
# t0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/s0at3.lhe")
# s0cp = s0.GetCopy()
# m0cp = m0.GetCopy()
# t0cp = t0.GetCopy()

cuttriboson = NvInvCut(1)
cutvbs = NvInvCut(0)
# cuttriboson = VBSTriboson(1)
# cutvbs = VBSTriboson(0)
eecut = FinalStateCut(0)
emcut = FinalStateCut(1)
mmcut = FinalStateCut(2)

"""
# for file in ["s0at3", "s0at10", "s0at14", "s0at30", "m0at3", "m0at10", "m0at14", "m0at30", "t0at3", "t0at10", "t0at14", "t0at30", "s1at3", "s1at10", "s1at14", "s1at30", "s2at3", "s2at10", "s2at14", "s2at30"]:
for file in ["s1at30", "s2at30"]:
    events = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/{}.lhe".format(file))
    eventscp1 = events.GetCopy()
    CutEvents(events, cutvbs)
    CutEvents(eventscp1, cuttriboson)
    eventsEEVBS = events.GetCopy()
    eventsEMVBS = events.GetCopy()
    eventsMMVBS = events.GetCopy()
    eventsEETB = eventscp1.GetCopy()
    eventsEMTB = eventscp1.GetCopy()
    eventsMMTB = eventscp1.GetCopy()
    CutEvents(eventsEEVBS, eecut)
    CutEvents(eventsEETB, eecut)
    CutEvents(eventsEMVBS, emcut)
    CutEvents(eventsEMTB, emcut)
    CutEvents(eventsMMVBS, mmcut)
    CutEvents(eventsMMTB, mmcut)
    print([eventsEEVBS.GetEventCount(), eventsEETB.GetEventCount(), eventsEMVBS.GetEventCount(),
           eventsEMTB.GetEventCount(), eventsMMVBS.GetEventCount(), eventsMMTB.GetEventCount()])

"""

"""

for file in ["m0at30", "t0at30"]:
    events = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/{}.lhe".format(file))
    eventscp1 = events.GetCopy()
    CutEvents(events, cutvbs)
    CutEvents(eventscp1, cuttriboson)
    eventsEEVBS = events.GetCopy()
    eventsEMVBS = events.GetCopy()
    eventsMMVBS = events.GetCopy()
    eventsEETB = eventscp1.GetCopy()
    eventsEMTB = eventscp1.GetCopy()
    eventsMMTB = eventscp1.GetCopy()
    CutEvents(eventsEEVBS, eecut)
    CutEvents(eventsEETB, eecut)
    CutEvents(eventsEMVBS, emcut)
    CutEvents(eventsEMTB, emcut)
    CutEvents(eventsMMVBS, mmcut)
    CutEvents(eventsMMTB, mmcut)
    SaveToLHCO("_DataFolder/WWWW/LHE/{}eevbs.lhco".format(file), eventsEEVBS)
    SaveToLHCO("_DataFolder/WWWW/LHE/{}eetb.lhco".format(file), eventsEETB)
    SaveToLHCO("_DataFolder/WWWW/LHE/{}emvbs.lhco".format(file), eventsEMVBS)
    SaveToLHCO("_DataFolder/WWWW/LHE/{}emtb.lhco".format(file), eventsEMTB)
    SaveToLHCO("_DataFolder/WWWW/LHE/{}mmvbs.lhco".format(file), eventsMMVBS)
    SaveToLHCO("_DataFolder/WWWW/LHE/{}mmtb.lhco".format(file), eventsMMTB)

"""

# CutEvents(s0, cuttriboson)
# CutEvents(m0, cuttriboson)
# CutEvents(t0, cuttriboson)

# print(s0.GetEventCount())
# print(m0.GetEventCount())
# print(t0.GetEventCount())

# SaveToLHCO("_DataFolder/WWWW/LHE/s0triboson30.lhe", s0)
# SaveToLHCO("_DataFolder/WWWW/LHE/m0triboson30.lhe", m0)
# SaveToLHCO("_DataFolder/WWWW/LHE/t0triboson10.lhe", t0)

# CutEvents(s0cp, cutvbs)
# CutEvents(m0cp, cutvbs)
# CutEvents(t0cp, cutvbs)

# print(s0cp.GetEventCount())
# print(m0cp.GetEventCount())
# print(t0cp.GetEventCount())

# SaveToLHCO("_DataFolder/WWWW/LHE/s0vbs30.lhe", s0cp)
# SaveToLHCO("_DataFolder/WWWW/LHE/m0vbs30.lhe", m0cp)
# SaveToLHCO("_DataFolder/WWWW/LHE/t0vbs10.lhe", t0cp)

"""

s0
[221159, 8392, 422774, 64443, 201168, 82064]
[245313, 190, 491326, 8533, 245586, 9052]
[247880, 191, 495640, 4381, 247283, 4625]
[249610, 33, 499114, 1011, 249245, 987]

m0
[124140, 125598, 245471, 198180, 120851, 185760]
[180000, 59287, 359298, 125864, 179300, 96251]
[189017, 51286, 377381, 110214, 188980, 83122]
[203450, 38207, 408711, 83024, 204094, 62514]

t0
[125563, 94736, 249533, 196877, 122531, 210760]
[175374, 39608, 350843, 128791, 175123, 130261]
[183361, 33363, 367034, 115310, 183911, 117021]
[196644, 24491, 394795, 92246, 198109, 93715]


s1-30:
[250082, 39, 499650, 184, 249845, 200]
s2-30:
[249522, 16, 499566, 388, 250080, 428]


"""
