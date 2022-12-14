import createForm
import numObjects


def test():
    testDict = collectData()
    for i in testDict:
        print(i, testDict.get(i))


def collectData():
    dataDict = dict()
    numForms = numObjects.askNumObjects()
    while len(dataDict) < numForms:
        formData = createForm.createForm()
        dataDict[id(formData)] = formData
    return dataDict


