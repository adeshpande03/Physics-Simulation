from collectData import *
from collections import OrderedDict
import solid


dataDict = collectData()


def generateObjects(dataDict):
    objArr = OrderedDict()
    for data in dataDict:
        print(data)
    return objArr


generateObjects(dataDict=dataDict)
