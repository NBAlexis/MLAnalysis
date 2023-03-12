import math

from DataStructure.Constants import *
from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType, ParticleStatus


def PtFilter(eventSample: EventSample) -> float:
    ptx = 0.0
    pty = 0.0
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status:
            ptx += particle.momentum.values[1]
            pty += particle.momentum.values[2]
    return math.sqrt(ptx * ptx + pty * pty)


def JetPtFilter(eventSample: EventSample) -> float:
    ptx = 0.0
    pty = 0.0
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status \
                and ParticleType.Jet == particle.particleType:
            ptx += particle.momentum.values[1]
            pty += particle.momentum.values[2]
    return math.sqrt(ptx * ptx + pty * pty)


def LeptonPtFilter(eventSample: EventSample) -> float:
    ptx = 0.0
    pty = 0.0
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status and \
                (ParticleType.Muon == particle.particleType
                 or ParticleType.Electron == particle.particleType):
            ptx += particle.momentum.values[1]
            pty += particle.momentum.values[2]
    beforeSq = ptx * ptx + pty * pty
    if beforeSq < 0.0:
        return 0.0
    return math.sqrt(beforeSq)


def PtSlashFilter(eventSample: EventSample) -> float:
    ptx = 0.0
    pty = 0.0
    for particle in eventSample.particles:
        if ParticleStatus.Invisible == particle.status:
            ptx += particle.momentum.values[1]
            pty += particle.momentum.values[2]
    beforeSq = ptx * ptx + pty * pty
    if beforeSq < 0.0:
        return 0.0
    return math.sqrt(beforeSq)


def LeptonCountFilter(eventSample: EventSample) -> float:
    return float(eventSample.GetLeptonCount())


def JetCountFilter(eventSample: EventSample) -> float:
    return float(eventSample.GetJetCount())


def MjjFilter(eventSample: EventSample) -> float:
    """
    (sum p)^2 of all jets
    :param eventSample:
    :return:
    """
    finalV = LorentzVector()
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status \
                and ParticleType.Jet == particle.particleType:
            finalV = finalV + particle.momentum
    beforeSqrt = 2.0 * (finalV * finalV)
    return math.sqrt(0.0 if beforeSqrt < 0.0 else beforeSqrt)


def Yjj2Filter(eventSample: EventSample) -> float:
    """
    Delta Pseudo Rapidity of the hardest two jets
    :param eventSample:
    :return:
    """
    largestJetIndex1 = 0
    largestJetM1 = 0.0
    largestJetIndex2 = 0
    largestJetM2 = 0.0
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status \
                and ParticleType.Jet == particle.particleType:
            momentum = particle.momentum.Momentum()
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
        return abs(p1.Y() - p2.Y())
    return 0.0


def Mjj2Filter(eventSample: EventSample) -> float:
    """
    The (p1+p2)^2 of largest (hardest) two jets
    :param eventSample:
    :return:
    """
    largestJetIndex1 = 0
    largestJetM1 = 0.0
    largestJetIndex2 = 0
    largestJetM2 = 0.0
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status \
                and ParticleType.Jet == particle.particleType:
            momentum = particle.momentum.Momentum()
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
        return math.sqrt(2.0 * (p1 * p2))
    return 0.0


def PjjFilter(eventSample: EventSample) -> float:
    """
    The $\vec{p1} \cdot \vec{p2}$ of the hardest two jets
    :param eventSample:
    :return:
    """
    largestJetIndex1 = 0
    largestJetM1 = 0.0
    largestJetIndex2 = 0
    largestJetM2 = 0.0
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status \
                and ParticleType.Jet == particle.particleType:
            momentum = particle.momentum.Momentum()
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
        return 2.0 * dot3d(p1.P3d(), p2.P3d())
    return 0.0


def MT_1_Plus(eventSample: EventSample) -> float:
    """
     sqrt( 2 Etmiss ptlepton (1- cos(phi)))
    :param eventSample:
    :return:
    """
    eTMissing = eventSample.GetETMissing()
    pTLepton = eventSample.GetPTLeptonPM(True)
    phiMissing = eventSample.GetPTMissingAzimuth()
    phiLepton = eventSample.GetPTLeptonAzimuthPM(True)
    beforeSqrt = 2.0 * eTMissing * pTLepton * (1.0 - math.cos(phiMissing - phiLepton))
    return math.sqrt(0.0 if beforeSqrt < 0.0 else beforeSqrt)


