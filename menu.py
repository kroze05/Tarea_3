import fractions
import math
from collections import deque
import datetime
from fractions import Fraction
def EscribirCentrado(a):
    centrado=40-(len(a)//2)
    print("el espacio de centrado en este caso es:",centrado)
    esp= " "*centrado
    print(esp+a)

def es_multiplo(mu_1,mu_2):
    val=mu_1%mu_2
    if val == 0:
        print(f"{mu_1} es multiplo de {mu_2}")
    else:
        print(f"{mu_1} no es multiplo de {mu_2}")

def temperatura_media(tdias):
    for i in range(1,tdias+1):
        tem_max = int(input("indica la temperatura maxima (en grados celcius)"))
        tem_min = int(input("indica la temperatura minima (en grados celcius)"))
        temp_media=tem_max/tem_min
        print(f"la temperatura promedio del dia {i} es de {temp_media}")

def convertirespaciado (frase):
    fras_mod = ""
    for i in frase:
        fras_mod+= i+" "
    print(fras_mod)

def calcularMaxMin(valores):
    minimo = valores[0]
    maximo = valores[-1]
    print(f"de los valores ingresados, el valor minimo es: {minimo} y el maximo es: {maximo}")

def area_perimetro(radio):
    area = math.pi*(radio**2)
    perimetro = 2 * math.pi * radio
    print(f"el area del circulo con radio de {radio} es {area} y el perimetro {perimetro}")

def login():
    usuario = ("usuario1")
    contraseña = ("asdasd")
    error = 3
    while error > 0:
        user=input("ingrese su nombre de usuario\n")
        password=input("ingrese su contraseña\n")
        enter=input("presione enter para login\n")
        if enter == "":
            if user == usuario:
                if password == contraseña:
                    print(f"hola {user}, bienvenido")
                    break
                else:
                    error -= 1
                    print(f"usuario o contraseña incorrecta, le quedan {error} intentos")
                    continue
            else:
                error -= 1
                print(f"usuario o contraseña incorrecta, le quedan {error} intentos")
                continue
        else:
            print("unicamente aplaste el enter sin caracteres adicionales")
    else:
        print("ha excedido  los intentos permitidos, acceda nuevamente para continuar")

def factorial(val):
    factorial_total=1
    while val > 0:
        factorial_total*=val
        val-=1
    print(factorial_total)

def MCD(a,b):
    if a>=b:
        c=0
        cola = deque([a,b,c])
        cola[2] = cola[0]%cola[1]
        while cola[2] != 0:
            new =  cola[1]%cola[2]
            cola.append(new)
            cola.popleft()
        else:
            print("el Maximo comun divisor es:",cola[1])
    elif a<b:
        c=0
        cola = deque([b,a,c])
        cola[2] = cola[0]%cola[1]
        while cola[2] != 0:
            new =  cola[1]%cola[2]
            cola.append(new)
            cola.popleft()
        else:
            print("el Maximo comun divisor es:",cola[1])

def datestdtojd(stddate):
    fmt = '%Y-%m-%d'
    stddate = datetime.datetime.strptime(stddate,fmt)
    stddate = stddate.timetuple()
    jdate = stddate.tm_yday
    return jdate

while True:
    print("""
    1.Escribir centrado
    2.Numero multiplos
    3.Temperatura media
    4.Espaciado entre letras
    5.Calcula el máximo y el mínimo
    6.Calculo de Area y Perimetro de la circunferencia
    7.Login Usuario y Contraseña
    8.Hallar el factorial de un número
    9.Hallar el MCD
    10.Convertir Horas, Minutos, Segundos
    11.Calcular el dia juliano
    12.Menu de fracciones
    13.Salir
    """)
    menu=int(input("selecciona la opcion que deseas\n"))
    if menu == 1:
        a=input("ingresa un texto/frase que quieras centrar\n")
        EscribirCentrado(a)
    elif menu == 2:
        mu_1=int(input("ingresa un valor\n"))
        mu_2=int(input("ingresa un segundo valor\n"))
        es_multiplo(mu_1,mu_2)
    elif menu == 3:
        tdias = int(input("introduce el numero de dias que se medira la temperatura media\n"))
        
        temperatura_media(tdias)
    elif menu == 4:
        frase = input("coloca una frase\n")
        convertirespaciado(frase)
    elif menu == 5:
        valores = list(map(int,input("ingresa los valores deseados (separados por una coma)\n").split(",")))
        valores.sort()
        calcularMaxMin(valores)
    elif menu == 6:
        radio = float(input("ingrese el radio de su circunferencia\n"))
        area_perimetro(radio)
    elif menu == 7:
        login()
    elif menu == 8:
        val = int(input("coloca un número para calcular su factorial\n"))
        factorial(val)
    elif menu == 9:
        a=int(input("ingresa un numero\n"))
        b=int(input("ingresa otro numero\n"))
        MCD(a,b)
    elif menu == 10:
        def con_segH():
            seg=int(input("ingresa la cifra de segundos\n"))
            min=seg //60
            seg_final = seg % 60
            horas = min//60
            min %= 60
            print(f"{seg} segundos equivale a {horas} horas {min} minutos y {seg_final} segundos\n")
        
        def con_hSeg():
            horas = int(input("ingresa el valor en horas\n"))
            min = int(input("ingresa el valor en minutos\n"))
            seg = int(input("ingresa el valor en segundos\n"))
            seg_final = seg + (min*60) + (horas*3600)
            print(f"el equivalente de {horas} horas, {min} minutos y {seg} segundos en segundos es: {seg_final}")

        while True:
            print("""
                Convertir:
                1. Segundos a Horas, Minutos, Segundos
                2. Hora, Minutos, Segundos a Segundos
                3. Salir
                """)
            sel = int(input("selecciona la opcion deseada\n"))
            if sel == 1:
                con_segH()
            elif sel == 2:
                con_hSeg()
            elif sel ==3:
                break

    elif menu == 11:
        fecha=input("ingresa AA-MM-DD tal cual el formato\n")
        print(datestdtojd(fecha))
    elif menu ==12:
        print("""
            1.Sumar dos fracciones: 
            2.Restar dos fracciones: 
            3.Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
            4.Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
            5.Salir
            """)
        while True:
            num = int(input("escribe el numero de la opcion a realizar\n"))
            if num == 1:
                f1 = input("ingresa la primera fraccion (n/d)\n")
                f2 = input("ingresa la segunda fraccion a sumar (n/d)\n")
                fra_1 = Fraction(f1)
                fra_2 = Fraction(f2)
                suma = fra_1+fra_2
                print(f"el resultado de: {fra_1} + {fra_2} es: {suma}")
            elif num ==2:
                f1 = input("ingresa la primera fraccion (n/d)\n")
                f2 = input("ingresa la segunda fraccion a restar(n/d)\n")
                fra_1 = Fraction(f1)
                fra_2 = Fraction(f2)
                resta = fra_1-fra_2
                print(f"el resultado de: {fra_1} - {fra_2} es: {resta}")
            elif num ==3:
                f1 = input("ingresa la primera fraccion (n/d)\n")
                f2 = input("ingresa la segunda fraccion multiplicar (n/d)\n")
                fra_1 = Fraction(f1)
                fra_2 = Fraction(f2)
                suma = fra_1*fra_2
                print(f"el resultado de: {fra_1} * {fra_2} es: {suma}")
            elif num == 4:
                f1 = input("ingresa la primera fraccion (n/d)\n")
                f2 = input("ingresa la segunda fraccion a dividir (n/d)\n")
                fra_1 = Fraction(f1)
                fra_2 = Fraction(f2)
                suma = fra_1/fra_2
                print(f"el resultado de: {fra_1} / {fra_2} es: {suma}")
            elif num == 5:
                print("salio del menu de Fracciones")
                break
    elif menu == 13:
        print("El programa se ejecuto correctamente")
        break