
def valoresLetras(palabra):
    total = 0
    for valor in palabra:
        if valor == "a":  
            total += 1
        elif valor == "b":
            total += 2
        elif valor == "c":
            total += 3
        elif valor == "d":
            total += 4
        elif valor == "e":
            total += 5
        elif valor == "f":
            total += 6
        elif valor == "g":
            total += 7
        elif valor == "h":
            total += 8
        elif valor == "i":
            total += 9
        elif valor == "j":
            total += 10
        elif valor == "k":
            total += 11
        elif valor == "l":
            total += 12
        elif valor == "m":
            total += 13
        elif valor == "n":
            total += 14
        elif valor == "ñ":
            total += 15
        elif valor == "o":
            total += 16
        elif valor == "p":
            total += 17
        elif valor == "q":
            total += 18
        elif valor == "r":
            total += 19
        elif valor == "s":
            total += 20
        elif valor == "t":
            total += 21
        elif valor == "u":
            total += 22
        elif valor == "v":
            total += 23
        elif valor == "w":
            total += 24
        elif valor == "x":
            total += 25
        elif valor == "y":
            total += 26
        elif valor == "z":
            total += 27
        else:
            total += 0
    
    return total

def prediccionClima(tempInicial,probLluvia,dias):
    i=1
    contLluvia=0
    contNolluvia=0
    tempMenor=100
    tempMayor=0
    for i in range (dias):
        if tempInicial<tempMenor:
            tempMenor=tempInicial
        if tempInicial>tempMayor:
            tempMayor=tempInicial
        if probLluvia>=100:
            probLluvia=100
            tempInicial-=1
            print("El dia ",i+1," tiene una temperatura de: ",tempInicial,"° y una probabilidad de lluvia de: ",probLluvia,"%")
            print("El dia ",i+1," va a llover.")
            print("------------------------------------------------------------------------------------------------------")
            contLluvia+=1
        elif tempInicial>25 and probLluvia!=100:
            if i%2==0 or i%7==0:
                probLluvia-=0.2*probLluvia
                print("El dia ",i+1," tiene una temperatura de: ",tempInicial,"° y una probabilidad de lluvia de: ",probLluvia,"%")
                if probLluvia>70:
                    print("El dia ",i+1," va a llover.")
                    print("------------------------------------------------------------------------------------------------------")
                    contLluvia+=1
                else:
                    print("El dia ",i+1," NO va a llover. ")
                    print("------------------------------------------------------------------------------------------------------")
                    contNolluvia+=1
            else:
                probLluvia+=0.2*probLluvia
                print("El dia ",i+1," tiene una temperatura de: ",tempInicial,"° y una probabilidad de lluvia de: ",probLluvia,"%")
                if probLluvia>70:
                    print("El dia ",i+1," va a llover.")
                    print("------------------------------------------------------------------------------------------------------")
                    contLluvia+=1
                else:
                    print("El dia ",i+1," NO va a llover. ")
                    print("------------------------------------------------------------------------------------------------------")
                    contNolluvia+=1
        elif tempInicial<5 and probLluvia!=100:
            probLluvia-=0.2*probLluvia
            print("El dia ",i+1," tiene una temperatura de: ",tempInicial,"° y una probabilidad de lluvia de: ",probLluvia,"%")
            if probLluvia>70:
                print("El dia ",i+1," va a llover.")
                print("------------------------------------------------------------------------------------------------------")
                contLluvia+=1
            else:
                print("El dia ",i+1," NO va a llover. ")
                print("------------------------------------------------------------------------------------------------------")
                contNolluvia+=1
        else:
            print("El dia ",i+1," tiene una temperatura de: ",tempInicial,"° y una probabilidad de lluvia de: ",probLluvia,"%")
            if probLluvia>70:
                print("El dia ",i+1," va a llover.")
                print("------------------------------------------------------------------------------------------------------")
                contLluvia+=1
            else:
                print("El dia ",i+1," NO va a llover. ")
                print("------------------------------------------------------------------------------------------------------")
                contNolluvia+=1
        if i%2==0 or i%5==0:
            tempInicial-=0.2
        else:
            tempInicial+=0.2
    print("La mayor temperatura en el periodo de tiempo de ",dias," es de: ",tempMayor,"°")
    print("La menor temperatura en el periodo de tiempo de ",dias," es de: ",tempMenor,"°")
    print("Lloverá en ",contLluvia," dias.")
    print("No lloverá en ",contNolluvia," dias.")
 
def compararCaracteres(cadena1, cadena2):
    infiltrados=[]
    for i in range(len(cadena1)):
        if cadena1[i]!=cadena2[i]:
            infiltrados+=cadena2[i]
    return infiltrados      
        
        
    


print("MENÚ PRINCIPAL")
print("--------------")
print("Por favor digite una de las siguientes opciones: ")
print("1. Palabra de 100 puntos.")
print("2. Simulador de clima.")
print("3. Carácter infiltrado. ")
opcion=input()

match(opcion):

    case "1":
        total=0
        while total != 100:
            palabra=input("Ingrese una palabra: ")
            total=valoresLetras(palabra)
            print("La palabra tiene un valor de: ",total)
    case "2":
        ubicacion=input("Por favor ingrese el nombre del lugar: ")
        tempInicial=int(input("Por favor ingrese la temperatura inicial (°): "))
        probLluvia=int(input("Por favor ingrese la probabilidad de lluvia (%): "))
        dias=int(input("Por favor ingrese el número de dias de la predicción : "))
        print("NOTA: Se debe tener en cuenta que para detenerminar si un dia llueve,")
        print("      la probabilidad de lluvia debe ser mayor a 70%.")
        print("---------------------------------------------------------------------")
        print("                          ",ubicacion)
        prediccionClima(tempInicial,probLluvia,dias)
    case "3":
        cadena1=input("Por favor ingrese la cadena 1: ")
        cadena2=input("Por favor ingrese la cadena 2: ")
        print("Los caracteres infiltrados son: ",compararCaracteres(cadena1,cadena2))
            
            