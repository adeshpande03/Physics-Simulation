from collectData import *
from collections import OrderedDict
import Rsolid


dataDict = collectData()


def generateObjects(dataDict):
    objArr = OrderedDict()
    for ID in dataDict:
        print(ID, dataDict[ID])
        objArr[ID] = Rsolid.Rsolid(**dataDict[ID])
    for ID in objArr:
        print(objArr[ID])
    return objArr


generateObjects(dataDict=dataDict)
