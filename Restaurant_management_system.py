from tkinter import *  # Importing all modules from tkinter for GUI creation
import time  # Importing time module for time-related operations
import random  # Importing random module for generating random numbers
from datetime import date  # Importing date module for handling date-related tasks

# Function to display the price list
def price():
        roo = Tk()  # Creating a new Tkinter window for the price list
        roo.geometry("600x280+0+0")  # Setting the size of the window
        roo.title("Price List")  # Setting the title of the window
        
        # Creating labels for items and their prices
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)  
        lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
        lblinfo.grid(row=0, column=2) 
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3) 

        # Adding food items and their respective prices
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drink", fg="#ED420B", anchor=W)
        lblinfo.grid(row=1, column=0)  
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W)
        lblinfo.grid(row=1, column=3)  

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger King", fg="#ED420B", anchor=W)
        lblinfo.grid(row=2, column=0)  
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="#ED420B", anchor=W)
        lblinfo.grid(row=2, column=3)  

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cherry", fg="#ED420B", anchor=W)
        lblinfo.grid(row=3, column=0)  
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="#ED420B", anchor=W)
        lblinfo.grid(row=3, column=3)  

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Nacho Fries", fg="#ED420B", anchor=W)
        lblinfo.grid(row=4, column=0)  
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="#ED420B", anchor=W)
        lblinfo.grid(row=4, column=3)  

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza", fg="#ED420B", anchor=W)
        lblinfo.grid(row=5, column=0)  
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="#ED420B", anchor=W)
        lblinfo.grid(row=5, column=3)  

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Biscuits", fg="#ED420B", anchor=W)
        lblinfo.grid(row=6, column=0)  
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W)
        lblinfo.grid(row=6, column=3)  

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Roll", fg="#ED420B", anchor=W)
        lblinfo.grid(row=7, column=0)  
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W)
        lblinfo.grid(row=7, column=3)  

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="#ED420B", anchor=W)
        lblinfo.grid(row=8, column=0)  
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W)
        lblinfo.grid(row=8, column=3)  

        roo.mainloop()  # Running the Tkinter main loop

# Function to clear the text field
def clear():
        text.delete(1.0, END)  # Deletes all text from the text widget

# Function to quit the application
def quit_fun():
        root.destroy()  # Destroys the Tkinter main window

# Function to calculate the total bill
def total():
        # Retrieving values entered by the user and converting to integers
        price1 = int(dringE.get())  
        price2 = int(burger_kingE.get())  
        price3 = int(cherry.get())  
        price4 = int(nacho_fries.get())  
        price5 = int(pizza.get())  
        price6 = int(biscuits.get())  
        price7 = int(roll.get())  
        price8 = int(tea.get())  

        # Calculating individual item costs
        p1 = price1 * 10  
        p2 = price2 * 30  
        p3 = price3 * 25  
        p4 = price4 * 20  
        p5 = price5 * 30  
        p6 = price6 * 10  
        p7 = price7 * 10  
        p8 = price8 * 5  

        # Calculating total cost
        cost = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8  
        display = cost  
        p1_label["text"] = display  

        # Service tax calculation
        service_charge = cost / 20  
        p2_label["text"] = service_charge  

        # Tax calculation
        tax_charge = int(cost / 3)  
        p3_label["text"] = tax_charge  

        # Sub-total calculation
        sub_total = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8  
        p4_label["text"] = sub_total  

        # Final total amount
        total = display + service_charge + tax_charge  
        p5_label["text"] = total  

        # Generating a random order number
        num = random.randint(1, 10000)  # Generating a random order number
        order_label["text"] = num  

# Function to reset all input fields and labels
def reset():
        dringE.delete(0, END)  
        burger_kingE.delete(0, END)  
        cherry.delete(0, END)  
        nacho_fries.delete(0, END)  
        pizza.delete(0, END)  
        biscuits.delete(0, END)  
        roll.delete(0, END)  
        tea.delete(0, END)  
        p1_label["text"] = ""  
        p2_label["text"] = ""  
        p3_label["text"] = ""  
        p4_label["text"] = ""  
        p5_label["text"] = ""  
        order_label["text"] = ""  

