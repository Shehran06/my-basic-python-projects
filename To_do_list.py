
from tkinter import *
#import os# For opening the file in Notepad
import subprocess  # For opening the file in Notepad without blocking

main = Tk() #Tk() creates the main window or interface

#creating an input parameter

#def onclickadd():
   #   label1 = Label(main, text= entry.get())#label shows entry data
    #  label1.pack()

user_entry = Entry(main)
user_entry.pack()
def onclickadd():
      userinput= user_entry.get()
      if userinput:  # Only write if there is some input
       with open('data.txt', 'a') as f1:  # Open the file in append mode
        f1.write(userinput + '\n')  # Write the input to the file
      label= Label(main, text="task added")
      label.pack()
      subprocess.Popen(['notepad', 'data.txt'])  # Open the file in Notepad without blocking

def onclickdelete():
    userinput = user_entry.get()
    if userinput:  # Only write if there is some input
        with open('data.txt', 'r') as f1:  # Open the file in read mode
            lines= f1.readlines()
        with open('data.txt', 'w') as f1:
            for line in lines:
                if line.strip() != userinput:#strip method can be used to white spaces or characters
                                            #if line.strip not matching input all other remain the same
                   f1.write(line)
        subprocess.Popen(['notepad', 'data.txt'])  # Open the file in Notepad without blocking

#creating a button
button_1 = Button(main, text="add", command=onclickadd)#should be given with the location for the button
button_1.pack()#put it on the location
button_2=Button(main, text="Delete", command=onclickdelete)
button_2.pack()

# Function to handle closing the application
def closing():

    main.destroy()  # Destroy the main window

# Corrected indentation for window close event handler
main.protocol("WM_DELETE_WINDOW", closing)

main.mainloop()#to take user input
