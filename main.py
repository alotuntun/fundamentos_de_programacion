import datetime
cuentas = [("admin","admin","Admin"),("user01","user01","Trabajador"),("user02","user02","Trabajador"),("user03","user03","Trabajador")]
lista_anuncios = []
lista_reclamos = []
lista_contratos = []
#Función logeo
def logeo():
    usuario = input("Colocar usuario:")
    password = input("Colocar contraseña:")
    encontro = False
    for cuenta in cuentas:
        if (usuario == cuenta[0]) & (password == cuenta[1]) :
            encontro = True 
            if (cuenta[2] == "Admin"):
                interfazAdmin()
            elif (cuenta[2] == "Trabajador"):
                interfazTrabajador()
    
    if encontro == False:
        print("Incorrecto")
        logeo()

         
    #Funcion Interfaz del Admin
    def interfazAdmin():
        print("Ingreso correctamente - Admin")

        opcion1 = input("Elige: \n1.Crear Anuncio\n2.Ver Reclamos\n3.Crear cuenta de trabajador\n4.Emitir contratos\n5.Cerrar sesión\n")

        if opcion1 == "1":
            print("Elegiste la opción 1")
            crearAnunciosAdmin()
            
        elif opcion1 == "2":
            print("Elegiste la opción 2")
            verReclamosAdmin()
            def retroceder():
                opcion1=input("1.Retroceder\n")
                if opcion1 == "1":
                    print("Has elegido retroceder")
                    interfazAdmin()
                else:
                    print("Opción No Valida !")
                    retroceder()
            retroceder()
        elif opcion1 == "3":
            print("Elegiste la opción 3")
            def Crearcuenta():
                crear_user= input("Ingrese el usuario:")
                crear_password= input("Ingrese la contraseña:")
                confirmar_password1= input("Confirme la constraseña:")
                cargo = input("Ingrese el cargo que desempeñara en la compañia:")
                if crear_password == confirmar_password1 :
                    print("¡Cuenta creada!")
                    cuentas.append([crear_user,crear_password,cargo])
                    opcion1=input("Elige: \n1.Crear otra cuenta\n2.Retroceder\n")
                    if opcion1 == "1":
                        Crearcuenta()
                    elif opcion1 == "2":
                        print("Has elegido retroceder")
                        interfazAdmin()
                else:
                    print("No coincidieron las credenciales ❌")
                    Crearcuenta()
            Crearcuenta()
        elif opcion1 == "4":
            print("Elegiste la opción 'Emitir contratos'")
            def emitir_contrato():
                print("Elige trabajador:")
                #FOR 1 : PARA MOSTRAR LAS OPCIONES (INFORMACION GANACIA: ORDEN QUE ENCUENTRA A LOS TRABAJADORES / OBJETIVO: PARA QUE EL ADMIN ELIJA AL USUARIO)
                z=1
                for elemento in cuentas:
                    if elemento[2] == "Trabajador":
                        print(f"{z}. {elemento[0]}")
                        z+=1
                opcion_contrato = int(input())

                
                #FOR 2 : PARA MOSTRAR LAS OPCIONES (INFORMACION GANACIA: NOMBRE DEL TRABAJADOR / OBJETIVO: CONSEGUIR EL NOMBRE SIN ESCRIBIR NADA)
                x=1
                nombre = "default"
                for elemento in cuentas:
                    if elemento[2] == "Trabajador":
                        if x == opcion_contrato:
                            nombre = elemento[0]
                        x += 1
                fecha_contrato = str(datetime.datetime.now())

                
                
                def contratos():
                    
                    description_option = input("Elige el tipo de contrato: \n1.Contrato Area Lacteos\n2.Contrato Area Frutas y Verduras\n3.Contrato Caja\n")
                    if description_option == "1":
                        contrato = "Contrato para el área de lácteos: El trabajador realizará la reposición, control de fechas y orden de productos lácteos en el turno asignado."
                        return contrato
                    elif description_option == "2":
                        contrato = "Contrato para el área de frutas y verduras: El trabajador apoyará en la selección, limpieza y exhibición de frutas y verduras según el horario asignado."
                        return contrato
                    elif description_option == "3":
                        contrato = "Contrato para el área de cajas: El trabajador se encargará del cobro de productos, atención al cliente y manejo de caja registradora."
                        return contrato
                    else:
                        print("Opcion Invalida !")
                        contratos()

                    
                contrato = contratos()

                firmo = False

                lista_contratos.append([nombre,fecha_contrato,contrato,firmo])
                        
                print(f"Contrato creado con éxito !. \nVisualización:\nTrabajador: {lista_contratos[-1][0]}\nFecha del Contrato: {lista_contratos[-1][1]}\nDescripcion: {lista_contratos[-1][2]}\nEstado (V: firmado /F: no firmado): {lista_contratos[-1][3]}")
            emitir_contrato()
            def option_contrato():
                opcion1=input("Elige: \n1.Crear Otro Contrato\n2.Retroceder\n")
                if opcion1 == "1":
                    print("Elegiste la opcion 1")
                    emitir_contrato()
                    option_contrato()
                elif opcion1 == "2":
                    interfazAdmin()
                else:
                    print("Opción No Valida !")
                    option_contrato()
            option_contrato()
            
            
        elif opcion1 == "5":
            print("Elegiste la opción 5")
            logeo()  
        else:
            print("Opción No Valida !")
            interfazAdmin()

    #Funcion Interfaz Trabajador
    def interfazTrabajador():
        print("Ingreso correctamente - Trabajador")
        opcion1 = input("Elige: \n1.Crear Reclamo\n2.Ver Anuncio\n3.Firmar Contratos\n4.Ver beneficios como trabajador\n5.Cerrar sesión\n")
        if opcion1 == "1":
            print("Elegiste la opción 1")
            def crearReclamosTrabajador():
                nombre_reclamo = input("Ingrese el título del reclamo:")
                fecha_reclamo = str(datetime.datetime.now())
                descripción_reclamo = input("Digite el mensaje que quiera transmitir en el reclamo:")
                lista_reclamos.append([nombre_reclamo, fecha_reclamo, descripción_reclamo])
                opcion1=input("Elige: \n1.Crear Otro Reclamo\n2.Retroceder\n")
                if opcion1 == "1":
                    print("Elegiste la opcion 1")
                    crearReclamosTrabajador()
            
                elif opcion1 == "2":
                    interfazTrabajador()
            crearReclamosTrabajador()        
        elif opcion1 == "2":
            print("Elegiste la opción 2")
            x=1
            for elemento in lista_anuncios:
                print("________________________________________________")
                print(f"Anuncio #{x}")
                print(".................................................")
                print("Título: "+ elemento[0])
                print("Fecha: "+ elemento[1])
                print("Descripción: "+ elemento[2])
                print("________________________________________________")
                x+=1
            opcion1=input("1.Retroceder\n")
            if opcion1 == "1":
                print("Has elegido retroceder")
                interfazTrabajador()
        elif opcion1 == "3":
            print("Elegiste la opción 3")
            def firmar_contrato():
                z=1
                for elemento in lista_contratos:                   
                    if elemento[0] == usuario:
                        print(f"Contrato #{z}:\nNombre:{elemento[0]}\nFecha:{elemento[1]}\nDescripcion:{elemento[2]}\nEstado:{elemento[3]}\n") 
                    z+=1
                numero_contrato = int(input())

                a=0
                encontro_contrato = False
                for elemento in lista_contratos:
                    if elemento[0] == usuario:
                        if a == numero_contrato:
                            elemento[3] = True
                            encontro_contrato = True
                        a+=1

                if encontro_contrato == False:
                    print("No se encontro el contrato")
                    firmar_contrato()
            
            firmar_contrato()
            def opciones():
                opcion = int(input("Elige: \n1)Firmar otro contrato\n2)Retroceder\n"))
                if opcion == 1:
                    firmar_contrato()
                elif opcion == 2:
                    interfazTrabajador() 
                else:
                    print("Opción No Valida !")
                    opciones()

            opciones()


            

        elif opcion1 == "4":
            print("Elegiste la opción 4")
            
            def beneficios():
                opcion_beneficios = input("1.Descuento adicional del 5% en PlazaVea\n2.Recompensas en Agora Club\n3.Descuentos en tiendas del grupo Intercorp\n4.Bonos y utilidades\n5.Capacitación y desarrollo profesional\n")
                if opcion_beneficios == "1":
                    print("Al pagar con Agora Pay, puedes obtener un 5% de descuento adicional en productos seleccionados en PlazaVea.\nEste beneficio aplica en categorías como alimentos, cuidado personal y limpieza")
                elif opcion_beneficios =="2":
                    print("Al realizar compras en PlazaVea con tu tarjeta oh!pay o Agora Pay, acumulas recompensas que se reflejan en tu cuenta Agora Club.\nEstas recompensas pueden utilizarse para futuras compras en tiendas afiliadas como PlazaVea, Inkafarma, Promart y Oechsle.")
                elif opcion_beneficios =="3":
                    print("Los empleados de PlazaVea pueden acceder a descuentos en otras tiendas del grupo Intercorp, como Mass, Makro, Inkafarma, Mifarma, Promart, Oechsle y Vivanda.\nEstos descuentos varían según la tienda y la promoción vigente.")
                elif opcion_beneficios =="4":
                    print("Los trabajadores de PlazaVea pueden recibir bonos por puntualidad y productividad, así como utilidades anuales, lo que representa un beneficio económico adicional.")
                elif opcion_beneficios =="5":
                    print("PlazaVea ofrece programas de capacitación y desarrollo profesional para sus empleados, brindándoles oportunidades de crecimiento dentro de la empresa.")
            beneficios()
            
            def opciones_beneficio():
                opcion1=input("Elige: \n1.Ver otro beneficio\n2.Retroceder\n")
            
                if opcion1 == "1":
                    beneficios()
                    opciones_beneficio()
                elif opcion1 == "2":
                    print("Has elegido retroceder")
                    interfazTrabajador()
                else:
                    print("Opción No Valida !")
                    opciones_beneficio()  

            opciones_beneficio()
        elif opcion1 == "5":
            print("Elegiste la opción 5")
            logeo()        
    #Funcion Crear anuncios         
    def crearAnunciosAdmin():
        nombre_anuncio = input("Ingrese el título del anuncio:")
        fecha_anuncio = str(datetime.datetime.now())
        descripción_anuncio = input("Digite el mensaje que quiera transmitir en el anuncio:")
        lista_anuncios.append([nombre_anuncio, fecha_anuncio, descripción_anuncio])

        def opciones_crearanuncio():
            opcion1=input("Elige: \n1.Crear Otro Anuncio\n2.Retroceder\n")
            if opcion1 == "1":
                print("Elegiste la opcion 1")
                crearAnunciosAdmin()   
            elif opcion1 == "2":
                interfazAdmin()
            else:
                print("Opción No Valida !")
                opciones_crearanuncio()

        opciones_crearanuncio()

    #VerReclamos:
    def verReclamosAdmin():
            print("A continuación se mostrarán todos los reclamos:") 
            y=1
            for e in lista_reclamos:
                print("________________________________________________")
                print(f"Reclamo #{y}")
                print(".................................................")
                print("Título: "+ e[0])
                print("Fecha: "+ e[1])
                print("Descripción: "+ e[2])
                print("________________________________________________")
                y+=1
logeo()

