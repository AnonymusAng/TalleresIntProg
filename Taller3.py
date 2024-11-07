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

def numeroAmstrong(numero):
    potencia=len(numero)
    print("",potencia)
    
    
        
    
print("                                       MENÚ PRINCIPAL                                                      ")
print("-----------------------------------------------------------------------------------------------------------")
print("Por favor digite el número de opción del siguiente menú:")
print("1. Area de un poligono.")
print("2. Invertir cadenas. ")
print("3. Eliminar caracteres. ")
print("4. Número de Amstrong. ")
print("5. Conversor de tiempo. ")
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
    case 3:
        print("wait")
    case 4:
        numero=int(input("Ingrese el número para verrificar si es de Amstrong: "))
        print("",numeroAmstrong(numero))