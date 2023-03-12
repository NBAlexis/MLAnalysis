import os

from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("F:/PyworkingFolder/CutExperiment/_DataFolder")

cutType = 1
jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)
vbfCut = StandardVBFCut(True, 0.0, 2.0)
ptMissingCutM = PtMissing(1, 120)
megammaCut = MeGammaCut(1, False, 800)
thetaGammaLeptonCut = ThetaGammaLeptonCut(0, False, 0)
phiGammaMissingCut = PhiGammaMissingCut(0, -0.75)
lmCut = PhiLeptonMissingCut(1, False, 0)
ptMissingCutT = PtMissing(1, 75)
r2Cut = RadiusACut(1, 0.15, 3)
r1Cut = RadiusACut(1, 0.15, 2)

fileHeader = "wa/fittings/fm1/fm1-"

event0 = LoadLHCOlympics("{}0.lhco".format(fileHeader))
event10 = LoadLHCOlympics("{}10.lhco".format(fileHeader))


lstCSfm0 = [9.542720, 9.539352]
lstCSfm1 = [9.532671, 9.541255]
lstCSfm7 = [9.494640, 9.487761]
lstCSft0 = [9.483595, 9.486116]
lstCSft1 = [9.482633, 9.488846]
lstCSft2 = [9.477430, 9.483161]

lstEventN = [event0.GetEventCount(),
             event10.GetEventCount()]

print(lstEventN)

eventLst = [event0, event10]

if 1 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        CutEvents(eventSet, vbfCut)
        CutEvents(eventSet, ptMissingCutM)
        CutEvents(eventSet, megammaCut)
        CutEvents(eventSet, thetaGammaLeptonCut)
        CutEvents(eventSet, phiGammaMissingCut)
        CutEvents(eventSet, lmCut)
elif 2 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        CutEvents(eventSet, r1Cut)
        CutEvents(eventSet, ptMissingCutT)
        CutEvents(eventSet, megammaCut)
        CutEvents(eventSet, thetaGammaLeptonCut)
elif 3 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        CutEvents(eventSet, r2Cut)
        CutEvents(eventSet, ptMissingCutT)
        CutEvents(eventSet, megammaCut)


lstEventN2 = [event0.GetEventCount(),
              event10.GetEventCount()]


print(lstEventN2)


for i in range(0, 2):
    print(lstEventN2[i] * lstCSfm0[i] / lstEventN[i])



