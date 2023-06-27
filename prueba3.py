#Grabar: Corresponde a guardar los datos de un jugador, entre ellos: Nombre del jugador, rut, fecha de nacimiento,
#categoría (Oro – Plata - Bronce), celular, identificador de parejas (nombre que le fue asignado a la pareja que compite). Además,
#debe validar que el nombre contenga al menos dos caracteres, que no tenga más de 80 años, correo contenga @ y largo mínimo 6.
import funciones as pn
nombre=[]
rut=[]
fecha=[]
fono=[]
categorias=[]
parejas=[]
correo=[]
opc1=0
ops1=0
while opc1!=4:
    print("Bienvenido ")
    print("1.- Grabar ")
    print("2.- buscar ")
    print("3.- Imprimir parejas ")
    print("4.- Salir ")
    opc1=int(input("Ingrese una opcion  \n = "))
    if opc1==1:
        nombre=pn.validalen("Ingrese el nombre de jugador \n = ",2, False)
        parejas.append(nombre)
        while True:
            rut=int(input("Ingrese rut sin digito verificador y sin punto ni gion \n = "))
            if 10000000<=rut<=99999999:
                break
            else:
                print("Ingrese denuevo el rut ")
        while True:
            fecha=int(input("Ingrese cuantos años tiene \n = "))
            if fecha<=80:
                break
            else:
                print("No se puede participar personas mayores de 80 años ")
        while True:
            ops1=int(input("Que categoria es\n 1.- Oro\n2.- Plata \n3.- Bronce \n = "))
            if ops1==1:
                categorias.append("Oro")
                break
            elif ops1==2:
                categorias.append("Plata")
                break
            elif ops1==3:
                categorias.append("Bronce")
                break
            else:
                print("Ingrese una de las 3 opciones \n = ")
        while True:
            fono=int(input("Ingrese su numero de celular de 9 digitos \n = "))
            if 100000000<=fono<=999999999:
                break
            else:
                print("Ingrese denuevo el celular ")
        correo = pn.validamail("Ingrese su correo = ")
    elif opc1==2:
        pn.mostrarparticipante(nombre, categorias, correo, fono)
    elif opc1==3:
        pn.validaparejas(parejas)
        pn.buscarpareja(parejas)
print("Alejandro Gómez Vargas Andrés PG1121_015D    ")


        
            
            




