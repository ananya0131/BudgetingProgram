"""imports the pyplot from matplotlib so I can use the pie() function from it for my pie chart. Also imported numpy so i can use
a numpy array to form my pie chart and add labels. I have included the class and constructor docustrings here and method docustrings in the functions.py module"""

import matplotlib.pyplot as plt
import numpy as np


"""The class Budget contains all the methods for the program and is defined with a monthly salary and rent amount given by user"""
class Budget:
    """Initializes budget class by setting monthly salary and rent amount as given by user. Assigns an empty percent list
    that is used for the last function.
    Sets initial budget as the monthly salary
    Sets the remaining budget called budgetAfter as the salary-rent
    sets a checker as 0 which is changed throughout the class
    
    Parameters
    ----------
    self
    MonthlySalary : float
    rent : float
    
    """
    def __init__(self, MonthlySalary, rent):
        self.MonthlySalary = MonthlySalary
        self.rent = rent 
        self.percentlist = []
        self.budget = MonthlySalary
        self.budgetAfter = MonthlySalary-rent
        self.checker = 0
  
    def budg_after_rent(self):
        percent = (self.rent/self.MonthlySalary)*100
        self.budget = self.MonthlySalary-self.rent
        self.percentlist.append(int(percent))
        return "Budget After Rent is " + str(self.budget)
        
        
        
    def budg_eatingout(self):
        value = input("What percent of your budget would you like to dedicate to eating out?")
        self.checker = int(value)
        FoodBudget = (int(value)/100)*self.budget
        self.budgetAfter = self.budgetAfter-FoodBudget
        percentval = (FoodBudget/self.MonthlySalary)*100
        self.percentlist.append(int(percentval))
        return ("You can spend " + str(FoodBudget) + " on eating out")
        
    def budg_groceries(self):
        value = input("What percent of your budget would you like to dedicate to groceries?")
        if(int(value) + self.checker>100):
            return "error! You are spending a percent that is too high! Remember your percents must be below 100. Rerun this and try a lower percent"
        GroceryBudget = (int(value)/100)*self.budget
        self.budgetAfter = self.budgetAfter-GroceryBudget
        percentval = (GroceryBudget/self.MonthlySalary)*100
        self.percentlist.append(int(percentval))
        return("You can spend " + str(GroceryBudget) + " on groceries")
    
    def budg_spending(self):
        
        SpendingBudget = self.budgetAfter
        percentval = (SpendingBudget/self.MonthlySalary)*100
        self.percentlist.append(int(percentval))
        return("You have " + str(SpendingBudget) + " left over for personal expenses")
    
    def display_chart(self):
        value = input("Would You like to see this visually?(yes or no) ")
        if(value == "yes"):
            color1 = input("what would you like the rent color to be?(black, purple, yellow, green, blue, brown, maroon) dont pick 2 of the same ")
            color2 = input("what would you like the eating out color to be?(black, purple, yellow, green, blue, brown, maroon) ")
            color3 = input("what would you like the groceries color to be?(black, purple, yellow, green, blue, brown, maroon) ")
            color4 = input("what would you like the personal expense color to be?(black, purple, yellow, green, blue, brown, maroon) ")
            pie_colors = [color1, color2, color3, color4]
            newlist = np.array([self.percentlist[0],self.percentlist[1],self.percentlist[2],self.percentlist[3]])
            chartlabels = ["rent", "Eating Out", "Groceries", "Personal expenses"]
        
            plt.pie(newlist, labels = chartlabels, colors = pie_colors)
            plt.show() 
        else:
            print("Ok! Have a nice day!")
            

            
            
        
                
        

        
                    
