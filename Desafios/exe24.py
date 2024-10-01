#Crie uma função que aceita um número como entrada e retorna o quadrado desse número

num = int(input("Digite um número:"))

def retorna_quadrado(num):
    return num * num


resultado = retorna_quadrado(num)

print(f'O quadrado de {num} é {resultado}')