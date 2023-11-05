#Convert N array to N matrix
import numpy as np
a=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
b=np.mat(a)
print(type(a))
print(type(b))
print(b)
print(b.shape)
