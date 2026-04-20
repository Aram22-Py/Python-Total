#Here we have some collections
# COUNTER returns a dictionary of how many of any values are in the list
from collections import Counter
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)# OUTPUT: Counter({5: 4, 2: 3, 1: 2, 3: 2, 6: 2, 7: 2, 4: 1})


# defaultdict with the lambda functions is used to return a default value when the key is not found in a random dictionary
#and it helps so it cannot return an error
from collections import defaultdict
mi_diccionario = {"palabra clave":"edad", "valor":44}
mi_diccionario =defaultdict(lambda: "Valor no hallado", mi_diccionario)
print(mi_diccionario["cinco"])
