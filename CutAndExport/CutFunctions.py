import math

from CutAndExport.FilterFunctions import *
from DataStructure.Constants import *
from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleStatus, ParticleType

'''
If return true, the events are cut off.
If return false, the events are preserved.
'''


class FunctionCut:

    def __init__(self, cutFunction, cutValue: float, bRemoveLarge: bool):
        """

        :param cutFunction: float v = f(eventSample)
        :param cutValue: the value to cut
        :param bRemoveLarge: if true, remove f(eventSample) > cutValue, otherwise remove f(eventSample) < cutValue
        """
        self.cutFunction = cutFunction
        self.cutValue = cutValue
        self.bRemoveLarge = bRemoveLarge

    def Cut(self, eventSample: EventSample) -> bool:
        if self.bRemoveLarge:
            if self.cutFunction(eventSample) > self.cutValue:
                return True
            return False
        if self.cutFunction(eventSample) < self.cutValue:
            return True
        return False


class JetNumberCut:
    """
    If cutType = 0, cut all with jets > parameters[0]
    If cutType = 1, cut all with jets < parameters[0]
    If cutType = 2, cut all with jets not in parameters
    """

    def __init__(self, cutType: int, parameters):
        self.cutType = cutType
        self.parameters = parameters

    def Cut(self, eventSample: EventSample) -> bool:
        jetCount = 0
        for particle in eventSample.particles:
            if 4 == particle.particleType:
                jetCount += 1
        if 0 == self.cutType:
            return jetCount > self.parameters[0]
        if 1 == self.cutType:
            return jetCount < self.parameters[0]
        return jetCount not in self.parameters


class PhotonNumberCut:
    """
    If cutType = 0, cut all with photons > parameters[0]
    If cutType = 1, cut all with photons < parameters[0]
    If cutType = 2, cut all with photons not in parameters
    """

    def __init__(self, cutType: int, parameters):
        self.cutType = cutType
        self.parameters = parameters

    def Cut(self, eventSample: EventSample) -> bool:
        photonCount = 0
        for particle in eventSample.particles:
            if 0 == particle.particleType:
                photonCount += 1
        if 0 == self.cutType:
            return photonCount > self.parameters[0]
        if 1 == self.cutType:
            return photonCount < self.parameters[0]
        return photonCount not in self.parameters


class LeptonPMCut:
    """
    If give a <0, don't check,
    for example LeptonPMCut(False, 1, -1) only check e+, mu+ = 1
    LeptonPMCut(False, 1, 0) check e+, mu+ = 1 and e- mu- = 0
    """

    def __init__(self, countTau: bool, positive: int, negative: int):
        self.countTau = countTau
        self.positive = positive
        self.negative = negative

    def Cut(self, eventSample: EventSample) -> bool:
        positiveCount = 0
        negativeCount = 0
        for particle in eventSample.particles:
            if 1 <= particle.particleType <= 3:
                if self.countTau or particle.particleType < 3:
                    if particle.PGDid > 0:
                        negativeCount = negativeCount + 1
                    else:
                        positiveCount = positiveCount + 1
        return not ((positiveCount == self.positive or self.positive < 0) and (
                negativeCount == self.negative or self.negative < 0))


