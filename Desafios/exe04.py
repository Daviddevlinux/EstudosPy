#Crie um script que pergunte o nome e a idade do usuário,
#usando a função input(). Depois disso, o script deve imprimir
#uma mensagem que diga "Olá, [nome]! Você tem [idade] anos."

nome = input("Qual o seu nome?")
idade = int(input("Qual a sua idade?"))

print(f'Olá, {nome}! Você tem {idade} anos.')