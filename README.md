# Restaurant-Management-System-in-Python
This application creates a graphical interface for a hotel management system using Tkinter. It includes functionalities for displaying the price list, calculating the total of an order, resetting input fields, real-time clock display and a simple built-in calculator.


Main elements of the code:

● Price list (price()):
 
Initializes a new window that displays a catalog of products along with their respective prices (e.g. drinks, hamburgers, pizza, etc.). Use Label to render textual information and use grid() to arrange these items.

● Main functionality:

Calculate total (total()): Takes user entered values for each product. Calculates aggregate cost, service charge and sales tax. Shows the cumulative order total and generates a random order ID number. 

Reset (reset()): Erases all input fields and returns the displayed labels to their original state. Real-time clock (clock()): Displays the current time and automatically refreshes at one-second intervals.

● Graphical interface (Tkinter):

The main window measures 1000x700 pixels and contains different frames for organizing the components: the frame for entering product quantities (frame1); the frame for displaying the total and taxes (frame2); the frame allocated for buttons (frame3); the separate frame for calculation functions (cal_frame); the frame for displaying the clock (frame_time)

● Built-in calculator:

Facilitates the execution of fundamental math operations (+, -, *,/) Uses StringVar() to refresh the display. Contains dedicated functions for each number and operator. Provides error notifications for division to zero via messagebox.showerror().

● Main Buttons:

"Price" - Initializes the price list window. 

"Total" - Calculates and displays the total cost. 

"Reset" - Resets all fields to their default state. 

"Quit - Closes the application. 

"Clear" - Removes the text entered in the text box.

#Enjoy
