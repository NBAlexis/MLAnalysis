import os

import numpy as np

from Applications.WWWW.Filters import ExportEvent
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../")
s0 = LoadLesHouchesEvent("_DataFolder/WWWW/LHE/s0at30.lhe")
print("s0", " loaded")
[toSave1, toSave2] = ExportEvent(s0)
all0 = toSave1 + toSave2
print("ExportEvent over ", len(toSave1), " and ", len(toSave2))
print(len(all0))
all = np.array(all0)

alls = all[:, 12]

print(len(alls))

for s in range(0, 10):
    coeff = 0.001 * (s + 1)
    shatcut = np.sqrt(np.sqrt(192 * np.pi / coeff)) * 1000
    print(len(alls[alls < shatcut]))

"""
996032
902284
773261
664566
578758
510229
455464
410182
372492
340872

Process finished with exit code 0

"""