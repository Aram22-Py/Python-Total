#Starting with INDEX method : searches for results in a string chain
#works with 2 paramaters, the one we are looking for and from where in indexing numbers it will start searching and a third one
#saying until what index it can search (note, if we say 10, it will search before 10)

#shows the 5th position 
palabra = "ordenador"
print(palabra[4])

#shows the position of which the entire word first letter appears
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))

#for this one, it is similar but it start search from right to left using Rindex
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))

#now, to extract elements from strings with SLICING method
text = "ABCDEFGHIJKLMNOPQ"
#this one says [ from where : to where : jumps ]
fragment = text[2:10:2]
print(fragment)

#in here we tried to extract the word "Controlar"
frase = "Controlar la complejidad es la esencia de la programación"
print(frase[0:9])

#special METHODS
#upper() - all upper cases
#split() - separate words and puts them as a list. its argument can be taken as a separator
#join() - joins variables with determiated separator, same for elements in lists
# can be used as  "separator_1".join(name_of_list)
#find() - does the same thing as index but if something is not found, it returns a -1
#replace() - requires 2 arguments, the 1st one is the word we want to replace and the 2nd one is the thing we are going to put in its place




