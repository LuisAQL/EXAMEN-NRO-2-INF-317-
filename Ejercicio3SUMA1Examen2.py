#3
#SUMA
import cv2
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

# Leer las imágenes en escala de grises
img1 = cv2.imread('/content/drive/My Drive/INF317/2DOEXAMEN/imagen3.jpg', 0)
img2 = cv2.imread('/content/drive/My Drive/INF317/2DOEXAMEN/imagen4.jpg', 0)

# Verificar si las imágenes fueron leídas correctamente
if img1 is None:
    print("Error: No se pudo leer la imagen img1.")
elif img2 is None:
    print("Error: No se pudo leer la imagen img2.")
else:
    # Calcular la diferencia absoluta entre las imágenes
    resultado2 = cv2.absdiff(img1, img2)

    # Imprimir valores de algunos píxeles
    print('img1[0,0]= ', img1[0,0])
    print('img2[0,0]= ', img2[0,0])
    print('resultado2[0,0]= ', resultado2[0,0])

    # Mostrar la imagen resultante usando matplotlib
    plt.imshow(resultado2, cmap='gray')
    plt.title('resultado2')
    plt.axis('off')
    plt.show()
