import numpy as np
import matplotlib.pyplot as plt

# Exercice 1

# Création de tableau puis affichage en image.

T=np.empty((91,91,3))
T=np.array(T,dtype=np.int8)

print(T.dtype)
print(T)
plt.imshow(T)
plt.show()

