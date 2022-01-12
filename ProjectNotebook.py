#!/usr/bin/env python
# coding: utf-8

# # Project Description

# For my project, I chose to make a Budgeting program that asks users for their monthly salary, housing costs and expenses and then provides them with a view of how their salary is alloted. 
# The program 
# -asks users for their salary and housing cost
# -provides them with a budget by subtracting the housing from the salary. This is their budget for the month
# -Then asks users how much of their budget they would like to allocate to expenses such as eating out and groceries
# -user is then given their remaining budget of personal expenses
# -user is asked if they would like to see this visually and they have the option to view their expenses from their salary on a pie chart

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:




#imports my functions and classes from their respective module files
#Program works best when you hit restart and run all under kernel
from my_module.functions import budg_after_rent, budg_eatingout, budg_groceries, budg_spending, display_chart
from my_module.classes import Budget


# In[ ]:


#value 1 asks the user their monthly salary and value2 asks user their rent ot mortgage
value1 = input("what is your Monthly Salary?")
value2 = input("what is your rent/mortgage?")
value1 = int(value1)
value2 = int(value2)
#Budget app only runs fully as long as the rent or mortgage is lower than monthly salary. If it is higher the app tells the user that perhaps where they 
#are living is too expensive to afford and suggests moving elsewhere
if(value2>value1):
    print("error! your rent is higher than your salary. You cannot afford to live here all on your own and your monthly salary does not provide enough income for you to have these expenses")
else:
    
    user_budget = Budget(value1, value2)
    print(user_budget.budg_after_rent())

    print(user_budget.budg_eatingout())
    print(user_budget.budg_groceries())
    print(user_budget.budg_spending())
    user_budget.display_chart()
        
                    


# In[ ]:





# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. Your Python Background
# 2. How your project went above and beyond the requirements of the project and/or how you challenged yourself to learn something new with the final project

# I am pretty new to Python. While I have some experience with Java, my first time learning Python was in this class. I believe my project went above and beyong because although it is not very complex, it utlized most of the concepts I learned in this class. I was initially not very good at importing files, using multiple files with .py extensions, or correctly formatting classes and that is what I wanted to focus on here in order to better improve myself. Additionally, I wanted to code something that is also useful to this day and age and because I know that some people are visual learners, I decided to include the pie chart at the end of my Budget program so users could get a holistic view at how their money is being spent per month.

# In[ ]:




