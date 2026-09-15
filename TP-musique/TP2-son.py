import numpy as np
from matplotlib import pyplot as plt

#note pour plus tard: @np.vectorize

from IPython.display import Audio
from IPython.display import display
from scipy.io import wavfile

RATE = 44_100
LA = 440
DO = 523.25

# SYNTHETISEUR - FREQUENCE

#1. Le tableau doit contenir 44100 échantillons.

#2. Position=np.sin(t*phi*2*np.pi) avec t le temps et phi la fréquence

#3.

T=np.linspace(0,1,RATE) #changer le 1 en 0.050 pour afficher 50 ms.
phi=LA
Position=np.sin(T*phi*2*np.pi)

plt.plot(T,Position)
#plt.show()

display(Audio(Position,rate=RATE))


