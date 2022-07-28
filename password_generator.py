# Programa que nos permite generar una contraseña aleatoria
# parecido al que genera Mozilla Firefox

import random

def generate_password():
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    signs = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']    
    caracters = capital + lowers + nums + signs

    password = []

    for i in range(12):
        caracter_random = random.choice(caracters)
        password.append(caracter_random)

    password = ''.join(password)

    return password

def run():
    password = generate_password()
    print('your new password is: ' + password)



if __name__=='__main__':
    run()
