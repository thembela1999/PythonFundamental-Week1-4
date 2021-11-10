# Multi_dot is used to compute the dot product of two or more arrays in a single function call,
#  while automatically selecting the fastest evaluation order. 

from numpy.linalg import multi_dot
import numpy as np


# calculate the product of the following arrays

A = np.array([ 1.2, 0.5, 1 , 5])

B = np.array([6.2, 0.9, 5, 6])

C = np.array([1, 0, 0, 5])


Result = np.dot(np.dot(A, B), C )

print(Result)