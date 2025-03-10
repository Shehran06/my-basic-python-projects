import tkinter as tk
from tkinter import *

class calculator_gui:
    def __init__(self):
      self.Calculator_gui=tk.Tk()

      self.Calculator_gui.geometry("400x400")
      self.Calculator_gui.title("Calculator GUI")

      self.Button1=tk.Button(self.Calculator_gui, font=('Arial',16), text="1")
      self.Button1.grid(row=0, column=0, padx=10,pady=10)#to horizontally align the buttons use grid and pack not allowed when using grid

      self.Button2=tk.Button(self.Calculator_gui, font=('Arial',16), text="2")
      self.Button2.grid(row=0, column=1, padx=10,pady=10)

      self.Button3=tk.Button(self.Calculator_gui, font=('Arial',16), text="3")
      self.Button3.grid(row=0, column=2, padx=10,pady=10)

      self.Button4=tk.Button(self.Calculator_gui, font=('Arial',16), text="4")
      self.Button4.grid(row=1, column=0, padx=10,pady=10)

      self.Button5=tk.Button(self.Calculator_gui, font=('Arial',16), text="5")
      self.Button5.grid(row=1, column=1, padx=10,pady=10)

      self.Button6=tk.Button(self.Calculator_gui, font=('Arial',16), text="6")
      self.Button6.grid(row=1, column=2, padx=10,pady=10)

      self.Button7=tk.Button(self.Calculator_gui, font=('Arial',16), text="7")
      self.Button7.grid(row=2, column=0, padx=10,pady=10)

      self.Button8=tk.Button(self.Calculator_gui, font=('Arial',16), text="8")
      self.Button8.grid(row=2, column=1, padx=10,pady=10)

      self.Button9=tk.Button(self.Calculator_gui, font=('Arial',16), text="9")
      self.Button9.grid(row=2, column=2, padx=10,pady=10)

      self.Button0=tk.Button(self.Calculator_gui, font=('Arial',16), text="0")
      self.Button0.grid(row=3, column=1, padx=10,pady=10)

      self.Button_

      self.Calculator_gui.mainloop()

calculator_gui()