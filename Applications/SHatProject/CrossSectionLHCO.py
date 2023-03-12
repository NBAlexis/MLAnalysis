import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics, SaveToLHCO
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

"""
we cut all events with:
1 - particle number cut
2 - Mjj cut
3 - yjj cut
4 - Mo1 cut
5 - phi lm cut
6 - theta ll cut
"""

jetNumberCut = JetNumberCut(2, [2, 3, 4, 5])
leptonNumberCut = LeptonPMCut(False, 1, 1)
vbfCut1 = StandardVBFCut(True, 0.0, 1.2)
vbfCut2 = StandardVBFCut(True, 150.0, 0.0)
phillmCut = PhiLLMCut(1, 0.3)
leptonCut = LeptonPMDotCut(0, False, -0.0)
molCut = MolCut(1, False, 600)

finalCSs = []
# a0
# doMjj = [True, True]
# lhcoNames = ["G:\\ww\\a0-0-", "G:\\ww\\a0-1-"]
# saveHead = "G:\\ww\\finalcs\\a0-c-"

doMjj = [True, True, False, False]
lhcoNames = ["G:\\ww\\a1-0-", "G:\\ww\\a1-1-", "G:\\wwnew\\a1-2-", "G:\\wwnew\\a1-3-"]
saveHead = "G:\\ww\\finalcs\\a1-c-"

# doMjj = [True, True, False]
# lhcoNames = ["G:\\ww\\a2-0-", "G:\\ww\\a2-1-", "G:\\wwnew\\a2-2-"]
# saveHead = "G:\\ww\\finalcs\\a2-c-"

# doMjj = [True, True, True, False]
# lhcoNames = ["G:\\ww\\a3-0-", "G:\\ww\\a3-1-", "G:\\ww\\a3-2-", "G:\\wwnew\\a3-2-"]
# saveHead = "G:\\ww\\finalcs\\a3-c-"

csa01 = [0.7253474, 0.7245036, 0.7245078, 0.723718, 0.7241555, 0.724039, 0.723857, 0.7241923, 0.7241295, 0.7249473, 0.7250127]
csa02 = [0.7253474, 0.7245036, 0.7245078, 0.723718, 0.7241555, 0.724039, 0.723857, 0.7241923, 0.7241295, 0.7249473, 0.7250127]

csa11 = [0.7241934, 0.7238891, 0.7241664, 0.7238983, 0.7240129, 0.7246298, 0.7242188, 0.724425, 0.7242562, 0.7241959, 0.7236802]
csa12 = [0.7245921, 0.7242747, 0.7240749, 0.724686, 0.7241323, 0.7242849, 0.7244692, 0.7240723, 0.7241654, 0.7240883, 0.7244164]
csa13 = [0.305594, 0.3055881, 0.3056025, 0.3056858, 0.3052609, 0.3055816, 0.3052318, 0.3054521, 0.3055094, 0.3054078, 0.3056296]
csa14 = [0.305594, 0.3055881, 0.3056025, 0.3056858, 0.3052609, 0.3055816, 0.3052318, 0.3054521, 0.3055094, 0.3054078, 0.3056296]

csa21 = [0.7244208, 0.7239309, 0.7241752, 0.7235036, 0.724295, 0.7236588, 0.7242745, 0.7241075, 0.7240619, 0.7241979, 0.7243225]
csa22 = [0.7244208, 0.7239309, 0.7241752, 0.7235036, 0.724295, 0.7236588, 0.7242745, 0.7241075, 0.7240619, 0.7241979, 0.7243225]
csa23 = [0.30580502806812276, 0.30562219554585995, 0.3054479045715647, 0.30563160429821656, 0.3055807, 0.305546, 0.3054174, 0.3054159, 0.3053932, 0.3055973, 0.3055578, 0.3058832]


csa31 = [0.7237773, 0.7237951, 0.7240702, 0.7236968, 0.72336, 0.7239009, 0.7238577, 0.723537, 0.7240993, 0.7239825, 0.7240108]
csa32 = [0.7236262, 0.7244081, 0.7240265, 0.7238683, 0.7243599, 0.7237965, 0.7238768, 0.7241674, 0.7242295, 0.7238172, 0.7244049]
csa33 = [0.7240756, 0.7240543, 0.7245112, 0.7241006, 0.7239527, 0.7240304, 0.7240067, 0.724737, 0.724381, 0.7238962, 0.7243846]
csa34 = [0.3415212, 0.3414818, 0.3414304, 0.3413322, 0.3414365, 0.3411867, 0.341372, 0.341534, 0.3413236, 0.3416104, 0.3414668]

# orignalCS = [csa01, csa02]
orignalCS = [csa11, csa12, csa13, csa14]
# orignalCS = [csa21, csa22, csa23]
# orignalCS = [csa31, csa32, csa33, csa34]

for i in range(0, 11):
    print("Working on ", i)
    emptyEv = EventSet()
    eventTotal = 0
    csTotal = 0.0
    for j in range(0, len(lhcoNames)):
        fileName = "{}{}.lhco".format(lhcoNames[j], i)
        print("Reading file: ", fileName)
        ev = LoadLHCOlympics(fileName)
        numberNow = ev.GetEventCount()
        CutEvents(ev, jetNumberCut)
        CutEvents(ev, vbfCut1)
        CutEvents(ev, phillmCut)
        CutEvents(ev, leptonCut)
        CutEvents(ev, molCut)
        if doMjj[j]:
            CutEvents(ev, vbfCut2)
        numberAfterCut = ev.GetEventCount()
        emptyEv.AddEventSet(ev)
        eventTotal = eventTotal + numberAfterCut
        csNow = orignalCS[j][i] * numberAfterCut / numberNow
        print("cs:", j, i, csNow)
        csTotal = csTotal + csNow * numberAfterCut
    finalCS = csTotal / eventTotal
    saveFileName = "{}{}.lhco".format(saveHead, i)
    print("saving: {} , number: {}, cs: {}".format(saveFileName, emptyEv.GetEventCount(), finalCS))
    SaveToLHCO(saveFileName, emptyEv)
    finalCSs.append(finalCS)

print(finalCSs)

"""
a0:
[-1.3e-08, -1.04e-08, -7.8e-09, -5.2e-09, -2.6e-09, 0.0, 2.6e-09, 5.2e-09, 7.8e-09, 1.04e-08, 1.3e-08]
[0.7253474, 0.7245036, 0.7245078, 0.723718, 0.7241555, 0.724039, 0.723857, 0.7241923, 0.7241295, 0.7249473, 0.7250127]
"""