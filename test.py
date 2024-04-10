
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
        self.total=0
        # Initialize the current attribute to an empty string
        self.current=''
        # Initialize the input_value attribute to True
        self.input_value=True
        # Initialize the check_sum attribute to False
        self.check_sum=False
        # Initialize the op attribute to an empty string
        self.op=''
        # Initialize the result attribute to False
        self.result=False

    def numberEnter(self, num):
        # set the result attridute to False
        self.result=False
        # Get the current value display on the calculator's display 
        firstnum=txtDisplay.get()
        # Convert the input number to a string
        secondnum=str(num)

        # Check if the input_value attribute is True
        if self.input_value:
               # If it is, set the current attribute to the input number
              self.current = secondnum
              # Set the input_value attribute to False
              self.input_value=False
        else:
             # If the input_value attribute is False, check if the input number is a decimal point
            if secondnum == '.':
                # If it is, check if there is already a decimal point in the current value
                if secondnum in firstnum:
                    # If there is, return without doing anything
                    return
            # If the input number is not a decimal point, or if there is no decimal point in the current value, concatenate the current value and the input number    
            self.current = firstnum+secondnum
        # Display the current value on the calculator's display
        self.display(self.current)

    def sum_of_total(self):
        # Set the result attribute to True
        self.result=True
        # Convert the current attribute
        self.current=float(self.current)

        # Check if the check_sum attribute is True
        if self.check_sum==True:
            # If it is, call the valid_function method
            self.valid_function()
        else:
            # Otherwise, set the total attribute to the value of the txtDisplay widget, converted to a float
            self.total=float(txtDisplay.get())

    def display(self, value):
        # Delete any existing existing text in the txtDisplay widget
        txtDisplay.delete(0, END)
        # Insert the given value in the  txtDisplay widget
        txtDisplay.insert(0, value)

    def valid_function(self):
    # Check the value of the op attribute and perform the corresponding operation on the total and current attributes
        if self.op == "add":
            if self.op == "add":
                self.total += self.current
            if  self.op=="sub":
                self.total -= self.current
            elif self.op=="multi":
                self.total *= self.current
            elif self.op=="divide":
                self.total /= self.current
            elif self.op == "mod":
                self.total %= self.current
            self.input_value=True
            self.check_sum=False
            self.display(self.total)

    def operation(self, op):
        # Convert the current attribute to a float
        self.current = float(self.current)
   
        # If the check_sum attribute is True, call the valid_function method
        if self.check_sum:
            self.valid_function()
        
        
        # If the check_sum attribute is True, call the valid_function method
        elif not self.result:
            self.total=self.current
            self.input_value=True
        
        # Set the check_sum attribute to True
        self.check_sum=True
        # Set the op attribute to the given value
        self.op=op
        # Set the result attribute to False
        self.result=False 

    def Clear_Entry(self):
        # Set the result attribute to False
        self.ressult = False
        # Set the current attribute to "0"
        self.current ="0"
        # Call the display method with an argument of 0
        self.display(0)
        # Set the input_value attribute to True
        self.input_value = True

    def All_claer_Entry(self):
        # Call the Clear_Entry method
        self.clear_Entry()
        # Set the total attribute to 0
        self.total=0

    def pi(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the value of math.pi
        self.current= math.pi
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def tau(self):
        # Set the result attribute to False
        self.result  = False
        # Set the current attribute to the value of math.tau
        self.current = math.tau
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def e(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the value of math.e
        self.current = math.e
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def mathPM(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the negative value of the text displayed in the txtDisplay widget
        self.current = -(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def squared(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the square root of the text displayed in the txtDisplay widge
        self.current = math.sqrt(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def cos(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the cosine of the value displayed in the txtDisplay widget, converted to radians
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def cosh(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the hyperbolic cosine of the value displayed in the txtDisplay widget, converted to radians
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def tan(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the tangent of the value displayed in the txtDisplay widget, converted to radians
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def tanh(self):
        # Set the result attribute to False
        self.result = False
         # Set the current attribute to the hyperbolic tangent of the value displayed in the txtDisplay widget, converted to radians
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def sin(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the hyperbolic sine of the value displayed in the txtDisplay widget, converted to radians
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def sinh(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the hyperbolic sine of the value displayed in the txtDisplay widget, converted to radians
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        # Call the display method with the value of the current attribute
        self.display(self.current)  

    def log(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the natural logarithm of the value displayed in the txtDisplay widget
        self.current = math.log(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def exp(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the exponential of the value displayed in the txtDisplay widget
        self.current = math.exp(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)