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
