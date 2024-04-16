numero_dentes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
numero_pessoas = [9, 5, 6, 7, 9, 5, 4, 3, 2]

multiplicacao = [x * y for x, y in zip (numero_dentes, numero_pessoas)]

media = sum(multiplicacao) / len(multiplicacao)

print (media)