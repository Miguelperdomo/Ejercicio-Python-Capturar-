print("Ingrese Nombre COMPLETO del conductor")
nombre= input()
print("Ingrese Documento del conductor")
documennto= int(input())
print("Ingrese la Dirrecion del conductor, EJ: Calle 18 Sur..")
direccion=input()
print("Ingrese la EPS del conductor")
eps=input()
print("Ingrese el Numero de Celular del conductor")
cell=int(input())
print("Ingrese un familiar con Nombre COMPLETO del conductor")
fami=input()
print("Ingrese Numero de celular de", fami)
nfa=int(input())

sueledomes=914000
sueldobuse=714000
gaso1=30000
gaso2=60000
gaso3=150000
gasolina2=60000
gasolina3=150000
vaitcos1=70000
viaticos2=150000
psajesbus=50
psajesbuseta=18
peaje1=12000
peajes2=20000
peajes3=33000
costo1=15000
costo2=60000
costo3=90000
cost1=15000
cost2=60000
cost3=90000


print("1.bus 2.buseta 3. Salida")
tp=int(input("Escoja del 1 al 3 \n"))

if tp== 1:
    print("Escogiste el bus")
    print("1. ruta de 1km a 50km 2. ruta de 51km a 80km 3. 81km a mas km 4. Salida del proceso")
    opc=int(input("Escoja del 1 al 4 \n"))

    if opc == 1:
      print("Escogiste la ruta de 1 a 50km")
      puestos=int(input("Cuantos pasajeros tienes \n"))
      while 50 <= puestos:
          print("Usted no puede salir")
          while 10<=puestos:
              print("Usted no puede salir")
              puestos=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del bus\n"))
          puestos=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del bus\n"))
          continue
      print("Puede salir")
      valor1=puestos*costo1
      print(valor1)
      restol=valor1+vaitcos1-peaje1-gaso1
      print(restol)
      print( "Este fue el valor de los tiquetes", valor1, )
      while restol < sueledomes:
          print("Usted tuvo perdida")
          continue
          
      print("Usted tuvo ganancias")
      
      
    
    



    if opc ==2:
     print("Escogiste la ruta de 51 a 80km")
     puestos1=int(input("Cuantos pasajeros tienes \n"))
     while 50 <= puestos1:
          print("Usted no puede salir")
          while 10<=puestos1:
              print("Usted no puede salir")
              puestos1=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del bus\n"))
          puestos1=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del bus\n"))
          continue
     print("Puede salir")
     valor2=puestos1*costo2
     print(valor2)
     restol1=valor2+vaitcos1-peajes2-gasolina2
     print(restol1)
     print( "Este fue el valor de los tiquetes", valor2, "Estos fueron los gastos del recorrido", restol1)
     while restol1 < sueledomes:
         print("Usted tuvo perdidas")
         continue
     print("Usted tuvo ganancias")
     
     
    if opc==3:
        print("Escogiste la ruta de 81km a mas km")
        puestos2=int(input("Cuantos pasajeros tienes \n"))
        while 50 <= puestos2:
          print("Usted no puede salir")
          while 10<=puestos2:
              print("Usted no puede salir")
              puestos2=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del bus\n"))
          puestos2=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del bus\n"))
          continue
        print("Puede salir")
        valor3=puestos2*costo3
        print(valor3)
        restol2=valor3+viaticos2-peajes3-gasolina3
        print(restol2)
        print( "Este fue el valor de los tiquetes", valor3, "Estos fueron los gastos del recorrido", restol2)
        while restol2 < sueledomes:
            print("Usted tuvo perdidas")
            continue
        print("Usted tuvo ganancias")
    
    if opc==4:
        print("No compraste ningun tiquete, feliz dia, porceso terminado")    
      




if tp== 2:
    print("Escogiste la buseta")
    print("1. ruta de 1km a 50km 2. ruta de 51km a 80km 3. 81km a mas km  4. Salida del proceso")
    opc=int(input("Escoja del 1 al 4 \n"))

    if opc == 1:
        print("Escogiste la ruta de 81km a mas km")
        puestos3=int(input("Cuantos pasajeros tienes \n"))
        while 18 <= puestos3:
          print("Usted no puede salir")
          while 10<=puestos3:
              print("Usted no puede salir")
              puestos3=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del buseta\n"))
          puestos3=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del buseta\n"))
          continue
        print("Puede salir")
        valor4=puestos3*cost1
        print(valor4)
        restol3=valor4+vaitcos1-peaje1-gaso1
        print(restol3)
        print( "Este fue el valor de los tiquetes", valor4, "Estos fueron los gastos del recorrido", restol3)
        while restol3 < sueldobuse:
            print("Usted tuvo perdidas")
            continue
        print("Usted tuvo ganancias")
    
    if opc == 2:
        print("Escogiste la ruta de 81km a mas km")
        puestos4=int(input("Cuantos pasajeros tienes \n"))
        while 18<=puestos4:
          print("Usted no puede salir")
          while 10<=puestos4:
              print("Usted no puede salir")
              puestos4=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del buseta\n"))
          puestos4=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del buseta\n"))
          continue
        print("Puede salir")
        valor5=puestos4*cost2
        print(valor5)
        restol4=valor5+vaitcos1-peajes2-gaso2
        print(restol4)
        print( "Este fue el valor de los tiquetes", valor5, "Estos fueron los gastos del recorrido", restol4)
        while restol4 < sueldobuse:
            print("Usted tuvo perdidas")
            continue
        print("Usted tuvo ganancias")
    
    if opc== 3:
        print("Escogiste la ruta de 81km a mas km")
        puestos5=int(input("Cuantos pasajeros tienes \n"))
        while 18<= puestos5:
          print("Usted no puede salir")
          while 10<=puestos5:
              print("Usted no puede salir")
              puestos5=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del buseta\n"))
          puestos5=int(input("Ingrese igual o mas de 10 puestos o no pase del limite de puestos del buseta\n"))
          continue
        print("Puede salir")
        valor6=puestos5*cost3
        print(valor6)
        restol5=valor6+viaticos2-peajes3-gaso3
        print(restol5)
        print( "Este fue el valor de los tiquetes", valor6, "Estos fueron los gastos del recorrido", restol5)
        while restol5 < sueldobuse:
            print("Usted tuvo perdidas")
            continue
        print("Usted tuvo ganancias")
        
        
    if opc == 4:
        print("No compraste ningun tiquete, feliz dia, porceso terminado")    
      
            


if tp== 3:
    print("Salida del Proceso")