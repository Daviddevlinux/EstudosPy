#Crie duas funções. A primeira função deve aceitar um número e retornar o dobro desse número.
#A segunda função deve aceitar um número e retornar o quadrado desse número. Em seguida, chame
#a primeira funcção dentro da segunda para retornar o quadrado do dobro de um número.


def retorna_dobro(num):
    result = num * 2
    return result


def retorna_quadrado(num):
    dobro = retorna_dobro(num)
    result = dobro ** 2
    return result




print(retorna_dobro(3))  # Esperado: 6 (3 * 2)



print(retorna_quadrado(3))  # Esperado: 36 ((3 * 2)^2 = 6^2 = 36)
