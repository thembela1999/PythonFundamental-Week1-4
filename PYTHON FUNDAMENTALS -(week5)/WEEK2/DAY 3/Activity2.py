import pandas as pd 

df = pd.DataFrame({'Date':['7/10/19', '8/10/19', '9/10/19', '10/10/19', '11/10/19'],'Hours Worked': [7, 7, 7, 7, 7]}) 


print(df)

Total_hours = df['Hours Worked'].sum()
print("You have worked total of ====>" ,round(Total_hours),"hours")
print(" — — — — — — — — — — — — — — — — — — — — — — — — — — —") 



