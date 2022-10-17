def run():
    mi_diccionario= {
        'llave1': 10,
        'llave2': 20,
        'llave3': 30,
    }
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Ecuador':1929323,
        'Colombia':213237,
        'Argentina':3827328,
    }

    #print(poblacion_paises['Ecuador'])

    #for i in poblacion_paises.keys():
    #    print(i)

    #for i in poblacion_paises.values():
    #    print(i)

    for pais,pobla in poblacion_paises.items():
        print(pais+' tiene '+ str(pobla)+ ' Habitantes')

    limite = int(input("Ingrese un limite como valor entero: "))

    i = 0
    incremento = 1
    simbolo = "*"

    while i <= limite:
        print(simbolo * (limite - i)) 
        #Funcion incremento/decremento
        i = i + incremento

if __name__=='__main__':
    run()