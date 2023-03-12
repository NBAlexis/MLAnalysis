import random

from CEVisualize.Hist import HistDraw
from CEVisualize.Hist import HistInfo

HistDraw(HistInfo().SetBin(0, 1, 40)
         .AddYData([1.0 + 0.1 * random.uniform(-0.1, 1.0) + 0.1 * i for i in range(0, 40)],
                   "SM", lineWidth=2.0, color="red")
         .AddYData([1.5 + 0.1 * random.uniform(-0.1, 1.0) + 0.2 * i for i in range(0, 40)],
                   "$NP_1$", lineStyle="densely dashed")
         .AddYData([1.0 + 0.1 * random.uniform(-0.1, 1.0) + 0.01 * i * i for i in range(0, 40)],
                   "$NP_2$")
         .SetAxisInfo("$m_{\\ell\\ell}\\;({\\rm MeV})$", "$\\frac{1}{N}\\times \\frac{d N}{0.025\\;{\\rm MeV}}$")
         .TurnOnLegend("upper left"),
         "../_Output/a.pdf")

