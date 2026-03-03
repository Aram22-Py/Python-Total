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
