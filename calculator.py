import tkinter
import tkinter.messagebox

class first_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()     #establishes the base of the GUI
       
        self.first_frame = tkinter.Frame(self.main_window, height=500, width=500)  #creates the first frame
        self.second_frame =tkinter.Frame(self.main_window) #creates the second frame
        self.third_frame = tkinter.Frame(self.main_window) #creates the third frame


        self.first_label = tkinter.Label(self.first_frame, text="Enter first number") #creates a label that tells the user to enter a number
        self.first_value = tkinter.Entry(self.first_frame, width=10) #creates a space where the user can enter a number

        self.first_label.pack(side='left') #packs the label in the first frame and sends it to the left
        self.first_value.pack(side='left') #packs the entry field in the first frame and sends it to the left

        self.second_label = tkinter.Label(self.first_frame, text="Enter second number") #creates a label that tells the user to enter a second number
        self.second_value = tkinter.Entry(self.first_frame, width=10) #creates a space to enter a second number

        self.second_label.pack(side='left') #packs the label in the first frame and sends it to the left
        self.second_value.pack(side='left') #packs the entry field in the first frame and sends it to left

        self.calc_button = tkinter.Button(self.second_frame, text='Calculate', command=self.addition) #creates a button that will calculate two numbers
        self.quit_button = tkinter.Button(self.second_frame, text='Quit', command=self.main_window.destroy) #creates a button that wil end the program

        self.calc_button.pack(side='left') #packs the calculate button in the second frame and sends it to the left
        self.quit_button.pack(side='left') #packs the quit button the in the second frame and sends it to the left

        self.third_label = tkinter.Label(self.third_frame, text='Answer: ') #creates a label in the thrid frame that will display answer

        self.final_value = tkinter.StringVar()

        self.fourth_label = tkinter.Label(self.third_frame, textvariable=self.final_value) #this will hold and display the answer with the numbers that the user enters

        self.third_label.pack(side='left') #packs the third label in the third frame and sends it to the left
        self.fourth_label.pack(side='left') #packs the fourth label into the third frame and sends it to the left



        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        tkinter.mainloop()
        
    def addition(self):
        first_num = float(self.first_value.get()) #gets the first number
        second_num = float(self.second_value.get()) #gets the second number
        total = first_num + second_num #adds them together
        self.final_value.set(total) #updates the StrVar() to the value of the two numbers that get added together
        
     
calculator = first_GUI() 