def MT_1_Minus(eventSample: EventSample) -> float:
    """
     sqrt( 2 Etmiss ptlepton (1- cos(phi)))
    :param eventSample:
    :return:
    """
    eTMissing = eventSample.GetETMissing()
    pTLepton = eventSample.GetPTLeptonPM(False)
    phiMissing = eventSample.GetPTMissingAzimuth()
    phiLepton = eventSample.GetPTLeptonAzimuthPM(False)
    beforeSqrt = 2.0 * eTMissing * pTLepton * (1.0 - math.cos(phiMissing - phiLepton))
    return math.sqrt(0.0 if beforeSqrt < 0.0 else beforeSqrt)


def LeptonDot(eventSample: EventSample) -> float:
    """
    This is very good for QGC operator with WW final state
    :param eventSample:
    :return:
    """
    leptonIdx1 = 0
    leptonIdx2 = 0
    lepton1Found = False
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 3:
            if not lepton1Found:
                lepton1Found = True
                leptonIdx1 = i
            else:
                leptonIdx2 = i
    p41 = eventSample.particles[leptonIdx1].momentum
    p42 = eventSample.particles[leptonIdx2].momentum
    return dot3d(normalize3d(p41.V3d()), normalize3d(p42.V3d()))


def LeptonMissingDot(eventSample: EventSample) -> float:
    """
    assume nu is close to l, so (pl1+pl2).(pn1+pn2) is close to 1
    :param eventSample:
    :return:
    """
    leptonIdx1 = 0
    leptonIdx2 = 0
    missingMomentum = LorentzVector()
    lepton1Found = False
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 3:
            if not lepton1Found:
                lepton1Found = True
                leptonIdx1 = i
            else:
                leptonIdx2 = i
        if ParticleType.Missing == eventSample.particles[i].particleType:
            missingMomentum = missingMomentum + eventSample.particles[i].momentum
    p41 = eventSample.particles[leptonIdx1].momentum
    p42 = eventSample.particles[leptonIdx2].momentum
    demon1 = (p41.values[1] + p42.values[1]) * (p41.values[1] + p42.values[1])
    demon1 = demon1 + (p41.values[2] + p42.values[2]) * (p41.values[2] + p42.values[2])
    demon2 = (missingMomentum.values[1] * missingMomentum.values[1]) + (
            missingMomentum.values[2] * missingMomentum.values[2])
    num = (p41.values[1] + p42.values[1]) * missingMomentum.values[1] + (p41.values[2] + p42.values[2]) * \
          missingMomentum.values[2]
    demon1 = demon1 * demon2
    if demon1 <= 1.0e-12:
        return 0.0
    demon1 = math.sqrt(demon1)
    return abs(num / demon1)


def LeptonMissingAmplitude(eventSample: EventSample) -> float:
    """
    assume nu is close to l, so (pl1+pl2).(pn1+pn2) is close to 1
    :param eventSample:
    :return:
    """
    leptonIdx1 = 0
    leptonIdx2 = 0
    missingMomentum = LorentzVector()
    lepton1Found = False
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 3:
            if not lepton1Found:
                lepton1Found = True
                leptonIdx1 = i
            else:
                leptonIdx2 = i
        if ParticleType.Missing == eventSample.particles[i].particleType:
            missingMomentum = missingMomentum + eventSample.particles[i].momentum
    p41 = eventSample.particles[leptonIdx1].momentum
    p42 = eventSample.particles[leptonIdx2].momentum
    demon1 = (p41.values[1] + p42.values[1]) * (p41.values[1] + p42.values[1])
    demon1 = demon1 + (p41.values[2] + p42.values[2]) * (p41.values[2] + p42.values[2])
    demon2 = (missingMomentum.values[1] * missingMomentum.values[1]) + (
            missingMomentum.values[2] * missingMomentum.values[2])
    return abs(demon1 - demon2)


