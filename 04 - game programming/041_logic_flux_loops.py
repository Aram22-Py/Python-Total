#For LOGIC operators we basically have : AND, OR, NOT
#for and, all the premises must match. For Or, only 1 premise can be true or fals, and for not is deniying something
num1 = 36
num2 = 72/2
num3=48
mi_bool= num1>num2 and num1<num3
print(mi_bool)

"""Verifica si las palabras almacenadas en las siguientes variables:
palabra1 = "éxito", y
palabra2 = "tecnología" 
no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) 
en una variable llamada mi_bool: """
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = "éxito" and "tecnología" and "si" not in frase


#Conditionals IF, ELIF, ELSE
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
if num1 > num2:
    print(f"{num1} es mayor que {num2}") #------basically returns a Yes or No
elif num2 == num1: # -------it executes when there is another specific value we want to test
    print (f"{num1} y {num2} son iguales")
else:  #--------it executes if the first IF returns a False value
    print(f"{num2} es mayor que {num1}")

#example
edad = 16
tiene_licencia = False
if edad >= 18:
    if tiene_licencia == False:
        print("No puedes conducir. Necesitas contar con una licencia") 
    else:
        print("Puedes conducir") 
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")



# Loop FOR 
# it reads every element in a list, tuple, dictionary or even a string; it executes the instructions for each element
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
#in here, the variable 'alumno' is an iteration variable or a loop variable
#NOTE: the iteration variable saves the last value of the iteration.
#it keeps existing after the cycle so it is advisable to use a name with no importance or that wont be used after that loop
for alumno in alumnos_clase:
    print("Hola " + alumno)
print(alumno) #it will print the last value of the list: 'Daniela'

#example: sum all the numbers in the list
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros =0 #we give a value to the variable so it can start from zero
for numero in lista_numeros:
    suma_numeros=numero + suma_numeros
#as it was an iteration it will add the previous value with the new one and it garanties to add all of them    
print(suma_numeros)

#sum evens and odds
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero%2==0 :
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
print(suma_pares)
print(suma_impares)

#BREAKing loop
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero < 0:
        break
    else:
        print(numero)


#RANGE
mi_lista = list(range(2500,2586)) #a list is created, note that the value 2586 is not included
#creates a list from 3 to 300(included) with 3-by-3 steps
mi_lista = list(range(3,301,3))
#EJERCICIO:
"""Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). 
Almacena el resultado en una variable llamada suma_cuadrados."""
mi_lista=list(range(1,16))
suma_cuadrados =0
for numero in mi_lista:
    suma_cuadrados = suma_cuadrados + (numero**2)
print(suma_cuadrados)



#WHILE Loop
#it executes something while its  contion is accomplished
numero = 10
while numero >=0: #condition
    print(numero) #do
    numero-=1 # it decreases the variable each iteration by 1

#Example: show the numbers only multiples by 5
numero = 50
while numero >= 0:
    if numero%5==0:
        print(numero)
    numero-=1


#ENUMERATE: we can create a list with its elements and their respective index WITH: list(enumerate(name_list)
#EXAMPLE:
"""Imprime en pantalla frases como la siguiente:
'{nombre} se encuentra en el índice {indice}'
Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate(). """
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
new_list=list(enumerate(lista_nombres))
for indice,nombre in new_list:
    print(f'{nombre} se encuentra en el índice {indice}')

#works also in STRINGS
lista_indices= list(enumerate("Python"))

#EXERCISE: 
#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
new_list= list(enumerate(lista_nombres))
for indice,nombre in new_list:
    if nombre.startswith("M")== True:
        print(indice)







