from tkinter import *
from tkinter import messagebox
import hashlib#to allow hashing for password, hashing is used to convet an input to fixed size string regardless
# of the size of input and each hash value is unique and it cannot be converted back to its original form
import calendar
import datetime
from reports import view_reportss

class income_and_expense:
    def __init__(self, username, password):
      self.incomandexp = Tk()#open a new window

      self.incomandexp.geometry("1000x1000")
      self.incomandexp.title("Income and expenses")

      self.hashpassword(password)#to pass data from here to the parameter of the method
       #to display the current data

      self.todaytime=datetime.datetime.today()#to find the current time and date
      self.year=self.todaytime.strftime("%Y")#to format only to find the year
      self.month=self.todaytime.strftime("%m")
      self.day=self.todaytime.strftime("%d")
      self.incdates = []

      self.currenttime=Label(self.incomandexp,font=('Arial', 16), text=self.day+"/"+self.month+"/"+self.year)
      self.currenttime.grid(row=0, column=0)

      self.incmonth=Entry(self.incomandexp,font=('Arial', 16), width=5)
      self.incmonth.insert(0, "M:")
      self.incmonth.grid(row=1, column=1)


      self.incdate = Entry(self.incomandexp, font=('Arial', 16), width=5)
      self.incdate.insert(0, "D:")
      self.incdate.grid(row=1, column=2,padx=20, pady=20)

      self.income1=Entry(self.incomandexp, font=('Arial', 16))
      self.income1.grid(row=1, column = 3, padx=20, pady=20)

      self.incamount=Entry(self.incomandexp,font=('Arial', 16))
      self.incamount.grid(row=1, column=4)

      self.incbuttion=Button(self.incomandexp, text="Add income", font=('Arial', 16), command=self.get_income_date_and_month_and_amount)
      self.incbuttion.grid(row=2,column=0,padx=20, pady=20)
      self.total_income = [] #to store the amunt of income to be added later on
      self.incomerevenue=[]

      self.expmonth=Entry(self.incomandexp, font=('Arial', 16), width=5)
      self.expmonth.insert(0, "M:")
      self.expmonth.grid(row=3,column=0,padx=20, pady=20)

      self.expdate=Entry(self.incomandexp, font=('Arial', 16), width=5)
      self.expdate.insert(0,"D:")
      self.expdate.grid(row=3,column=1,padx=20, pady=20)

      self.exp=Entry(self.incomandexp,font=('Arial', 16))
      self.exp.grid(row=3,column=2,padx=20, pady=20)

      self.expamount=Entry(self.incomandexp,font=('Arial', 16))
      self.expamount.grid(row=3,column=3, padx=20, pady=20)
      self.expenses = []#to store the amount of expenses that will be added later
      self.expenses_sources=[]
      self.expensedates=[]
      self.expbutton=Button(self.incomandexp, text="Add expense", font=('Arial', 16),command=self.get_expenses_date_and_month_and_amount)
      self.expbutton.grid(row=4,column=0,padx=20, pady=20)


      self.openreport=Button(self.incomandexp, text="Open reports", font=('Arial', 16), command=self.open_reports)
      self.openreport.grid(row=5, column=0)


    def hashpassword(self,password):
      hashpassword = hashlib.new("SHA256")#to chose a hashing algorithm
      hashpassword.update(password.encode('utf-8'))#to use the alogrith forr updates
      #return  hashpassword.hexdigest()#return the password in a hexadecimal format
      if hashpassword:
       with open('usern&passw','a') as hashfile:
        hashfile.write(hashpassword.hexdigest() + '\n')

    def get_income_date_and_month_and_amount(self):

      date=self.incdate.get().replace("D:", " ").strip() #to avoid consider the D; in the entry box
      month=self.incmonth.get().replace("M:", " ").strip() #to avoid consider the M; in the entry box
      income=self.income1.get().strip()
      incomeamount = self.incamount.get().strip()

      if not date or not month or not income or not incomeamount:#not to allow blank data
        messagebox.showwarning("warning", "please fill in the blank boxes")
        return#ro stop further message

      try:
          # to convert the dates into an integer and also month
          date=int(date)
          month=int(month)
          incomeamount=int(incomeamount)
          currentdate=datetime.datetime(int(self.year),month, date)


          if month<1 or month>12:
            messagebox.showwarning("Warning", "invalid month")
            return

          days_in_month =calendar.monthrange(int(self.year), month)[1]#this variable is a tuple using [1] ensures the second value is accessibble

          if  date>days_in_month or date<1:#to find the number of days in the month
            messagebox.showwarning("warning", "invalid date")
            return

          if currentdate>self.todaytime:
              messagebox.showwarning("warning", "invalid date")
              return

          else:
            messagebox.showinfo("successful", "income added")
            formmatedd_date=f"{month:02}/{date:02}/{self.year}"#to format as mm/dd/yyyy
            self.incdates.append(formmatedd_date)
            self.total_income.append(incomeamount)
            self.incomerevenue.append(income)

      except ValueError:
           messagebox.showwarning("warning", "error")

    def get_expenses_date_and_month_and_amount(self):
        expdate = self.expdate.get().replace("D:", " ").strip()  # to avoid consider the D; in the entry box
        expmonth = self.expmonth.get().replace("M:", " ").strip()  # to avoid consider the M; in the entry box
        expensesource = self.exp.get().strip()

        expamount=self.expamount.get().strip()


        if not expdate or not expmonth or not expensesource or not expamount:  # not to allow blank data
            messagebox.showwarning("warning", "please fill in the blank boxes")
            return  # ro stop further message

        try:
            # to convert the dates into an integer and also month
            expdate = int(expdate)
            expmonth = int(expmonth)
            expamount= int(expamount)

            if expmonth < 1 or expmonth > 12:
                messagebox.showwarning("Warning", "invalid month")
                return

            days_in_month = calendar.monthrange(int(self.year), expmonth)[
                1]  # this variable is a tuple using [1] ensures the second value is accessibble

            if expdate > days_in_month or expdate<1:  # to find the number of days in the month
                messagebox.showwarning("warning", "invalid date")
                return

            else:
                messagebox.showinfo("successful", "expense added")
                formmatedd_date=f"{expmonth:02}/{expdate:02}/{self.year}"#to format as mm/dd/yyyy
                self.expensedates.append(formmatedd_date)
                self.expenses.append(expamount)
                self.expenses_sources.append(str(self.exp))

        except ValueError:
            messagebox.showwarning("warning", "error")

    def open_reports(self):
        self.incomandexp.destroy()
        view_reportss(self.incdates, self.incomerevenue, self.total_income, self.expensedates, self.expenses_sources, self.expenses)#to pass on the dates array to the other class
