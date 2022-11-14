from tkinter import simpledialog



def askNumObjects():
    numObjects = simpledialog.askinteger(
        "Physics Sumulation",
        "How many objects would you like to initialize?",
        minvalue=0,
        maxvalue=10
    )
    return numObjects



