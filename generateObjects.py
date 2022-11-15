from collectData import *
from collections import OrderedDict
import solid


dataDict = collectData()


def generateObjects(dataDict):
    objArr = OrderedDict()
    for ID in dataDict:
        print(ID, dataDict[ID])
        objArr[ID] = solid.solid(**dataDict[ID])
    for ID in objArr:
        print(objArr[ID])
    return objArr


generateObjects(dataDict=dataDict)
