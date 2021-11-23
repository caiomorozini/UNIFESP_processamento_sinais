valor = int(input("Valor inteiro: "))
flag = 0
for index in range(2,valor):
    if valor % index == 0:
        flag = 1
        break
if flag == 0:
    print("{} é primo".format(valor))
else:
    print("{} não é primo".format(valor))
