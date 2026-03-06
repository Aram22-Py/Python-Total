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


#EXAMPLE: in this case, the function returned a list with the 2 values
lista_numeros=[0,1,2,300,1000,4000]
def cantidad_pares(lista_numeros):
    suma_pares=0
    cantidad_pares=0
    for n in lista_numeros:
        if n%2==0:
            suma_pares=suma_pares + n
            cantidad_pares+=1
        else:pass
    return [cantidad_pares,suma_pares]
pares_c=cantidad_pares(lista_numeros)
print(pares_c)


#Example
from random import randint
def lanzar_dados(): #we through the dice and we obtain 2 random results
    resultado_dado1=randint(1,6)
    resultado_dado2 =randint(1,6)
    return (resultado_dado1, resultado_dado2)
dados_resultado= lanzar_dados()#we call the function to obtain the 2 dice results

#we use dice results to evaluate our chances according to the text
def evaluar_jugada(dados_resultado):
    suma_dados=dados_resultado[0] + dados_resultado[1]
    if suma_dados<=6:
        return print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados>6 and suma_dados<10:
        return print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados>=10 and suma_dados<=12:
        return print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")        
final=evaluar_jugada(dados_resultado)
print(final)

#excercise "REMOVING DUPLICATES"
lista_numeros=[1,2,15,7,2,1,7,2,2,2,2,2]
reduce_=[]
def reducir_lista(lista):
    reduce_=[]
#esta parte nos ayuda a "comparar" 2 listas, basicamente agregamos 1 elemento a una lista vacía
#pero que venga de la lista dada. Entonces, en la sig iteración, si el elemento ya está en la nueva lista simplemente no lo agregamos y así vamos eliminando duplicados
    for n in lista:
        if n not in reduce_:
            reduce_.append(n)
        else:
            pass
    reduce_.remove(max(lista))
    return reduce_

xy=reducir_lista(lista_numeros)
print(xy)
#new function with average obtained from previous list
def promedio(lista):
    suma=0
    for n in lista:
        suma= suma +n
    return (suma/len(lista))
average=promedio(xy)
print(average)


#ejemplo
from random import choice
moneda=["Cara", "Cruz"]
lista_numeros=[1,2,3,4,5]
def lanzar_moneda():
    moneda=["Cara", "Cruz"]
    resultado_lanzamiento=choice(moneda)
    return resultado_lanzamiento
lanzamiento=lanzar_moneda()

def probar_suerte(lanzamiento,lista):
    if lanzamiento=="Cara":
        texto_cara=print("La lista se autodestruirá")
        lista.clear()
        return lista
    elif lanzamiento=="Cruz":
        texto_cruz=print("La lista fue salvada")
        return lista

