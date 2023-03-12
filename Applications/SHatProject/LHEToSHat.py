from CutAndExport.FilterFunctions import SHatWWReal
from Interfaces.LesHouchesEvent import LoadLargeLesHouchesEvent

def ExportSHatToFile(eventSetLHCOFileName, fileName):
    eventSetLHCO = LoadLargeLesHouchesEvent(eventSetLHCOFileName, True)
    shatFile = open(fileName, 'w')
    for oneevent in eventSetLHCO.events:
        realShat = SHatWWReal(oneevent)
        shatFile.write("{:.8e}\n".format(realShat))
    shatFile.close()
    print("done")

readFileName = "G://samplea0.lhe"
writeFileName = "../../_DataFolder/shat/samplea0.csv"
ExportSHatToFile(readFileName, writeFileName)
