#Peça ao usuário para digitar o nome de uma fruta.
#Se a fruta não for 'abacate', o loop deve continuar
#pedindo ao usuário para digitar o nome de uma fruta.
#Se a fruta for 'abacate', o loop deve terminar e o 
#programa deve imprimir "Parabéns, você acertou a fruta!"

# O programa pede o nome de uma fruta até que o usuário digite 'abacate'
fruta = input("Digite o nome de uma fruta: ")

# Enquanto a fruta não for 'abacate' (ignorando maiúsculas e minúsculas), continua pedindo ao usuário.
while fruta.lower() != 'abacate':
    fruta = input("Digite o nome de uma fruta: ")

print("Parabéns, você acertou a fruta!")
