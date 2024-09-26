#Crie uma lista de frutas que inclui "maçã" três vezes e outras
#frutas da sua escolha. Use um loop para contar quantas "maçã"
#aparecem na lista e imprima o resultado.

frutas = ['maçã', 'banana', 'laranja', 'abacate', 'maçã', 'uva', 'maçã', 'melão']

contador = 0

for x in frutas:
    if x == 'maçã':
        contador += 1
              
print(f'A fruta "maçã" aparece {contador} vezes')