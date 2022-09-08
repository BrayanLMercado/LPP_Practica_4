'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 4 : Estructuras De Control Anidadas
Archivo De Funciones
Ejercicio 1: Elabora un programa que contenga un menú con 4 opciones, cada opción del menú será una función
             diferente. El programa terminara cuando el usuario seleccione la opción 4.
Fecha: 15 De Septiembre De 2022
'''

def menu():
    print("              Ménu       ")
    print("1) Imprimir Tabla De Caracteres")
    print("2) Imprimir Tablas Numéricas")
    print("3) Imprimir Piramide De Números")
    print("4) Salir")

def tablasChar():
    ren=int(input("Cantidad De Renglones: "))
    col=int(input("Cantidad De Columnas: "))
    carac=str(input("Caracter A Imprimir: "))
    for x in range (ren):
        for t in range(col):
            print(carac,end=" ")
        print()

def tablasMult():
    ren=int(input("Cantidad De Renglones: "))
    col=int(input("Cantidad De Columnas: "))
    for x in range(1,ren+1):
        for t in range(1,col+1):
            print(t ,"*", x ,"=", x*t,end="     ")
        print()

def piramide():
    pisos=int(input("Captura El Número De Pisos De La Piramide: "))
    for x in range(1,pisos+1):
        for t in range(1,x+1):
            print(x,end=" ")
        print()