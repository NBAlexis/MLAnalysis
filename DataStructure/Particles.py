from enum import IntEnum

# To new, call with ParticleStatus(-1)
from DataStructure.LorentzVector import LorentzVector

PGDIdToName = {
    1: "d",
    2: "u",
    3: "s",
    4: "c",
    5: "b",
    6: "t",
    -1: "dbar",
    -2: "ubar",
    -3: "sbar",
    -4: "cbar",
    -5: "bbar",
    -6: "tbar",
    11: "e-",
    12: "ve",
    13: "mu-",
    14: "vmu",
    15: "tau-",
    16: "vtau",
    -11: "e+",
    -12: "vebar",
    -13: "mu+",
    -14: "vmubar",
    -15: "tau+",
    -16: "vtaubar",
    22: "a",
    23: "Z",
    24: "W+",
    -24: "W-"
}


class ParticleStatus(IntEnum):
    Incoming = -1  # –1 Incoming particle
    Outgoing = 1  # +1 Outgoing final state particle
    IntermediateSpaceLick = -2  # –2 Intermediate space-like propagator defining an x and Q2 which should be preserved
    IntermediateResonanceMassPreserved = 2  # +2 Intermediate resonance, Mass should be preserved
    IntermediateResonance = 3  # +3 Intermediate resonance, for documentation only4
    IncomingBeam = -9  # –9 Incoming beam particles at time t = −INFINITY
    Invisible = 10


class ParticleType(IntEnum):
    Photon = 0
    Electron = 1
    Muon = 2
    Tau = 3
    Jet = 4
    Intermediate = 5
    Missing = 6


class Particle:

    def __init__(self,
                 index: int,
                 PGDid: int,
                 particleType: ParticleType,
                 status: ParticleStatus,
                 momentum: LorentzVector,
                 mass: float,
                 decayLength: float,
                 hecility: float
                 ):
        self.index = index
        self.PGDid = PGDid
        self.particleType = particleType
        self.status = status
        self.momentum = momentum
        self.mass = mass
        self.decayLength = decayLength
        self.hecility = hecility
        self.nTrack = 0
        self.bTag = 0
        self.hadEm = 0

    def SetLHCOOtherInfo(self, nTrack: float, bTag: float, hadEm: float):
        self.nTrack = nTrack
        self.bTag = bTag
        self.hadEm = hadEm

    def __str__(self) -> str:
        return self.DebugPrint()

    def DebugPrint(self, sep: str = ", ") -> str:
        return "{: >3d}{}{: >5d}{}{: >2d}{}{}{}{:+.8e}{}{:+.8e}{}{:+.8e}{}{:+.8e}{}{:+.8e}{}{:+.8e}, {}" \
            .format(self.index, sep,
                    self.PGDid, sep,
                    self.status, sep,
                    self.particleType, sep,
                    self.mass, sep,
                    self.momentum.values[0], sep,
                    self.momentum.values[1], sep,
                    self.momentum.values[2], sep,
                    self.momentum.values[3], sep,
                    self.hecility,
                    PGDIdToName.get(self.PGDid))
