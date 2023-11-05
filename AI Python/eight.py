#Slicing Matrix
import numpy as np
a=np.matrix([[4,2,3],[8,5,6],[10,8,9]])
print(a)
print("After Slicing")
b=a[:] #Same Output
print(b)
b=a[:] #Same Output
print(b)
b=a[:1] #First Raw
print("Print First Raw")
print(b)
b=a[1:] #Except First Raw
print("Print Except First Raw")
print(b)
b=a[:,:1] # First Column
print("Print First Column")
print(b)
b=a[:,1:] # ExceptFirst Column
print("Print First Column")
print(b)
b=a[:,-1:] # Except last Column
print("Print Last Column")
print(b)
