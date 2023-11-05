#Slicing Vector
import numpy as np
a=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[100]])
print(a)
print("After Slicing")
b=a[0:7:3] # [start:stop:steps]
print(b)
c=a[1:3:1] # [start:stop:steps]
print(c)
