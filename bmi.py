
# Import the Tkinter library for graphics
from tkinter import *

class bmiApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        # Display the weight label      
        label = Label(self,bg="white",text='WEIGHT : ',font = "Verdana 10 bold")
        label.grid(row=0,pady=(20,15),padx=(10,5))
        
        # the weight entry box
        self.weight = Entry(self,bd=3,width=4,justify=CENTER)
        self.weight.grid(row=0, column=1)
        
        # Display the lbs label
        label = Label(self,bg="white",text='lbs')
        label.grid(row=0,column=2)
        
        # Display the height label
        label = Label(self,bg="white",text='HEIGHT : ',font = "Verdana 10 bold")
        label.grid(row=1,padx=(10,5))
        
        # setup and display the height in feet entry box
        self.heightFeet = Entry(self,bd=3,width=4,justify=CENTER)
        self.heightFeet.grid(row=1, column=1)
        
        # Display the word feet
        label = Label(self,bg="white",text='FEET ')
        label.grid(row=1,column=2,padx=(5,5))
        
        # setup and display the height in inches entry box
        self.heightInches = Entry(self,bd=3,width=4,justify=CENTER)
        self.heightInches.grid(row=1, column=3)
        
        # Display the word inches
        label = Label(self,bg="white",text='INCHES')
        label.grid(row=1,column=4,padx=(5,5))
        
        # setup and display the calculate button
        self.calculateButton = Button (self, text = "Calculate", bd=3, command = self.findBMI)
        self.calculateButton.grid(row=2,column=1,columnspan=2,pady=(20,0))
        
        # setup the output message label
        self.info = Label (self, bg= "White", text = "",font = "Verdana 10 bold")
        self.info.grid(row=3,columnspan=5,pady=(25,0))
            
    def findBMI(self):
        
        # get values from entry boxes
        mass = self.weight.get().strip()
        feet = self.heightFeet.get().strip()
        inches = self.heightInches.get().strip()
        
        # Make sure no entry box is empty
        if mass == '' or feet == '' or inches == '':
            self.info.config(text = "Please Enter All Values",fg='red')
            return
        
        else:
            # calculate the bmi
            bmi = round(int(mass) * 703 /  ((int(feet)*12) + int(inches))**2,2)
            
            # depending on the bmi make a choice
            if bmi < 18.5:
                self.info.config(text = "BMI : " + str(bmi) + ", STATUS : UNDER WEIGHT",fg='black')
            elif bmi > 18.5 and bmi < 25:
                self.info.config(text = "BMI : " + str(bmi) + ", STATUS : NORMAL",fg='green')
            elif bmi > 24.9 and bmi < 30:
                self.info.config(text = "BMI : " + str(bmi) + ", STATUS : OVER WEIGHT",fg='black')
            elif bmi > 30:
                self.info.config(text = "BMI : " + str(bmi) + ", STATUS : OBESE",fg='red')
        return
        
# Set up window, background color, title and size
app = bmiApp()
app.configure(background='white')
app.geometry('300x200')
app.title('Body Mass Index')

# Start the event loop to react to user inputs
app.mainloop()

#------------------------------------------------------------------#
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
