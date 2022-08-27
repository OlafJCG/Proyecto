"""
            Este programa calcula el Índice de masa corporal de 
            una persona y arroja una leyenda dependiendo los datos de la persona.
"""

# NOMBRE
nombre = str(input("Escribe tu nombre: "))
# Bucle While para no dejar una variable vacia.
while nombre == "":
    nombre = str(input("No escribiste nada, por favor Escribe tu nombre: "))

# APELLIDO PATERNO
apellido_Pat = str(input("Escribe tu Apellido Paterno: "))
# Bucle While para no dejar una variable vacia.
while apellido_Pat == "":
    apellido_Pat = str(input("No escribiste nada, por favor Escribe tu Apellido Paterno: "))

# APELLIDO MATERNO
apellido_Mat = str(input("Escribe tu Apellido Materno: "))
# Bucle While para no dejar una variable vacia.
while apellido_Mat == "":
    apellido_Mat = str(input("No escribiste nada, por favor Escribe tu Apellido Materno: "))

# EDAD
#  "While True" es para especificar un bucle infinito y para romperlo utilicé "continue" y "break" para romper el bucle
while True:
    # "try" y "except" se utilizan para anticipar errores y en este caso lo usaré para anticipar un dato que no sea un número (una letra)
    try:
        edad = int(input("Escribe tu edad: "))   
    except (ValueError):
        print("Escribiste una letra o algún valor que no es valido")
        continue

    if edad < 0:
        print("Escribiste un valor negativo")
        continue
    else:
        break

# PESO
#  "While True" es para especificar un bucle infinito y para romperlo utilicé "continue" y "break" para romper el bucle
while True:
    # "try" y "except" se utilizan para anticipar errores y en este caso lo usaré para anticipar un dato que no sea un número (una letra)
    try:
        peso = float(input("Escribe tu peso: "))     
    except (ValueError):
        print("Escribiste una letra o algún valor que no es valido")
        continue

    if peso < 0:
        print("Escribiste un valor negativo")
        continue
    else:
        break

# ESTATURA
#  "While True" es para especificar un bucle infinito y para romperlo utilicé "continue" y "break" para romper el bucle
while True:
    # "try" y "except" se utilizan para anticipar errores y en este caso lo usaré para anticipar un dato que no sea un número (una letra)
    try:
        estatura = float(input("Escribe tu estatura en numero decimal, por ejemplo 1.98m \n"))     
    except (ValueError):
        print("Escribiste una letra o algún valor que no es valido")
        continue

    if estatura < 0:
        print("Escribiste un valor negativo")
        continue
    else:
        break

imc = peso / (estatura ** 2)

if imc < 18.9:
    resultado = "Peso Bajo"
elif (imc >18.91) and (imc < 24.99):
    resultado = "Peso Normal"
elif (imc > 25.00) and (imc < 29.99):
    resultado = "Sobrepeso"
elif (imc > 30.00) and (imc < 34.99):
    resultado =  "Obesidad Leve"
elif (imc > 35.00) and (imc < 39.99):
    resultado = "Obesidad media"
elif (imc > 40):
    resultado = "Obesidad Mórbida"
     
# Impresión de datos usando el metodo "upper"
print("Hola ", nombre.upper(), " ", apellido_Pat.upper(), " ", apellido_Mat.upper(),"\n")
print("Tu Índice de Masa Corporal es de: ", round(imc, 2))
print("Por lo tanto tienes: ", '\033[1m' + resultado + '\033[0m')


