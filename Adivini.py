# -*- coding: cp1252 -*-
def adivino():
    numero = input("Dime un numero del 1 al 10: ")
    intento = input("Intentalo mi rey: ")
    while intento!=numero:
        if intento>numero:
            print "Este no era el numero, demasiado grande"
        if intento<numero:
            print "Este no era el numero, demasiado pequeño"
        intento=input("Intentalo: ")
    print "Mission passed + respect"





adivino()
