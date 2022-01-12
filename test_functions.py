"""Test for my functions.

All my functions except the last return something and therefore only the assert for the last one can equal None
"""

from functions import budg_after_rent, budg_eatingout, budg_groceries, budg_spending, display_chart
##
##

def test_budg_after_rent():
    """Asserts that the function does return a value
    """
    assert budg_after_rent() != None

def test_budg_eatingout():
    """Asserts that the function does return a value
    """
    assert budg_eatingout() != None
    
def test_budg_groceries():
    """Asserts that the function does return a value
    """
    assert budg_groceries() != None

def test_budg_spending():
    """Asserts that the function does return a value
    """
    assert budj_spending() !=None

def test_display_chart():
    """Asserts that the function does not return a value
    """
    assert display_chart == None
    



                 
    