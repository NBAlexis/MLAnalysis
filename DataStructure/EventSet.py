from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector


class EventSet:
    def __init__(self):
        self.events = []

    def AddEvent(self, event: EventSample):
        self.events.append(event)

    def AddEventSet(self, eventSet):
        self.events = self.events + eventSet.events

    def GetEventCount(self) -> int:
        return len(self.events)

    def GetCopy(self):
        ret = EventSet()
        ret.events = self.events.copy()
        return ret

    def DebugPrint(self, i: int):
        print(self.events[i].DebugPrint())

    def RemoveWrongEventLeptonCount(self, lst):
        idxAdd = 0
        for i in range(len(self.events)):
            if 0 <= i + idxAdd < len(self.events):
                if not (self.events[i + idxAdd].GetLeptonCount() in lst):
                    del self.events[i + idxAdd]
                    idxAdd = idxAdd - 1

    def RemoveWrongEventJetCount(self, lst):
        idxAdd = 0
        for i in range(len(self.events)):
            if 0 <= i + idxAdd < len(self.events):
                if not (self.events[i + idxAdd].GetJetCount() in lst):
                    del self.events[i + idxAdd]
                    idxAdd = idxAdd - 1

    def RecalculateMissing(self, vSum: LorentzVector):
        """
        For lepton collider, the z-direction of missing can be calculated
        due to momentum conservation
        :return:
        """
        for i in range(len(self.events)):
            self.events[i].RecalculateMissing(vSum)
