#Librerias a utilizar
import cv2
import numpy as np
import matplotlib.pyplot as plt
#cargar imagen
imagen = cv2.imread('img/hand.png')
#height, width, channels = imagen.shape
# Convertir imagen a formato RGB
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

gris = cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
#cv2.namedWindow('Imagen en gris', cv2.WINDOW_NORMAL)
cv2.imshow("Imagen en gris",gris)

_,binaria = cv2.threshold(gris,255,255,cv2.THRESH_BINARY)
print(np.array(binaria))
plt.imshow(binaria, cmap="gray")
plt.show()


