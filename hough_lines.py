import cv2  
import numpy as np  
import matplotlib.pyplot as plt  

def detect_lines(image_path):  
    # Cargar la imagen  
    image = cv2.imread(image_path)  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    
    # Aplicar Canny para detección de bordes  
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)  
    
    # Detectar líneas usando la Transformada de Hough  
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)  
    
    # Dibujar líneas en la imagen original  
    if lines is not None:  
        for rho, theta in lines[:, 0]:  
            a = np.cos(theta)  
            b = np.sin(theta)  
            x0 = a * rho  
            y0 = b * rho  
            x1 = int(x0 + 1000 * (-b))  
            y1 = int(y0 + 1000 * (a))  
            x2 = int(x0 - 1000 * (-b))  
            y2 = int(y0 - 1000 * (a))  
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)  
    
    # Mostrar la imagen con las líneas detectadas  
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  
    plt.title('Line Detection using Hough Transform')  
    plt.axis('off')  
    plt.show()  

# Ruta a tu imagen  
image_path = 'C:/Users/Esteban/Documents/SIGLO/IA/TP4/iatp4.jpg'  
detect_lines(image_path)