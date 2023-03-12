import math

import numpy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as mcolors

linestyle_tuple = {
    'solid': 'solid',
    'dotted': 'dotted',
    'dashed': 'dashed',
    'dashdot': 'dashdot',

    'loosely dotted': (0, (1, 10)),
    'densely dotted': (0, (1, 1)),
    'long dash with offset': (5, (10, 3)),
    'loosely dashed': (0, (5, 10)),
    'dashed': (0, (5, 5)),
    'densely dashed': (0, (5, 1)),

    'loosely dashdotted': (0, (3, 10, 1, 10)),
    'dashdotted': (0, (3, 5, 1, 5)),
    'densely dashdotted': (0, (3, 1, 1, 1)),

    'dashdotdotted': (0, (3, 5, 1, 5, 1, 5)),
    'loosely dashdotdotted': (0, (3, 10, 1, 10, 1, 10)),
    'densely dashdotdotted': (0, (3, 1, 1, 1, 1, 1))
}


class HistInfo:

    def __init__(self):
        self.left = 0.0
        self.right = 1.0
        self.binCount = 1
        self.YData = []
        self.YLabel = []
        self.YColor = []
        self.YLineWidth = []
        self.YLineStyle = []
        self.OccupiedColor = []
        self.xLabel = ""
        self.xMinMax = None
        self.xScale = "linear"
        self.yLabel = ""
        self.yMinMax = None
        self.yScale = "linear"
        self.fontSize = 12.0
        self.showLegend = False
        self.graphicSizeSet = False
        self.width = 5
        self.height = 4
        self.dpi = 1
        self.aspectRatio = 1.0
        self.bShowLegend = False
        self.sLegendPos = "best"
        self.maxLineWidth = 1.0


    def SetBin(self, left: float, right: float, binCount: int):
        self.left = left
        self.right = right
        self.binCount = binCount
        return self

    def AddYData(self, yData: list, label: str,
                 color: str = None, lineWidth: float = 1,
                 lineStyle: str = "solid"):
        if len(yData) != self.binCount:
            print("length of yData not fit binCount")
            return self
        bXKCDColor = False
        if color is not None and color.startswith("xkcd:"):
            bXKCDColor = True
        realColor = None
        if bXKCDColor:
            realColor = mcolors.XKCD_COLORS.get(color)
        else:
            realColor = mcolors.CSS4_COLORS.get(color)
        if realColor is None:
            # print("here?")
            for colorName in mcolors.CSS4_COLORS.keys():
                if self.OccupiedColor.count(colorName) < 1:
                    toBeAssigned = mcolors.to_rgba(mcolors.CSS4_COLORS[colorName])
                    if toBeAssigned[0] + toBeAssigned[1] + toBeAssigned[2] < 2.0:
                        self.OccupiedColor.append(colorName)
                        realColor = mcolors.CSS4_COLORS[colorName]
                        break
        else:
            self.OccupiedColor.append(color)
        self.YData.append(yData)
        self.YLabel.append(label)
        self.YColor.append(realColor)
        self.YLineWidth.append(lineWidth)
        self.YLineStyle.append(lineStyle)
        if lineWidth > self.maxLineWidth:
            self.maxLineWidth = lineWidth
        return self

    def SetAxisInfo(self, xLabel: str, yLabel: str,
                    xMinMax: list = None, xScale: str = "linear",
                    yMinMax: list = None, yScale: str = "linear"):
        if xMinMax is None:
            xMinMax = [self.left, self.right]
        if yMinMax is None:
            yLength = np.array(self.YData).max() - np.array(self.YData).min()
            if "linear" == yScale:
                yMinMax = [np.array(self.YData).min() - yLength * 0.1, np.array(self.YData).max() + yLength * 0.1]
            elif "log" == yScale:
                yMinMax = [0, np.array(self.YData).max() + yLength * 0.1]
        self.xLabel = xLabel
        self.xMinMax = xMinMax
        self.xScale = xScale
        self.yLabel = yLabel
        self.yMinMax = yMinMax
        self.yScale = yScale
        return self

    def SetFontSize(self, fontSize: float):
        self.fontSize = fontSize
        return self

    def TurnOnLegend(self, pos):
        """
        'best' 0
        'upper right' 1
        'upper left' 2
        'lower left' 3
        'lower right' 4
        'right' 5
        'center left' 6
        'center right' 7
        'lower center' 8
        'upper center' 9
        'center' 10
        """
        self.bShowLegend = True
        self.sLegendPos = pos
        return self

    def SetGraphicSize(self, width, height):
        self.width = width
        self.height = height
        return self

    def ResizeGraphic(self):
        if self.xMinMax is None:
            self.xMinMax = [self.left, self.right]
        if self.yMinMax is None:
            yLength = np.array(self.YData).max() - np.array(self.YData).min()
            if "linear" == self.yScale:
                self.yMinMax = [np.array(self.YData).min() - yLength * 0.1, np.array(self.YData).max() + yLength * 0.1]
            elif "log" == self.yScale:
                self.yMinMax = [0, np.array(self.YData).max() + yLength * 0.1]
        self.aspectRatio = ((self.xMinMax[1] - self.xMinMax[0]) / (self.yMinMax[1] - self.yMinMax[0])) * (4 / 5)
        if self.yScale == "log":
            self.aspectRatio = ((self.xMinMax[1] - self.xMinMax[0]) / np.log(self.yMinMax[1])) * (3 / 5)
        self.dpi = math.ceil(max(5 / self.width, self.fontSize))
        print(self.width, self.height, self.dpi, self.aspectRatio)


