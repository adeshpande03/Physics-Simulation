from numObjects import *
from createForm import *
from collections import OrderedDict
import solid



def generateObjects(dataArr):
    objArr = OrderedDict()
    for dataDict in dataArr:
        objArr.append(solid(**dataDict))
    return objArr
    