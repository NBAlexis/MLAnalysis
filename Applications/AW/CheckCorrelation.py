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

# testEventsm0 = LoadLHCOlympics("wa/features/bgsm2.lhco")
# testEventsm = LoadLHCOlympics("wa/features/bgsm.lhco")
# testEventsm.AddEventSet(testEventsm0)
# testEventm0 = LoadLHCOlympics("wa/features/fm0.lhco")
# testEventm1 = LoadLHCOlympics("wa/features/fm1.lhco")
testEventm2 = LoadLHCOlympics("signal_a0.lhco")
# testEventm3 = LoadLHCOlympics("wa/features/fm3.lhco")
# testEventm4 = LoadLHCOlympics("wa/features/fm4.lhco")
# testEventm5 = LoadLHCOlympics("wa/features/fm5.lhco")
# testEventt5 = LoadLHCOlympics("wa/features/ft5.lhco")

# CorrelationData(testEventm2, SHatAW, Megamma, 20, 20, [0, 1.0e7], [0, 1000])
# CorrelationData(testEventm2, SHatAW, PTLandPTMissing, 20, 20, [0, 1.0e7], [0, 4000])
# CorrelationData(testEventm2, SHatAW, Yjj2Filter, 20, 20, [0, 1.0e7], [0, 5])
# CorrelationData(testEventm2, SHatAW, ThetaEGamma, 20, 20, [0, 1.0e7], [-1, 1])
# CorrelationData(testEventm2, SHatAW, PhiGammaMissing, 20, 20, [0, 1.0e7], [-1, 1])
# CorrelationData(testEventm2, SHatWW, PtSlashFilter, 20, 20, [0, 1.0e7], [0, 5.0e5])
# CorrelationData(testEventm2, SHatAW, Mjj2Filter, 20, 20, [0, 1.0e7], [0, 4000])
# CorrelationData(testEventm2, SHatAW, RadiusA, 20, 20, [0, 1.0e7], [0, 2])
# CorrelationData(testEventt5, SHatAW, RadiusB, 20, 20, [0, 1.0e7], [0, 2])


