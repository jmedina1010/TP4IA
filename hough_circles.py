import cv2
import numpy as np  
import matplotlib.pyplot as plt  

def detect_circles(image_path):  
    # Cargar la imagen  
    image = cv2.imread(image_path)  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    
    # Aplicar un filtro de desenfoque para reducir el ruido  
    blurred = cv2.medianBlur(gray, 5)  
    
    # Detectar círculos usando la Transformada de Hough  
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20,  
                               param1=50, param2=30, minRadius=0, maxRadius=0)  
    
    # Dibujar los círculos detectados  
    if circles is not None:  
        circles = np.uint16(np.around(circles))  
        for i in circles[0, :]:  
            # Dibujar el círculo exterior  
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)  
            # Dibujar el centro del círculo  
            cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)  
    
    # Mostrar la imagen con los círculos detectados  
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  
    plt.title('Circle Detection using Hough Transform')  
    plt.axis('off')  
    plt.show()  

# Ruta a tu imagen  
image_path = 'C:/Users/Esteban/Documents/SIGLO/IA/TP4/iatp4.jpg'  
detect_circles(image_path)