import numpy as np
import matplotlib.pyplot as plt

# Exercice 1

# Création de tableau puis affichage en image.
"""
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
"""

# Lecture d'une image en couleur
IMAGE=plt.imread("data/les-mines.jpg")
IMAGECOPIE=IMAGE.copy()
plt.imshow(IMAGECOPIE)
#plt.show()
print(IMAGECOPIE.flags.writeable)
print(type(IMAGECOPIE)) #C'est un ndarray
#Pour trouver sa dimension, on peut donc utiliser .shape
print(IMAGECOPIE.shape) #-> 533 pixels par 800
print(IMAGECOPIE.nbytes/(IMAGECOPIE.shape[0]*IMAGECOPIE.shape[1])) #-> 3 bytes par pixel
print(IMAGECOPIE.dtype) #-> entiers uint8 (sur 8bits)
print(IMAGECOPIE.min(), IMAGECOPIE.max()) #-> 0 et 255 sont les minimum et maximum atteints

plt.imshow(IMAGECOPIE[:10,:10,:])
#plt.show()

