#Crie uma função que calcule a potência de um número. A função deve aceitar
#dois argumentos: a base e o expoente. No entanto, se o expoente não for fornecido
#ao chamar a função, ele deve assumir o valor padrão de 2.


def calcula_potencia(base, expoente=2):
    result = base ** expoente
    return result


print(calcula_potencia(3))
print("------")
print(calcula_potencia(3, 3)) 