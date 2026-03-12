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
