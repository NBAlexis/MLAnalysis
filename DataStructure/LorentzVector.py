import math
import sys


class LorentzVector:

    def __init__(self, t: float = 0.0, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.values = [t, x, y, z]

    def __str__(self) -> str:
        return "({0}, {1}, {2}, {3})".format(self.values[0], self.values[1], self.values[2], self.values[3])

    def __mul__(self, other) -> float:
        return self.values[0] * other.values[0] \
               - self.values[1] * other.values[1] \
               - self.values[2] * other.values[2] \
               - self.values[3] * other.values[3]

    def __rmul__(self, other) -> float:
        return self.__mul__(other)

    def __add__(self, other):
        return LorentzVector(self.values[0] + other.values[0],
                             self.values[1] + other.values[1],
                             self.values[2] + other.values[2],
                             self.values[3] + other.values[3])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return LorentzVector(self.values[0] - other.values[0],
                             self.values[1] - other.values[1],
                             self.values[2] - other.values[2],
                             self.values[3] - other.values[3])

    @staticmethod
    def MakeRest():
        return LorentzVector(1, 0, 0, 0)

    # eta = Pseudo Rapidity
    # theta = 2 atan(exp(-eta))
    # p = pt / sin(theta)
    # E = sqrt(p ^ 2 + m ^ 2)
    # v = (E, p sin theta cos phi, p sin theta sin phi, p cos theta)
    @staticmethod
    def MakeWithRapidity(pseudoRapidity: float, azimuthal: float, pt: float, mass: float = 0):
        ret = LorentzVector()
        theta = 2 * math.atan(math.exp(-pseudoRapidity))
        p = pt / math.sin(theta)
        ret.values[0] = math.sqrt(p * p + mass * mass)
        ret.values[1] = pt * math.cos(azimuthal)
        ret.values[2] = pt * math.sin(azimuthal)
        ret.values[3] = p * math.cos(theta)
        return ret

    def V3d(self):
        return [self.values[1] / self.values[0], self.values[2] / self.values[0], self.values[3] / self.values[0]]

    def P3d(self):
        return [self.values[1], self.values[2], self.values[3]]

    def MassSq(self) -> float:
        return self.values[0] * self.values[0] - (
                    self.values[1] * self.values[1] + self.values[2] * self.values[2] + self.values[3] * self.values[3])

    def Mass(self) -> float:
        beforeSqrt = self.values[0] * self.values[0] - (
                    self.values[1] * self.values[1] + self.values[2] * self.values[2] + self.values[3] * self.values[3])
        return math.sqrt(0.0 if beforeSqrt < 0.0 else beforeSqrt)

    def Momentum(self) -> float:
        return math.sqrt(
            self.values[1] * self.values[1] + self.values[2] * self.values[2] + self.values[3] * self.values[3])

    # PseudoRapidity = - log (tan(theta / 2)) \approx y
    def PseudoRapidity(self) -> float:
        momentum = self.Momentum()
        if momentum < 1.0e-12:
            return 0.0
        cs = self.values[3] / momentum
        if cs > 1:
            cs = 1
        elif cs < -1:
            cs = -1
        beforelog = math.tan(math.acos(cs) / 2)
        if beforelog <= 0:
            beforelog = 1.0e-12
        return -math.log(beforelog)

    def R(self) -> float:
        eta = self.PseudoRapidity()
        phi = self.Azimuth()
        ToBeSqrt = eta * eta + phi * phi
        if ToBeSqrt < 0:
            return 0.0
        return math.sqrt(ToBeSqrt)

    # Rapidity = log((E + pz) / (E - pz)) / 2
    def Y(self) -> float:
        denominator = self.values[0] - self.values[3]
        if denominator <= 0:
            return sys.float_info.max
        denominator = (self.values[0] + self.values[3]) / denominator
        if denominator <= 0:
            return sys.float_info.max
        return 0.5 * math.log(denominator)

    def Pt(self) -> float:
        return math.sqrt(self.values[1] * self.values[1] + self.values[2] * self.values[2])

    def ToPt(self):
        return LorentzVector(self.values[0], self.values[1], self.values[2], 0.0)

    def Scale(self, scale: float):
        return LorentzVector(self.values[0] * scale, self.values[1] * scale, self.values[2] * scale,
                             self.values[3] * scale)

    def Et(self) -> float:
        mass = self.Mass()
        return math.sqrt(self.values[1] * self.values[1] + self.values[2] * self.values[2] + mass * mass)

    # calculate phi
    def Azimuth(self) -> float:
        return math.atan2(self.values[2], self.values[1])

    # calculate Theta
    def Theta(self):
        mass = self.MassSq()
        kValue = self.values[0] * self.values[0] - mass
        if kValue > 0.0:
            kValue = math.sqrt(kValue)
        else:
            return 0
        if abs(kValue) > abs(self.values[3]):
            return math.acos(self.values[3] / kValue)
        else:
            if self.values[3] > 0.0:
                return 0
            else:
                return math.pi

    @staticmethod
    def DeltaPhi(v1, v2) -> float:
        dot = v1.values[1] * v2.values[1] + v1.values[2] * v2.values[2]
        l1 = v1.values[1] * v1.values[1] + v1.values[2] * v1.values[2]
        l2 = v2.values[1] * v2.values[1] + v2.values[2] * v2.values[2]
        if l1 * l2 > 1.0e-20:
            tobeacos = dot / math.sqrt(l1 * l2)
            if tobeacos > 1.0:
                tobeacos = 1.0
            elif tobeacos < -1.0:
                tobeacos = -1.0
            return math.acos(tobeacos)
        return 0

    @staticmethod
    def DeltaR(v1, v2) -> float:
        deltaPhi = LorentzVector.DeltaPhi(v1, v2)
        deltaEta = v1.PseudoRapidity() - v2.PseudoRapidity()
        return math.sqrt(deltaPhi * deltaPhi + deltaEta * deltaEta + 1.0e-8)
