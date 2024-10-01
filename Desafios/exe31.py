#Crie uma função lambda que aceite um número e retorne
#"Par" se o npumero foir par e "Ímpar" se o número for ímpar.

retorna = lambda x: "É Par" if x % 2 == 0 else "É Ímpar" 

print(retorna(2))
print(retorna(3))