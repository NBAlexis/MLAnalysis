import math

from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import Particle, ParticleStatus, ParticleType


class EventSample:
    def __init__(self):
        self.particles = []

    def AddParticle(self, particle: Particle):
        particle.index = len(self.particles) + 1
        self.particles.append(particle)

    def GetParticleCount(self) -> int:
        return len(self.particles)

    def GetLeptonCount(self) -> int:
        leptonCount = 0
        for particle in self.particles:
            if 1 <= particle.particleType <= 3:
                leptonCount += 1
        return leptonCount

    def GetJetCount(self) -> int:
        jetCount = 0
        for particle in self.particles:
            if 4 == particle.particleType:
                jetCount += 1
        return jetCount

    def GetPhotonCount(self) -> int:
        photonCount = 0
        for particle in self.particles:
            if ParticleType.Photon == particle.particleType:
                photonCount += 1
        return photonCount

    def GetPTMissing2d(self) -> list:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Invisible == particle.status:
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return [ptx, pty]

    def GetETMissing(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Invisible == particle.status:
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return math.sqrt(ptx * ptx + pty * pty)

    def GetPTMissingAzimuth(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Invisible == particle.status:
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return math.atan2(pty, ptx)

    def GetPTLepton(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Outgoing == particle.status and \
                    (ParticleType.Electron == particle.particleType
                     or ParticleType.Muon == particle.particleType
                     or ParticleType.Tau == particle.particleType):
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return math.sqrt(ptx * ptx + pty * pty)

    def GetPTLeptonAzimuth(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Outgoing == particle.status and \
                    (ParticleType.Electron == particle.particleType
                     or ParticleType.Muon == particle.particleType
                     or ParticleType.Tau == particle.particleType):
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return math.atan2(pty, ptx)

    def GetPTLeptonPM(self, bPM: bool) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Outgoing == particle.status and \
                    (ParticleType.Electron == particle.particleType
                     or ParticleType.Muon == particle.particleType
                     or ParticleType.Tau == particle.particleType):
                if bPM and particle.PGDid < 0:
                    ptx += particle.momentum.values[1]
                    pty += particle.momentum.values[2]
                elif (not bPM) and particle.PGDid > 0:
                    ptx += particle.momentum.values[1]
                    pty += particle.momentum.values[2]
        return math.sqrt(ptx * ptx + pty * pty)

    def GetPTLeptonAzimuthPM(self, bPM: bool) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Outgoing == particle.status and \
                    (ParticleType.Electron == particle.particleType
                     or ParticleType.Muon == particle.particleType
                     or ParticleType.Tau == particle.particleType):
                if bPM and particle.PGDid < 0:
                    ptx += particle.momentum.values[1]
                    pty += particle.momentum.values[2]
                elif (not bPM) and particle.PGDid > 0:
                    ptx += particle.momentum.values[1]
                    pty += particle.momentum.values[2]
        return math.atan2(pty, ptx)

    def RecalculateMissing(self, vSum: LorentzVector):
        newparticle = []
        allMomentum = LorentzVector(0, 0, 0, 0)
        for particle in self.particles:
            if ParticleType.Missing != particle.particleType:
                particle.index = len(newparticle) + 1
                newparticle.append(particle)
                allMomentum = allMomentum + particle.momentum
        missingmomentum = vSum - allMomentum
        oneParticle = Particle(
            len(newparticle) + 1,  # index
            12,  # PGD
            ParticleType.Missing,  # Particle Type
            ParticleStatus.Invisible,  # Status
            missingmomentum,  # Momentum
            0,  # Mass
            0.0,  # Decay Length
            0.0  # Hecility
        )
        newparticle.append(oneParticle)
        self.particles = newparticle

    def DebugPrint(self) -> str:
        ret = "PID  PGDID  ST  T  ---MASS(GeV)---  MOMENTUM_T(GeV)  MOMENTUM_X(GeV)  MOMENTUM_Y(GeV)  MOMENTUM_Z(GeV)  ----HECILITY---\n"
        for i in range(len(self.particles)):
            ret += self.particles[i].DebugPrint() + "\n"
        return ret
