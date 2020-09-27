#!/usr/bin/python3.7
#
#0,1,1, 2, 3, 5, 8, 13, 21, 34 

def fibonacci(maximo):
    penultimo=0
    ultimo=1
    print('{},{}' .format(penultimo,ultimo), end=',')

    while ultimo < maximo:
        proximo = ultimo + penultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo

print('\n')
fibonacci(1000)
print('\n')
