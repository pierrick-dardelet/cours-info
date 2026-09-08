import numpy as np
import matplotlib.pyplot as plt

# Exercice 1

# Création de tableau puis affichage en image.

T=np.empty((91,91,3))
T=np.array(T,dtype=np.int16)

print(T.dtype)
print(T)

T[:,:]=[0,255,0]

T[::10]=[0,0,255]
T[:,::10]=[0,0,255]


plt.imshow(T)
plt.show()

print(T[0,0],T[-1,-1])