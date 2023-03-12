import os

from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

from CutAndExport.CutFunctions import JetNumberCut, PhotonNumberCut, LeptonPMCut, StandardVBFCut, PtMissing, MeGammaCut, \
    ThetaGammaLeptonCut, PhiGammaMissingCut, PhiLeptonMissingCut, RadiusACut

os.chdir("../../_Output")

with PyCallGraph(output=GraphvizOutput()):
    cutType = 1
    jetNumberCut = JetNumberCut(1, [2])
    photonNumberCut = PhotonNumberCut(1, [1])
    leptonNumberCut = LeptonPMCut(False, 1, 0)
    vbfCut = StandardVBFCut(True, 0.0, 2.0)
    ptMissingCutM = PtMissing(1, 120)
    megammaCut = MeGammaCut(1, False, 800)
    thetaGammaLeptonCut = ThetaGammaLeptonCut(0, False, 0)
    phiGammaMissingCut = PhiGammaMissingCut(0, -0.75)
    lmCut = PhiLeptonMissingCut(1, False, 0)
    ptMissingCutT = PtMissing(1, 75)
    r2Cut = RadiusACut(1, 0.15, 3)
    r1Cut = RadiusACut(1, 0.15, 2)
