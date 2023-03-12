import math
import os

import numpy as np

from Applications.WWWW.Filters import IsVBS, ExportEvent
from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType, ParticleStatus
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent
from Interfaces.UsefulFunctions import SaveCSVFile


def ExportEventTag(eventSet: EventSet, debugCount: bool = True) -> [list, list]:
    saveList1 = []
    saveList2 = []
    count = 0
    evenOdd = False
    for event in eventSet.events:
        evenOdd = not evenOdd
        count = count + 1
        if debugCount:
            print("{} / {}".format(count, eventSet.GetEventCount()))
        pl = LorentzVector(0, 0, 0, 0)
        pm = LorentzVector(0, 0, 0, 0)
        plpgd = 0
        pmpgd = 0
        for particle in event.particles:
            if ParticleStatus.Outgoing == particle.status:
                if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
                    if particle.PGDid > 0:
                        pm = particle.momentum
                        pmpgd = particle.PGDid
                    else:
                        pl = particle.momentum
                        plpgd = particle.PGDid
        missingAll = LorentzVector(0, 0, 0, 0)
        for particle in event.particles:
            if ParticleStatus.Invisible == particle.status:
                missingAll = missingAll + particle.momentum
        isvbs = IsVBS(event)
        if evenOdd:
            saveList1.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                             pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                             missingAll.values[0], missingAll.values[1], missingAll.values[2], missingAll.values[3],
                             abs(pmpgd) - 11, abs(plpgd) - 11,
                             isvbs])
        else:
            saveList2.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                             pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                             missingAll.values[0], missingAll.values[1], missingAll.values[2], missingAll.values[3],
                             abs(pmpgd) - 11, abs(plpgd) - 11,
                             isvbs])
    return [saveList1, saveList2]


def ExportEventTagWithCount(eventSet: EventSet, countMax: int) -> [list, list]:
    saveList1 = []
    saveList2 = []
    count = 0
    evenOdd = False
    for event in eventSet.events:
        evenOdd = not evenOdd
        count = count + 1
        if count > countMax:
            break
        print("{} / {}".format(count, eventSet.GetEventCount()))
        pl = LorentzVector(0, 0, 0, 0)
        pm = LorentzVector(0, 0, 0, 0)
        plpgd = 0
        pmpgd = 0
        for particle in event.particles:
            if ParticleStatus.Outgoing == particle.status:
                if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
                    if particle.PGDid > 0:
                        pm = particle.momentum
                        pmpgd = particle.PGDid
                    else:
                        pl = particle.momentum
                        plpgd = particle.PGDid
        missingAll = LorentzVector(0, 0, 0, 0)
        for particle in event.particles:
            if ParticleStatus.Invisible == particle.status:
                missingAll = missingAll + particle.momentum
        isvbs = IsVBS(event)
        if evenOdd:
            saveList1.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                             pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                             missingAll.values[0], missingAll.values[1], missingAll.values[2], missingAll.values[3],
                             abs(pmpgd) - 11, abs(plpgd) - 11,
                             isvbs])
        else:
            saveList2.append([pl.values[0], pl.values[1], pl.values[2], pl.values[3],
                             pm.values[0], pm.values[1], pm.values[2], pm.values[3],
                             missingAll.values[0], missingAll.values[1], missingAll.values[2], missingAll.values[3],
                             abs(pmpgd) - 11, abs(plpgd) - 11,
                             isvbs])
    return [saveList1, saveList2]

# """
os.chdir("../../")
for energies in ["m0", "m1", "m7", "t0", "t1", "t2"]:
    s0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/{}at30.lhe".format(energies))
    print(energies, " loaded")
    [toSave1, toSave2] = ExportEventTag(s0)
    # print(len(toSave1), len(toSave2))
    # with open('t30tagtrain.csv', 'a') as csvfile1:
    #     np.savetxt(csvfile1, toSave1, delimiter=',')
    with open('{}30tagvalid.csv'.format(energies), 'a') as csvfile2:
        np.savetxt(csvfile2, toSave2, delimiter=',')
# """

"""
os.chdir("../../")
s0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/m1at30.lhe")
print("m1", " loaded")
[toSave1, toSave2] = ExportEventTag(s0)
print(len(toSave2))
with open('m1at30tag.csv', 'a') as csvfile:
    np.savetxt(csvfile, toSave2, delimiter=',')
"""