def PTLandPTMissing(eventSample: EventSample) -> float:
    """
    This is Mo1 = sqrt( (|pl_T|+|pl_T|+|pmissing_T|)^2 -  (pl_T+pl_T+pmissing_T)^2)
    The momenta here are 3D
    :param eventSample:
    :return:
    """
    leptonIdx1 = 0
    leptonIdx2 = 0
    missingMomentum = LorentzVector()
    lepton1Found = False
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 3:
            if not lepton1Found:
                lepton1Found = True
                leptonIdx1 = i
            else:
                leptonIdx2 = i
        if ParticleType.Missing == eventSample.particles[i].particleType:
            missingMomentum = missingMomentum + eventSample.particles[i].momentum
    p41 = eventSample.particles[leptonIdx1].momentum
    p42 = eventSample.particles[leptonIdx2].momentum
    left = p41.Pt() + p42.Pt() + missingMomentum.Pt()
    missingMomentum = missingMomentum + p41
    missingMomentum = missingMomentum + p42
    right = missingMomentum.Pt()
    if left * left - right * right <= 0:
        return 0
    return math.sqrt(left * left - right * right)


def PhotonDegree(eventSample: EventSample) -> float:
    largestPhotonIdx = -1
    largestEa = -1.0
    for i in range(len(eventSample.particles)):
        if 0 == eventSample.particles[i].particleType:
            if eventSample.particles[i].momentum.values[0] > largestEa:
                largestEa = eventSample.particles[i].momentum.values[0]
                largestPhotonIdx = i
    momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
    return momentumPhoton.Theta()


def PhotonDegreeCS(eventSample: EventSample) -> float:
    largestPhotonIdx = -1
    largestEa = -1.0
    for i in range(len(eventSample.particles)):
        if 0 == eventSample.particles[i].particleType:
            if eventSample.particles[i].momentum.values[0] > largestEa:
                largestEa = eventSample.particles[i].momentum.values[0]
                largestPhotonIdx = i
    momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
    return math.cos(momentumPhoton.Theta())


def Megamma(eventSample: EventSample) -> float:
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
    momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
    momentumLepton = eventSample.particles[leptonIdx].momentum
    momentumPhoton = momentumPhoton + momentumLepton
    return momentumPhoton.Mass()


def ThetaEGamma(eventSample: EventSample) -> float:
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
    momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
    momentumLepton = eventSample.particles[leptonIdx].momentum
    return dot3d(normalize3d(momentumPhoton.V3d()), normalize3d(momentumLepton.V3d()))


def PhiGammaMissing(eventSample: EventSample) -> float:
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
    return math.cos(momentumPhoton.Azimuth() - momentumMissing.Azimuth())


def LpCornerMiddle(eventSample: EventSample) -> float:
    missingIdx = -1
    leptonIdx = -1
    largestPhotonIdx = -1
    largestEa = -1.0
    for i in range(len(eventSample.particles)):
        if 0 == eventSample.particles[i].particleType:
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
    cosThetaStar = 2 * (lp - 0.5)
    cosGammaTheta = abs(math.cos(momentumPhoton.Theta())) - 1.0
    radius = cosGammaTheta * cosGammaTheta + cosThetaStar * cosThetaStar
    return radius


def PhiLeptonMissing(eventSample: EventSample) -> float:
    leptonIdx = -1
    missingIdx = -1
    for i in range(len(eventSample.particles)):
        if 6 == eventSample.particles[i].particleType:
            missingIdx = i
        if 1 == eventSample.particles[i].particleType or 2 == eventSample.particles[i].particleType:
            leptonIdx = i
    momentumLepton = eventSample.particles[leptonIdx].momentum
    momentumMissing = eventSample.particles[missingIdx].momentum
    return math.cos(momentumLepton.Azimuth() - momentumMissing.Azimuth())


def LpFilter(eventSample: EventSample) -> float:
    missingIdx = -1
    leptonIdx = -1
    largestEa = -1.0
    for i in range(len(eventSample.particles)):
        if 0 == eventSample.particles[i].particleType:
            if eventSample.particles[i].momentum.values[0] > largestEa:
                largestEa = eventSample.particles[i].momentum.values[0]
        if 6 == eventSample.particles[i].particleType:
            missingIdx = i
        if 1 == eventSample.particles[i].particleType or 2 == eventSample.particles[i].particleType:
            leptonIdx = i
    pMissing = eventSample.particles[missingIdx].momentum
    pLepton = eventSample.particles[leptonIdx].momentum
    p2Wt = [pMissing.values[1] + pLepton.values[1], pMissing.values[2] + pLepton.values[2]]
    p2Lt = [pLepton.values[1], pLepton.values[2]]
    lp = (p2Lt[0] * p2Wt[0] + p2Lt[1] * p2Wt[1]) / (p2Wt[0] * p2Wt[0] + p2Wt[1] * p2Wt[1])
    return lp


