from cgitb import text



    #for contador in range(1000):
    #    if contador % 2 != 0:
    #        continue
    #    print(contador)

    #for i in range(1000):
    #   print(i)
    #   if i==679:
    #        break

    #texto= input("Escribe un texto: ")
    #for texto in texto:
    #    if texto=='o':
    #        break
    #    print(texto) 

    #cont =1
    #while cont < 1000:
    #    cont = cont+1
    #    if cont %2 !=0:
    #        continue
    #    print(cont)

    #cont =1
    #while cont < 1000:
    #    cont = cont+1
    #    if cont == 190:
    #        break
    #    print(cont)
def mostrar(letter,action):
    print("Como en la frase viene la letra " + letter + " entonces " + action)

def run():
    frase=input("Introduzca una frase: ")
    longi=len(frase)
    i=0
    while longi != 0 and i< longi:
        letra=frase[i:i+1]
        if letra.upper() == 'J':
            mostrar(letra,'salgo')
            i += 1
            break
         
        else:
            print("Letra: " + letra)
            i += 1
       



if __name__ == '__main__':
    run()