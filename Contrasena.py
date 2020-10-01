#Escribe un programa que genere contrasena
def contrasena():
    nombre=raw_input("Introduce el nombre: ")
    apellido =raw_input("Introduce el apellido: ")
    print nombre," ", apellido, "eres el impostor?"
    print "Tu lindo nombre emppieza por la ",3*nombre+2*apellido

contrasena()
