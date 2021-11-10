import pandas as pd

import matplotlib.pyplot as plt


# df.plot(x ='Date', y='Hours Worked', kind = 'bar') 

Date =['7/10/19', '8/10/19', '9/10/19', '10/10/19', '11/10/19']
Hours_worked = [7, 7, 7, 7, 7]
plt.bar(Date, Hours_worked)
plt.title('Date vs Hours Worked')
plt.xlabel('Date')
plt.ylabel('Hours Worked')
plt.show()
