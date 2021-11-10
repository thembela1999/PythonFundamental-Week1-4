import pandas as pd
import csv
with open('mycsv.csv','w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['Chips', 'Cooldrinks', 'Chocolates', 'Pies',  'Fruit', 'Cupcake', 'Veggies'])
    

    thewriter.writerow( ['Simba, Lays', ' Coke, Fanta', ' Cadbury, Tex',   'Pepper Steak, Chicken', 'Pear, Apple, Orange', 'vanilla, chocolate', 'spinach, cabbage'])
    