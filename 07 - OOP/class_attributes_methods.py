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
