import os

from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import HistogramWithMinMax
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../")

m0triboson30 = LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30emtb.lhco")
m0triboson30.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30eetb.lhco"))
m0triboson30.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30mmtb.lhco"))
m0vbs30 = LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30emvbs.lhco")
m0vbs30.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30eevbs.lhco"))
m0vbs30.AddEventSet(LoadLHCOlympics("_DataFolder/WWWW/LHE/m0at30mmvbs.lhco"))


def PtZ(eventSample: EventSample) -> float:
    for particle in eventSample.particles:
        if ParticleType.Missing == particle.particleType:
            return particle.momentum.values[3]
    return 0


def PtM(eventSample: EventSample) -> float:
    for particle in eventSample.particles:
        if ParticleType.Missing == particle.particleType:
            return particle.momentum.Mass()
    return 0


def LtMin(eventSample: EventSample) -> float:
    minLt = -1
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            lt = particle.momentum.Pt()
            if minLt < 0 or lt < minLt:
                minLt = lt
    return minLt


def ThetaLepMax(eventSample: EventSample) -> float:
    thetaMax = -1
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            lt = abs(math.cos(particle.momentum.Theta()))
            if lt > thetaMax:
                thetaMax = lt
    return thetaMax


def ThetaLepMin(eventSample: EventSample) -> float:
    thetaMin = 1
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            lt = abs(math.cos(particle.momentum.Theta()))
            if lt < thetaMin:
                thetaMin = lt
    return thetaMin


def ThetaLepSum(eventSample: EventSample) -> float:
    thetaSum = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            thetaSum = thetaSum + particle.momentum.Theta()
    return thetaSum


def ThetaMissing(eventSample: EventSample) -> float:
    for particle in eventSample.particles:
        if ParticleType.Missing == particle.particleType:
            return abs(math.cos(particle.momentum.Theta()))
    return 0


def LeptonMass(eventSample: EventSample) -> float:
    ltall = LorentzVector(0, 0, 0, 0)
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            ltall = ltall + particle.momentum
    return ltall.Mass()


def LeptonTheta(eventSample: EventSample) -> float:
    pl = LorentzVector(0, 0, 0, 0)
    pm = LorentzVector(0, 0, 0, 0)
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            print(particle.PGDid)
            if particle.PGDid > 0:
                pm = particle.momentum
            else:
                pl = particle.momentum
    print(pl.values)
    print(pm.values)
    lpl = pl.values[1] * pl.values[1] + pl.values[2] * pl.values[2] + pl.values[3] * pl.values[3]
    lpm = pm.values[1] * pm.values[1] + pm.values[2] * pm.values[2] + pm.values[3] * pm.values[3]
    denorm = lpl * lpm
    if denorm <= 0:
        return 0
    return (pl.values[1] * pm.values[1] + pl.values[2] * pm.values[2] + pl.values[3] * pm.values[3]) / math.sqrt(denorm)


def MissingMass(eventSample: EventSample) -> float:
    ltall = LorentzVector(0, 0, 0, 0)
    for particle in eventSample.particles:
        if ParticleType.Missing == particle.particleType:
            ltall = ltall + particle.momentum
    return ltall.Mass()


def MuonTheta(eventSample: EventSample) -> float:
    for particle in eventSample.particles:
        if ParticleType.Muon == particle.particleType:
            return abs(math.cos(particle.momentum.Theta()))
    return 0


print(m0triboson30.GetEventCount())
res1 = HistogramWithMinMax(m0triboson30, ThetaMissing, [0, 1], 40)
print(res1.listCount)
print(m0vbs30.GetEventCount())
res2 = HistogramWithMinMax(m0vbs30, ThetaMissing, [0, 1], 40)
print(res2.listCount)

"""

theta missing

m30
183745
[3529, 3361, 3501, 3373, 3386, 3539, 3420, 3595, 3581, 3596, 3507, 3631, 3732, 3667, 3785, 3792, 3859, 3822, 4086, 4120, 3996, 4150, 4203, 4346, 4455, 4538, 4547, 4784, 4878, 4824, 5279, 5308, 5591, 5885, 6188, 6428, 7036, 7538, 8712, 8177]
816255
[10928, 10639, 10727, 10696, 10740, 11082, 10514, 11058, 11163, 11571, 11478, 11738, 11823, 11859, 12353, 12419, 12783, 12899, 13665, 13868, 14163, 14503, 14788, 16038, 16261, 17012, 17541, 19112, 19584, 20530, 22364, 23833, 26114, 28197, 31232, 34656, 39975, 47764, 60575, 98010]

theta muon

t30
92246
[1581, 1573, 1498, 1552, 1545, 1592, 1508, 1556, 1546, 1575, 1623, 1488, 1566, 1635, 1659, 1674, 1687, 1694, 1659, 1759, 1745, 1796, 1820, 1844, 1856, 1877, 1920, 2049, 2066, 2145, 2323, 2384, 2511, 2753, 3091, 3430, 4072, 5338, 8310, 6946]
394795
[7415, 7219, 7232, 7175, 7279, 7442, 7238, 7724, 7575, 7830, 7805, 7798, 8038, 8168, 8424, 8280, 8510, 8651, 8859, 9074, 9152, 9405, 9574, 10070, 10146, 10323, 10505, 11194, 11401, 11526, 12396, 12610, 13178, 13387, 14110, 14349, 15110, 15496, 16020, 7107]

"""