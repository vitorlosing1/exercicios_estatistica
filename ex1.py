import statistics

notas = [14,19,16,17]

media_notas = sum (notas) / len(notas)
print (media_notas)

mediana_notas = statistics.median(notas)
print (mediana_notas)

moda_notas = statistics.mode(notas)
print(moda_notas)