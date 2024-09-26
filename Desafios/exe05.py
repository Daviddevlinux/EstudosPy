#Crie um script que solicite ao usuário dois números.
#Em seguida, seu script deve imprimir a soma, a subtração,
#a multiplicação, a divisão (resultado decimal) e a exponenciação
#(primeiro número elevado ao segundo número) desses dois números.

num1 = int(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
exp = num1 ** num2

print("Soma: ", soma)
print("Subtração: ", sub)
print("Multiplicação: ", mult)
print("Divisão: ", div)
print("Exponenciação: ", exp)