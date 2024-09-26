#Comece com alista 'frutas' do desafio anterior. Primeiro,
#remova "manga" da lista usando o método remove(). Depois,
#remova o último item da lista usando o comando del. Por fim,
#imprima a lista modificada na console.

frutas = ["maçã", "banana", "manga", "uva"]

frutas.remove("manga")

#O -1 sempre remove o último da lista.
del frutas[-1]


print(frutas)