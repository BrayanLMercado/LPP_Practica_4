'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 4 : Estructuras De Control Anidadas
Ejercicio 1: Elabora un programa que contenga un menú con 4 opciones, cada opción del menú será una función
             diferente. El programa terminara cuando el usuario seleccione la opción 4.
Fecha: 15 De Septiembre De 2022
'''

from funciones_menu_tablas_piramide import * 

opcCont=0
while opcCont!=4:
    menu()
    opc=int(input("Selecciona Una Opción: "))
    while opc<1 or opc>4:
        print("Elige Una Opción Del Ménu")
        opc=int(input("Selecciona Una Opción: "))
    if opc==1:
        tablasChar()
    elif opc==2:
        tablasMult()
    elif opc==3:
        piramide()
    elif opc==4:
        opcCont=4
        break
    opcCont=int(input("Desea Continuar?, Presiona 4 Para Salir: "))
    print()