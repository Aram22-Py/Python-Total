#Errors handling
def cociente(num1,num2):
    try: #Usual code that must be tested
        print(num1/num2)
    except TypeError: #exception for an specific error
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

#another example
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print ("El archivo no fue encontrado")
    except : #any other error
        print("Error desconocido")
    else: #if no errors
        print("Abriendo exitosamente")
    finally: #no matter what happens, errors or not
        print("Finalizando ejecución")


#PYLINT 
      #a way to check errors and to improve the code
#we need to install the pylint using terminal: pip install pylint
#then we go to the directory, and we use this line to print a report (-r y) "y" is for Yes
#  pylint file1.py -r y
