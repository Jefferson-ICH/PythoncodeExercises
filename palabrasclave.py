""" lenguaje ="Python"

if lenguaje=="Python":
    print("Es de acuerdo Python es el lenguaje")
elif lenguaje == "Java":
    print("Es interesante Java")
else:
    print("Alun rato exista un nuevo lenguaje") """

#While
x=0
while x<5:
    print("hola",(x))
    x += 1

#FOR

for i in range(6):
    print("es",(i))

#for-continue

for i in range(7):
    if i==4:
        continue
    print(i)

#while - break

x=0
while True:
    print(x)
    if x==3:
        break
    x += 1

#True -False-None

x=(8==0)
print(x)

x= True
if x:
    print("Hola")

def mi_funcion():
    pass
print(mi_funcion())


#def
def funcion_suma(a, b):
    print("La suma es", a + b)

funcion_suma(3, 5)
#
def funcion_suma(a, b):
    return a + b

suma = funcion_suma(3, 5)
print("La suma es", suma)

#Lambda
print("La suma es", (lambda a, b: a + b)(3, 5))

#pass
def funcion_suma(a, b):
    pass

#yield
#está asociado a los generadores y las corrutinas, un concepto un tanto avanzado pero muy interesante.

def generador():
    n = 1
    yield n

    n += 1
    yield n
    
    n += 1
    yield n

    n += 1
    yield n

for i in generador():
    print(i)


#Class clases

class Miclase:
    def __init__(self):
        print("Creando un objeto de miclase")
objeto=Miclase()

class Milugar:
    def __init__(self) -> None:
        print("En mi lugar")
objeto=Milugar()




   
