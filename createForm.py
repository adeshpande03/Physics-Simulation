import tkinter as tk
import inspect
from solid import *
from collections import OrderedDict
import random

args = [
    d.strip().split("=")[0]
    for d in str(inspect.signature(solid.__init__))[1:-1].split(",")[1:]
]


def createForm():
    def printForm():
        for j, i in enumerate(varArr):
            print(f"{args[j]}: {i.get()}")

    master = tk.Tk()
    varArr = [tk.DoubleVar() for _ in range(len(args))]
    for j, i in enumerate(args):
        tk.Label(master, text=f"{i}").grid(row=j)

    tk.Button(
        master,
        text="Enter",
        command=master.quit,
        activebackground="gray",
        justify="center",
    ).grid(row=len(varArr), column=0)
    tk.Button(
        master,
        text="Close",
        command=master.quit,
        activebackground="gray",
        justify="center",
    ).grid(row=len(varArr), column=2)
    eArr = [
        tk.Entry(master, textvariable=f"{i}").grid(row=j, column=1)
        for j, i in enumerate(varArr)
    ]
    master.mainloop()
    varDict = OrderedDict()
    for j, i in enumerate(varArr):
        varDict[args[j]] = i.get()

    # {args[j]: i.get() for j, i in enumerate(varArr)}
    return varDict


def main():
    print(createForm())


main()


# Original Code

################################################################################################################
# def printz():
#     print('\n\nnum1: ',var1.get(),'num2: ', var2.get(),'num3: ', var3.get())

# master = tk.Tk()

# var1 = tk.StringVar()
# var2 = tk.StringVar()
# var3 = tk.StringVar()


# tk.Label(master, text="num1").grid(row=0)
# tk.Label(master, text="num2").grid(row=1)
# tk.Label(master, text="num3").grid(row=2)
# tk.Button(master,text ="Enter", command = printz,activebackground='green',
#           justify='center').grid(row=3, column=1)

# e1 = tk.Entry(master, textvariable=var1).grid(row=0, column=1)
# e2 = tk.Entry(master, textvariable=var2).grid(row=1, column=1)
# e3 = tk.Entry(master, textvariable=var3).grid(row=2, column=1)
################################################################################################################


# master.mainloop()