# Function to display the current time
def clock():
        current = time.strftime("%H:%M:%S")  # Getting the current time
        label1["text"] = current  
        root.after(1000, clock)  # Refreshing the time every second

root = Tk()  # Creating the main Tkinter window
root.geometry("1000x700")  
root.minsize(1000, 700)  
root.maxsize(1000, 700)  

# Creating the heading labels
heading1 = Label(root, text="Hotel Management", font="arial 30 bold", fg="#fc5a03")  
heading2 = Label(root, text="Cashier: Popescu Ion", font="arial 18 bold", fg="#fc5a03")  

# Creating frames for different sections of the application
frame1 = Frame(root, height="420", width="330", bd=10, bg="#ED420B", highlightthickness=1, relief=SUNKEN)  
frame1.place(x=40, y=140)  
frame2 = Frame(root, height="420", width="330", bd=10, bg="#33A9CE", highlightthickness=1, relief=SUNKEN)  
frame2.place(x=380, y=140)  

# Button Frame
frame3 = Frame(root, height="100", width="670", bd=10, bg="#ED420B", highlightthickness=1, relief=SUNKEN)  
frame3.place(x=40, y=565)  

cal_frame = Frame(root, height="500", width="450", bd=10, highlightthickness=1, relief=SUNKEN)  
cal_frame.place(x=750, y=150)  

text_frame = Frame(root, height="100", width="100")  
text_frame.place(x=1000, y=50)  

frame_time = Frame(root, height="200", width="200", bd=10, highlightthickness=1, relief=SUNKEN)  
frame_time.place(x=100, y=50)  

# Price Frame
p1_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")  
p1_label.place(x=200, y=80)  
p2_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")  
p2_label.place(x=200, y=120)  
p3_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")  
p3_label.place(x=200, y=160)  
p4_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")  
p4_label.place(x=200, y=200)  
p5_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")  
p5_label.place(x=200, y=240)  
order_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")  
order_label.place(x=200, y=40)  

text = Text(root, height=10, width=25, bd=10, font="arial 10")  
text.insert(END, "Enter Text Here")  
text.place(x=750, y=500)  

# Time
label1 = Label(frame_time, font="article 30", bg="black", fg="#ED420B")  
label1.grid(row=0, column=0)  
clock()  

# Buttons
# Frame 3
new_window = Button(frame3, text="Price", command=price, font="arial 15 bold", bd=10)  # Button to show price list
new_window.place(x=80, y=10)  
total_btn = Button(frame3, text="Total", command=total, font="arial 15 bold", bd=10)  # Button to calculate total
total_btn.place(x=210, y=10)  
reset_btn = Button(frame3, text="Reset", command=reset, font="arial 15 bold", bd=10)  # Button to reset inputs
reset_btn.place(x=350, y=10)  
quit_btn = Button(frame3, text="Quit", command=quit_fun, font="arial 15 bold", bd=5)  # Button to quit application
quit_btn.place(x=500, y=10)  
clear = Button(root, text="Clear", command=clear, font="arial 10 bold", bd=10)  # Button to clear text input
clear.place(x=760, y=450)  

# Payment Entry Created
# Frame 2
order_number = Label(frame2, text="Order Number", font="arial 12 bold", bg="#33A9CE")  
cost_label = Label(frame2, text="Cost", font="arial 12 bold ", bg="#33A9CE")  
service_tax = Label(frame2, text="Service Cost", font="arial 12 bold", bg="#33A9CE")  
tax = Label(frame2, text="Tax", font="arial 12 bold ", bg="#33A9CE")  
sub_total = Label(frame2, text="Sub Total", font="arial 12 bold", bg="#33A9CE")  
total = Label(frame2, text="Total", font="arial 12 bold ", bg="#33A9CE")  
# Payment Entry Close
# Frame 2
order_number.place(x=10, y=40)  
cost_label.place(x=10, y=80)  
service_tax.place(x=10, y=120)  
tax.place(x=10, y=160)  
sub_total.place(x=10, y=200)  
total.place(x=10, y=240)  

