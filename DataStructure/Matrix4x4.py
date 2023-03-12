import math
from DataStructure import Constants
from DataStructure.LorentzVector import LorentzVector


class Matrix4x4:

    def __init__(self, values=None):
        if values is None:
            values = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.values = values

    @staticmethod
    def MakeZero():
        return Matrix4x4()

    @staticmethod
    def MakeOne():
        return Matrix4x4([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    @staticmethod
    def MakeRotation(degree: float, x: float, y: float, z: float):
        """
        assume x, y, z is a unit vector
        :param degree:
        :param x:
        :param y:
        :param z:
        :return:
        """
        cs = math.cos(degree)
        sn = math.sin(degree)
        ret = Matrix4x4()
        ret.values[0][0] = 1
        ret.values[1] = [0, cs + (1 - cs) * x * x, (1 - cs) * x * y - sn * z, (1 - cs) * x * z + sn * y]
        ret.values[2] = [0, (1 - cs) * x * y + sn * z, cs + (1 - cs) * y * y, (1 - cs) * y * z - sn * x]
        ret.values[3] = [0, (1 - cs) * x * z - sn * y, (1 - cs) * y * z + sn * x, cs + (1 - cs) * z * z]
        return ret

    @staticmethod
    def MakeRotationFromTo(v3from, v3to):
        cr3d = Constants.cross3d(v3from, v3to)
        lengthXYZ = math.sqrt(Constants.dot3d(cr3d, cr3d))
        if lengthXYZ < Constants.minFloat:
            return Matrix4x4.MakeOne()
        x = cr3d[0] / lengthXYZ
        y = cr3d[1] / lengthXYZ
        z = cr3d[2] / lengthXYZ
        degree = math.atan2(lengthXYZ, Constants.dot3d(v3from, v3to))
        return Matrix4x4.MakeRotation(degree, x, y, z)

    @staticmethod
    def MakeRotationFromToV4(v4from: LorentzVector, v4to: LorentzVector):
        return Matrix4x4.MakeRotationFromTo(v4from.V3d(), v4to.V3d())

    @staticmethod
    def MakeBoost(v3velocity):
        vsq = Constants.dot3d(v3velocity, v3velocity)
        ga = 1 / math.sqrt(1 - vsq)
        ret = Matrix4x4()
        x = v3velocity[0]
        y = v3velocity[1]
        z = v3velocity[2]
        ret.values[0] = [ga, -ga * x, -ga * y, -ga * z]
        ret.values[1] = [-ga * x, (ga - 1) * x * x / vsq + 1, (ga - 1) * x * y / vsq, (ga - 1) * x * z / vsq]
        ret.values[2] = [-ga * y, (ga - 1) * y * x / vsq, (ga - 1) * y * y / vsq + 1, (ga - 1) * y * z / vsq]
        ret.values[3] = [-ga * z, (ga - 1) * z * x / vsq, (ga - 1) * z * y / vsq, (ga - 1) * z * z / vsq + 1]
        return ret

    def MultiplyMatrix(self, otherMatrix):
        ret = Matrix4x4()
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    ret.values[i][j] += self.values[i][k] * otherMatrix.values[k][j]
        return ret

    def MultiplyVector(self, vector: LorentzVector) -> LorentzVector:
        ret = LorentzVector()
        for i in range(4):
            for j in range(4):
                ret.values[i] += self.values[i][j] * vector.values[j]
        return ret
