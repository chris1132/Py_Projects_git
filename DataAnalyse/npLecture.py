import numpy as np

dtype = np.dtype({"names":["name","chinese","math"],"formats":["S32","i","i"]});

person = np.array([("wang",95,85),("chao",56,55)],dtype=dtype)

print(person['name'])
