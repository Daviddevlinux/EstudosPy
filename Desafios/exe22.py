#Crie uma lista com 5 nomes de países e as capitais desses países.
#Peça ao usuário para digitar o nome de um país. Se o país estiver na lista,
#imprima "A capital de [país] é [capital]". Se o país não estiver na lista, 
#imprima "Desculpe, não temos informações sobre a capital desse país". 



pais_capital = {
    'Alemanha': 'Berlin',
    'França': 'Paris',
    'Brasil': 'Brasília',
    'Japão': 'Tóquio',
    'Canadá': 'Ottawa'
}

pais = input("Digite um país: ")

if pais in pais_capital:
    print(f"A capital de {pais} é {pais_capital[pais]}")
else:
    print("Desculpe, não temos informações sobre a capital desse país.")