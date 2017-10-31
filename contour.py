import cv2
import numpy as np
original = cv2.imread('holes.jpg')
img = cv2.resize(original,(300,300))
cv2.imshow('Original',img)
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Filtrado de la Imagen 
blurimg = cv2.GaussianBlur(gris,(5,5),0)
cv2.imshow('Suavizado',blurimg)

#Deteccion de Bordes
contour = cv2.Canny(blurimg,400,475) #Hasta tener una toma estandariza los niveles (400,475) se adaptaran para cada imagen 


cv2.imshow('Contornos',contour)

#Cuenta la cantidad de contornos encontrados
(_, defectos ,_) = cv2.findContours(contour.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Se encontraron {} defectos".format(len(defectos)))

#Dibuja los defectos encontrados en la imagen original 
cv2.drawContours(img,defectos,-1,(0,255,0),2)
cv2.imshow("Defectos",img)

#k = cv2.waitKey(0)
cv2.waitKey(0)
#if k == 27:
#	cv2.destroyAllWindows()


#elif k== ord('s'):
#	 cv2.imwrite('original.png',img)
#	 cv2.imwrite('contorno.png',contour)
 #        print("Imagenes Guardadas")

