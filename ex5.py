import statistics

gasolina = [5.61, 5.64, 5.56, 5.61, 5.60, 5.58]
alcool = [4.90, 4.79, 4.88, 4.81, 4.88, 4.84]

media_gas = sum (gasolina) / len(gasolina)
media_alc = sum (alcool) / len(gasolina)

var_gas = statistics.variance(gasolina)
var_alc = statistics.variance(alcool)

desv_gas = statistics.stdev(gasolina)
desv_alc = statistics.stdev(alcool)

coef_var_gas = desv_gas / media_gas
coef_var_alc = desv_alc / media_alc

print (f'Variância Gasolina: {var_gas}')
print (f'Variância Álcool: {var_alc}')

print (f'Desvio-Padrão Gasolina: {desv_gas}')
print (f'Desvio-Padrão Álcool: {desv_alc}')

print (f'Coeficiente de variação Gasolina: {coef_var_gas}')
print (f'Coeficiente de variação Álcool: {coef_var_alc}')