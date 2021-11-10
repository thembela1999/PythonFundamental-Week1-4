import pandas as pd

data = {"col_1": ["John" , "Peter" ,"Tinker"],
        "col_2": [" Doe", "Pan" , "Bell"],
        "col_3": [23, 29, 21]}
df = pd.DataFrame(data)
df.rename(columns = { "col_1": "Name","col_2" :"Surname","col_3": "Age"} , inplace = True)
print(df)
