print("THE GHOST")

edad = int(input("\nANTES DE COMENZAR INGRESE TU EDAD: "))

if edad <= 0:
    print("EDAD NO VALIDA INGRESE NUEVAMENTE SU EDAD")
elif edad >= 90:
    print("EDAD NO VALIDA INGRESE NUEVAMENTE SU EDAD")
elif edad < 18:
    print("LO SIENTO ESTE JUEGO ES PARA MAYORES DE EDAD")
else:

    print("\nESTE ES UN JUEGO DE SUPERVIVENCIA")
    print("CONFIA EN TU INSTINTO NADA ES LO QUE PARECE SER")

    print("\nAS DESPERTADO EN EL FONDO DE UN SOTANO DEBES ENCONTRAR LA MANERA DE SALIR ")

    valor1 = input("\nELIGE 1: Linterna 2: Telefono 3: Mapa: ").lower()

    if valor1 == "linterna" or valor1 == "1":
        print("\nILUMINAS UN PASILLO QUE AL FINAL TIENE 3 PUERTAS DEBES ELEGIR LA PUERTA CORRECTA PARA PODER AVANSAR")
        print("1: Puerta Negra")
        print("2: Puerta Roja")
        print("3: Puerta Azul")

    elif valor1 == "telefono" or valor1 == "2":
        print("\nEL TELEFONO MUESTRA UN MENSAJE")
        print("NO HAY SALIDA")
        print("LA PANTALLA SE APAGA ENTRAS EN DESESPERACION")
        print("GAME OVER")

    elif valor1 == "mapa" or valor1 == "3":
        print("\nEL MAPA TE MUESTRA LA RUTA Y TE DICE")
        print("QUE AL FINAL DEL PASILLO HAY 3 PUERTAS DEBES ELEIGIR LA CORRECTA")
        print("1: Puerta Negra")
        print("2: Puerta Roja")
        print("3: Puerta Azul")

    else:
        print("OPCION NO VALIDA")

    if valor1 in ["linterna", "1", "mapa", "3"]:

        puerta = input("\nQUE PUERTA ABRES 1: Puerta Negra 2: Puerta Roja 3: Puerta Azul: ").lower()

        if puerta == "1" or puerta == "negra":
            print("\nUNA MANO TE ARRASTRA HACIA LA OSCURIDAD")
            print("GAME OVER")

        elif puerta == "2" or puerta == "Puerta Roja" or puerta == "3" or puerta == "Puerta Azul":

            if puerta == "3" or puerta == "azul":
                print("\nLA PUERTA AZUL ESTA BLOQUEADA")
                otra = input("ELIGE 1: Puerta Negra 2: Puerta Roja ").lower()

                if otra == "1" or otra == "Puerta Negra":
                    print("\nALGO TE EMPUJA HACIA DENTRO")
                    print("GAME OVER")
                    exit()
                elif otra not in ["2", "Puerta Roja"]:
                    print("OPCION NO VALIDA")
                    exit()

            print("\nSUBES UNA ESCALERA HACIA UNA HABITACION OSCURA EN LA QUE APENAS LOGRAR VER")
            print("HAY UNA MESA UNA SILLA Y UNA PUERTA ")

            accion = input("ELIGE 1: Revisar la Mesa 2: Sentarte 3: Intentar Abrir la Puerta: ").lower()

            if accion == "1" or accion == "revisar la Mesa":
                print("\nAs encontrado una llave en la mesa")

                decision = input("ELIGE 1: Usar la llave 2: Guardar la llave : ").lower()

                if decision == "1" or decision == "Usar la llave":
                    print("\nLA PUERTA SE ABRE Y ENTRAS A AL SIGIENTE CUARTO VASIO CON UNA PUERTA APENAS VISIBLE AL FONDO")
                    print("TE ASERCAS A LA PUERTA VES QUE UNA PALABRA MUY RARA ")
                    print("ESA PALABRA ES DALISA")

                    respuesta = input("QUE CREES QUE SEA 1:Salida 2:Su Nombre 3: Una Distraccion: ").lower()

                    if respuesta == "1" or respuesta == "salida":
                        print("\nORDENAS LAS PALABRAS DE DALISA FORMADO UNA NUEVA PALABRA LA CUAL DICE SALIDA")
                        print("LA PUERTA SE ABRE CORRES Y CIERRAS LA PUERTA JUSTO A TIEMPO ANTES DE QUE EL ENTE TE ARRASTRARA DE NUEVO A DENTRO ")
                        print("HAS ESCAPADO")
                        print("YA CREO QUE SERIA TODO PROFE")

                    elif respuesta == "2" or respuesta == "su nombre":
                        print("\nPIENSAS QUE ES SU NOMBRE")
                        print("PIENSAS QUE SE ENCUENTRA DETRAS DE LA PUERTA Y TE ALEJAS")
                        print("NO ENCUENTRAS COMO SALIR ")
                        print("TERMINAS SIENDO ATRAPADO")
                        print("GAME OVER")

                    elif respuesta == "3" or respuesta == "Una Distraccion":
                        print("\nIGNORAS EL MENSAJE")
                        print("UNA SOMBRA TE BLOQUEA EL PASO")
                        print("GAME OVER")

                    else:
                        print("OPCION NO VALIDA")

                elif decision == "2" or decision == "guardar la llave":
                    print("\nEL TIEMPO PASA")
                    print("ALGO SE ACERCA Y ERES ATRAPADO")
                    print("GAME OVER")

                else:
                    print("OPCION NO VALIDA")

            elif accion == "2" or accion == "sentarte":
                print("\nLA SILLA SE ROMPE Y CAES AL SUELO")
                print("AS ECHO MUCHO RUIDO ALGO VIENE POR TI")
                print("NO AS LOGRADO SALIR A TIEMPO")
                print("GAME OVER")

            elif accion == "3" or accion == "Intentar Abrir la Puerta":
                print("\nLA PUERTA ESTA CERRADA INTENTAS BUSCAR COMO ABRIRLA EL TIEMPO PASA ")
                print("SE TE A ECHO MUY TARDE PARA ESCAPAR EL ENTE YA TE A ALCANSADO ")
                print("GAME OVER")

            else:
                print("OPCION NO VALIDA")

        else:
            print("OPCION NO VALIDA")  