# Food item Entry Created
# Frame 1 objects
dringE = Entry(frame1, bd="3")  # Entry for Drink quantity
burger_kingE = Entry(frame1, bd="5")  # Entry for Burger King quantity
cherry = Entry(frame1, bd="5")  # Entry for Cherry quantity
nacho_fries = Entry(frame1, bd="5")  # Entry for Nacho Fries quantity
pizza = Entry(frame1, bd="5")  # Entry for Pizza quantity
biscuits = Entry(frame1, bd="5")  # Entry for Biscuits quantity
roll = Entry(frame1, bd="5")  # Entry for Roll quantity
tea = Entry(frame1, bd="5")  # Entry for Tea quantity
# Food item Entry Close
# Frame 1 objects
dringE.place(x=130, y=35)  
burger_kingE.place(x=130, y=80)  
cherry.place(x=130, y=125)  
nacho_fries.place(x=130, y=170)  
pizza.place(x=130, y=215)  
biscuits.place(x=130, y=260)  
roll.place(x=130, y=305)  
tea.place(x=130, y=350)  

# Food item Label Created
# Frame 1 objects
drink_label = Label(frame1, text="Drink", font="arial 12 bold ", bg="#ED420B")  
burger_king_label = Label(frame1, text="Burger King", font="arial 12 bold", bg="#ED420B")  
cherry_label = Label(frame1, text="Cherry", font="arial 12 bold", bg="#ED420B")  
nacho_fries_label = Label(frame1, text="Nacho Fries", font="arial 12 bold", bg="#ED420B")  
pizza_label = Label(frame1, text="Pizza", font="arial 12 bold ", bg="#ED420B")  
biscuits_label = Label(frame1, text="Biscuits", font="arial 12 bold", bg="#ED420B")  
roll_label = Label(frame1, text="Roll", font="arial 12 bold ", bg="#ED420B")  
tea_label = Label(frame1, text="Tea", font="arial 12 bold ", bg="#ED420B")  
# Food item Label Close
drink_label.place(x=10, y=35)  
burger_king_label.place(x=10, y=80)  
cherry_label.place(x=10, y=125)  
nacho_fries_label.place(x=10, y=175)  
pizza_label.place(x=10, y=215)  
biscuits_label.place(x=10, y=260)  
roll_label.place(x=10, y=305)  
tea_label.place(x=10, y=350)  

from tkinter import messagebox  # Importing messagebox for error handling
val = ""  # Variable to store input for calculator
A = 0  # Variable to store first operand for calculator
operator = ""  # Variable to store operator for calculator

# Functions for calculator button clicks
def btn_1_isclicked():
        global val
        val = val + "1"  
        data.set(val)  

def btn_2_isclicked():
        global val
        val = val + "2"  
        data.set(val)  

def btn_3_isclicked():
        global val
        val = val + "3"  
        data.set(val)  

def btn_4_isclicked():
        global val
        val = val + "4"  
        data.set(val)  

def btn_5_isclicked():
        global val
        val = val + "5"  
        data.set(val)  

def btn_6_isclicked():
        global val
        val = val + "6"  
        data.set(val)  

def btn_7_isclicked():
        global val
        val = val + "7"  
        data.set(val)  

def btn_8_isclicked():
        global val
        val = val + "8"  
        data.set(val)  

def btn_9_isclicked():
        global val
        val = val + "9"  
        data.set(val)  

def btn_0_isclicked():
        global val
        val = val + "0"  
        data.set(val)  

def btn_plus_isclicked():
        global A
        global operator
        global val
        A = int(val)  
        operator = "+"  
        val = val + "+"  
        data.set(val)  

def btn_min_isclicked():
        global A
        global operator
        global val
        A = int(val)  
        operator = "-"  
        val = val + "-"  
        data.set(val)  

def btn_mult_isclicked():
        global A
        global operator
        global val
        A = int(val)  
        operator = "*"  
        val = val + "*"  
        data.set(val)  

def btn_div_isclicked():
        global A
        global operator
        global val
        A = int(val)  
        operator = "/"  
        val = val + "/"  
        data.set(val)  

def btn_c_isclicked():
        global A
        global operator
        global val
        A = 0  
        operator = ""  
        val = ""  
        data.set(val)  

