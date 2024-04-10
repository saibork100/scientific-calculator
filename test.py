
from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("sciebfic calculator")
root.comfiguer (bg="black", fg='white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")
calc =Frame(root)
calc.grid()

class Calc():
    