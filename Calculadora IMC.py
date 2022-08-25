# Este programa calcula el Índice de masa corporal de una persona y arroja una leyenda dependiendo los datos de la persona.

# En nombre y apellidos, hay que validar que sean solo letras.



nombre = str(input("Escribe tu nombre: "))
# Bucle While para no dejar una variable vacia.
while nombre == "":
    nombre = str(input("No escribiste nada, por favor Escribe tu nombre: "))


        # if not nombre:
        #     print("No escribiste")
#     else:
#         print(nombre)
# print ("ok")


# Capellido_paterno = input("Escribe tu apellido paterno: ")

# apellido_materno = input("Escribe tu apellido materno: ")

# edad = int(input("Teclea tu edad: "))

# peso = float(input("Teclea tu peso en Kilos: "))

# estatura = float(input("Teclea tu estatura en metros: "))

# imc = peso / (estatura ** 2)


# Impresión de datos usando el metodo "upper"
print("Nombre: ", nombre.upper())
# print(imc)



# cadena = "1"
# # Comprobar con la forma idiomática
# if not cadena:
# 	print("La cadena está vacía")
# else:
# 	print("La cadena NO está vacía")

# # O contar sus caracteres
# if len(cadena) is 0:
# 	print("La cadena está vacía")
# else:
# 	print("La cadena NO está vacía")

# # Lo contrario de hace un momento:
# if cadena:
# 	print("Ok la cadena no está vacía")
# else:
# 	print("La cadena está vacía")