def RadiusA(eventSample: EventSample) -> float:
    missingIdx = -1
    leptonIdx = -1
    largestEa = -1.0
    largestPhotonIdx = -1
    for i in range(len(eventSample.particles)):
        if 0 == eventSample.particles[i].particleType:
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
        return -1.0
    thetaPhoton = math.cos(momentumPhoton.Theta())
    return (1 - abs(thetaPhoton)) * (1 - abs(thetaPhoton)) + (lp - 0.5) * (lp - 0.5)


def RadiusB(eventSample: EventSample) -> float:
    """
    (1 - costheta)^2 + L_p^2
    """
    missingIdx = -1
    leptonIdx = -1
    largestEa = -1.0
    largestPhotonIdx = -1
    for i in range(len(eventSample.particles)):
        if 0 == eventSample.particles[i].particleType:
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
    # if lp < 0 or lp > 1:
    #    return -1.0
    thetaPhoton = math.cos(momentumPhoton.Theta())
    return (1 - abs(thetaPhoton)) * (1 - abs(thetaPhoton)) + lp * lp


def RadiusC(eventSample: EventSample) -> float:
    missingIdx = -1
    leptonIdx = -1
    largestEa = -1.0
    largestPhotonIdx = -1
    for i in range(len(eventSample.particles)):
        if 0 == eventSample.particles[i].particleType:
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
    # if lp < 0 or lp > 1:
    #    return -1.0
    thetaPhoton = math.cos(momentumPhoton.Theta())
    return (1 - abs(thetaPhoton)) * (1 - abs(thetaPhoton)) + (1 - lp) * (1 - lp)


def RadiusD(eventSample: EventSample) -> float:
    lp = LpFilter(eventSample)
    # if lp < 0 or lp > 1:
    #    return -1.0
    thetaPhoton = math.cos(PhotonDegree(eventSample))
    # print(lp, " and ", thetaPhoton)
    return (1.0 - abs(thetaPhoton)) + 8.0 * abs(0.5 - lp)


def SHatAW2(eventSample: EventSample) -> float:
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
    lengthMissingT = math.sqrt(pMissing.values[1] * pMissing.values[1] + pMissing.values[2] * pMissing.values[2])
    lengthLeptonT = math.sqrt(pLepton.values[1] * pLepton.values[1] + pLepton.values[2] * pLepton.values[2])
    alpha = 2
    if lengthLeptonT > 1.0e-12:
        alpha = lengthMissingT / lengthLeptonT
    pLargestPhotn = eventSample.particles[largestPhotonIdx].momentum
    pAll = pLepton + pLargestPhotn
    pMissing2 = LorentzVector(pLepton.values[0] * abs(alpha), pMissing.values[1], pMissing.values[2],
                              alpha * pLepton.values[3])
    pAll = pAll + pMissing2
    return pAll * pAll


def SHatAW(eventSample: EventSample) -> float:
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
    lengthMissingT = math.sqrt(pMissing.values[1] * pMissing.values[1] + pMissing.values[2] * pMissing.values[2])
    lengthLeptonT = math.sqrt(pLepton.values[1] * pLepton.values[1] + pLepton.values[2] * pLepton.values[2])
    alpha = 2
    if lengthLeptonT > 1.0e-12:
        alpha = lengthMissingT / lengthLeptonT
    pLargestPhoton = eventSample.particles[largestPhotonIdx].momentum
    pAll = pLepton + pLargestPhoton
    pMissing2 = LorentzVector(math.sqrt(pMissing.values[1] * pMissing.values[1]
                                        + pMissing.values[2] * pMissing.values[2]
                                        + pLepton.values[3] * pLepton.values[3] * alpha * alpha),
                              pMissing.values[1],
                              pMissing.values[2],
                              alpha * pLepton.values[3])
    pAll = pAll + pMissing2
    return pAll * pAll


