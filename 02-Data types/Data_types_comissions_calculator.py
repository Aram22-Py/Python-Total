#We have different types of data
#string (str) - "hola", "#$%#$", " ", "123"
#integer(int) - 5,150, 963 , -3
#floating(float) -  1.25,  205.3,  -4.5
#lists(list) - ["salt", 1 , -3, "beach", 0]
#dictionaries (dic) - {'color':'rojo', 'arte':'cine'}
#Tuples(tuple) - ('mon', 'tue', 'wed')
#sets(set) {'a','b','c','d','e'} no duplicated values

#To know what type is a variable we use
type(name_variable)

#we also have converters
#implicit converters = we dont use any functions
v1= 7.5
v2= 10
suma=v1 + v2
#si hacemos esto, el tipo será combinado de float, aunque tengamos un integer en v2
type(suma)

#explicit converters = we use special functions
int(name_variable)
float(name_variable)
string(name_variable)

#function FORMAT, kind of weird to human eye and little bit difficult to read
print("My car is {} and it has a plate number {}".format(car_color, plate_n))
puntos_anteriores = 875
puntos_nuevos = 350
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_nuevos + puntos_anteriores))


#literal chains
print(f"My car is {car_color} and it has a plate number {plate_n}")


#operators: +, -, / , * , al piso  //, module %, power **, sqrt **0.5
print(874//27)
print(456%33)
print(783**0.5)

# ROUND function, second factor rounds the decimals after point
round(number_to_round, number_of_digits_after_point)
print(round(10/3,2))




