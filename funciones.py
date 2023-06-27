
import funciones as pn
def validalen(texto, large, estricto):
    while True:
        entrada=input(texto)
        if estricto:
            if len(entrada)==large:
                break
            else:
                print(f"El largo debe ser de 80 caracteres maximo {large} ")
        else:
            if len(entrada)>=large:
                break
            else:
                print(f"El largo minimo debe ser de 2 caracteres {large}")
    return entrada

def validamail():
    while True:
        correo=validalen("Ingrese su correo que contenga @ y . ",6,False).upper
        if correo=="@":
            if correo==".":
                break
            else:
                print("Debe contener . el correo ")
        else:
            print("Debe contener @ el correo")
    return correo

def mostrarparticipante(nombre, rut, fono, correo, categoria):
    if len(rut)!=0:
        opl=0
        while True:
            opl=int(input("Buscar participante por rut \n = "))
            if opl==1:
                while True:
                    ruts=int("Ingrese el rut del participante ")
                    for a in range(len(nombre)):
                        if ruts==rut[a]:
                            print(f"{nombre[a]} | {categoria[a]} | {fono[a]} | {correo[a]} ")
                            break
            else:
                break
    else:
        print("Rut ingresado no a sido encontrado en los participantes \n = ")

def buscarpareja(parejas):
    while True:
        pareja=validalen("Ingrese el nombre de la persona para buscar su pareja \n = ",2 , False)
        existe=False
        for p in range(len(parejas)):
            if pareja==parejas[p]:
                existe=True
                return p
        if not existe:
            return -1

def validaparejas(parejas):
    while True:
        pareja=validalen("Ingrese el nombre de la pareja \n = ",2, False)
        if len (parejas)!=0:
            existe=False
            if pareja in parejas:
                existe=True
            if existe:
                print("Pareja de participante encontrada ")
            else:
                break
        else:
            break
    return pareja

            






