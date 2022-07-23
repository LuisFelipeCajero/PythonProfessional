def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantos pesos ' + tipo_pesos + ' tienes? : ')
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Usted tiene $' + dolares + ' dolares')


menu = """
Bienvenido al conversor de Monedas 💸

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

Elige una opción: 
"""

opcion = int(input(menu))

if opcion == 1:
   conversor('Colombianos', 4453.34)
elif opcion == 2:
    conversor('Argentinos', 129.76)
elif opcion == 3:
    conversor('mexicanos', 20.51)
else:
    print('Elección invalida, ingresa una opción correta, por favor')
