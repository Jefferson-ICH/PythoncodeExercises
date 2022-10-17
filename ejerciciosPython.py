import string


def max(n1:int, n2:int):
    if n1>n2:
        return n1
    elif n2>n1:
        return n2
    else:
        print("No , se puede comparar")

print(max(3,5))

def max_tres(n1:int, n2:int, n3:int):
    if n1>n2>n3:
        return n1
    elif n2>n3:
        return n2
    elif(n1>n3):
        return n1
    elif(n1==n2 and n2 ==n3 and n3==n1):
        print("Son valores iguales")
    else:
        return n3

print(max_tres(51,2,51))


def longitudChar(cadena):
    c=0
    for i in cadena:
        c +=1
    print("la cadena tiene %d caracteres" %c)


string = input("Ingrese la cadena de caracteres:")
longitudChar(string)

def es_vocal(caracter):
    lista_vocales = ['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    else:
        return False

print(es_vocal('d'))

def suma(lista):
    result=0
    for n in lista:
        result = result + (n)

    print(result)

suma([1,2,-3,5])


def mult(lista):
    result = lista[0]
    i=1
    while i in range(1,len(lista)):
        result = result * lista[i]
        i +=1
        print(result)

mult([1,2,5,0])

nombre="jefferson"
nombre.upper()
'JEFFERSON'
nombre
'jefferson'
nombre.capitalize()
'Jefferson'
nombre
'jefferson'
nombre=nombre.capitalize()
nombre
'Jefferson'
nombre=nombre.strip()
nombre
'Jefferson'
nombre=nombre.lower()
nombre
'jefferson'
nombre=nombre.strip()
nombre
'jefferson'
nombre=nombre.capitalize()
nombre
'Jefferson'
nombre.replace('o','a')
'Jeffersan'
nombre.replace('o','e')
'Jeffersen'
nombre.replace('Jefferson','Jeff')

#rebanadas


nombre="Jefferson"
nombre
'Jefferson'
nombre[3]
'f'
nombre[0:4]
'Jeff'
nombre[:4]
'Jeff'
nombre[3:]
'ferson'
nombre[1:6]
'effer'
nombre[1:6:2]
'efr'
nombre[2:6:2]
'fe'
nombre[::2]
'Jfesn'
nombre[::-1]
'nosreffeJ'