# File Name: main.py
# Student Name: David Becker, Ian McDaniel, Derick Bellofatto
# Email: beckerd8@mail.uc.edu, mcdaniip@mail.uc.edu, bellofdk@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Access SQL Server data from the GroceryStoreSimulator DB and print a formatted result using modularized Python code.
# Brief Description of what this module does: Runs main logic to fetch product data and display output.
# Citations: 
# Anything else that's relevant: 

from databasePackage.queries import *
from databasePackage.connector import *
from logicPackage.logic import *
from random import choice

if __name__ == "__main__":
    # Step 1: Get all products
    products = get_all_products()

    # Step 2: Randomly select one
    product = choice(products)
    product_id = product.ProductID
    description = product.Description
    manufacturer_id = product.ManufacturerID
    brand_id = product.BrandID

    # Step 3 & 4: Get manufacturer name
    manufacturer = get_manufacturer_name(manufacturer_id)
    brand = get_brand_name(brand_id)

    # Step 5: Get sales data
    query_sales = product_sales(product_id)


    sentence = build_sentence(description, manufacturer, brand, query_sales)
    print(sentence)