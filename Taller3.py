def calcularAreaCuadrado(lado):
    return lado*lado

def calcularAreaRectangulo(base,altura):
    return base*altura
    
def calcularAreaTriangulo(base,altura):
    return(base*altura)/2

def calcularArea():
         
    print("Por favor digite el número de opción del siguiente menú:")
    print("1. Area de Cuadrado.")
    print("2. Area de Rectangulo. ")
    print("3. Area de Triangulo. ")
    print("--------------------------------------------------------")
    opcionMenu=input()
    match opcionMenu:
        case "1":
            lado=float(input("Ingrese el valor de un lado del cuadrado: "))
            print("El valor del area del cuadrado es de: ",calcularAreaCuadrado(lado))
            
        case "2":
            base=float(input("Ingrese el valor de la base del rectangulo: "))
            altura=float(input("Ingrese el valor de la altura del rectangulo: "))
            print("El valor del area del cuadrado es de: ",calcularAreaRectangulo(base,altura))
        
        case "3":
            base=float(input("Ingrese el valor de la base del triangulo: "))
            altura=float(input("Ingrese el valor de la altura del triangulo: "))
            print("El valor del area del cuadrado es de: ",calcularAreaTriangulo(base,altura))
    

def invertirCadena(cadena):
    cadenaInvertida = ""
    for i in range(len(cadena)-1,-1,-1):
        cadenaInvertida += cadena[i]
    return cadenaInvertida

def eliminarCaracteres(str1, str2):
    out1 = ""
    out2 = ""
    
    for char in str1:
        if char not in str2:
            out1 += char
    
    for char in str2:
        if char not in str1:
            out2 += char
    
    print("out1:", out1)
    print("out2:", out2)

def numeroAmstrong(numero):
    digitos=str(numero)
    potencia=len(digitos)
    numeroFinal=0
    for digito in digitos:
        numeroFinal += pow(int(digito),potencia)
    if numeroFinal==numero:
        print("El ",numero,"es un número de Amstrong.")
    else:
        print("El ",numero,"NO es un número de Amstrong.")

def tiempoMilisegundos():
    dias=int(input("Ingrese la cantidad de dias: "))
    horas=int(input("Ingrese la cantidad de horas: "))
    minutos=int(input("Ingrese la cantidad de minutos: "))
    segundos=int(input("Ingrese la cantidad de segundos: "))
    conversion=(dias*86400000+horas*3600000+minutos*60000+segundos*1000)
    print("La cantidad de tiempo ingresada en Milisegundos es: ",conversion)

def figura():
    print("Por favor digite el número de opción del siguiente menú:")
    print("1. Figura 2D Cuadrado.")
    print("2. Figura 2D Triangulo. ")
    print("--------------------------------------------------------")
    opcionMenu=input()
    match opcionMenu:
        case "1":
            lado=int(input("Ingrese el valor de un lado del cuadrado: "))
            for i in range(lado):
                print("*"*lado)
            
        case "2":
            altura=int(input("Ingrese el valor de la altura del triangulo (equilatero): "))
            for i in range(altura):
                print(" " * (altura-i-1) + "* " * (i+1))
        
def marcoPalabras():
    frase = input("Ingresa una frase: ")
    palabras = []  
    palabra = ""

    for char in frase:
        if char == " ":
            if palabra != "":
                palabras += [palabra]  
                palabra = ""  
        else:
            palabra += char 

    if palabra != "":
        palabras += [palabra]

    tamanoMaximaPalabra = 0
    for palabra in palabras:
        if len(palabra) > tamanoMaximaPalabra:
            tamanoMaximaPalabra = len(palabra)

    borde = "*" * (tamanoMaximaPalabra + 4)
    print(borde)
    for palabra in palabras:
        print("* " + palabra + " " * (tamanoMaximaPalabra - len(palabra)) + " *")

    print(borde)

def valoresURL(url):
    valores = ""
    for valor in url:
        if '0' <= valor <= '9':  
            valores += (" "+ valor)  
    
    return valores

print("                                       MENÚ PRINCIPAL                                                      ")
print("-----------------------------------------------------------------------------------------------------------")
print("Por favor digite el número de opción del siguiente menú:")
print("1. Area de un poligono.")
print("2. Invertir cadenas. ")
print("3. Eliminar caracteres. ")
print("4. Número de Amstrong. ")
print("5. Conversor de tiempo a milisegundos. ")
print("6. Cuadrado y triangulo en 2D. ")
print("7. Marco de palabras. ")
print("8. Obtener parametros de URL. ")
print("------------------------------------------------------------------------------------------------------------")

opcionMenu=input()
    
match opcionMenu:
    case "1":
        calcularArea()
    case "2":
        cadena=input("Ingrese la cadena a invertir: ")
        print("La cadena invertida es: ",invertirCadena(cadena))
    case "3":
        str1=input("Ingrese la primera cadena: ")
        str2=input("Ingrese la segunda cadena: ")
        print(" ",eliminarCaracteres(str1,str2))
    case "4":
        numero=int(input("Ingrese el número para verrificar si es de Amstrong: "))
        print("",numeroAmstrong(numero))
    case "5":
        tiempoMilisegundos()
    case "6":
        figura()
    case "7":
        marcoPalabras()
    case "8":
        url=input("Ingresa el URL: ")
        print("Los parametros del URL son: ",valoresURL(url))
    
        