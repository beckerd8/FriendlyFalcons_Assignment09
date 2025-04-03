# File Name: logic.py
# Student Name: David Becker, Ian McDaniel, Derick Bellofatto
# Email: beckerd8@mail.uc.edu, mcdaniip@mail.uc.edu, bellofdk@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Access SQL Server data from the GroceryStoreSimulator DB and print a formatted result using modularized Python code.
# Brief Description of what this module does: Builds and returns a grammatically correct summary sentence using fetched data.
# Citations: 
# Anything else that's relevant: 

def build_sentence(description, manufacturer, brand, query_sales):
    """
    Makes a sentence about a product using description, manufacturer, brand, and its units sold
    """
    return f"The product \"{description}\" by {manufacturer}, under the {brand} brand, has sold {query_sales} units."