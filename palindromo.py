from operator import truediv


def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra= palabra.lower()
    palabraInvertida= palabra[::-1]
    if palabra == palabraInvertida:
        print("palabra: "+palabra+" palindromo "+palabraInvertida)
        return True
    else:
        print("palabra: "+palabra+"  palindromo:  "+palabraInvertida)
        return False

def run():
    palabra = input("Esciba una palabra: ")
    es_palindromo= palindromo(palabra)
    if es_palindromo==True:
        print("Es palindromo")
    else:
        print("no es palindromo")


if __name__=='__main__':
    run()
