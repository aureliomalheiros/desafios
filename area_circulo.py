#!/usr/bin/python3.7

'''
Calculo da área do circulo utiliando argv
Para executar o programa é necessário fazer os seguintes procedimentos:
    > Ter instalado o Python3.7
    > Permissões de execução para o programa
        > chmod ugo+x area_circulo.py
Forma de execução:
    $./area_circulo.py <raio>

'''
from math import pi
import sys

def circulo (raio):
    return pi * float (raio) ** 2

def help (error):
    print("""\
            Error!
            {} <raio>""" .format(error)) 

if __name__ == '__main__':
     
    if len(sys.argv) < 2:
        help(sys.argv[0])
    
    elif not sys.argv[1].isnumeric():
        print("Valor deve ser numerico!")

    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do círculo: ', area)
