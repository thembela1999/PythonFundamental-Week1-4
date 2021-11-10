# median funcion
# The Python median() function allows you to calculate the median of any data set
#  without first sorting the list

import numpy as np
a = np.array([[30,65,70],[80,95,10],[50,90,60]])
print ('Our array is:')
print (a)
print ('\n') 
print ('Applying median() function:')
print (np.median(a))