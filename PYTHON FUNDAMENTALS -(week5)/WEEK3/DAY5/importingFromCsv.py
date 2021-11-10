import sqlite3, csv
connection = sqlite3.connect('products.db')
cursor = connection.cursor()

with open('mycsv.csv','r') as file:
    no_records = 0
    for row in file:
        ("INSERT INTO productsTable VALUES (?,?,?,?,?,?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print('\nRecords Transferred'.format(no_records))   