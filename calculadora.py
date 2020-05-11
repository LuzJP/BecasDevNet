

def suma ():
    resultado = float(op1)+float(op2)
    return resultado

def resta ():
    resultado = float(op1)-float(op2)
    return resultado

def multiplicacion ():
    resultado = float(op1)*float(op2)
    return resultado

def division ():
    if (op2 != "0"):
        resultado = float(op1)/float(op2)
        return resultado
    else : 
        print ("Operacion no válida")

def exponencial ():
    resultado = float(op1)**float(op2)
    return resultado

op1 = ""
while (op1 != "q"):
    print("""

        CALCULADORA
        Las operaciones disponibles son las siguientes:

        Suma (+)
        Resta (-)
        Multiplicacion(*)
        Divison(/)
        Exponenciales (^)
        Raiz cuadrada (por favor, siga el formato: operador = ^ y segundo operando = 0.5)

        Pulse q para salir de la aplicacion
    """)
    try:
        op1 = input("Introduzca el primer operando: ")
        if (op1 == "q"):
            break
        oper = input ("Introduzca el operador: ")
        op2 = input ("Introduzca el segundo operando: ")

        float(op1)
        float(op2)
    except:
        print("Operando incorrecto")
        continue
        
    if (oper== str("+")) :
        res = suma()
    elif (oper== str("-")) :
        res = resta()
    elif (oper== str("*")) :
        res = multiplicacion()
    elif (oper== str("/")) :
        res = division ()
    elif (oper== str("^")) : 
        res = exponencial()
    else :
        print("Operacion no soportada/Operador no válido")

    if res != None : 
        print ("El resultado de la operacion " + op1 + oper + op2 + " es " + str(res))





