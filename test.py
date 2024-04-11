
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

    def acosh(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the inverse hyperbolic cosine of the value displayed in the txtDisplay widget
        self.current = math.acosh(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def asinh(self):
        # Set the result attribute to False
        self.result = False
         # Set the current attribute to the inverse hyperbolic sine of the value displayed in the txtDisplay widget
        self.current = math.asinh(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)    

    def expm1(self):# Set the result attribute to False
        self.result = False
        # Set the current attribute to the exponential of the value displayed in the txtDisplay widget, minus 1
        self.current = math.expm1(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)                          

    def lgamma(self):
        self.result = False
         # Set the current attribute to the natural logarithm of the gamma function of the value displayed in the txtDisplay widget
        self.current = math.lgamma(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)
        

    def degrees(self):
        # Set the result attribute to False
        self.result = False
         # Set the current attribute to the natural logarithm of the gamma function of the value displayed in the txtDisplay widget
        self.current = math.degrees(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def log2(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the base 2 logarithm of the value displayed in the txtDisplay widget
        self.current = math.log2(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def log10(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the base 10 logarithm of the value displayed in the txtDisplay widget
        self.current = math.log10(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)

    def log1p(self):
        # Set the result attribute to False
        self.result = False
        # Set the current attribute to the natural logarithm of 1 plus the value displayed in the txtDisplay widget
        self.current = math.log1p(float(txtDisplay.get()))
        # Call the display method with the value of the current attribute
        self.display(self.current)

# Create an instance of the Calc class
added_value = Calc()

# Create a text entry widget for the calculator display
txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),
				bg='black',fg='white',
				bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

# Define a string of numbers for the number pad
numberpad = "789456123"
i=0
# Create a list to store the number pad buttons
btn = []
for j in range(2,5):
	for k in range(3):
        # Create a button for each number in the number pad
		btn.append(Button(calc, width=6, height=2,
						bg='black',fg='white',
						font=('Helvetica',20,'bold'),
						bd=4,text=numberpad[i]))
        # Place the button in the correct position in the grid
		btn[i].grid(row=j, column= k, pady = 1)
        # Set the command of the button to call the numberEnter method of the Calc instance
		btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
        # Increment the index of the number pad string
		i+=1

# Create a button for the "Clear" function
btnClear = Button(calc, text=chr(67), # Use the chr() function to display the character 'C' on the button
				width=6, height=2, # Set the width and height of the button
				bg='powder blue', # Set the background color of the button
				font=('Helvetica',20,'bold'), # Set the font style of the button
				bd=4, # Set the border width of the button
				command=added_value.Clear_Entry # Set the command to be executed when the button is clicked
				).grid(row=1, column= 0, pady = 1) # Add the button to the grid layout manager

# Create a button for the "All Clear" function
btnAllClear = Button(calc, text=chr(67)+chr(69), # Use the chr() function to display the characters 'CN' on the button
					width=6, height=2,
					bg='powder blue', 
					font=('Helvetica',20,'bold'),
					bd=4,
					command=added_value.All_Clear_Entry
					).grid(row=1, column= 1, pady = 1) # Add the button to the grid layout manager

# Create a button for the square root function
btnsq = Button(calc, text="\u221A", # The Unicode character for the square root symbol
			width=6, height=2, # The size of the button
			bg='powder blue', # The background color of the button
			font=('Helvetica', 20, 'bold'), # The font style of the button
			bd=4, # The border width of the button
			command=added_value.squared # The command to execute when the button is clicked
			).grid(row=1, column= 2, pady = 1) # Add the button to the grid layout manager

# Create a button for the addition function
btnAdd = Button(calc, text="+", # The text on the button
				width=6, height=2, # The size of the button
				bg='powder blue', # The background color of the button
				font=('Helvetica',20,'bold'), # The font style of the button
				bd=4, # The border width of the button
				command=lambda:added_value.operation("add") # The command to execute when the button is clicked
				).grid(row=1, column= 3, pady = 1) # Add the button to the grid layout manager

# Create a button for the subtraction operation
btnSub = Button(calc, text="-", # The text on the button is "-"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='powder blue', # The background color of the button is powder blue
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=lambda:added_value.operation("sub") # The command to execute when the button is clicked is a lambda function that calls the operation method of the added_value object with the argument "sub"
				).grid(row=2, column= 3, pady = 1) # The button is added to the grid at row 2, column 3, with a padding of 1

# Create a button for the multiplication operation
btnMul = Button(calc, text="x", # The text on the button is "x"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='powder blue', # The background color of the button is powder blue
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=lambda:added_value.operation("multi") # The command to execute when the button is clicked is a lambda function that calls the operation method of the added_value object with the argument "multi"
				).grid(row=3, column= 3, pady = 1) # The button is added to the grid at row 3, column 3, with a padding of 1

# Create a button for the division operation
btnDiv = Button(calc, text="/", # The text on the button is "/"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='powder blue', # The background color of the button is powder blue
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=lambda:added_value.operation("divide") # The command to execute when the button is clicked is a lambda function that calls the operation method of the added_value object with the argument "divide"
				).grid(row=4, column= 3, pady = 1) # The button is added to the grid at row 4, column 3, with a padding of 1

# Create a button for the number 0
btnZero = Button(calc, text="0", # The text on the button is "0"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=lambda:added_value.numberEnter(0) # The command to execute when the button is clicked is a lambda function that calls the numberEnter method of the added_value object with the argument 0
				).grid(row=5, column= 0, pady = 1) # The button is added to the grid at row 5, column 0, with a padding of 1

# Create a button for the decimal point
btnDot = Button(calc, text=".", # The text on the button is "."
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='powder blue', # The background color of the button is powder blue
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=lambda:added_value.numberEnter(".") # The command to execute when the button is clicked is a lambda function that calls the numberEnter method of the added_value object with the argument "."
				).grid(row=5, column= 1, pady = 1) # The button is added to the grid at row 5, column 1, with a padding of 1

# Create a button for the mathematical operation "plus or minus"
btnPM = Button(calc, text=chr(177), # The text on the button is the unicode character for "plus or minus"
			height=2, # The height of the button is 2
			width=6,  # The width of the button is 6
			bg='powder blue', # The background color of the button is powder blue
			font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
			bd=4, # The border width of the button is 4
			command=added_value.mathPM # The command to execute when the button is clicked is the mathPM method of the added_value object
			).grid(row=5, column= 2, pady = 1) # The button is added to the grid at row 5, column 2, with a padding of 1

# Create a button for calculating the sum of the current and total values
btnEquals = Button(calc, text="=", # The text on the button is "="
				height=2, # The height of the button is 2
				width=6, # The width of the button is 6
				bg='powder blue', # The background color of the button is powder blue
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.sum_of_total # The command to execute when the button is clicked is the sum_of_total method of the added_value object
				).grid(row=5, column= 3, pady = 1) # The button is added to the grid at row 5, column 3, with a padding of 1

# ROW 1 :
# Create a button for the mathematical constant pi
btnPi = Button(calc, text="pi", # The text on the button is "pi"
			width=6, # The width of the button is 6
			height=2, # The height of the button is 2
			bg='black', # The background color of the button is black
			fg='white', # The foreground color of the button is white
			font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
			bd=4, # The border width of the button is 4
			command=added_value.pi # The command to execute when the button is clicked is the pi method of the added_value object
			).grid(row=1, column= 4, pady = 1) # The button is added to the grid at row 1, column 4, with a padding of 1

# Create a button for the cosine function
btnCos = Button(calc, text="Cos", # The text on the button is "Cos"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 2
				bd=4,# The border width of the button is 4
                command=added_value.cos # The command to execute when the button is clicked is the cos method of the added_value object
			).grid(row=1, column= 5, pady = 1)# The button is added to the grid at row 1, column 4, with a padding of 1

# Create a button for the tangent function
btntan = Button(calc, text="tan", # The text on the button is "tan"
			width=6, # The width of the button is 6
			height=2, # The height of the button is 2
			bg='black', # The background color of the button is black
			fg='white', # The foreground color of the button is white
			font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
			bd=4, # The border width of the button is 4
			command=added_value.tan # The command to execute when the button is clicked is the tan method of the added_value object
			).grid(row=1, column= 6, pady = 1) # The button is added to the grid at row 1, column 6, with a padding of 1

# Create a button for the sine function
btnsin = Button(calc, text="sin", # The text on the button is "sin"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.sin # The command to execute when the button is clicked is the sin method of the added_value object
				).grid(row=1, column= 7, pady = 1) # The button is added to the grid at row 1, column 7, with a padding of 1

# ROW 2 :
# Create a button for the mathematical constant 2pi
btn2Pi = Button(calc, text="2pi", # The text on the button is "2pi"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.tau # The command to execute when the button is clicked is the tau method of the added_value object
			).grid(row=2, column= 4, pady = 1) # The button is added to the grid at row 2, column 4, with a padding of 1

# Create a button for the hyperbolic cosine function
btnCosh = Button(calc, text="Cosh", # The text on the button is "Cosh"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.cosh # The command to execute when the button is clicked is the cosh method of the added_value object
				).grid(row=2, column= 5, pady = 1) # The button is added to the grid at row 2, column 5, with a padding of 1

# Create a button for the hyperbolic tangent function
btntanh = Button(calc, text="tanh", # The text on the button is "tanh"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.tanh # The command to execute when the button is clicked is the tanh method of the added_value object
				).grid(row=2, column= 6, pady = 1) # The button is added to the grid at row 2, column 6, with a padding of 1

# Create a button for the hyperbolic sine function
btnsinh = Button(calc, text="sinh", # The text on the button is "sinh"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.sinh # The command to execute when the button is clicked is the sinh method of the added_value object
				).grid(row=2, column= 7, pady = 1) # The button is added to the grid at row 2, column 7, with a padding of 1

# ROW 3 :
# Create a button for the natural logarithm function
btnlog = Button(calc, text="log", # The text on the button is "log"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.log # The command to execute when the button is clicked is the log method of the added_value object
			).grid(row=3, column= 4, pady = 1) # The button is added to the grid at row 3, column 4, with a padding of 1

# Create a button for the exponential function
btnExp = Button(calc, text="exp", # The text on the button is "exp"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.exp # The command to execute when the button is clicked is the exp method of the added_value object
			).grid(row=3, column= 5, pady = 1) # The button is added to the grid at row 3, column 5, with a padding of 1

# Create a button for the modulus operation
btnMod = Button(calc, text="Mod", # The text on the button is "Mod"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=lambda:added_value.operation("mod") # The command to execute when the button is clicked is a lambda function that calls the operation method of the added_value object with the argument "mod"
			).grid(row=3, column= 6, pady = 1) # The button is added to the grid at row 3, column 6, with a padding of 1

# Create a button for the mathematical constant e
btnE = Button(calc, text="e", # The text on the button is "e"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.e # The command to execute when the button is clicked is the e method of the added_value object
			).grid(row=3, column= 7, pady = 1) # The button is added to the grid at row 3, column 7, with a padding of 1

# ROW 4 :
# Create a button for the common logarithm function
btnlog10 = Button(calc, text="log10", # The text on the button is "log10"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.log10 # The command to execute when the button is clicked is the log10 method of the added_value object
			).grid(row=4, column= 4, pady = 1) # The button is added to the grid at row 4, column 4, with a padding of 1

# Create a button for the natural logarithm of 1 plus x function
btncos = Button(calc, text="log1p", # The text on the button is "log1p"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.log1p # The command to execute when the button is clicked is the log1p method of the added_value object
			).grid(row=4, column= 5, pady = 1) # The button is added to the grid at row 4, column 5, with a padding of 1

# Create a button for the exponential of x minus 1 function
btnexpm1 = Button(calc, text="expm1", # The text on the button is "expm1"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.expm1 # The command to execute when the button is clicked is the expm1 method of the added_value object
			).grid(row=4, column= 6, pady = 1) # The button is added to the grid at row 4, column 6, with a padding of 1

# Create a button for the gamma function
btngamma = Button(calc, text="gamma", # The text on the button is "gamma"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.lgamma # The command to execute when the button is clicked is the lgamma method of the added_value object
			).grid(row=4, column= 7, pady = 1) # The button is added to the grid at row 4, column 7, with a padding of 1

# ROW 5 :
# Create a button for the binary logarithm function
btnlog2 = Button(calc, text="log2", # The text on the button is "log2"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.log2 # The command to execute when the button is clicked is the log2 method of the added_value object
			).grid(row=5, column= 4, pady = 1) # The button is added to the grid at row 5, column 4, with a padding of 1

# Create a button for the degree conversion function
btndeg = Button(calc, text="deg", # The text on the button is "deg"
				width=6, # The width of the button is 6
				height=2, # The height of the button is 2
				bg='black', # The background color of the button is black
				fg='white', # The foreground color of the button is white
				font=('Helvetica',20,'bold'), # The font of the button is Helvetica, bold, and size 20
				bd=4, # The border width of the button is 4
				command=added_value.degrees # The command to execute when the button is clicked is the degrees method of the added_value object
			).grid(row=5, column= 5, pady = 1) # The button is added to the grid at row 5, column 5, with a padding of 1

