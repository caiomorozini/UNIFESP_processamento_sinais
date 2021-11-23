import numpy as np
import scipy.special as scispe
valor_euler = int(input("Valor euler: "))

x = np.ones(20)
x[0] = 0
numerador_euler = (x*valor_euler)**x.cumsum()
denominador_euler = scispe.factorial(x.cumsum())
resultado_euler = sum(numerador_euler/denominador_euler)
print(resultado_euler)

valor_sen = int(input("Valor sen: "))
y = np.arange(1,40,2)
numerador_sen = valor_sen**y
denominador_sen = scispe.factorial(y)
resultado_sen = sum(numerador_sen/denominador_sen)
print(resultado_sen)