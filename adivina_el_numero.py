#Juego en donde la computadora genera
#un número aleatorio y pregunta al usuario
# para introducir un numero hasta que acierte

#Modulo: paquete de codigo, 
# escrito por los creadores de python
#Para ejecutar funciones ya escritas 
import random
def run():
    numero_aleatorio = random.randint(1, 100) #Generando un número aleatorio entre 1 y 100
    numero_elegido = int(input('Elige un número entre el 1 y el 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Elige un numero más grande: ')
        else: 
            print('Elige un número más pequeño: ')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Felicidadeees, ganastee!')



if __name__ =='__main__':
    run()
