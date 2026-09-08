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


# Accès à des parties d'image

h=5 #facteur de compression à régler à notre guise
plt.imshow(IMAGECOPIE[:,::h,:])
#plt.show()

def isoler_rectangle_central(l,c):
    nombre_lignes,nombre_colonnes=IMAGECOPIE.shape[0],IMAGECOPIE.shape[1]
    print(IMAGECOPIE.shape)
    lc=nombre_lignes//2 #ligne centrale
    cc=nombre_colonnes//2 #colonne centrale
    print(lc-l//2, lc+l-l//2,cc-c//2, cc+c-c//2)
    plt.imshow(IMAGECOPIE[max(lc-l//2,0):min(lc+l-(l//2),nombre_lignes-1),max(cc-c//2,0):min(cc+c-(c//2),nombre_colonnes-1)])
    #on sélectionne par slicing le rectangle voulu. Les min et max servent à ne pas dépasser les dimensions de l'image, donc éviter le "out of range"
    plt.show()

#isoler_rectangle_central(10,20)

