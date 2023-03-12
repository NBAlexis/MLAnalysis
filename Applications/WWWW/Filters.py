import math

from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleStatus, ParticleType


def V4Dot(p1: LorentzVector, p2: LorentzVector) -> float:
    lpl = p1.values[1] * p1.values[1] + p1.values[2] * p1.values[2] + p1.values[3] * p1.values[3]
    lpm = p2.values[1] * p2.values[1] + p2.values[2] * p2.values[2] + p2.values[3] * p2.values[3]
    denorm = lpl * lpm
    if denorm <= 0:
        return 0
    return (p1.values[1] * p2.values[1] + p1.values[2] * p2.values[2] + p1.values[3] * p2.values[3]) / math.sqrt(denorm)


def IsVBS(event: EventSample) -> bool:
    nmu = 1
    nmubar = 1
    ne = 0
    nebar = 0
    ntau = 0
    ntaubar = 0
    nnmu = 0
    nnmubar = 0
    nne = 0
    nnebar = 0
    nntau = 0
    nntaubar = 0
    for particle in event.particles:
        if ParticleStatus.Outgoing == particle.status:
            if 11 == particle.PGDid:
                nebar = nebar + 1
            elif -11 == particle.PGDid:
                ne = ne + 1
            elif 13 == particle.PGDid:
                nmubar = nmubar + 1
            elif -13 == particle.PGDid:
                nmu = nmu + 1
        elif ParticleStatus.Invisible == particle.status:
            if 12 == particle.PGDid:
                nne = nne + 1
            elif -12 == particle.PGDid:
                nnebar = nnebar + 1
            elif 14 == particle.PGDid:
                nnmu = nnmu + 1
            elif -14 == particle.PGDid:
                nnmubar = nnmubar + 1
            elif 16 == particle.PGDid:
                nntau = nntau + 1
            elif -16 == particle.PGDid:
                nntaubar = nntaubar + 1
    if ne != nne or nebar != nnebar or nmu != nnmu or nmubar != nnmubar or ntau != nntau or ntaubar != nntaubar:
        return False
    pnv1 = LorentzVector(0, 0, 0, 0)
    pnv2 = LorentzVector(0, 0, 0, 0)
    pnvbar1 = LorentzVector(0, 0, 0, 0)
    pnvbar2 = LorentzVector(0, 0, 0, 0)
    pgdidnv1 = 0
    pgdidnv2 = 0
    pgdidnvbar1 = 0
    pgdidnvbar2 = 0
    bnv1found = False
    bnvbar1found = False
    for particle in event.particles:
        if particle.PGDid == 12 or particle.PGDid == 14 or particle.PGDid == 16:
            if bnv1found:
                pnv2 = particle.momentum
                pgdidnv2 = particle.PGDid
            else:
                pnv1 = particle.momentum
                pgdidnv1 = particle.PGDid
                bnv1found = True
        elif particle.PGDid == -12 or particle.PGDid == -14 or particle.PGDid == -16:
            if bnvbar1found:
                pnvbar2 = particle.momentum
                pgdidnvbar2 = particle.PGDid
            else:
                pnvbar1 = particle.momentum
                pgdidnvbar1 = particle.PGDid
                bnvbar1found = True
    m1 = abs((pnv1 + pnvbar1).Mass() - 91.1876) if 0 == pgdidnv1 + pgdidnvbar1 else 300000
    m2 = abs((pnv1 + pnvbar2).Mass() - 91.1876) if 0 == pgdidnv1 + pgdidnvbar2 else 300000
    m3 = abs((pnv2 + pnvbar2).Mass() - 91.1876) if 0 == pgdidnv2 + pgdidnvbar2 else 300000
    m4 = abs((pnv2 + pnvbar1).Mass() - 91.1876) if 0 == pgdidnv2 + pgdidnvbar1 else 300000
    minM = min(m1, m2, m3, m4)
    return minM > 15


class NvInvCut:

    def __init__(self, mode: int):
        self.mode = mode

    def Cut(self, eventSample: EventSample) -> bool:
        vbs = IsVBS(eventSample)
        if not vbs:
            return True if 0 == self.mode else False
        return False if 0 == self.mode else True


