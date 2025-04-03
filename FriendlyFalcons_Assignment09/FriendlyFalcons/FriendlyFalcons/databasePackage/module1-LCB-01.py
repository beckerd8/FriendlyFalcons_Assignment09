import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=GroceryStoreSimulator;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()

# Execute your query
query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
cursor.execute(query)

# Print column names
columns = [column[0] for column in cursor.description]
print("Column headers:", columns)

# Print the first few rows to see the data
rows = cursor.fetchmany(5)
for row in rows:
    print(row)


