#Añadiendo un nueva forma de crear listas a partir de un
# ciclo [element for element in iterable if condition]

def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #        squares.append(i**2)
    
    # print(squares)

    square = [i for i in range(1, 100000) if i % 9 == 0 and i % 6 == 0 and i % 4 == 0]
    print(square)
if __name__ == '__main__':
    run()
