import math

from DataStructure import Constants
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Matrix4x4 import Matrix4x4


def NComponentTest(eventSet: EventSet, idx: int):
    wpIndex = 0
    wmIndex = 0
    lpIndex = 0
    lmIndex = 0
    xList = []
    yList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if 24 == eventSample.particles[i].PGDid:
                wpIndex = i
            if -24 == eventSample.particles[i].PGDid:
                wmIndex = i
            if -11 == eventSample.particles[i].PGDid or -13 == eventSample.particles[i].PGDid or -15 == \
                    eventSample.particles[i].PGDid:
                lpIndex = i
            if 11 == eventSample.particles[i].PGDid or 13 == eventSample.particles[i].PGDid or 15 == \
                    eventSample.particles[i].PGDid:
                lmIndex = i
        p4wp = eventSample.particles[wpIndex].momentum
        p4wm = eventSample.particles[wmIndex].momentum
        p4lp = eventSample.particles[lpIndex].momentum
        p4lm = eventSample.particles[lmIndex].momentum
        rotMatrixWp = Matrix4x4.MakeRotationFromTo(p4wp.V3d(), [0.0, 0.0, 1.0])
        p4lpTowpDir = rotMatrixWp.MultiplyVector(p4lp)
        p4wpTowpDir = rotMatrixWp.MultiplyVector(p4wp)
        p4lpInwpRest = Matrix4x4.MakeBoost(p4wpTowpDir.V3d()).MultiplyVector(p4lpTowpDir)
        p3lp = Constants.normalize3d(p4lpInwpRest.P3d())
        xList.append(p3lp[idx])
        rotMatrixWm = Matrix4x4.MakeRotationFromTo(p4wm.V3d(), [0.0, 0.0, 1.0])
        p4lmTowpDir = rotMatrixWm.MultiplyVector(p4lm)
        p4wmTowpDir = rotMatrixWm.MultiplyVector(p4wm)
        p4lmInwpRest = Matrix4x4.MakeBoost(p4wmTowpDir.V3d()).MultiplyVector(p4lmTowpDir)
        p3lm = Constants.normalize3d(p4lmInwpRest.P3d())
        yList.append(p3lm[idx])
    import matplotlib.pyplot as plt
    plt.scatter(xList, yList, s=1)
    plt.show()


def WLTest(eventSet: EventSet):
    wpIndex = 0
    wmIndex = 0
    lpIndex = 0
    lmIndex = 0
    xList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if 24 == eventSample.particles[i].PGDid:
                wpIndex = i
            if -24 == eventSample.particles[i].PGDid:
                wmIndex = i
            if -11 == eventSample.particles[i].PGDid or -13 == eventSample.particles[i].PGDid or -15 == \
                    eventSample.particles[i].PGDid:
                lpIndex = i
            if 11 == eventSample.particles[i].PGDid or 13 == eventSample.particles[i].PGDid or 15 == \
                    eventSample.particles[i].PGDid:
                lmIndex = i
        p4wp = eventSample.particles[wpIndex].momentum
        p4wm = eventSample.particles[wmIndex].momentum
        p4lp = eventSample.particles[lpIndex].momentum
        p4lm = eventSample.particles[lmIndex].momentum
        dot1 = Constants.dot3d(Constants.normalize3d(p4wp.P3d()), Constants.normalize3d(p4lp.P3d()))
        dot2 = Constants.dot3d(Constants.normalize3d(p4wm.P3d()), Constants.normalize3d(p4lm.P3d()))
        mindot = min(dot1, dot2)
        if mindot < 0:
            xList.append(mindot)
    import matplotlib.pyplot as plt
    plt.hist(xList, 100)
    plt.show()


def WOnShellTest(eventSet: EventSet):
    wpIndex = 0
    wmIndex = 0
    xList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if 24 == eventSample.particles[i].PGDid:
                wpIndex = i
            if -24 == eventSample.particles[i].PGDid:
                wmIndex = i
        p4wp = eventSample.particles[wpIndex].momentum
        p4wm = eventSample.particles[wmIndex].momentum
        maxDeviate = max(abs(p4wp.Mass() - 80.4), abs(p4wm.Mass() - 80.4))
        xList.append(maxDeviate)
    import matplotlib.pyplot as plt
    plt.hist(xList, 100)
    plt.show()


