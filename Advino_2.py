# -*- coding: cp1252 -*-
import random

def adivino_2():
    maxn=100
    numero=random.randint(1, maxn)
    intento = input("Intentalo mi rey: ")
    while intento!=numero:
        if intento>numero:
            print "Este no era el numero, demasiado grande"
        if intento<numero:
            print "Este no era el numero, demasiado pequeño"
        intento=input("Intentalo: ")
    print "Mission passed + respect"





adivino_2()
