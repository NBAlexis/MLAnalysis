from random import *


class IsolateTree:

    def __init__(self, points, dim: int, largestDepth: int):
        self.points = points
        self.dim = dim
        self.depth = 0
        self.largestDepth = largestDepth
        self.root = self
        self.divAttr = 0
        self.divValue = 0.0
        self.parent = None
        self.ChildA = None
        self.ChildB = None
        self.canSplit = len(points) > 1
        self.pointIndex = range(0, len(points))

    def Split(self) -> bool:
        if not self.canSplit:
            print("Error! 0\n")
            return False
        if self.ChildA is None:
            # I am not split yet
            if self.ChildB is not None:
                print("Error! 1\n")
                return False
            if len(self.pointIndex) < 2:
                print("Error! 2\n")
                return False
            attributeIndex: int = randint(0, self.root.dim - 1)
            minAttr: float = 0.0
            maxAttr: float = 0.0
            for i in range(0, len(self.pointIndex)):
                if 0 == i:
                    minAttr = self.root.points[self.pointIndex[i]][attributeIndex]
                    maxAttr = self.root.points[self.pointIndex[i]][attributeIndex]
                elif self.root.points[self.pointIndex[i]][attributeIndex] > maxAttr:
                    maxAttr = self.root.points[self.pointIndex[i]][attributeIndex]
                elif self.root.points[self.pointIndex[i]][attributeIndex] < minAttr:
                    minAttr = self.root.points[self.pointIndex[i]][attributeIndex]
            divValue: float = uniform(minAttr, maxAttr)
            childListA = []
            childListB = []
            for pIdx in self.pointIndex:
                if self.root.points[pIdx][attributeIndex] < divValue:
                    childListA = childListA + [pIdx]
                else:
                    childListB = childListB + [pIdx]
            if len(childListA) == 0 or len(childListB) == 0:
                print("Error! 3: ", childListA, " - ", divValue, " - ", childListB, "\n")
                for id1 in childListA:
                    print("attrA: ", self.root.points[id1][attributeIndex], "\n")
                for id2 in childListB:
                    print("attrB: ", self.root.points[id2][attributeIndex], "\n")
                return False
            self.ChildA = IsolateTree([], self.dim, self.largestDepth)
            self.ChildA.parent = self
            self.ChildA.depth = self.depth + 1
            self.ChildA.root = self.root
            self.ChildA.pointIndex = childListA
            self.ChildA.canSplit = len(childListA) > 1 and (self.largestDepth <= 0 or self.ChildA.depth < self.largestDepth)
            self.ChildB = IsolateTree([], self.dim, self.largestDepth)
            self.ChildB.parent = self
            self.ChildB.depth = self.depth + 1
            self.ChildB.root = self.root
            self.ChildB.pointIndex = childListB
            self.ChildB.canSplit = len(childListB) > 1 and (self.largestDepth <= 0 or self.ChildA.depth < self.largestDepth)
            self.divAttr = attributeIndex
            self.divValue = divValue
            self.canSplit = self.ChildA.canSplit or self.ChildB.canSplit
            # print("{} seperate to {} and {}\n".format(len(self.pointIndex), len(childListA), len(childListB)))
        else:
            if self.ChildB is None:
                print("Error! 4\n")
                return False
            if self.ChildA.canSplit and self.ChildB.canSplit:
                choose = randint(0, 1)
                if 0 == choose:
                    self.ChildA.Split()
                else:
                    self.ChildB.Split()
            elif self.ChildA.canSplit:
                self.ChildA.Split()
            elif self.ChildB.canSplit:
                self.ChildB.Split()
            else:
                print("Error! 5\n")
                return False
        self.canSplit = self.ChildA.canSplit or self.ChildB.canSplit

    def SetDepth(self, depthList, depthElementIndex: int, depthStart: int):
        if self.ChildA is None:
            for indexes in self.pointIndex:
                depthList[indexes][depthElementIndex] = depthStart
        else:
            self.ChildA.SetDepth(depthList, depthElementIndex, depthStart + 1)
            self.ChildB.SetDepth(depthList, depthElementIndex, depthStart + 1)

