def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    inverseWord = palabra[::-1]
    if palabra == inverseWord:
        True
    else:
        False


def run():
    palabra = input('Escribe una palabra o frase: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Tu palabra o frase es un palindomo')
    else:
        print('Tu palabra o frase NO es un palindromo')


if __name__ == '__main__':
    run()
