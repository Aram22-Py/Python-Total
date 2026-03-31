#Now we have the OOP fundamentals
class Personaje: #we declarate the class
    pass
harry_potter=Personaje() # we are creating an OBJECT of the Personaje's class

#definying attributes
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color=color
        self.cantidad_pisos=cantidad_pisos
casa_blanca=Casa('blanco', 4)#in here we created a class with 2 attributes

#example
class Personaje:
    real = False # here we have a class attribute, all of the objects will have it
    def __init__(self, especie, magico, edad):
        self.especie=especie
        self.magico=magico
        self.edad=edad
harry_potter = Personaje('Humano', True, 17)


# METHODS
class Perro:
    def __init__(self):
        pass
    def ladrar(self): #basically a function that will be executed in a class instance
        print('Guau!')

##example
class Mago:
    def __init__(self):
        pass
    def lanzar_echizo(self):
        print('¡Abracadabra!')
merlin=Mago()
merlin.lanzar_echizo()



#Types of METHODS
#STATHIC method
class Mascota:
    def __init__(self):
        pass
    @staticmethod #stathic method, does not access to other methods and no class attributes, does not required an instance
    def respirar():
        print("Inhalar... Exhalar")


#Class METHOD
class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo=True #modify the class attribute



#HERITANCE
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
class Alumno(Persona):#we just pass the main class as argument and it heritates the same attributes
    pass


#EXTENDED heritance
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre, Padre):#it heritates the methods firs of the mother and then the father
    pass


# EXAMPLE 2
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
#we had 3 classes with the same method so we applied the polimorfismo to create an iterator to run it in a list of class intances
arquero1=Arquero()
mago1=Mago()
samurai1=Samurai()
#we create the list
personajes=[arquero1,mago1,samurai1]
#iterator runs it in  the list
for character in personajes:
    character.atacar()


#polomorfismo in a function
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")
#we create the function and receive any instance of any class
def personaje_defender(instancia):
    return instancia.defender()



#Special MEthods like __str__, __len__, __del__
#EXAMPLE of them
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):#makes a literal chain using attributes
        return f' "{self.titulo}", de {self.autor}'
        
    def __len__(self): #counts how many things we have on the attribute
        return self.cantidad_paginas
mi_libro=Libro("It","Stephen King",390)#we create an instance and we assign attributes
print(mi_libro)
print(len(mi_libro))
