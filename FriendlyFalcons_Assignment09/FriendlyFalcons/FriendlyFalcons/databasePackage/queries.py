# File Name: queries.py
# Student Name: David Becker, Ian McDaniel, Derick Bellofatto
# Email: beckerd8@mail.uc.edu, mcdaniip@mail.uc.edu, bellofdk@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Access SQL Server data from the GroceryStoreSimulator DB and print a formatted result using modularized Python code.
# Brief Description of what this module does: Contains all DB query functions getting products, manufacturer name, brand name, and sales data.
# Anything else that's relevant: 

from unittest import result
from databasePackage.connector import *

def get_all_products():
    '''
    Retrieve all product entries from the database.
    @return list: A list of tuples, each containing (ProductID, UPC-A, Description, ManufacturerID, BrandID)
    '''
    db = DBConnection()
    db.cursor.execute("SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct")
    return db.cursor.fetchall()

def get_manufacturer_name(manufacturer_id):
    '''
    Retrieve the manufacturer name associated with the given ManufacturerID.
    @param manufacturer_id int: The ID of the manufacturer
    @return str: The name of the manufacturer if found, otherwise "Unknown"
    '''
    db = DBConnection()
    db.cursor.execute(f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}")
    result = db.cursor.fetchone()
    return result[0] if result else "Unknown"

def get_brand_name(brand_id):
    '''
    Retrieve the brand name associated with the given BrandID.
    @param brand_id int: The ID of the brand
    @return str: The name of the brand if found, otherwise "Unknown"
    '''
    db = DBConnection()
    db.cursor.execute(f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}")
    result = db.cursor.fetchone()
    return result[0] if result else "Unknown"

def product_sales(product_id):
    '''
    Calculate the total quantity sold for a specific product based on ProductID.
    @param product_id int: The ID of the product to analyze
    @return int or str: The number of items sold if data is found, otherwise "Unknown"
    '''
    db = DBConnection()
    db.cursor.execute(f"SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = {product_id})")
    result = db.cursor.fetchone()
    return result[0] if result else "Unknown"
