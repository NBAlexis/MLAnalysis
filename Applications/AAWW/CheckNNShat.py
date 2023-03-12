import h5py
import numpy as np
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

FILENAME = "F:\\PyworkingFolder\\WWSHat\\_Data\\alpha0.h5"

with h5py.File(FILENAME, 'r') as f:
    dense_0 = f['/model_weights/dense/dense']
    dense_0_bias = dense_0['bias:0'][:]
    dense_0_kernel = dense_0['kernel:0'][:]
    dense_1 = f['/model_weights/dense_1/dense_1']
    dense_1_bias = dense_1['bias:0'][:]
    dense_1_kernel = dense_1['kernel:0'][:]
    dense_2 = f['/model_weights/dense_2/dense_2']
    dense_2_bias = dense_2['bias:0'][:]
    dense_2_kernel = dense_2['kernel:0'][:]


def layer_output(v, kernel, bias):
    return np.dot(v, kernel) + bias


reluFunction = np.vectorize(lambda x: x if x >= 0.0 else 0.0)


def Predict(vec):
    output_1 = layer_output(vec, dense_0_kernel, dense_0_bias)
    output_2 = reluFunction(output_1)
    output_3 = layer_output(output_2, dense_1_kernel, dense_1_bias)
    output_4 = reluFunction(output_3)
    output_5 = layer_output(output_4, dense_2_kernel, dense_2_bias)
    output_6 = reluFunction(output_5)
    return float(output_6[0][0])


def TestNetwork(eventSetLHCO, eventSetLHE, startIndex, endIndex):
    normalizer = 6500.0
    listRealS = []
    listPredictS = []
    for i in range(startIndex, endIndex):
        oneEvent = eventSetLHCO.events[i]
        lepton1 = LorentzVector(0, 0, 0, 0)
        lepton2 = LorentzVector(0, 0, 0, 0)
        jet1 = LorentzVector(0, 0, 0, 0)
        jet2 = LorentzVector(0, 0, 0, 0)
        missing = LorentzVector(0, 0, 0, 0)
        largestJetIndex1 = 0
        largestJetM1 = 0.0
        largestJetIndex2 = 0
        largestJetM2 = 0.0
        leptonIdx1 = 0
        leptonIdx2 = 0
        leptonCount = 0
        lepton1Found = False
        hasMissing = False
        for oneParticle in oneEvent.particles:
            if ParticleStatus.Outgoing == oneParticle.status \
                    and ParticleType.Jet == oneParticle.particleType:
                momentum = oneParticle.momentum.Momentum()
                if momentum > largestJetM1:
                    largestJetM2 = largestJetM1
                    largestJetIndex2 = largestJetIndex1
                    largestJetM1 = momentum
                    largestJetIndex1 = oneParticle.index
                elif momentum > largestJetM2:
                    largestJetM2 = momentum
                    largestJetIndex2 = oneParticle.index
            elif ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
                leptonCount = leptonCount + 1
                if not lepton1Found:
                    lepton1Found = True
                    leptonIdx1 = oneParticle.index
                else:
                    leptonIdx2 = oneParticle.index
            elif ParticleType.Missing == oneParticle.particleType:
                hasMissing = True
                missing = missing + oneParticle.momentum
        if largestJetIndex1 > 0 and largestJetIndex2 > 0:
            jet1 = oneEvent.particles[largestJetIndex1 - 1].momentum
            jet2 = oneEvent.particles[largestJetIndex2 - 1].momentum
        else:
            continue
        if leptonCount != 2:
            continue
        if leptonIdx1 > 0 and leptonIdx2 > 0:
            lepton1 = oneEvent.particles[leptonIdx1 - 1].momentum
            lepton2 = oneEvent.particles[leptonIdx2 - 1].momentum
        else:
            continue
        if not hasMissing:
            print(oneEvent.DebugPrint())
            continue
            # all good
        realShat = SHatAWReal(eventSetLHE.events[i])
        listRealS.append(realShat)
        vecArray = np.array([[
            jet1.values[1] / normalizer,
            jet1.values[2] / normalizer,
            jet1.values[3] / normalizer,
            jet2.values[1] / normalizer,
            jet2.values[2] / normalizer,
            jet2.values[3] / normalizer,
            lepton1.values[1] / normalizer,
            lepton1.values[2] / normalizer,
            lepton1.values[3] / normalizer,
            lepton2.values[1] / normalizer,
            lepton2.values[2] / normalizer,
            lepton2.values[3] / normalizer,
            missing.values[1] / normalizer,
            missing.values[2] / normalizer]])
        predictsHat = normalizer * Predict(vecArray)
        listPredictS.append(predictsHat * predictsHat)
    return [listRealS, listPredictS]


exportEventLHCO = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhco")
exportEventLHE = LoadLesHouchesEvent("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhe")

allList = TestNetwork(exportEventLHCO, exportEventLHE, 0, 50000)
import matplotlib.pyplot as plt
plt.hist2d(allList[0], allList[1], [50, 50])
plt.show()