class ETMissingCount:
    """
    If cutType = 0, cut ETMissing > cutValue
    If cutType = 1, cut ETMissing < cutValue
    """

    def __init__(self, cutType: int, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        if 0 == self.cutType:
            return eventSample.GetETMissing() > self.cutValue
        return eventSample.GetETMissing() < self.cutValue


class StandardVBFCut:
    def __init__(self, onlyHardestMjj: bool, mjj: float, deltaYjj: float):
        self.onlyHardestMjj = onlyHardestMjj
        self.mjj = mjj
        self.deltaYjj = deltaYjj

    def Cut(self, eventSample: EventSample) -> bool:
        largestJetIndex1 = 0
        largestJetM1 = 0.0
        largestJetIndex2 = 0
        largestJetM2 = 0.0
        finalV = LorentzVector()
        for particle in eventSample.particles:
            if ParticleStatus.Outgoing == particle.status \
                    and ParticleType.Jet == particle.particleType:
                momentum = particle.momentum.Momentum()
                finalV = finalV + particle.momentum
                if momentum > largestJetM1:
                    largestJetM2 = largestJetM1
                    largestJetIndex2 = largestJetIndex1
                    largestJetM1 = momentum
                    largestJetIndex1 = particle.index
                elif momentum > largestJetM2:
                    largestJetM2 = momentum
                    largestJetIndex2 = particle.index
        if largestJetIndex1 > 0 and largestJetIndex2 > 0:
            p1 = eventSample.particles[largestJetIndex1 - 1].momentum
            p2 = eventSample.particles[largestJetIndex2 - 1].momentum
        else:
            return True
        yjj = abs(p1.Y() - p2.Y())
        if self.onlyHardestMjj:
            hardestP = p1 + p2
            beforeSqrt = 2.0 * (hardestP * hardestP)
            mjj = math.sqrt(0.0 if beforeSqrt < 0.0 else beforeSqrt)
        else:
            beforeSqrt = 2.0 * (finalV * finalV)
            mjj = math.sqrt(0.0 if beforeSqrt < 0.0 else beforeSqrt)
        return yjj < self.deltaYjj or mjj < self.mjj


class LeptonPMDotCut:
    """
    If cutType = 0, cut lepton dot > cutValue
    If cutType = 1, cut lepton dot < cutValue
    """

    def __init__(self, cutType: int, countTau: bool, cutValue):
        self.cutType = cutType
        self.cutValue = cutValue
        self.countTau = countTau

    def Cut(self, eventSample: EventSample) -> bool:
        positiveIndex = 0
        negativeIndex = 0
        for i in range(len(eventSample.particles)):
            if 1 <= eventSample.particles[i].particleType <= 3:
                if self.countTau or eventSample.particles[i].particleType < 3:
                    if eventSample.particles[i].PGDid > 0:
                        negativeIndex = i
                    else:
                        positiveIndex = i
        p41 = eventSample.particles[negativeIndex].momentum
        p42 = eventSample.particles[positiveIndex].momentum
        dotValue = dot3d(normalize3d(p41.P3d()), normalize3d(p42.P3d()))
        if 0 == self.cutType:
            return dotValue > self.cutValue
        return dotValue < self.cutValue


class MolCut:
    """
    If cutType = 0, cut mol > cutValue
    If cutType = 1, cut mol < cutValue
    """

    def __init__(self, cutType: int, countTau: bool, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue
        self.countTau = countTau

    def Cut(self, eventSample: EventSample) -> bool:
        positiveIndex = 0
        negativeIndex = 0
        p4missing = LorentzVector()
        for i in range(len(eventSample.particles)):
            if 1 <= eventSample.particles[i].particleType <= 3:
                if self.countTau or eventSample.particles[i].particleType < 3:
                    if eventSample.particles[i].PGDid > 0:
                        negativeIndex = i
                    else:
                        positiveIndex = i
            if ParticleType.Missing == eventSample.particles[i].particleType:
                p4missing = p4missing + eventSample.particles[i].momentum
        p41 = eventSample.particles[negativeIndex].momentum
        p42 = eventSample.particles[positiveIndex].momentum
        left = p41.Pt() + p42.Pt() + p4missing.Pt()
        p4missing = p4missing + p41
        p4missing = p4missing + p42
        right = p4missing.Pt()
        mol = math.sqrt(left * left - right * right)
        if 0 == self.cutType:
            return mol > self.cutValue
        return mol < self.cutValue


class MeGammaCut:
    """
    If cutType = 0, cut mol > cutValue
    If cutType = 1, cut mol < cutValue
    """

    def __init__(self, cutType: int, countTau: bool, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue
        self.countTau = countTau

    def Cut(self, eventSample: EventSample) -> bool:
        largestPhotonIdx = -1
        largestEa = -1.0
        leptonIdx = -1
        for i in range(len(eventSample.particles)):
            if 0 == eventSample.particles[i].particleType:
                if eventSample.particles[i].momentum.values[0] > largestEa:
                    largestEa = eventSample.particles[i].momentum.values[0]
                    largestPhotonIdx = i
            if 1 == eventSample.particles[i].particleType or 2 == eventSample.particles[i].particleType:
                leptonIdx = i
            elif -1 == leptonIdx and self.countTau and 3 == eventSample.particles[i].particleType:
                leptonIdx = i
        momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
        momentumLepton = eventSample.particles[leptonIdx].momentum
        momentumPhoton = momentumPhoton + momentumLepton
        megamma = momentumPhoton.Mass()
        if 0 == self.cutType:
            return megamma > self.cutValue
        return megamma < self.cutValue


class PtMissing:
    """
    If cutType = 0, cut mol > cutValue
    If cutType = 1, cut mol < cutValue
    """

    def __init__(self, cutType: int, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        ptx = 0.0
        pty = 0.0
        for particle in eventSample.particles:
            if ParticleStatus.Invisible == particle.status:
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        ptslash = ptx * ptx + pty * pty
        if ptslash > 0:
            ptslash = math.sqrt(ptslash)
        else:
            ptslash = 0.0
        if 0 == self.cutType:
            return ptslash > self.cutValue
        return ptslash < self.cutValue


class PhiGammaMissingCut:
    """
    If cutType = 0, cut mol > cutValue
    If cutType = 1, cut mol < cutValue
    """

    def __init__(self, cutType: int, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        largestPhotonIdx = -1
        largestEa = -1.0
        missingIdx = -1
        for i in range(len(eventSample.particles)):
            if 0 == eventSample.particles[i].particleType:
                if eventSample.particles[i].momentum.values[0] > largestEa:
                    largestEa = eventSample.particles[i].momentum.values[0]
                    largestPhotonIdx = i
            if 6 == eventSample.particles[i].particleType:
                missingIdx = i
        momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
        momentumMissing = eventSample.particles[missingIdx].momentum
        phiGammaMissing = math.cos(momentumPhoton.Azimuth() - momentumMissing.Azimuth())
        if 0 == self.cutType:
            return phiGammaMissing > self.cutValue
        return phiGammaMissing < self.cutValue


class ThetaGammaLeptonCut:
    """
    If cutType = 0, cut mol > cutValue
    If cutType = 1, cut mol < cutValue
    """

    def __init__(self, cutType: int, countTau: bool, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue
        self.countTau = countTau

    def Cut(self, eventSample: EventSample) -> bool:
        largestPhotonIdx = -1
        largestEa = -1.0
        leptonIdx = -1
        for i in range(len(eventSample.particles)):
            if 0 == eventSample.particles[i].particleType:
                if eventSample.particles[i].momentum.values[0] > largestEa:
                    largestEa = eventSample.particles[i].momentum.values[0]
                    largestPhotonIdx = i
            if 1 == eventSample.particles[i].particleType or 2 == eventSample.particles[i].particleType:
                leptonIdx = i
            elif -1 == leptonIdx and self.countTau and 3 == eventSample.particles[i].particleType:
                leptonIdx = i
        momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
        momentumLepton = eventSample.particles[leptonIdx].momentum
        cosTheta = dot3d(normalize3d(momentumPhoton.V3d()), normalize3d(momentumLepton.V3d()))
        if 0 == self.cutType:
            return cosTheta > self.cutValue
        return cosTheta < self.cutValue


class PhiLeptonMissingCut:
    """
    If cutType = 0, cut mol > cutValue
    If cutType = 1, cut mol < cutValue
    """

    def __init__(self, cutType: int, countTau: bool, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue
        self.countTau = countTau

    def Cut(self, eventSample: EventSample) -> bool:
        missingIdx = -1
        leptonIdx = -1
        for i in range(len(eventSample.particles)):
            if 6 == eventSample.particles[i].particleType:
                missingIdx = i
            if 1 == eventSample.particles[i].particleType or 2 == eventSample.particles[i].particleType:
                leptonIdx = i
            elif -1 == leptonIdx and self.countTau and 3 == eventSample.particles[i].particleType:
                leptonIdx = i
        momentumMissing = eventSample.particles[missingIdx].momentum
        momentumLepton = eventSample.particles[leptonIdx].momentum
        cosTheta = math.cos(momentumLepton.Azimuth() - momentumMissing.Azimuth())
        if 0 == self.cutType:
            return cosTheta > self.cutValue
        return cosTheta < self.cutValue


class RadiusACut:
    """
    If cutType = 0, cut mol > cutValue
    If cutType = 1, cut mol < cutValue
    """

    def __init__(self, cutType: int, cutValue: float, radiusType: int):
        self.cutType = cutType
        self.cutValue = cutValue
        self.radiusType = radiusType

    def Cut(self, eventSample: EventSample) -> bool:
        missingIdx = -1
        leptonIdx = -1
        largestEa = -1.0
        largestPhotonIdx = -1
        for i in range(len(eventSample.particles)):
            if ParticleType.Photon == eventSample.particles[i].particleType:
                if eventSample.particles[i].momentum.values[0] > largestEa:
                    largestEa = eventSample.particles[i].momentum.values[0]
                    largestPhotonIdx = i
            if 6 == eventSample.particles[i].particleType:
                missingIdx = i
            if 1 == eventSample.particles[i].particleType or 2 == eventSample.particles[i].particleType:
                leptonIdx = i
        pMissing = eventSample.particles[missingIdx].momentum
        pLepton = eventSample.particles[leptonIdx].momentum
        p2Wt = [pMissing.values[1] + pLepton.values[1], pMissing.values[2] + pLepton.values[2]]
        p2Lt = [pLepton.values[1], pLepton.values[2]]
        momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
        lp = (p2Lt[0] * p2Wt[0] + p2Lt[1] * p2Wt[1]) / (p2Wt[0] * p2Wt[0] + p2Wt[1] * p2Wt[1])
        if lp < 0 or lp > 1:
            return True
        thetaPhoton = math.cos(momentumPhoton.Theta())
        ra = 0
        if 1 == self.radiusType:
            ra = (1 - abs(thetaPhoton)) * (1 - abs(thetaPhoton)) + (lp - 0.5) * (lp - 0.5)
        elif 2 == self.radiusType:
            ra = (1 - abs(thetaPhoton)) * (1 - abs(thetaPhoton)) + lp * lp
        elif 3 == self.radiusType:
            ra = (1 - abs(thetaPhoton)) * (1 - abs(thetaPhoton)) + (1 - lp) * (1 - lp)
        if 0 == self.cutType:
            return ra > self.cutValue
        return ra < self.cutValue


class LeptonPtCut:
    """
    If cutType = 0, cut off pt > cutValue (Not support, meaningless)
    If cutType = 1, cut off pt < cutValue
    """

    def __init__(self, cutValue: float):
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        return LeptonPtFilter(eventSample) < self.cutValue


class SHatCut2:
    """
    shat = (p_nu + p_l + p_a)^2 < (p_nu + p_l + p_a)_T^2
    so if (p_nu + p_l + p_a)_T^2 < cut_value, then shat is sure to be < cut_value
    """

    def __init__(self, cutType: int, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        pAll2 = SHatAW(eventSample)
        if 0 == self.cutType:
            return pAll2 > self.cutValue
        return pAll2 < self.cutValue


class SHatCutWWTest:
    """
    use SHatWW
    """

    def __init__(self, cutType: int, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        pAll2 = SHatWW(eventSample)
        if 0 == self.cutType:
            return pAll2 > self.cutValue
        return pAll2 < self.cutValue


class PhiLLMCut:
    """
    use PhiLLM
    """

    def __init__(self, cutType: int, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        pAll2 = PhiLLM(eventSample)
        if 0 == self.cutType:
            return pAll2 > self.cutValue
        return pAll2 < self.cutValue