def result():
        global A
        global operator
        global val
        val2 = val  
        if operator == "+":  
                B = int((val2.split("+")[1]))  
                C = A + B  
                data.set(C)  
                val = str(C)  
        elif operator == "-":  
                B = int((val2.split("-")[1]))  
                C = A - B  
                data.set(C)  
                val = str(C)  
        elif operator == "*":  
                B = int((val2.split("*")[1]))  
                C = A * B  
                data.set(C)  
                val = str(C)  
        elif operator == "/":  
                B = int((val2.split("/")[1]))  
                if B == 0:  
                        messagebox.showerror("Error", "Divisible by 0 not allowed.")  
                        A = ""  
                        val = ""  
                        data.set(val)  
                else:
                        C = int(A / B)  
                        data.set(C)  
                        val = str(C)  

data = StringVar()  # Creating a StringVar to hold the calculator display value
lbl = Label(cal_frame, text="LABEL", anchor=SE,  
            font=("Verdana", 20), textvariable=data, background="#ffffff", fg="#000000")
lbl.pack(expand=True, fill="both")  # Packing the label to fill the frame

# Creating button rows for the calculator
btnrow1 = Frame(cal_frame, bg="#000000")  
btnrow1.pack(expand=True, fill="both")  
btnrow2 = Frame(cal_frame)  
btnrow2.pack(expand=True, fill="both")  
btnrow3 = Frame(cal_frame)  
btnrow3.pack(expand=True, fill="both")  
btnrow4 = Frame(cal_frame)  
btnrow4.pack(expand=True, fill="both")  

# Creating buttons for the calculator
btn1 = Button(btnrow1, text="1", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_1_isclicked)  # Button for '1'
btn1.pack(side=LEFT, expand=True, fill="both")  
btn2 = Button(btnrow1, text="2", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_2_isclicked)  # Button for '2'
btn2.pack(side=LEFT, expand=True, fill="both")  
btn3 = Button(btnrow1, text="3", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_3_isclicked)  # Button for '3'
btn3.pack(side=LEFT, expand=True, fill="both")  
btnplus = Button(btnrow1, text="+", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_plus_isclicked)  # Button for '+'
btnplus.pack(side=LEFT, expand=True, fill="both")  

btn4 = Button(btnrow2, text="4", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_4_isclicked)  # Button for '4'
btn4.pack(side=LEFT, expand=True, fill="both")  
btn5 = Button(btnrow2, text="5", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_5_isclicked)  # Button for '5'
btn5.pack(side=LEFT, expand=True, fill="both")  
btn6 = Button(btnrow2, text="6", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_6_isclicked)  # Button for '6'
btn6.pack(side=LEFT, expand=True, fill="both")  
btnminus = Button(btnrow2, text="-", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_min_isclicked)  # Button for '-'
btnminus.pack(side=LEFT, expand=True, fill="both")  

btn7 = Button(btnrow3, text="7", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_7_isclicked)  # Button for '7'
btn7.pack(side=LEFT, expand=True, fill="both")  
btn8 = Button(btnrow3, text="8", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_8_isclicked)  # Button for '8'
btn8.pack(side=LEFT, expand=True, fill="both")  
btn9 = Button(btnrow3, text="9", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_9_isclicked)  # Button for '9'
btn9.pack(side=LEFT, expand=True, fill="both")  
btnmult = Button(btnrow3, text="*", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_mult_isclicked)  # Button for '*'
btnmult.pack(side=LEFT, expand=True, fill="both")  

btnc = Button(btnrow4, text="C", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_c_isclicked)  # Button for 'C' (clear)
btnc.pack(side=LEFT, expand=True, fill="both")  
btn0 = Button(btnrow4, text="0", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_0_isclicked)  # Button for '0'
btn0.pack(side=LEFT, expand=True, fill="both")  
btnequal = Button(btnrow4, text="=", font=("Verdana", 22), relief=GROOVE, border=0, command=result)  # Button for '=' (calculate)
btnequal.pack(side=LEFT, expand=True, fill="both")  
btndiv = Button(btnrow4, text="/", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_div_isclicked)  # Button for '/'
btndiv.pack(side=LEFT, expand=True, fill="both")  

# Positioning the heading labels
heading1.place(x=350, y=10)  # Positioning main heading
heading2.place(x=400, y=80)  # Positioning cashier name

root.mainloop()  # Running the Tkinter main loop to keep the application open