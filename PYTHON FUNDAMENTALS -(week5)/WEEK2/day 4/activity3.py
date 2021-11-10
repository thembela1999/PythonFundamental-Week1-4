import pandas as pd
wine_df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
# wine_df.head()

wine_df.columns = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide','density','pH','sulphates', 'alcohol', 'quality' ]
# wine_df.filter(["volatile acidity", "pH","alcohol"]) 

wine_df.describe() 
print(wine_df)
