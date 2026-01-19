#Adivina el Numero
#Importamos el Modulo random 
import random
#Damos la Bienvenida a El Programa
print('Bienvenido a Adivina el numero')
#Creamos una variable con un numero random fuera del Bucle while 
numero_secreto = random.randint(1,20)
intentos = 0
#Mientras Sea verdad 
while True:
    #Pedimos un dato y lo convertimos en entero
    Entrada = int(input("¿Cual es el Numero (1 al 20)? "))
    #Si el dato es igual al Nuemero random que nos dio se termina el juego
    if Entrada == numero_secreto : 
        print('Felicidades Advinaste el Numero')
        print('Gracias por Jugar')
        break
    #Si el dato es distinto del numero ramdom peudes seguir jugando hasta adivinarlo   
    elif Entrada!= numero_secreto : 
        print('El Numero es incorrecto')
        #Si el Nuemero no es el correcto suma la cantidad de intentos 
        intentos+= 1 
        print(f"Intento n° {intentos}")
    else : 
        print("lo que ingresaste no es valido")
