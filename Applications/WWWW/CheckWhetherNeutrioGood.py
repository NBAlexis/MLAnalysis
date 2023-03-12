import os

from Applications.WWWW.Filters import V4Dot
from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType, ParticleStatus
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../")


def TwoW(eventSample: EventSample) -> [bool, float]:
    ltall = LorentzVector(0, 0, 0, 0)
    wfound = 0
    for particle in eventSample.particles:
        if ParticleType.Intermediate == particle.particleType and 24 == abs(particle.PGDid):
            ltall = ltall + particle.momentum
            wfound = wfound + 1
    if 2 == wfound:
        return [True, ltall.Mass()]
    return [False, 0.0]


def FindNeutrinos(eventSample: EventSample) -> [bool, float]:
    pl = LorentzVector(0, 0, 0, 0)
    pm = LorentzVector(0, 0, 0, 0)
    plpgd = 0
    pmpgd = 0
    lepCount = 0
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status:
            if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
                lepCount = lepCount + 1
                if particle.PGDid > 0:
                    pm = particle.momentum
                    pmpgd = particle.PGDid
                else:
                    pl = particle.momentum
                    plpgd = particle.PGDid
    # find the closest nu
    if 0 == plpgd or 0 == pmpgd or 2 != lepCount:
        print("lepton not found!")
        print(eventSample.DebugPrint())
        return [False, 0.0]
    pnvp = LorentzVector(0, 0, 0, 0)
    pnvm = LorentzVector(0, 0, 0, 0)
    maxDot1 = -2
    maxDot2 = -2
    nupgd = 0
    nubarpgd = 0
    nuCount = 0
    missingAll = LorentzVector(0, 0, 0, 0)
    for particle in eventSample.particles:
        if ParticleStatus.Invisible == particle.status:
            nuCount = nuCount + 1
            missingAll = missingAll + particle.momentum
            if particle.PGDid > 0 and 1 == particle.PGDid + plpgd:
                dotlm = V4Dot(pl, particle.momentum)
                if dotlm > maxDot1:
                    maxDot1 = dotlm
                    pnvp = particle.momentum
                    nupgd = particle.PGDid
            elif particle.PGDid < 0 and -1 == particle.PGDid + pmpgd:
                dotlm = V4Dot(pm, particle.momentum)
                if dotlm > maxDot2:
                    maxDot2 = dotlm
                    pnvm = particle.momentum
                    nubarpgd = particle.PGDid
    # cosll = V4Dot(pl, pm)
    if 0 == nupgd or 0 == nubarpgd or 4 != nuCount:
        print("neutrino not found!")
        print(eventSample.DebugPrint())
        return [False, 0.0]
    return [True, (pl + pm + pnvp + pnvm).Mass()]


s0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/s0at30.lhe")

print("s0 loaded!")

msq = 0.0
msqcount = 0
mismatch = 0
for eventsample in s0.events:
    [hasw, shat] = TwoW(eventsample)
    if hasw:
        [hasn, shat2] = FindNeutrinos(eventsample)
        if hasn:
            print("shat a = {}, b = {}", shat, shat2)
            msq = msq + (shat - shat2) * (shat - shat2)
            msqcount = msqcount + 1
            if abs(shat - shat2) > 0.1:
                mismatch = mismatch + 1

print(msqcount)
print(mismatch)
print(msq / msqcount)
