#Usage of *args as a non-declarated number of arguments of a function
def suma_cuadrados(*args):#we can use any other text besides *args but we are goin to use it as a convention
    suma=0
    for i in args:
        suma=suma +(i**2)
    return suma
#suma_cuadrados(1,2,3)
print(suma_cuadrados(1,2,3))
