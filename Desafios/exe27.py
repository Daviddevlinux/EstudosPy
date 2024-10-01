#Mostre o fatoral de um número criando uma função para isso.
import math


def factorial_num(num):
    return math.factorial(num)

numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {factorial_num(numero)}")
