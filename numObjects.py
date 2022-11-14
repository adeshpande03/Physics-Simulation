from tkinter import simpledialog
from solid import *


def askNumObjects():
    numObjects = simpledialog.askinteger(
        "Physics Sumulation",
        "How many objects would you like to initialize?",
        minvalue=0,
        maxvalue=10
    )
    return numObjects



