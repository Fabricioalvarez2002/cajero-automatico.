SALDO=10000
CONTRASEÑA=1313
while True:
    U=input ("ESCRIBA SU USUARIO")
    if U==("CAJERO"):
        while True:
            C=int (input ("ESCRIBA SU CLAVE"))
            if C==CONTRASEÑA:
                print ("MENU")
                print ("1: VER SALDO")
                print ("2: RETIRAR")
                print ("3: SALIR")
                while True:
                    o=int (input("SELECCIONA UNA OPCION"))
                    if o==1:
                        print ("EL SALDO DE SU CUENTA ES:"+str(SALDO))
                        break;
                    elif o==2:
                        print ("MENU")
                        print ("1: s/20")
                        print ("2: s/50")
                        print ("3: s/100")
                        print ("4: s/150")
                        print ("5: s/500")
                        R=int (input("SELECCIONE UN MONTO"))
                        if R==1:
                            SALDO=SALDO-20
                            break;
                        elif R==2:
                            SALDO=SALDO-50
                            break;
                        elif R==3:
                            SALDO=SALDO-100
                            break;
                        elif R==4:
                            SALDO=SALDO-150
                            break;
                        elif R==5:
                            SALDO=SALDO-500
                            break;
                        else:
                            print("OPCION INCORRECTA")
                            break;
                    elif o==3:
                        break;
            else:
                print("CONTRASEÑA INCORRECTA")
    else:
        print("USUARIO INCORRECTO")

                                        

                        
                              

                        

