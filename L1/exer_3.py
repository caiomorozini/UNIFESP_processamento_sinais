import random

def remove_duplicatas(lista):
    return list(dict.fromkeys(lista))

# Funciona independente dos valores contidos na lista.
lista_a = random.sample(range(0,10),5)
lista_b = random.sample(range(0,10),5)

#lista_a = ["banana","maca","pera"] #teste com strings
#lista_b = ["uva","banana"]

print("Lista a: {} \nLista b: {}".format(lista_a,lista_b))

lista_c = remove_duplicatas(lista_a+lista_b)

valores_comuns = [x for x in lista_a for y in lista_b if x == y]
print("Valores comuns nas listas a e b: {}".format(remove_duplicatas(valores_comuns))) # Letra a

for valor in valores_comuns:
    lista_a.remove(valor)
    lista_b.remove(valor)
    lista_c.remove(valor)

print("Valores que só existem em a: {}".format(lista_a))    # Letra b
print("Valores que só existem em b: {}".format(lista_b))    # Letra c
print("Valores que não se repetem: " + str(lista_c))        # Letra d