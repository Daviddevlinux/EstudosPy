#Para esse desafio, crie uma lista de números de 1 a 10. Use um
#'for loop' para iterar sobre a lista. Se o número atual da iteração 
#for par, imprima "O número [número] é par". Se o número for ímpar,
#imprima "O número [número] é impar."

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    if i % 2 == 0:
        print(f"O número {i} é par")
    else: 
        print(f"O número {i} é ímpar")