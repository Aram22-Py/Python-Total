#Functions
#define a function 
def potencia(base,expo):#takes 2 arguments
    elevado=base**expo
    return elevado #returns something and it storages it

#EXAMPLE - reversing a string
def invertir_palabra(palabra):
    palabra=palabra.upper()
    reverse1=palabra[::-1]
    return reverse1
#summoning the functions with our argument    
invert=invertir_palabra("Hello") 
print(invert) #OLLEH

#EXAMPLE a function with loops (DYNAMIC funtions)
#we want the functions to check the numbers in a list and return a True if ALL of them are positive. IF, at least 1 is negative, it will return False
lista_numeros=[1,2,5,100,-5,6]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n >= 0:
            pass
        else:
            return False
    return True
yes_no=todos_positivos(lista_numeros)
print(yes_no) #False

#Example to print a sum for only numbers in range [1,1000]
lista_numeros=[-5,-6,0,1,2,300,1000,4000]
def suma_menores(lista_numeros):
    suma=0
    for n in lista_numeros:
        if n>0 and n<1001:
            suma=suma +n
        else:pass
    return suma
print(suma_menores(lista_numeros)) #1303
