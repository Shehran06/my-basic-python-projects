from tkinter import  *
from Savings import savings
class types_of_budget_goals:
    def __init__(self, incdates, incamount, category, expense_date, expenses, expenseamount):
        self.types_of_budget_goals= Tk()

        self.types_of_budget_goals.geometry("500x500")

        #self.label1=Label(self.types_of_budget_goals, text=incamount)
        #self.label1.pack()

        self.spending_limit=Button(self.types_of_budget_goals, text="Spending limit")
        self.spending_limit.pack()

        self.savings_target=Button(self.types_of_budget_goals, text="Saving Targets", command=self.open_saving)
        self.savings_target.pack()

        self.debt_reduce=Button(self.types_of_budget_goals, text="Debt reduction")
        self.debt_reduce.pack()

        self.emergentfund=Button(self.types_of_budget_goals, text="Emergency Fund")
        self.emergentfund.pack()

        #to pass on to the saving class
        self.incomeamount= incamount
        self.incomecategory=category

        self.types_of_budget_goals.mainloop()

    def open_saving(self):
        self.types_of_budget_goals.destroy()
        savings(self.incomeamount)


