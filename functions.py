"""A collection of function for doing my project"""

  

def budg_after_rent(self):
    """Calculates the budget the user can spend of their monthly salary after rent
    Finds what percent of the monthly salary it is
    Adds the percent as an int to the empty percent list
    
    Parameters
    ----------
    self
    
    Returns
    -------
    str(self.budget) : String
        budget
    """
    percent = (self.rent/self.MonthlySalary)*100
    self.budget = self.MonthlySalary-self.rent
    self.percentlist.append(int(percent))
    return "Budget After Rent is " + str(self.budget)
        
        
def budg_eatingout(self):
    """Calculates the remaining budget after the user inputs what percent of their budget they would like to spend on eating out
    every month and how much of the salary the user may spend on eating out.
    Assigns the checker variable to the user's percent they answered which is used in the next function
    Calculates what percent of the salary the eating out expense is and appends it as an int to the percent list
    
    Parameters
    ----------
    self
    
    Returns
    -------
    str(FoodBudget) : String
        eating out budget from salary
    str(self.budgetAfter): String
        remaining budget
    """
    value = input("What percent of your budget would you like to dedicate to eating out?")
    self.checker = int(value)
    FoodBudget = (int(value)/100)*self.budget
    self.budgetAfter = self.budgetAfter-FoodBudget
    percentval = (FoodBudget/self.MonthlySalary)*100
    self.percentlist.append(int(percentval))
    return ("You can spend " + str(FoodBudget) + " on eating out. The remaining budget is " + str(self.budgetAfter))


    
def budg_groceries(self):
    """calculates how much of of the monthly salary they may spend on groceries per month
    Uses checker variable to ensure both percents entered by user are not more than 100
    Calculates what percent of the salary the grocery expense is and appends it as an int to the percent list
    
    Parameters
    ----------
    self
    
    Returns
    -------
    str(GroceryBudget) : String
        Budget for groceries each month
    """
    value = input("What percent of your budget would you like to dedicate to groceries?")
    if(int(value) + self.checker>100):
        return "error! You are spending a percent that is too high! Remember your percents must be below 100. Rerun this and try a lower percent"
    GroceryBudget = (int(value)/100)*self.budget
    self.budgetAfter = self.budgetAfter-GroceryBudget
    percentval = (GroceryBudget/self.MonthlySalary)*100
    self.percentlist.append(int(percentval))
    return("You can spend " + str(GroceryBudget) + " on groceries")
    
   
    
def budg_spending(self):
    """Calculates remaining budget for personal expenses, finds what percent of the salary it is and appends it as an int 
    to the percent list
    
    Parameters
    ----------
    self
    
    Returns
    -------
    str(SpendingBudget) : String
    
    """
        
    SpendingBudget = self.budgetAfter
    percentval = (SpendingBudget/self.MonthlySalary)*100
    self.percentlist.append(int(percentval))
    return("You have " + str(SpendingBudget) + " left over for personal expenses")
    

def display_chart(self):
    """Asks user whether they would like to see how their salary is spent visually and if so, allows them to pick their
    colors and displays a pie chart
    otherwise,
    ends program
    
    Parameters
    ----------
    self
    
    
    Used https://www.w3schools.com/python/matplotlib_pie_charts.asp to learn how to make a pie chart but modified it to my code
    
    """
    
    value = input("Would You like to see this visually?(yes or no) ")
    if(value == "yes"):
        color1 = input("what would you like the rent color to be?(black, purple, yellow, green, blue, brown, maroon) dont pick 2 of the same")
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
            
        
                