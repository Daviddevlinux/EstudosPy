#Crie uma função lambda que eleve o número ao quadrado. Em seguida, use essa
#função para calcular o quadrado de todos os números em uma lista usando um loop for.


quadrado = lambda x: x ** 2

lista_num = [2, 4, 5, 3, 1, 7, 8]

for i in lista_num:
    print(quadrado(i))