from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
import  matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

#first the users enters the goals such as the saviing 300 for the month of january for food
#the savings shall be dedicated from the income to the saving category
#use 2 variables currentamount and targeted amount
# the targeted amount shall be allocated from the income and the current amount can be added each time
#the current amount increases only when the user adds their details and it fulfills the category thet have chosen
#if the current amount exceeds or nearing the target there shall be a notification
#calcualte prgresss by Progress (%) = (Current Amount / Target Amount) * 100
#use graphs and all

class savings:
    def __init__(self, savingamount):

        self.savings=Tk()
        self.savings.geometry("1000x600")

        self.total_income=sum(savingamount)

        self.labeli= Label(self.savings, text= self.total_income)
        self.labeli.grid(row=0, column=1)
        self.saving_category=["Emergency Fund", "Vacation Fund", "Down Payment", "Retirement Savings"]
        self.Emergency_fund = 0
        self.Vacation_fund = 0
        self.down_payment = 0
        self.retirement_saving = 0

        self.label1=Label(self.savings, text="Create saving goals", font=('Arial', 16))
        self.label1.grid(row=0, column=0)

        self.savdate=Entry(self.savings, font=('Arial', 16), width=30)
        self.savdate.insert(0, "MM/DD/YYYY:")
        self.savdate.grid(row=1, column=0, padx=10, pady=10)

        self.savcategory = ttk.Combobox(self.savings, font=('Arial', 16), values=self.saving_category)
        self.savcategory.grid(row=1, column=1, padx=10, pady=10)

        self.savamount=Entry(self.savings, font=('Arial', 16))
        self.savamount.insert(0,"Amount:")
        self.savamount.grid(row=1, column=2, padx=10, pady=10)

        self.saved=Button(self.savings, font=('Arial', 16), text="Create saving budget", command=self.create_saving_goals)
        self.saved.grid(row=2,column=0, padx=10, pady=10)

        self.budgetrack=Label(self.savings, font=('Arial', 16), text="Budget Tracking")
        self.budgetrack.grid(row=3, column=0)

        self.trackdate=Entry(self.savings, font=('Arial', 16),width=30)
        self.trackdate.insert(0, "MM/DD/YYYY:")
        self.trackdate.grid(row=4, column=0, padx=10, pady=10)

        self.trackcategory=ttk.Combobox(self.savings, font=('Arial', 16),width=30, values=self.saving_category)
        self.trackcategory.grid(row=4, column=1,padx=10, pady=10)

        self.trackamount=Entry(self.savings, font=('Arial', 16))
        self.trackamount.insert(0, "Amount:")
        self.trackamount.grid(row=4, column=2, padx=10, pady=10)

        self.trackbutton=Button(self.savings, font=('Arial', 16), text= "confirm", command= self.track_progress)
        self.trackbutton.grid(row=5, column=0, padx=10, pady=10)

        self.label2=Label(self.savings, font=('Arial', 16))
        self.label2.grid(row=5, column=1)

        self.view_progress = Button(self.savings, text="view progress", command=self.view_progress_graph)
        self.view_progress.grid(row=6, column=0)

        #to track the total tracked amount
        self.trackemergencyfund=0
        self.trackvacationfund=0
        self.trackdownpayment=0
        self.trackretirementsav=0

        #to track the list of transactions
        self.track_emergency_fund_trans = []
        self.trackvacationfund_trans = []
        self.down_payment_trans = []
        self.retirementsav_trans = []

        #to track the dates for progress
        self.track_emergrancy_date=[]
        self.track_vacation_fund_date=[]
        self.trackdownpayment_date=[]
        self.trackretirementsav_date=[]

        self.today = datetime.today()

        self.progress=0

        self.savings.mainloop()
    def create_saving_goals(self):

        savdate = self.savdate.get().replace("MM/DD/YYYY:", " ").strip()
        savedamount= self.savamount.get().replace("Amount:", " ").strip()
        category=self.savcategory.get().strip()

        if not savdate or not savedamount or not category:
            messagebox.showwarning("invalid", "please fill in the blank spaces")
            return

        try:
            #self.total_income=int(self.total_income)
            saveddate=datetime.strptime(savdate, "%m/%d/%Y")#to convert string to datetime
            savedamount=int(savedamount)
            #self.saving_budget.append(savedamount)
            #self.target_saving_date.append(savdate)
            if saveddate.year != self.today.year:#ensure only for this year
                messagebox.showwarning("invalid date", "this is only for the current year")
                return

            if savedamount>self.total_income:
                messagebox.showwarning("insufficient", "your income is insufficient for the savings")
                return
            #self.target_saving_date.append(savdate)

            if category=="Emergency Fund":
                self.Emergency_fund+=savedamount
                self.label2.config(text=self.Emergency_fund)
            elif category == "Vacation Fund":
                self.Vacation_fund+=savedamount
            elif category== "Down Payment":
                self.down_payment+=savedamount
            elif category == "Retirement Savings":
                self.retirement_saving+=savedamount

            self.total_income-=savedamount
            messagebox.showinfo("tt", "Savings budget added")
        except:
                 messagebox.showwarning("tt", "error")

    def track_progress(self):
        track_date=self.trackdate.get().replace("MM/DD/YYYY:", " ").strip()
        trackcategory=self.trackcategory.get().strip()
        track_amount=self.trackamount.get().replace("Amount:", " ").strip()

        if not track_date or not trackcategory or not track_amount:
            messagebox.showwarning("invalid", "Please fill in the blank spaces")
            return

        try:
            track_date=datetime.strptime(track_date, "%m/%d/%Y")
            track_amount=int(track_amount)
            #self.total_income=int(self.total_income)

            if track_date.year!=self.today.year:
              messagebox.showwarning("invalid date", "this is only for this year")
              return

            if track_date>self.today:
              messagebox.showwarning("invalid date", "you can save only upto today")
              return

            if trackcategory == "Emergency Fund":
                if self.trackemergencyfund<=self.Emergency_fund:
                    self.trackemergencyfund += track_amount
                    self.Emergency_fund-=track_amount
                    self.track_emergency_fund_trans.append(track_amount)
                    self.track_emergrancy_date.append(str(track_date))
                    messagebox.showinfo("success", "you have successfully updated your progress")
                else:
                    messagebox.showwarning("sss", "you have insufficient balance")

            elif trackcategory == "Vacation Fund":
                if self.trackvacationfund<=self.Vacation_fund:
                    self.trackvacationfund += track_amount
                    self.Vacation_fund-=track_amount
                    self.trackvacationfund_trans.append(track_amount)
                    self.track_vacation_fund_date.append(str(track_date))
                    messagebox.showinfo("success", "you have successfully updated your progress")
                else:
                    messagebox.showwarning("sss", "you have insufficient balance")

            elif trackcategory == "Down Payment":
                if self.trackdownpayment<=self.down_payment:
                    self.trackdownpayment += track_amount
                    self.down_payment-=track_amount
                    self.down_payment_trans.append(track_amount)
                    self.trackdownpayment_date.append(str(track_date))
                    messagebox.showinfo("success", "you have successfully updated your progress")
                else:
                    messagebox.showwarning("sss", "you have insufficient balance")

            elif trackcategory == "Retirement Savings":
                if self.trackretirementsav<=self.retirement_saving :
                    self.trackretirementsav += track_amount
                    self.down_payment-=track_amount
                    self.retirementsav_trans.append(track_amount)
                    self.trackretirementsav_date.append(str(track_date))
                    messagebox.showinfo("success", "you have successfully updated your progress")
                else:
                    messagebox.showwarning("sss", "you have insufficient balance")

            else:
                messagebox.showwarning("invalid", "invalid category")
        except Exception as e:
            messagebox.showwarning("error", "Error", f"An error occurred: {e}")


    def view_progress_graph(self):
        savingprogress = Tk()

        category=self.trackcategory.get()

        #create frame
        frame1=Frame(savingprogress)

        #create canvas
        fig, ax= plt.subplots()
        #fig is where the graph shall be displayed like the window
        #ax represents the axes can be used instead of plt to plot the graph

        #display canvas on the frame
        canvas=FigureCanvasTkAgg(fig, master=frame1)
        canvas.get_tk_widget().pack()#integrate to the frame

        if category== "Emergency Fund":
           ax.plot(self.track_emergrancy_date, self.track_emergency_fund_trans)
           canvas.draw()#to display graph
           self.progress = (self.trackemergencyfund/self.Emergency_fund)*100

        elif category=="Vacation Fund":
            ax.plot(self.track_vacation_fund_date, self.trackvacationfund_trans)
            canvas.draw()
            self.progress=(self.trackvacationfund/ self.Vacation_fund)*100

        elif category == "Down Payment":
            ax.plot(self.trackdownpayment_date, self.down_payment_trans)
            canvas.draw()
            self.progress=(self.trackdownpayment/self.down_payment)*100
        elif category == "Retirement Savings":
            ax.plot(self.trackretirementsav_date,self.retirementsav_trans)
            canvas.draw()
            self.progress=(self.trackretirementsav/self.retirement_saving)*100
        else:
            ax.plot()
            canvas.draw()

        frame1.pack(side=BOTTOM, padx=10, pady=10)#to adjust this to the left side of the window

         #to add round progress bar
        frameprogress=Frame(savingprogress)

        progressbar=ttk.Progressbar(frameprogress, mode='indeterminate', value=self.progress)
        progressbar.pack(side=TOP, padx=10, pady=10)

        frameprogress.pack(side=BOTTOM, padx=10, pady=10)#to below the graph
