#Escribe un programa que genere una contrasena
#con 3 letras de tu nombre y 3 del aellido
def contrasena_2():
    nombre=raw_input("Introduce el nombre: ")
    apellido=raw_input("Introduce el apellido: ")
    print nombre[-3:]+apellido[-3:]


contrasena_2()
