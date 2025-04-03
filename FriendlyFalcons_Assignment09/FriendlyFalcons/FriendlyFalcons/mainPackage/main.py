# File Name: main.py
# Student Name: David Becker, Ian McDaniel, Derick Bellofatto
# Email: beckerd8@mail.uc.edu, mcdaniip@mail.uc.edu, bellofdk@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Access SQL Server data from the GroceryStoreSimulator DB and print a formatted result using modularized Python code.
# Brief Description of what this module does: Runs main logic from Steps 1–7 to fetch product data and display output.
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
    brand_id = product.BrandID  # for later use in step 5

    # Step 3 & 4: Get manufacturer name
    manufacturer = get_manufacturer_name(manufacturer_id)

    # Output
    #print("Step 1-4 complete below team (remove this later):")
    #print(f"Description: {description}")
    #print(f"Product ID: {product_id}")
    #print(f"Manufacturer ID: {manufacturer_id}")
    #print(f"Manufacturer Name: {manufacturer}")

    brand = get_brand_name(brand_id)

    #print(f"\nBRAND (Step 5):\n")
    #print(f"Brand ID: {brand_id}")
    #print(f"Brand Name: {brand}")

    query_sales = product_sales(product_id)
    #print(f"{brand} \n\nSales (Step 6): {query_sales}")

    sentence = build_sentence(description, manufacturer, brand, query_sales)
    print(sentence)