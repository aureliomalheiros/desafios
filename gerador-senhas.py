'''
Crie um programa capaz de gerar senhas aleatorias para o usuario
Onde o usuario insira a quantidade de senhas
'''
from random import random, choice
import string

def gerar_senha (tamanho):

    senha = " "

    valores = string.ascii_letters
    valores += string.digits
    valores += string.punctuation

    for i in range (tamanho):
        senha += choice(valores)

    return senha

tamanho = int(input(" "))

print(gerar_senha(tamanho))
