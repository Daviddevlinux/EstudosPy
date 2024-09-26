#Crie um loop que imprima os números de 1 a 10, mas pare de imprimir assim 
#que chegar a 5 usando o comando "break". Em seguida, crie um segundo loop 
#que loop que imprima os números de 1 a 10, mas pule a impressão do número 5
#usando o comando "continue".

for i in range(1, 11):
    print(i)
    if i == 5:
        break
    
print("---")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

