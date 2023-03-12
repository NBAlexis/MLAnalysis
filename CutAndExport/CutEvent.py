from DataStructure.EventSet import EventSet


def CutEvents(eventSet: EventSet, cutFunction):
    idxAdd = 0
    for i in range(len(eventSet.events)):
        if 0 <= i + idxAdd < len(eventSet.events):
            if cutFunction.Cut(eventSet.events[i + idxAdd]):
                del eventSet.events[i + idxAdd]
                idxAdd = idxAdd - 1
