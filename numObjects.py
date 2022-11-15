from tkinter import simpledialog


def askNumObjects(minvalue = 0, maxvalue = 10):
    numObjects = simpledialog.askinteger(
        title="Physics Sumulation",
        prompt="How many objects would you like to initialize?",
        minvalue = minvalue,
        maxvalue = maxvalue,
    )
    return numObjects
