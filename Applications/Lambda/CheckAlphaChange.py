from math import *

from DataStructure.Matrix4x4 import *
from DataStructure.LorentzVector import *

krest = 0.10058
k0proton = 0.943648
k0pion = 0.172035
vlambda = 0.6932
m = 6
thetalambda = 3.14159265359 * (1 - ((m - 0.5) / 40.0))
maximumAllowedAngle = 0.93
minpt = 0.05

matrixres = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
allcount = 0

for sx in range(0, 3):
    nxsum = 0.0
    nysum = 0.0
    nzsum = 0.0
    ncount = 0
    fileName: str = "../../_DataFolder/lambda/res{}-6.csv".format(sx)
    with open(fileName) as f:
        for lines in f.readlines():
            allcount = allcount + 1
            print("{} / 25165824".format(allcount))
            valueList = lines.split(',')
            nlist = [float(valueList[0]), float(valueList[1]), float(valueList[2])]
            p1 = LorentzVector(k0proton, -krest * nlist[0], -krest * nlist[1], -krest * nlist[2])
            p2 = LorentzVector(k0pion, -p1.values[1], -p1.values[2], -p1.values[3])
            boostback = Matrix4x4.MakeBoost([0, 0, -vlambda])
            rotback = Matrix4x4.MakeRotationFromTo([0, 0, 1], [sin(thetalambda), 0, cos(thetalambda)])
            p1lab = boostback.MultiplyVector(p1)
            p1lab = rotback.MultiplyVector(p1lab)
            p2lab = boostback.MultiplyVector(p2)
            p2lab = rotback.MultiplyVector(p2lab)
            if abs(cos(p1lab.Theta())) > maximumAllowedAngle:
                continue
            if abs(cos(p2lab.Theta())) > maximumAllowedAngle:
                continue
            if p1lab.Pt() < minpt or p2lab.Pt() < minpt:
                continue
            nxsum = nxsum + nlist[0]
            nysum = nysum + nlist[1]
            nzsum = nzsum + nlist[2]
            ncount = ncount + 1
    if ncount > 0:
        matrixres[sx][0] = nxsum / ncount
        matrixres[sx][1] = nysum / ncount
        matrixres[sx][2] = nzsum / ncount
        print("(s:{}, theta:{}, count:{}): ({}, {}, {})".format(sx, m, ncount, nxsum / ncount, nysum / ncount,
                                                                nzsum / ncount))
    else:
        print("s:{}, theta:{}, ncount = 0", sx, m)

print("matrix = {{ {{{}, {}, {}}}, {{{}, {}, {}}}, {{{}, {}, {}}} }};".format(
    matrixres[0][0], matrixres[1][0], matrixres[2][0],
    matrixres[0][1], matrixres[1][1], matrixres[2][1],
    matrixres[0][2], matrixres[1][2], matrixres[2][2]))

"""
res:

w=1:

w=2:


"""
