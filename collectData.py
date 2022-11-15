import createForm
import numObjects
import solid

def test():
    testDict = main()
    for i in testDict:
        print(i, testDict.get(i))


def main():
    dataDict = dict()
    numForms = numObjects.askNumObjects()
    for _ in range(numForms):
        formData = createForm.createForm()
        dataDict[id(formData)] = formData
    return dataDict

