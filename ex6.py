import statistics

conjunto_a = [1010, 815, 1002, 950, 1007, 1008, 1009, 1040, 1001, 903]

media = sum(conjunto_a) / len(conjunto_a)

mediana = statistics.median(conjunto_a)

moda = statistics.mode(conjunto_a)

variancia = statistics.variance(conjunto_a)

desvio_padrao = statistics.stdev(conjunto_a)

coef_variacao = desvio_padrao / media 

print (f'Média: {media}')
print (f'Mediana: {mediana}')
print (f'Moda: {moda}')
print (f'Variância: {variancia}')
print (f'Desvio-Padrão: {desvio_padrao}')
print (f'Coeficiente de Variação: {coef_variacao}')