#Crie dois conjuntos, cada um contendo 5 nomes de seus amigos.
#Alguns nomes devem estar presentes em ambos os conjuntos.
#Use um método para encontrar quais nomes aparecem em ambos
#os conjuntos e imprima o resultado.


amigos1 = ['Aldemir', 'Esther', 'Filipe', 'Wellington', 'Edwirges']
amigos2 = ['Esther', 'Larissa', 'Filipe', 'Marcus', 'Daniel']



def encontra_nome(amigos1, amigos2):
    lista1 = set(amigos1)
    lista2 = set(amigos2)
    print(lista1 & lista2)



encontra_nome(amigos1, amigos2)