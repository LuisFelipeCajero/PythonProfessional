#Write square natural numbers who can be multiples of 4, 6 or 9
square = [i for i in range(1, 100) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
print(square)
#quares = [ i for i in range(1, 100000) if 1 % 36 == 0]
#print(squares)