def WBosonCorrelate(eventSet: EventSet):
    wpIndex = 0
    wmIndex = 0
    vList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if 24 == eventSample.particles[i].PGDid:
                wpIndex = i
            if -24 == eventSample.particles[i].PGDid:
                wmIndex = i
        vList.append(Constants.dot3d(eventSample.particles[wpIndex].momentum.V3d(),
                                     eventSample.particles[wmIndex].momentum.V3d()))
    import matplotlib.pyplot as plt
    plt.hist(vList, 10)
    plt.show()


def LeptonCorrelationTest(eventSet: EventSet, idx: int):
    lpIndex = 0
    lmIndex = 0
    xList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if -11 == eventSample.particles[i].PGDid or -13 == eventSample.particles[i].PGDid or -15 == \
                    eventSample.particles[i].PGDid:
                lpIndex = i
            if 11 == eventSample.particles[i].PGDid or 13 == eventSample.particles[i].PGDid or 15 == \
                    eventSample.particles[i].PGDid:
                lmIndex = i
        p4lp = eventSample.particles[lpIndex].momentum
        p4lm = eventSample.particles[lmIndex].momentum
        rotMatrix = Matrix4x4.MakeRotationFromTo(p4lp.V3d(), [0.0, 0.0, 1.0])
        # p4lpToLpDir = rotMatrix.MultiplyVector(p4lp)
        p4lmToLpDir = rotMatrix.MultiplyVector(p4lm)
        # p4lmRest = Matrix4x4.MakeBoost(p4lpToLpDir.V3d()).MultiplyVector(p4lmToLpDir)
        p3lm = Constants.normalize3d(p4lmToLpDir.P3d())
        xList.append(p3lm[idx])
    import matplotlib.pyplot as plt
    plt.hist(xList, 100)
    plt.show()


def ELeptonCutTest(eventSet: EventSet):
    lpIndex = 0
    lmIndex = 0
    xList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if -11 == eventSample.particles[i].PGDid or -13 == eventSample.particles[i].PGDid or -15 == \
                    eventSample.particles[i].PGDid:
                lpIndex = i
            if 11 == eventSample.particles[i].PGDid or 13 == eventSample.particles[i].PGDid or 15 == \
                    eventSample.particles[i].PGDid:
                lmIndex = i
        p4lp = eventSample.particles[lpIndex].momentum
        p4lm = eventSample.particles[lmIndex].momentum
        minE = min(p4lp.Momentum(), p4lm.Momentum())
        if minE < 4000:
            xList.append(minE)
    import matplotlib.pyplot as plt
    plt.hist(xList, 100)
    plt.show()


def LeptonCorrelationTest2(eventSet: EventSet, idx: int):
    lpIndex = 0
    lmIndex = 0
    xList = []
    yList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if -11 == eventSample.particles[i].PGDid or -13 == eventSample.particles[i].PGDid or -15 == \
                    eventSample.particles[i].PGDid:
                lpIndex = i
            if 11 == eventSample.particles[i].PGDid or 13 == eventSample.particles[i].PGDid or 15 == \
                    eventSample.particles[i].PGDid:
                lmIndex = i
        p4lp = eventSample.particles[lpIndex].momentum
        p4lm = eventSample.particles[lmIndex].momentum
        # Infer wp momentum by lp momentum
        elp = p4lp.Momentum()
        if elp < 41:
            continue
        pwp = (4.0 * elp * elp - 80.379 * 80.379) / (4.0 * elp)
        p4wp = LorentzVector(math.sqrt(pwp * pwp + 80.379 * 80.379),
                             pwp * p4lp.values[1] / elp,
                             pwp * p4lp.values[2] / elp,
                             pwp * p4lp.values[3] / elp)
        # Infer wm momentum by lm momentum
        elm = p4lm.Momentum()
        if elm < 41:
            continue
        pwm = (4.0 * elm * elm - 80.379 * 80.379) / (4.0 * elm)
        p4wm = LorentzVector(math.sqrt(pwm * pwm + 80.379 * 80.379),
                             pwm * p4lm.values[1] / elm,
                             pwm * p4lm.values[2] / elm,
                             pwm * p4lm.values[3] / elm)
        # Calculate correlation
        # print(p4lp.values)
        # print(p4wp.values)
        rotMatrixWp = Matrix4x4.MakeRotationFromTo(p4wp.V3d(), [0.0, 0.0, 1.0])
        p4lpTowpDir = rotMatrixWp.MultiplyVector(p4lp)
        p4wpTowpDir = rotMatrixWp.MultiplyVector(p4wp)
        p4lpInwpRest = Matrix4x4.MakeBoost(p4wpTowpDir.V3d()).MultiplyVector(p4lpTowpDir)
        p3lp = Constants.normalize3d(p4lpInwpRest.P3d())
        xList.append(p3lp[idx])
        rotMatrixWm = Matrix4x4.MakeRotationFromTo(p4wm.V3d(), [0.0, 0.0, 1.0])
        p4lmTowpDir = rotMatrixWm.MultiplyVector(p4lm)
        p4wmTowpDir = rotMatrixWm.MultiplyVector(p4wm)
        p4lmInwpRest = Matrix4x4.MakeBoost(p4wmTowpDir.V3d()).MultiplyVector(p4lmTowpDir)
        p3lm = Constants.normalize3d(p4lmInwpRest.P3d())
        yList.append(p3lm[idx])
    import matplotlib.pyplot as plt
    print(len(xList))
    plt.scatter(xList, yList, s=1)
    plt.show()


