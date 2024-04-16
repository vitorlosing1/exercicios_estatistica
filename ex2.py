import statistics

faixa_etaria = [18, 54, 20, 46, 25, 48, 53, 27, 26, 37, 40, 36, 42, 25, 27, 33, 28, 40, 45, 25]

media = sum (faixa_etaria) / len(faixa_etaria)
print (media)

mediana = statistics.median(faixa_etaria)
print (mediana)

moda = statistics.mode (faixa_etaria)
print(moda)