def HistDraw(histInfo: HistInfo, output: str):
    histInfo.ResizeGraphic()
    # increase a little so that the text can be included
    fig = plt.figure(figsize=(histInfo.width * 1.4, histInfo.height * 1.4), dpi=histInfo.dpi)
    frame = gridspec.GridSpec(1, 1)
    pad = fig.add_subplot(frame[0])
    pad.set_aspect(histInfo.aspectRatio)
    binnings = np.linspace(histInfo.left, histInfo.right, histInfo.binCount + 1, endpoint=True)
    middlePoints = np.array([histInfo.left + (histInfo.right - histInfo.left) * (i + 0.5) / histInfo.binCount for i in
                             range(0, histInfo.binCount)])
    for i in range(0, len(histInfo.YData)):
        pad.hist(x=middlePoints, bins=binnings, weights=np.array(histInfo.YData[i]),
                 label=histInfo.YLabel[i], histtype="step", rwidth=1.0,
                 color=histInfo.YColor[i], edgecolor=histInfo.YColor[i], linewidth=histInfo.YLineWidth[i],
                 linestyle=linestyle_tuple[histInfo.YLineStyle[i]],
                 bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")
    plt.rc('text', usetex=False)
    plt.xlabel(histInfo.xLabel, fontsize=histInfo.fontSize, color="black")
    plt.ylabel(histInfo.yLabel, fontsize=histInfo.fontSize, color="black")
    ax = plt.gca()
    ax.spines['top'].set_linewidth(histInfo.maxLineWidth)
    ax.spines['right'].set_linewidth(histInfo.maxLineWidth)
    ax.spines['bottom'].set_linewidth(histInfo.maxLineWidth)
    ax.spines['left'].set_linewidth(histInfo.maxLineWidth)
    if histInfo.xMinMax is not None:
        ax.set_xlim(histInfo.xMinMax[0], histInfo.xMinMax[1])
    if histInfo.xScale == "linear":
        ax.set_xscale("linear")
    elif histInfo.xScale == "log":
        ax.set_xscale("log", nonpositive="clip")
    if histInfo.yMinMax is not None:
        ax.set_ylim(histInfo.yMinMax[0], histInfo.yMinMax[1])
    if histInfo.yScale == "linear":
        ax.set_yscale("linear")
    elif histInfo.yScale == "log":
        ax.set_yscale("symlog")
    if histInfo.bShowLegend:
        plt.legend(loc=histInfo.sLegendPos)
    print("saving to: ", output)
    plt.savefig(output)
