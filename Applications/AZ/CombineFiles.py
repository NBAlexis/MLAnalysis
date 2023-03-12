import os

from Interfaces.UsefulFunctions import CombineEventsLHCO

os.chdir("../../_DataFolder/za/newnew")
for i in range(2, 17):
    CombineEventsLHCO(["fm4/fm4-{}a.lhco".format(i), "fm4/fm4-{}b.lhco".format(i)],
                      "fm4/fm4-{}.lhco".format(i))