def ExportEvent(eventSet: EventSet, debugCount: bool = True) -> [list, list]:
    saveList1 = []
    saveList2 = []
    count = 0
    evenOdd = False
    for event in eventSet.events:
        count = count + 1
        if debugCount and 0 == (count % 10000):
            print("{} / {}".format(count, eventSet.GetEventCount()))
        isvbs = IsVBS(event)
        if not isvbs:
            continue
        evenOdd = not evenOdd
        pl = LorentzVector(0, 0, 0, 0)
        pm = LorentzVector(0, 0, 0, 0)
        plpgd = 0
        pmpgd = 0
        lepCount = 0
        for particle in event.particles:
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
            print(event.DebugPrint())
            continue
        pnvp = LorentzVector(0, 0, 0, 0)
        pnvm = LorentzVector(0, 0, 0, 0)
        maxDot1 = -2
        maxDot2 = -2
        nupgd = 0
        nubarpgd = 0
        nuCount = 0
        missingAll = LorentzVector(0, 0, 0, 0)
        for particle in event.particles:
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
            print(event.DebugPrint())
            continue
        shat = (pl + pm + pnvp + pnvm).Mass()
        if evenOdd:
            saveList1.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                              pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                              missingAll.values[0], missingAll.values[1], missingAll.values[2], missingAll.values[3],
                              shat, abs(pmpgd) - 11, abs(plpgd) - 11])
        else:
            saveList2.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                              pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                              missingAll.values[0], missingAll.values[1], missingAll.values[2], missingAll.values[3],
                              shat, abs(pmpgd) - 11, abs(plpgd) - 11])
    return [saveList1, saveList2]


def ExportEventWithCount(eventSet: EventSet, countMax: int) -> [list, list]:
    saveList1 = []
    saveList2 = []
    count = 0
    savedcount = 0
    evenOdd = False
    for event in eventSet.events:
        count = count + 1
        print("{} / {}".format(count, eventSet.GetEventCount()))
        isvbs = IsVBS(event)
        if not isvbs:
            continue
        savedcount = savedcount + 1
        if savedcount > countMax:
            break
        evenOdd = not evenOdd
        pl = LorentzVector(0, 0, 0, 0)
        pm = LorentzVector(0, 0, 0, 0)
        plpgd = 0
        pmpgd = 0
        lepCount = 0
        for particle in event.particles:
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
            print(event.DebugPrint())
            continue
        pnvp = LorentzVector(0, 0, 0, 0)
        pnvm = LorentzVector(0, 0, 0, 0)
        maxDot1 = -2
        maxDot2 = -2
        nupgd = 0
        nubarpgd = 0
        nuCount = 0
        missingAll = LorentzVector(0, 0, 0, 0)
        for particle in event.particles:
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
            print(event.DebugPrint())
            continue
        shat = (pl + pm + pnvp + pnvm).Mass()
        if evenOdd:
            saveList1.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                              pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                              missingAll.values[0], missingAll.values[1], missingAll.values[2], missingAll.values[3],
                              shat, abs(pmpgd) - 11, abs(plpgd) - 11])
        else:
            saveList2.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                              pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                              missingAll.values[0], missingAll.values[1], missingAll.values[2], missingAll.values[3],
                              shat, abs(pmpgd) - 11, abs(plpgd) - 11])
    return [saveList1, saveList2]


def ExportEventLHCO(eventSet: EventSet, debugCount: bool = True) -> [list, list]:
    saveList = []
    count = 0
    for event in eventSet.events:
        count = count + 1
        if debugCount and 0 == (count % 10000):
            print("{} / {}".format(count, eventSet.GetEventCount()))
        event.RecalculateMissing(LorentzVector(30000, 0, 0, 0))
        largest1 = -1
        largest2 = -1
        largeste1 = -1
        largeste2 = -1
        missing = -1
        for particle in event.particles:
            if ParticleType.Muon == particle.particleType or ParticleType.Electron == particle.particleType:
                if particle.momentum.values[0] > largeste1:
                    largeste2 = largeste1
                    largest2 = largest1
                    largest1 = particle.index
                    largeste1 = particle.momentum.values[0]
                elif particle.momentum.values[0] > largeste2:
                    largeste2 = particle.momentum.values[0]
                    largest2 = particle.index
            elif ParticleType.Missing == particle.particleType:
                missing = particle.index
        if largest1 < 0 or largest2 < 0 or missing < 0:
            # print(largest1, largest2, missing)
            continue
        if event.particles[largest1 - 1].PGDid * event.particles[largest2 - 1].PGDid > 0:
            # print(event.particles[largest1 - 1].PGDid, event.particles[largest2 - 1].PGDid)
            continue
        # print(missing, len(event.particles))
        if event.particles[largest1 - 1].PGDid > 0:
            pl = event.particles[largest2 - 1].momentum
            plpgd = event.particles[largest2 - 1].PGDid
            pm = event.particles[largest1 - 1].momentum
            pmpgd = event.particles[largest1 - 1].PGDid
        else:
            pl = event.particles[largest1 - 1].momentum
            plpgd = event.particles[largest1 - 1].PGDid
            pm = event.particles[largest2 - 1].momentum
            pmpgd = event.particles[largest2 - 1].PGDid
        pmissing = event.particles[missing - 1].momentum
        saveList.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                         pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                         pmissing.values[0], pmissing.values[1], pmissing.values[2], pmissing.values[3],
                         abs(pmpgd) - 11, abs(plpgd) - 11])
    return saveList
