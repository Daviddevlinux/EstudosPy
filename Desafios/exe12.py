#Crie uma lista de frutas e outra de vegetais. Use um "for loop"
#aninhado (Nested for loop) para imprimir todas as combinações
#possíveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo.

frutas = ['Maçã', 'Abacaxí', 'Banana', 'Melancia']

vegetais = ['Alface', 'Cenoura', 'Couve', 'Brócolis']

for fruta in frutas:
    for vegetal in vegetais:
        print(f'{fruta} e {vegetal}')