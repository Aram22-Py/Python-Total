#GENERATORS
def mi_generador() :
    x=0
    #for x in range[1,float(inf)]:
    while True:
        x+=1
        yield x #it generates a number in each new iteration
generador=mi_generador()
print(next(generador))
print(next(generador)) #prints next number
