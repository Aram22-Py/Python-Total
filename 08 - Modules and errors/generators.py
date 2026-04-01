#GENERATORS
#"Son tipos especiales de funciones que devuelven un iterador que no almacena su contenido 
#completo en memoria, sino que "demora" la ejecución de una expresión hasta que su valor se solicita."
def mi_generador() :
    x=0
    #for x in range[1,float(inf)]:
    while True:
        x+=1
        yield x #it generates a number in each new iteration
generador=mi_generador()
print(next(generador))
print(next(generador)) #prints next number



#ejemplo
def generador1(vidas):
    x=vidas
    while x >0:
        if x==1:
            yield f"Te quedan {x} vidas"

        else:
            yield f"Te quedan {x} vidas"
        x-=1
    yield "Game Over"

perder_vida=generador1(3)
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))






# Crear generador:
# perder_vida = generador1(3)
#   ↓
# (Aún NO se ejecuta el código)
#   ↓
# Se llama next(perder_vida)
#   ↓
# Inicio del generador
#   ↓
# vidas = 3
#   ↓
# ¿vidas > 0?
#   ↓
# Sí ------------------------------- No
# ↓                                  ↓
# ¿vidas == 1?                       yield "Game Over"
# ↓                                  ↓
# No                                 (termina el generador)
# ↓
# yield "Te quedan 3 vidas"
#   ↓
# (PAUSA el generador y regresa el valor a next())
#   ↓
# Se llama next(perder_vida) otra vez
#   ↓
# Continúa DESDE donde se pausó
#   ↓
# vidas -= 1 → vidas = 2
#   ↓
# ¿vidas > 0?
#   ↓
# Sí
# ↓
# yield "Te quedan 2 vidas"
#   ↓
# (PAUSA)
#   ↓
# next() otra vez
#   ↓
# vidas -= 1 → vidas = 1
#   ↓
# ¿vidas == 1?
#   ↓
# Sí
# ↓
# yield "Te queda 1 vida"
#   ↓
# (PAUSA)
#   ↓
# next() otra vez
#   ↓
# vidas -= 1 → vidas = 0
#   ↓
# ¿vidas > 0?
#   ↓
# No
# ↓
# yield "Game Over"
#   ↓
# (PAUSA final)
#   ↓
# next() otra vez
#   ↓
# ❌ StopIteration (ya no hay más valores)
