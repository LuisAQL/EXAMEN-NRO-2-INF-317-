# RESTA
import cv2
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

# Leer las imágenes en escala de grises
img1 = cv2.imread('/content/drive/My Drive/INF317/2DOEXAMEN/imagen3.jpg', 0)
img2 = cv2.imread('/content/drive/My Drive/INF317/2DOEXAMEN/imagen4.jpg', 0)

# Verificar si las imágenes fueron leídas correctamente
if img1 is None:
    print("Error img1")
elif img2 is None:
    print("Error img2")
else:
    resultado = cv2.subtract(img1, img2)

    # Mostrar la imagen resultante usando matplotlib
    plt.imshow(resultado, cmap='gray')
    plt.title('resultado ')
    plt.axis('off')
    plt.show()