def PXMissingTest(eventSet: EventSet):
    lpIndex = 0
    lmIndex = 0
    # xList = []
    yList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if -11 == eventSample.particles[i].PGDid or -13 == eventSample.particles[i].PGDid or -15 == \
                    eventSample.particles[i].PGDid:
                lpIndex = i
            if 11 == eventSample.particles[i].PGDid or 13 == eventSample.particles[i].PGDid or 15 == \
                    eventSample.particles[i].PGDid:
                lmIndex = i
        p4lp = eventSample.particles[lpIndex].momentum
        p4lm = eventSample.particles[lmIndex].momentum
        ptMissing = eventSample.GetPTMissing2d()
        etMissing = eventSample.GetETMissing()
        elp = p4lp.Momentum()
        elm = p4lm.Momentum()
        # xList.append((ptMissing[0]
        #               + p4lp.values[1] * 80.379 * 80.379 / (4.0 * elp * elp)
        #               + p4lm.values[1] * 80.379 * 80.379 / (4.0 * elm * elm)))
        # yList.append((ptMissing[1]
        #               + p4lp.values[2] * 80.379 * 80.379 / (4.0 * elp * elp)
        #               + p4lm.values[2] * 80.379 * 80.379 / (4.0 * elm * elm)))
        # xList.append(ptMissing[0])
        yList.append((p4lm.values[0] - p4lp.values[0]) * etMissing
                     - (p4lm.values[1] + p4lp.values[1]) * ptMissing[0]
                     - (p4lm.values[2] + p4lp.values[2]) * ptMissing[1])
    import matplotlib.pyplot as plt
    plt.hist(yList, 100)
    plt.show()


def MomentumDot(eventSet: EventSet) -> float:
    leptonIdx1 = 0
    leptonIdx2 = 0
    leptonIdx3 = 0
    leptonIdx4 = 0
    dotList = []
    for eventSample in eventSet.events:
        for i in range(len(eventSample.particles)):
            if -11 == eventSample.particles[i].PGDid or -13 == eventSample.particles[i].PGDid:
                leptonIdx1 = i
            if 12 == eventSample.particles[i].PGDid or 14 == eventSample.particles[i].PGDid:
                leptonIdx2 = i
            if 11 == eventSample.particles[i].PGDid or 13 == eventSample.particles[i].PGDid:
                leptonIdx3 = i
            if -12 == eventSample.particles[i].PGDid or -14 == eventSample.particles[i].PGDid:
                leptonIdx4 = i
        p41 = eventSample.particles[leptonIdx1].momentum
        p42 = eventSample.particles[leptonIdx2].momentum
        p43 = eventSample.particles[leptonIdx3].momentum
        p44 = eventSample.particles[leptonIdx4].momentum
        dot1 = p41.values[0] * p43.values[0]
        dot2 = p41.values[1] * p43.values[1] + p41.values[2] * p43.values[2] + p41.values[3] * p43.values[3]
        dotList.append(abs(dot1))
    import matplotlib.pyplot as plt
    plt.hist(dotList, 100)
    plt.show()
