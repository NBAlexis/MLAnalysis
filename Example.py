from CutAndExport.CutEvent import CutEvents
from DataStructure.EventSet import *
from DataStructure.Particles import *
from Interfaces.LHCOlympics import LoadLHCOlympics


class AtLeastThreePhotons:
    def Cut(self, eventSample: EventSample) -> bool:
        photonCount = 0
        for particle in eventSample.particles:
            if ParticleType.Photon == particle.particleType:
                photonCount = photonCount + 1
        return photonCount < 3


events = LoadLHCOlympics("_DataFolder/triphoton.lhco")
cut = AtLeastThreePhotons()
CutEvents(events, cut)

contents = []
for event in events.events:
    largest1 = LorentzVector(0, 0, 0, 0)
    largest2 = LorentzVector(0, 0, 0, 0)
    largest3 = LorentzVector(0, 0, 0, 0)
    for particle in event.particles:
        if ParticleType.Photon == particle.particleType:
            if particle.momentum.values[0] > largest1.values[0]:
                largest3 = largest2
                largest2 = largest1
                largest1 = particle.momentum
            elif particle.momentum.values[0] > largest2.values[0]:
                largest3 = largest2
                largest2 = particle.momentum
            elif particle.momentum.values[0] > largest3.values[0]:
                largest3 = particle.momentum
    contents.append(largest1.values + largest2.values + largest3.values)
f = open("_DataFolder/triphoton.csv", "w")
for lines in contents:
    f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(
        lines[0], lines[1], lines[2], lines[3], lines[4], lines[5],
        lines[6], lines[7], lines[8], lines[9], lines[10], lines[11]
    ))
f.flush()
f.close()