def SHatAWReal(eventSample: EventSample) -> float:
    """
    pW + pW = pl + pl + pnu + pnu
    assume LHE file, so nu is visible
    :param eventSample:
    :return:
    """
    pall = LorentzVector(0, 0, 0, 0)
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 2:
            pall = pall + eventSample.particles[i].momentum
        if ParticleType.Missing == eventSample.particles[i].particleType:
            pall = pall + eventSample.particles[i].momentum
        if ParticleType.Photon == eventSample.particles[i].particleType:
            pall = pall + eventSample.particles[i].momentum
    return pall * pall


def SHatAWRealDebug(eventSample: EventSample) -> float:
    """
    pW + pW = pl + pl + pnu + pnu
    assume LHE file, so nu is visible
    :param eventSample:
    :return:
    """
    pall = LorentzVector(0, 0, 0, 0)
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 2:
            pall = pall + eventSample.particles[i].momentum
        if ParticleType.Missing == eventSample.particles[i].particleType:
            pall = pall + eventSample.particles[i].momentum
        if ParticleType.Photon == eventSample.particles[i].particleType:
            pall = pall + eventSample.particles[i].momentum
    print(pall)
    print(pall * pall)
    return pall * pall


def PhiLLM(eventSample: EventSample) -> float:
    leptonIdx1 = 0
    leptonIdx2 = 0
    pm = LorentzVector(0, 0, 0, 0)
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 2:
            if eventSample.particles[i].PGDid > 0:
                leptonIdx2 = i
            else:
                leptonIdx1 = i
        if ParticleType.Missing == eventSample.particles[i].particleType:
            pm = pm + eventSample.particles[i].momentum
    p1 = eventSample.particles[leptonIdx1].momentum
    p2 = eventSample.particles[leptonIdx2].momentum
    plx = p1.values[1] + p2.values[1]
    ply = p1.values[2] + p2.values[2]
    lengthLepton = math.sqrt(plx * plx + ply * ply)
    lengthM = math.sqrt(pm.values[1] ** 2 + pm.values[2] ** 2)
    return abs((pm.values[1] * plx + pm.values[2] * ply) / (lengthLepton * lengthM))


def SHatWW(eventSample: EventSample) -> float:
    """
    pW + pW = pl + pl + pnu + pnu
    :param eventSample:
    :return:
    """
    leptonIdx1 = 0
    leptonIdx2 = 0
    pm = LorentzVector(0, 0, 0, 0)
    bAllLeptonFound = 0
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 2:
            if eventSample.particles[i].PGDid > 0:
                leptonIdx2 = i
                bAllLeptonFound = bAllLeptonFound + 1
            else:
                leptonIdx1 = i
                bAllLeptonFound = bAllLeptonFound + 1
        if ParticleType.Missing == eventSample.particles[i].particleType:
            pm = pm + eventSample.particles[i].momentum
    p1 = eventSample.particles[leptonIdx1].momentum
    p2 = eventSample.particles[leptonIdx2].momentum
    kappa = p1.values[2] * p2.values[1] - p1.values[1] * p2.values[2]
    if abs(kappa) < 0.000001:
        return 169000000.0
    u = (pm.values[2] * p2.values[1] - pm.values[1] * p2.values[2]) / kappa
    v = -(pm.values[2] * p1.values[1] - pm.values[1] * p1.values[2]) / kappa
    final = ((1 + abs(u)) * p1.values[0] + (1 + abs(v)) * p2.values[0]) ** 2
    final = final - (((1 + u) * p1.values[3] + (1 + v) * p2.values[3]) ** 2)
    final = final - ((p1.values[1] + p2.values[1] + pm.values[1]) ** 2)
    final = final - ((p1.values[2] + p2.values[2] + pm.values[2]) ** 2)
    return min(abs(final), 169000000.0)


