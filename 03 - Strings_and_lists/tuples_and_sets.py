#Using Tuples
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(my_tuple.count(2)) # counts how many times the argument of the method appears in the tuple
#it can be converted to a list
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(type(mi_lista))
#extracting values and storaging them in variables
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print (d) #it will print the value 4


# SETS : collection of UNIQUE elements with no order and immutable(no changes allowed or indexing)
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3 = mi_set_1.union(mi_set_2) #union() method combine 2 sets 
#deletes a random item in the set
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo.pop())
#add an element
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
