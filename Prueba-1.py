#Carillas Porcelana
#$250.000
#Implantes Dentales
#$475.000
#Ortodoncia Brackets
#$800.000
#limpieza y destartraje
#aplicacion sellante
#aplicacion fluor
#Trabajador Auxiliar, se aplicará un descuesto del 15%
#Trabajador Administrativo, se aplica un descuento del 10%
#Trabajador Docente, 5% descuento.
descuento=0
tratamiento1=0
tratamiento2=0
tratamiento3=0
total=0
Linea=30*"-"
tratamiento=0
print("1.- Auxiliar")
print("2.- Administrativo")
print("3.- Docente")
print("4.- Trabajo aqui quiero renunciar")
print("5.- Salir chao")
while True:
    try:
        trabajador=int(input("¿De que quiere Trabajar?\n: "))
        if trabajador==1:
            descuento*=0.15
            break
        elif trabajador==2:
            descuento*=0.1
            break
        elif trabajador==3:
            descuento*0.5
            break
        elif trabajador==4:
            descuento=0
            tratamiento1=0
            tratamiento2=0
            tratamiento3=0
            cuotas=0
            total=0
            trabajador=0
            break
        elif trabajador==5:
            iniciador=0
            break
    except ValueError:
        print("Las opciones solo se pueden elejir con los numeros designados")
    except:
        print("Error vuelva a intentarlo")
while trabajador==4:
    try:
        print("1.-Carillas Porcelana\n= $250.000")
        print("2.-Implantes Dentales\n= $475.000")
        print("3.-Ortodoncia Bracket\n= $800.000")
        print("4.-No deseo otro tratamiento salir")
        op1=int(input("¿Que tratamiento desea ordenar? \n: "))#cotizacion
        if op1==1:
            tratamiento1+=250000
        elif op1==2:
            tratamiento2+=475000
        elif op1==3:
            tratamiento3+=800000
        elif op1==4:
            break
    except ValueError:
        print("Las opciones de tratamiento solo se escogen con numeros")
while trabajador==4:
    try:
        cuotas=int(input("¿En cuantas cuotas quiere pagar su tratamiento?\n Recuerde el minimo es de 3 y el maximo de 60\n= "))
        if 3<=cuotas<=60:
            break
        else:
            print("El limite de cuotas es de 3 hasta 60")
    except ValueError:
        print("Cuotas solo con numeros porfavor")
    except:
        print("Error vuelva a intentarlo")         
print(f"{Linea}")
print("Cotización")
print(f"{Linea}")
total+=(tratamiento1+tratamiento2+tratamiento3)
subtotal=total
subtotal*=descuento
if trabajador==1:
    if op1<0 and op1!=4:
        print(F"-->1 Tratamiento es de =\n$ {tratamiento1} ")
    elif tratamiento2<0:
        print(F"-->2 Tratamiento es de =\n$ {tratamiento2} ")
    elif tratamiento<0:
        print(f"-->3 tratamiento es de =\n$ {tratamiento3} ")
    if 3<=cuotas<=60:
        print(f"Son {cuotas} cuotas de: {total/cuotas}")
        print(f"{Linea}")
        print(f"Subtotal        ${total}")
        print(f"Descuento 15%     ${total-descuento}")
        print(f"{Linea}")
        print(f"Total                     {subtotal}")
        print(f"{Linea}")
elif trabajador==2:
    if op1<0 and op1!=4:
        print(F"-->1 Tratamiento es de =\n$ {tratamiento1} ")
    elif tratamiento2<0:
        print(F"-->2 Tratamiento es de =\n$ {tratamiento2} ")
    elif tratamiento<0:
        print(f"-->3 tratamiento es de =\n$ {tratamiento3} ")
    if 3<=cuotas<=60:
        print(f"Son {cuotas} cuotas de: {total/cuotas}")
        print(f"{Linea}")
        print(f"Subtotal                    ${total}")
        print(f"Descuento 10%     ${total-descuento}")
        print(f"{Linea}")
        print(f"Total                     {subtotal}")
        print(f"{Linea}")
elif trabajador==3:
    if op1<0 and op1!=4:
        print(F"-->1 Tratamiento es de =\n$ {tratamiento1} ")
    elif tratamiento2<0:
        print(F"-->2 Tratamiento es de =\n$ {tratamiento2} ")
    elif tratamiento<0:
        print(f"-->3 tratamiento es de =\n$ {tratamiento3} ")
    if 3<=cuotas<=60:
        print(f"Son {cuotas} cuotas de: {total/cuotas}")
        print(f"{Linea}")
        print(f"Subtotal                    ${total}")
        print(f"Descuento 5%     ${total-descuento}")
        print(f"{Linea}")
        print(f"Total                     {subtotal}")
        print(f"{Linea}")
iniciador=1
    




        

