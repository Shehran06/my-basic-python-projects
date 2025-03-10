from tkinter import *
from tkinter import messagebox
from  income_and_expenses import income_and_expense

class login :

    def __init__(self):
      self.login=Tk()

      self.login.geometry("400x500")#to set the length and width of the window
      self.login.title("Login or signup")

      self.entusernam = Label(self.login, font=('Arial', 16), text="enter user name")
      self.entusernam.pack()
      self.user=Entry(self.login, font=('Arial', 16))#to set a textbox
      self.user.pack(padx=10)

      self.entpassw = Label(self.login, font=('Arial', 16), text="enter password")
      self.entpassw.pack()
      self.passw=Entry(self.login, font=('Arial', 16))
      self.passw.pack(padx=10, pady=20)

      self.lbutton1=Button(self.login, text="login",command=self.openincome_and_expensestebb)#open another window
      self.lbutton1.pack()

      self.lbutton2=Button(self.login, text="Sign up")
      self.lbutton2.pack()
      self.login.mainloop()#to execute and continue to take inputs and outputs

    def openincome_and_expensestebb(self):
      password=self.passw.get()
      username=self.user.get()
      if not password.strip() or not username.strip():
        messagebox.showwarning("warning", "please enter correct password or username")
      else:#to display next window only if there no blank
        self.login.destroy()
        income_and_expense(username,password)#to take in the usernname and password from this method and copy it
#has to be the same in the variablke decalired

login()