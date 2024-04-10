
from tkinter import *
import math
import tkinter.messagebox

root = Tk()     # Create a new Tkinter window
root.title("Scientific Calculator")     # Set the title of the window
root.comfiguer (background = 'white')   # Set the background color of the window to white
root.resizable(width=False, height=False)   # Prevent the window from being resized by the user
root.geometry("480x568+450+90")     # Set the size and position of the window
calc =Frame(root)    # Create a new frame widget inside the window
calc.grid()       # Add the frame to the window using the grid geometry manager

class Calc():
    def __init__(self):
        # Initialize the total attribute to 0
        self.total = 0
        # Initialize the current attribute to an empty string
        self.current = ''
        # Initialize the input_value attribute to True
        self.input_value = True
        # Initialize the check_sum attribute to False
        self.check_sum = False
        # Initialize the op attribute to an empty string
        self.op = ''
        # Initialize the result attribute to False
        self.result = False