def SHatWWUV(eventSample: EventSample):
    """
    pW + pW = pl + pl + pnu + pnu
    :param eventSample:
    :return:
    """
    leptonIdx1 = 0
    leptonIdx2 = 0
    pm = LorentzVector(0, 0, 0, 0)
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 3:
            if eventSample.particles[i].PGDid > 0:
                leptonIdx2 = i
            else:
                leptonIdx1 = i
        if ParticleType.Missing == eventSample.particles[i].particleType:
            pm = pm + eventSample.particles[i].momentum
    p1 = eventSample.particles[leptonIdx1].momentum
    p2 = eventSample.particles[leptonIdx2].momentum
    kappa = p1.values[2] * p2.values[1] - p1.values[1] * p2.values[2]
    # if abs(kappa) < 10:
    #    return [-1.0, -1.0]
    u = (pm.values[2] * p2.values[1] - pm.values[1] * p2.values[2]) / kappa
    v = -(pm.values[2] * p1.values[1] - pm.values[1] * p1.values[2]) / kappa
    return [u, v]


def SHatWWDebug(eventSample: EventSample) -> float:
    """
    pW + pW = pl + pl + pnu + pnu
    :param eventSample:
    :return:
    """
    leptonIdx1 = 0
    leptonIdx2 = 0
    pm = LorentzVector(0, 0, 0, 0)
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 3:
            if eventSample.particles[i].PGDid > 0:
                leptonIdx2 = i
            else:
                leptonIdx1 = i
        if ParticleType.Missing == eventSample.particles[i].particleType:
            pm = pm + eventSample.particles[i].momentum
    p1 = eventSample.particles[leptonIdx1].momentum
    p2 = eventSample.particles[leptonIdx2].momentum
    kappa = p1.values[2] * p2.values[1] - p1.values[1] * p2.values[2]
    u = (pm.values[2] * p2.values[1] - pm.values[1] * p2.values[2]) / kappa
    v = -(pm.values[2] * p1.values[1] - pm.values[1] * p1.values[2]) / kappa
    k = 1
    print(u)
    print(v)
    if u < 0 or v < 0:
        u = 1
        v = 1
        k = 0
    final = ((1 + u) * p1.values[0] + (1 + v) * p2.values[0]) ** 2
    final = final - (((1 + u) * p1.values[3] + (1 + v) * p2.values[3]) ** 2) * k
    final = final - ((p1.values[1] + p2.values[1] + pm.values[1]) ** 2)
    final = final - ((p1.values[2] + p2.values[2] + pm.values[2]) ** 2)
    print(p1.Scale(u))
    print(p2.Scale(v))
    return final


def SHatWWReal(eventSample: EventSample) -> float:
    """
    pW + pW = pl + pl + pnu + pnu
    assume LHE file, so nu is visible
    :param eventSample:
    :return:
    """
    pall = LorentzVector(0, 0, 0, 0)
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 2:
            pall = pall + eventSample.particles[i].momentum
        if ParticleType.Missing == eventSample.particles[i].particleType:
            pall = pall + eventSample.particles[i].momentum
    return pall * pall


def SHatWWRealDebug(eventSample: EventSample) -> LorentzVector:
    """
    pW + pW = pl + pl + pnu + pnu
    assume LHE file, so nu is visible
    :param eventSample:
    :return:
    """
    pall = LorentzVector(0, 0, 0, 0)
    for i in range(len(eventSample.particles)):
        if 1 <= eventSample.particles[i].particleType <= 2:
            pall = pall + eventSample.particles[i].momentum
        if ParticleType.Missing == eventSample.particles[i].particleType:
            pall = pall + eventSample.particles[i].momentum
    return pall


def MinDrll(eventSample: EventSample) -> float:
    leptonMomentums = []
    for particle in eventSample.particles:
        if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
            leptonMomentums.append(particle.momentum)
    if len(leptonMomentums) < 2:
        return 0
    mindr = -1
    for i in range(0, len(leptonMomentums)):
        for j in range(i + 1, len(leptonMomentums)):
            deltaPhi = LorentzVector.DeltaPhi(leptonMomentums[i], leptonMomentums[j])
            eta1 = leptonMomentums[i].PseudoRapidity()
            eta2 = leptonMomentums[j].PseudoRapidity()
            dr = (eta1 - eta2) * (eta1 - eta2) + deltaPhi * deltaPhi
            if dr < 0:
                dr = 0
            dr = math.sqrt(dr)
            if mindr < 0 or dr < mindr:
                mindr = dr
    return mindr
