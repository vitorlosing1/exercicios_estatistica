import statistics

funcionario_a = [10, 9, 11, 12, 8]
funcionario_b = [15, 12, 16, 10, 11]
funcionario_c = [11, 10, 8, 11, 12]
funcionario_d = [8, 12, 15, 9, 11]

media_a = sum(funcionario_a) / len(funcionario_a)
media_b = sum(funcionario_b) / len(funcionario_b)
media_c = sum(funcionario_c) / len(funcionario_c)
media_d = sum(funcionario_d) / len(funcionario_d)

var_fun_a = statistics.variance(funcionario_a)
var_fun_b = statistics.variance(funcionario_b)
var_fun_c = statistics.variance(funcionario_c)
var_fun_d = statistics.variance(funcionario_d)

desv_pad_a = statistics.stdev(funcionario_a)
desv_pad_b = statistics.stdev(funcionario_b)
desv_pad_c = statistics.stdev(funcionario_c)
desv_pad_d = statistics.stdev(funcionario_d)

coef_var_a = desv_pad_a / media_a
coef_var_b = desv_pad_b / media_b
coef_var_c = desv_pad_c / media_c
coef_var_d = desv_pad_d / media_d

print (f'Variância A: {var_fun_a}')
print (f'Variância B: {var_fun_b}')
print (f'Variância C: {var_fun_c}')
print (f'Variância D: {var_fun_d}')

print (f'Desvio-Padrao A: {desv_pad_a}')
print (f'Desvio-Padrao B: {desv_pad_b}')
print (f'Desvio-Padrao C: {desv_pad_c}')
print (f'Desvio-Padrao D: {desv_pad_d}')

print (f'Coeficiente de variação A: {coef_var_a}')
print (f'Coeficiente de variação B: {coef_var_b}')
print (f'Coeficiente de variação C: {coef_var_c}')
print (f'Coeficiente de variação D: {coef_var_d}')