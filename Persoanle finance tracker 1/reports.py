from tkinter import *
from tkinter import ttk
import  matplotlib.pyplot as plt #allow graphs to be plot
import datetime
from datetime import *
from _datetime import datetime
from Budget_goals import types_of_budget_goals

class view_reportss:
    def __init__(self, dates, income_sources,income, expdates, expensesource, total_expenses):
        self.reports = Tk()
        self.reports.geometry("1000x1000")

        self.options=["current week", "current month", "current year"]
        self.combobox1=ttk.Combobox(self.reports, values=self.options)
        self.combobox1.pack()

        #initate table
        self.incometable= ttk.Treeview(self.reports, columns=('dates', 'income sources', 'income amount'))#use a tuple to store the names of the columns)
        self.incometable.pack()

        #declare table headers
        self.incometable.heading('dates', text="Dates")
        self.incometable.heading('income sources', text="Income revenue")
        self.incometable.heading('income amount', text='amount')

        #inserting values to the table
        for date, source, incomess in zip(dates, income_sources, income):#zip method to combine elements from multiple lists
            self.incometable.insert(parent='', index=0, values=(date,source, incomess))#in here each date variables is represented on the dates list,
            # sources from the income revenue list and incomeess from the income amount list to decide to add later
        self.days = []
        self.income = []

        self.incgraphbutton=Button(self.reports, text="view income graph", command=lambda:self.incomegraph(dates, income))
        #lambdas serves as a nameless function
        self.incgraphbutton.pack()

        self.combobox2 = ttk.Combobox(self.reports, values=self.options)
        self.combobox2.pack()
        # initate table
        self.expensetable = ttk.Treeview(self.reports, columns=(
        'dates', 'expenses', 'expense amount'))  # use a tuple to store the names of the columns)
        self.expensetable.pack()

        # declare table headers
        self.expensetable.heading('dates', text="Dates")
        self.expensetable.heading('expenses', text="Expenses")
        self.expensetable.heading('expense amount', text='Expense amount')

        for expensedates, source, expenseamount in zip(expdates, expensesource, total_expenses):
            self.expensetable.insert(parent='', index=0, values=(expensedates, source, expenseamount))

        self.expensedays = []
        self.expense = []

        self.expgraphs = Button(self.reports, text="view expense graph", command=lambda:self.expensesgraph(expdates, total_expenses))
        self.expgraphs.pack()

        self.create_budget_goals=Button(self.reports, text="Create budget goals", command=self.open_create_budget_goals)
        self.create_budget_goals.pack()

        #to pass on later to another class
        self.income_sources=income_sources
        self.expensesource=expensesource

        self.reports.mainloop()
    def incomegraph(self, dates, incomes):

        today=datetime.today()
        selected_option=self.combobox1.get()

        if selected_option == "current week":
            for i, j in zip(dates, incomes):
             currentday=datetime.strptime(i,"%m/%d/%Y")# to convert the dates taken as a string to a datetime object
             current_week=today.weekday()#calculate the difference to the previous mondays #monday is 0, tuesday=1
             start_of_week=currentday-timedelta(days=current_week)#to calvculate the diffrences between these two dates

             if start_of_week<=currentday<=today:
                   self.days.append(i)
                   self.income.append(j)

            if self.days and self.income:
               plt.clf()#clear the current graph but keep the windows open
               plt.plot(self.days, self.income)
               plt.show()

        elif selected_option =="current month":

            for i, j in zip(dates, incomes):
                currentday = datetime.strptime(i,
                                               "%m/%d/%Y")  # to convert the dates taken as a string to a datetime object
                beginning_of_the_month = today.replace(day=1)  # to replace the day label to the beginning of the month
                end_of_month = today.replace(day=31)
                # difference = currentday - timedelta(days=)  # to calvculate the diffrences between these two date

                if beginning_of_the_month.date() <= currentday.date() <= today.date() <= end_of_month.date():  # by using .date it will only consider the dates
                    self.days.append(i)  # if condition fulfilled date will be appended
                    self.income.append(j)  # if conditions fulfilled income shall be appendedd

            if self.days and self.income:
                plt.clf()
                plt.plot(self.days, self.income)
                plt.show()

        #plt.plot(dates, incomes)#dates is x axis, incomeamount is y axis
        #plt.show()#to show the graph'''

        elif "current year":

            for i, j in zip(dates, incomes):
                currentday = datetime.strptime(i,"%m/%d/%Y")  # to convert the dates taken as a string to a datetime object
                beginning_of_the_year = today.replace(month=1,day=1)  # to replace the day label to the beginning of the month
                end_of_year = today.replace(month= 12, day=31)
                # difference = currentday - timedelta(days=)  # to calvculate the diffrences between these two date

                if beginning_of_the_year.date() <= currentday.date() <= today.date() <= end_of_year.date():  # by using .date it will only consider the dates
                    self.days.append(i)  # if condition fulfilled date will be appended
                    self.income.append(j)  # if conditions fulfilled income shall be appendedd

            if self.days and self.income:
                plt.clf()
                plt.plot(self.days, self.income)
                plt.show()

    def expensesgraph(self, expensedate, expenses):
        today = datetime.today()
        selected_option = self.combobox2.get()

        if selected_option == "current week":

            for i, j in zip(expensedate, expenses):
                currentday = datetime.strptime(i,"%m/%d/%Y")  # to convert the dates taken as a string to a datetime object
                current_week = today.weekday()  # calculate the difference to the previous mondays #monday is 0, tuesday=1
                difference = currentday - timedelta(days=current_week)  # to calvculate the diffrences between these two dates

                if difference <= currentday <= today:
                    self.expensedays.append(i)
                    self.expense.append(j)

            if  self.expensedays and self.expense:
                plt.clf()
                plt.plot( self.expensedays, self.expense)
                plt.show()


        elif selected_option =="current month":

            for i, j in zip(expensedate, expenses):
                currentday = datetime.strptime(i,"%m/%d/%Y")  # to convert the dates taken as a string to a datetime object
                beginning_of_the_month= today.replace(day=1)#to replace the day label to the beginning of the month

                #difference = currentday - timedelta(days=)  # to calvculate the diffrences between these two date

                if beginning_of_the_month.date() <= currentday.date() <= today.date():#by using .date it will only consider the dates
                    self.expensedays.append(i)#if condition fulfilled date will be appended
                    self.expense.append(j)#if conditions fulfilled income shall be appendedd

            if  self.expensedays and self.expense:
                plt.clf()
                plt.plot( self.expensedays, self.expense)
                plt.show()

        elif "current year":

            for i, j in zip(expensedate, expenses):
                currentday = datetime.strptime(i,"%m/%d/%Y")  # to convert the dates taken as a string to a datetime object
                beginning_of_the_year = today.replace(month=1,day=1)  # to replace the day label to the beginning of the month
                end_of_year = today.replace(month=12, day=31)
                # difference = currentday - timedelta(days=)  # to calvculate the diffrences between these two date

                if beginning_of_the_year.date() <= currentday.date() <= today.date() <= end_of_year.date():  # by using .date it will only consider the dates
                    self.expensedays.append(i)  # if condition fulfilled date will be appended
                    self.expense.append(j)  # if conditions fulfilled income shall be appendedd

            if  self.expensedays and self.expense:
                plt.clf()
                plt.plot( self.expensedays, self.expense)
                plt.show()

    def open_create_budget_goals(self):
        self.reports.destroy()
        types_of_budget_goals(self.days, self.income, self.income_sources, self.expensedays, self.expensesource,self.expense)