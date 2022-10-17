from turtle import st
def conversorPesos(tipodolar,valordolar):
    dolar=input("Ingrese los dolares que tiene para cambiar a "+ tipodolar+"\n")
    dolar=float(dolar)
    pesos= dolar * valordolar
    pesos=round(pesos,2)
    pesos=str(pesos)
    print("Tienes $ "+pesos+" pesos.")

def conversorEuro(tipodolar,valordolar):
    dolar=input("Ingrese los dolares que tiene para cambiar a "+ tipodolar+"\n")
    dolar=float(dolar)
    euro= dolar*valordolar
    euro=round(euro,2)
    euro=str(euro)
    print("Tienes $ "+euro+" Euros")

def conversorYen(tipodolar,valordolar):
    dolar=input("Ingrese los dolares que tiene para cambiar a "+ tipodolar+"\n")
    dolar=float(dolar)
    yen=dolar*valordolar
    yen=round(yen,2)
    yen=str(yen)
    print("Tienes $ "+yen+" Yenes.")



 

print("A cual moneda quiere convertir: ")
opcion=input("\n 1.Peso Colombiano \n 2.Euros \n 3.Yenes \n 4.Peso Mexicano \n")
opcion=int(opcion)
if opcion==1:
    conversorPesos("Pesos colombianos", 3785)
elif opcion==2:
    conversorEuro("Euros", 1.20)
elif opcion==3:
    conversorYen("Yenes", 114.20)
elif opcion==4:
    conversorPesos("Pesos Mexicano", 20)
else:
    print("oPCION NO VALIDA")



