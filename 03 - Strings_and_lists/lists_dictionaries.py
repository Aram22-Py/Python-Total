#some LISTS properties
mi_lista= [1,"dos", True, "nope", -5]

#Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

#Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado.
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)



#Dictionaries
#trusted resource from Udemy : https://claude.ai/public/artifacts/1550b6ba-0e0d-44f0-9307-cf207cc33b67

producto = {"nombre": "Laptop", "precio": 850}
# Agregar una clave nueva
producto["marca"] = "HP"
# → {"nombre": "Laptop", "precio": 850, "marca": "HP"}

# Modificar un valor existente
producto["precio"] = 799
# → {"nombre": "Laptop", "precio": 799, "marca": "HP"}

#useful METHODS for dictionaries
print (type(producto))
print (producto)
print(producto.keys())
print(producto.values())
print(producto.items())
print(producto.keys())
print(producto.update({"stock": 10}))

print (producto)
print(len(producto)) #how many keys

# Eliminar una clave
del producto["marca"]
# → {"nombre": "Laptop", "precio": 799}

# Eliminar y obtener el valor
precio = producto.pop("precio")
# precio = 799, producto = {"nombre": "Laptop"}

#EJERCICIO 1
Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#solution
print(mi_dict['puntos']['points2'][1])

#EJERCICIO 2
#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), 
#y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son: ocupación=Editora, edad=36
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"] = 36
mi_dic["ocupacion"] ="Editora"
mi_dic.update({"pais": "Colombia"})

print(mi_dic)
