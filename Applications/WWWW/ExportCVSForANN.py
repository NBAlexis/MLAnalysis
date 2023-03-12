import math
import os

from Applications.WWWW.Filters import IsVBS, ExportEvent, ExportEventLHCO
from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType, ParticleStatus
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent
from Interfaces.UsefulFunctions import SaveCSVFile, SaveCSVFileA

"""
os.chdir("../../")
for energies in ["sm", "s0", "s1", "s2", "m0", "m7", "t0", "t1", "t2"]:
    s0 = LoadLHCOlympics("_DataFolder/WWWW/LHCO/wwww{}.lhco".format(energies))
    toSave = ExportEventLHCO(s0)
    print(len(toSave))
    SaveCSVFile("_DataFolder/WWWW/LHCO/{}.csv".format(energies), toSave, 0, 13)
"""

"""
os.chdir("../../")
for energies in ["m1"]:
    s0 = LoadLHCOlympics("_DataFolder/WWWW/LHCO/wwww{}.lhco".format(energies))
    toSave = ExportEventLHCO(s0)
    print(len(toSave))
    SaveCSVFileA("_DataFolder/WWWW/LHCO/m1.csv".format(energies), toSave, 0, 13)
"""

# """
#
os.chdir("../../")
s0 = LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm2.lhco")
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm3.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm4.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm5.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm6.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm7.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm8.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm9.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/sm10.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/newsm1.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/newsm2.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/newsm3.lhco"))
s0.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/newsm4.lhco"))
print(len(s0.events))
toSave = ExportEventLHCO(s0)
SaveCSVFile("_DataFolder/WWWW/LHCO/int/smint.csv", toSave, 0, 13)

s1 = LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/full1.lhco")
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/full2.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/full3.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/full4.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/full5.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/full6.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/gfull1.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/gfull2.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/gfull3.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/gfull4.lhco"))
s1.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHCO/int/gfull5.lhco"))
toSave2 = ExportEventLHCO(s1)
SaveCSVFile("_DataFolder/WWWW/LHCO/int/fullint.csv", toSave2, 0, 13)

print(len(s0.events))
print(len(s1.events))

#261635
#376231

# """