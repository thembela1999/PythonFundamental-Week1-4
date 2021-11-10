import sqlite3
from sqlite3.dbapi2 import connect
con = sqlite3.connect('products.db')
cur = con.cursor()

sql = """
CREATE TABLE productsTable(
productsID TEXT,
product TEXT,
brand TEXT,
primary key(productsID)

)
"""

cur.execute(sql)
print('products table has been created')

con.commit()
con.close