# solving linear equatiopns

import numpy as np

a = np.array([[6,2], [8,1]])
b = np.array([18,16])

x = np.linalg.solve(a, b)

print(x)

