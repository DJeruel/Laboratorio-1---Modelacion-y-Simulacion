import os
import time
λ = 10 #Tasa de ejecuciones por minuto
µ = 12 #Ejecuciones por minuto que puede soportar el servidor
s = 1 #Servidor
vagancia = s - (λ/µ)  #En minutos
cola = (((λ) / ( µ * (µ-λ) ) )) *10  #wq

#sleep => pausar el programa (seg)
tiempo = 5 #segundos por app


print ("Ejecutando aplicación 1...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 2...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 3...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 4...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 5...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 6...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 7...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 8...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 9...\n")
time.sleep(tiempo)
print ("Ejecutando aplicación 10...\n")
time.sleep(tiempo)


print ("Sistema MM1 - SOLUCION\n")
print ("Proporcion de tiempo que el servidor esta desocupado: ")
print (vagancia * 60 , " Segundos")

print ("Numero medio de programas esperando en la cola del servidor: ")
print (cola, " programas")

