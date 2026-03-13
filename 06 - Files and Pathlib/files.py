#Now we are learning about opening, reading and modifying files
text1=open('texto.txt')#we storage and open it here
print(text1.read())#we read the document IMPORTANT: to use the method .read()

#read 1 line
text1=open('texto.txt')
print(text1.readline())

#here we have now the availability to write something on the file opening it with '"w"' i will oeverwrite on the file deleting
#everything that was there before
archivo=open('mi_archivo.txt','w')
archivo.write("Nuevo texto")
archivo=open('mi_archivo.txt','r')# here we open the file to read it with 'r'
print(archivo.read())
archivo.close()

#now we have the option in opening the dile with 
archivo=open('mi_archivo.txt','a')
archivo.write("Nuevo inicio de sesión")
archivo=open('mi_archivo.txt','r')# we have to open it again with readable mode
print(archivo.read())
archivo.close()

#example
reg_sesion=open("registro.txt",'a')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for info in registro_ultima_sesion: #add each element of the list at the end of the file
    reg_sesion.write(info +"\t")
reg_sesion=open("registro.txt",'r')
print(reg_sesion.read() )



#example with FUNCTIONS
def abrir_leer(parametro): #it opens a file and returns what is read
    texto=open(parametro,'r')
    return texto.read()


#example, it overwrites all thext with the specified
def sobrescribir(parametro):
    texto=open(parametro,'w')
    return texto.write("contenido eliminado")

#Example. it adds text at the end of the cursor
def registro_error(parametro):
    texto = open(parametro, 'a')
    return texto.write("se ha registrado un error de ejecución")
