import math
import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.Histogram import HistogramWithMinMax
from DataStructure.EventSample import EventSample
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../_DataFolder/")


class ParticleNumberWWZ:
    """
    Every cut class must implement "Cut(self, eventSample: EventSample) -> bool:" function
    """

    def Cut(self, eventSample: EventSample) -> bool:
        hasLplus: bool = False
        hasLminus: bool = False
        for particle in eventSample.particles:
            if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
                if particle.PGDid < 0:
                    hasLplus = True
                else:
                    hasLminus = True
        if not hasLplus or not hasLminus:
            return True
        return False


def LeptonInvarientMass(eventSample: EventSample) -> float:
    largestLplusIndex: int = -1
    largestLplusEnergy: float = 0
    largestLminusIndex: int = -1
    largestLminusEnergy: float = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            if particle.PGDid < 0:
                if particle.momentum.values[0] > largestLplusEnergy:
                    largestLplusEnergy = particle.momentum.values[0]
                    largestLplusIndex = particle.index
            else:
                if particle.momentum.values[0] > largestLminusEnergy:
                    largestLminusEnergy = particle.momentum.values[0]
                    largestLminusIndex = particle.index
    momentumSum = eventSample.particles[largestLplusIndex - 1].momentum + eventSample.particles[
        largestLminusIndex - 1].momentum
    return momentumSum.Mass()


class InvarientMassCut:
    """
    Every cut class must implement "Cut(self, eventSample: EventSample) -> bool:" function
    """

    def Cut(self, eventSample: EventSample) -> bool:
        if LeptonInvarientMass(eventSample) < 500:
            return True
        return False


def ETMissing(eventSample: EventSample) -> float:
    missingIndex: int = -1
    for particle in eventSample.particles:
        if ParticleType.Missing == particle.particleType:
            missingIndex = particle.index
            break
    return eventSample.particles[missingIndex - 1].momentum.values[0]


def LeptonAngle(eventSample: EventSample) -> float:
    largestLplusIndex: int = -1
    largestLplusEnergy: float = 0
    largestLminusIndex: int = -1
    largestLminusEnergy: float = 0
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            if particle.PGDid < 0:
                if particle.momentum.values[0] > largestLplusEnergy:
                    largestLplusEnergy = particle.momentum.values[0]
                    largestLplusIndex = particle.index
            else:
                if particle.momentum.values[0] > largestLminusEnergy:
                    largestLminusEnergy = particle.momentum.values[0]
                    largestLminusIndex = particle.index
    p3dPlus = [
        eventSample.particles[largestLplusIndex - 1].momentum.values[1],
        eventSample.particles[largestLplusIndex - 1].momentum.values[2],
        eventSample.particles[largestLplusIndex - 1].momentum.values[3]]
    p3dMinus = eventSample.particles[largestLminusIndex - 1].momentum.P3d()
    # lepton dot cos(theta_l)
    sizePlus = math.sqrt(p3dPlus[0] * p3dPlus[0] + p3dPlus[1] * p3dPlus[1] + p3dPlus[2] * p3dPlus[2])
    sizeMinus = math.sqrt(p3dMinus[0] * p3dMinus[0] + p3dMinus[1] * p3dMinus[1] + p3dMinus[2] * p3dMinus[2])
    leptonDot = (p3dPlus[0] * p3dMinus[0] + p3dPlus[1] * p3dMinus[1] + p3dPlus[2] * p3dMinus[2]) / (
                sizePlus * sizeMinus)
    return leptonDot


signalEvent = LoadLHCOlympics("mumuZZAWWA/run05.lhco")
print("event number of signal events before cut:", len(signalEvent.events))

particleNumberCut = ParticleNumberWWZ()
CutEvents(signalEvent, particleNumberCut)
print("event number of signal events after cut:", len(signalEvent.events))

HistogramWithMinMax(signalEvent, LeptonAngle, [-1, 1], 50)
