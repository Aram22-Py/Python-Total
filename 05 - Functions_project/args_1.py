#Usage of *args as a non-declarated number of arguments of a function
def suma_cuadrados(*args):#we can use any other text besides *args but we are goin to use it as a convention
    suma=0
    for i in args:
        suma=suma +(i**2)
    return suma
#suma_cuadrados(1,2,3)
print(suma_cuadrados(1,2,3))

#Example
def suma_absolutos(*args):
    return sum(abs(x) for x in args) #uses lists comprehension
print(suma_absolutos(-1,-2,0,1,2))

#example
def numeros_persona(nombre, *args): #takes the name and then an underterminated number of values
    suma_numeros=sum(args)
    frase=f"{nombre}, la suma de tus números es {suma_numeros}"
    return frase
print(numeros_persona("Armando",1,2,3,4,5))


#Now we have, for the arguments: **kwargs basically it stands for "keyword args"
def cantidad_atributos(**kwargs):
    cantidad=0
    for key,value in kwargs.items(): #this is because it reads **kwargs as a dictionary
        cantidad +=1
    return cantidad
print(cantidad_atributos(x=45,y=69,z=89)) #what is printed in screen is 3

#EXAMPLE:
def lista_atributos(**kwargs):
    lista1=[]
    for key,value in kwargs.items():
        lista1.append(value)
    return lista1
print(lista_atributos(x=1,y=2,z=3)) #[1, 2, 3]

#EXAMPLE
def describir_persona(nombre, **kwargs):
    Carac=f"Características de {nombre}:\n"
    for key,value in kwargs.items():
        Carac+= f"{key}: {value}\n"
    return Carac
print(describir_persona("María", color_ojos="azules",color_pelo="rubio"))

