#Crie uma lista com carros que você tem em estoque: BMW X6,
#BMW i5, BMW i8. Peça ao usuário para que ele insira o nome 
#do carro que deseja comprar. Se o carro estiver em estoque,
#imprima "Este carro está disponível". Se não estiver em estoque,
#imprima "Desculpe, este carro não está disponível."

carros = ['BMW X6','BMW i5', 'BMW i8']

selecionar = input("Qual carro que você deseja?")

if selecionar in carros:
    print("Este carro está disponível")
else:
    print("Desculpe, este carro não está disponível.")