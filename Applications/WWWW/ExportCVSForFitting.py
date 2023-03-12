import math
import os

import numpy as np

from Applications.WWWW.Filters import IsVBS, ExportEvent, ExportEventWithCount
from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType, ParticleStatus
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent
from Interfaces.UsefulFunctions import SaveCSVFile

# """
os.chdir("../../")
h=["s", "m", "t"]
hs=["0", "1", "2"]
hm=["0", "1", "7"]
ht=["0", "1", "2"]
allh = [hs, hm, ht]
for head in range(0, 3):
    for energies in allh[head]:
        s0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/{}{}at30.lhe".format(h[head], energies))
        print(energies, " loaded")
        [toSave1, toSave2] = ExportEvent(s0)
        # print(len(toSave1), len(toSave2))
        with open('{}30shattrain.csv'.format(h[head]), 'a') as csvfile1:
            np.savetxt(csvfile1, toSave1, delimiter=',')
        with open('{}30shatvalid.csv'.format(h[head]), 'a') as csvfile2:
            np.savetxt(csvfile2, toSave2, delimiter=',')
# """

"""
os.chdir("../../")
for energies in ["s0", "s1", "s2", "m0", "m1", "m7", "t0", "t1", "t2"]:
    s0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/{}at30.lhe".format(energies))
    print(energies, " loaded")
    [toSave1, toSave2] = ExportEvent(s0)
    with open('{}at30valid.csv'.format(energies), 'w') as csvfile2:
        np.savetxt(csvfile2, toSave2, delimiter=',')
"""