import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data , index=labels)

count = df["score"].isna().sum()

score = 2.5, 9, 16.5, 9, 20, 14.5, 8, 19 , 0 , 0
print(df)
average = sum(score) / len(score)

print("The average score achieved in this assessment is :",str(round(average, 2)))
print("The total amount of NAN values in the dataframe is :" , count)