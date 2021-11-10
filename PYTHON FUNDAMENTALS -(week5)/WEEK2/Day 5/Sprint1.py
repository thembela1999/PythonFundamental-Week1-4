import pandas as pd 

x = ['Chips:', 'Cooldrinks:', 'Chocolates:', 'Pies:',  'Fruit:', 'Cupcake:', 'Veggies:']


y = ['Simba, Lays', ' Coke, Fanta', ' Cadbury, Tex',   'Pepper Steak, Chicken', 'Pear, Apple, Orange', 'vanilla, chocolate', 'spinach, cabbage'] 
# Calling DataFrame after zipping both lists, with columns specified 
df = pd.DataFrame(list(zip(x, y)), columns =['products', 'Type'], index=['a','b', 'c', 'd', 'e', 'f', 'g']) 
print(df)