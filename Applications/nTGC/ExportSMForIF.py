import os

import numpy as np

from Applications.nTGC.nTGCCuts import *
from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../_DataFolder/nTGC/")

testEventsm1 = LoadLHCOlympics("sm-025-1.lhco")
particleNumberCut = ParticleNumberNTGC()
drminCut = DeltaRllMin(0.2)
CutEvents(testEventsm1, particleNumberCut)
CutEvents(testEventsm1, drminCut)
print(testEventsm1.GetEventCount())
momentumlist = []
k = 0
for eventSample in testEventsm1.events:
    largestLM1 = 0
    largestLM2 = 0
    largestLIndex1 = 0
    largestLIndex2 = 0
    largestPhoton = 0
    largestPhotonIndex = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestLM1:
                largestLM2 = largestLM1
                largestLIndex2 = largestLIndex1
                largestLM1 = momentum
                largestLIndex1 = particle.index
            elif momentum > largestLM2:
                largestLM2 = momentum
                largestLIndex2 = particle.index
        elif ParticleType.Photon == particle.particleType:
            momentum = particle.momentum.Momentum()
            if momentum > largestPhoton:
                largestPhoton = momentum
                largestPhotonIndex = particle.index
    p41 = eventSample.particles[largestLIndex1 - 1].momentum
    p42 = eventSample.particles[largestLIndex2 - 1].momentum
    p43 = eventSample.particles[largestPhotonIndex - 1].momentum
    momentumlist.append([
        p43.values[0], p43.values[1], p43.values[2], p43.values[3],
        p41.values[0], p41.values[1], p41.values[2], p41.values[3],
        p43.values[0], p43.values[1], p43.values[2], p43.values[3]
    ])
    k = k + 1
np.savetxt("sm-025-1.csv", np.array(momentumlist), delimiter=',')


"""
counts = []
for idx in range(0, 22):
    testEventsm1 = LoadLHCOlympics("s025-{}.lhco".format(idx))
    particleNumberCut = ParticleNumberNTGC()
    drminCut = DeltaRllMin(0.2)
    CutEvents(testEventsm1, particleNumberCut)
    CutEvents(testEventsm1, drminCut)
    print(testEventsm1.GetEventCount())
    counts.append(testEventsm1.GetEventCount())
    momentumlist = []
    k = 0
    for eventSample in testEventsm1.events:
        largestLM1 = 0
        largestLM2 = 0
        largestLIndex1 = 0
        largestLIndex2 = 0
        largestPhoton = 0
        largestPhotonIndex = 0
        for particle in eventSample.particles:
            if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
                momentum = particle.momentum.Momentum()
                if momentum > largestLM1:
                    largestLM2 = largestLM1
                    largestLIndex2 = largestLIndex1
                    largestLM1 = momentum
                    largestLIndex1 = particle.index
                elif momentum > largestLM2:
                    largestLM2 = momentum
                    largestLIndex2 = particle.index
            elif ParticleType.Photon == particle.particleType:
                momentum = particle.momentum.Momentum()
                if momentum > largestPhoton:
                    largestPhoton = momentum
                    largestPhotonIndex = particle.index
        p41 = eventSample.particles[largestLIndex1 - 1].momentum
        p42 = eventSample.particles[largestLIndex2 - 1].momentum
        p43 = eventSample.particles[largestPhotonIndex - 1].momentum
        momentumlist.append([
            p43.values[0], p43.values[1], p43.values[2], p43.values[3],
            p41.values[0], p41.values[1], p41.values[2], p41.values[3],
            p43.values[0], p43.values[1], p43.values[2], p43.values[3]
        ])
        k = k + 1
        print("{}/{} done", k, counts[idx])
    np.savetxt("s025-{}.csv".format(idx), np.array(momentumlist), delimiter=',')

print(counts)
"""
