#Crie uma lista com os nomes de três cidades. Peça ao usuário
#para digitar o nome de uma cidade. Se a cidade estiver na lista,
#imprima "A cidade está na lista de cidades". Se a cidade não estiver
#na tupla, imprima "A cidade não está na lista de cidades."

cidades = ['Rio de Janeiro','Brasília', 'São Paulo', 'João Pessoa']

cidade = input("Digite o nome de uma cidade: ")

if cidade in cidades:
    print("A cidade está na lista de cidades.")
else:
    print("A cidade não está na lista de cidades.")