# UCamp
## Fundamentos de Python
### Módulo 1
#### Proyecto (Calculadora de IMC)
![](https://www.gob.mx/cms/uploads/article/main_image/74044/09_11_18_blog_indice_de_masa_corporal_CM-01.jpg)

###### Se usó el ciclo  `<while>` para no permitir que el programa avanzara cuando un dato haya quedado vacio en las variables `<nombre>`, `<apellido_Pat>` y `<apellido_Mat>`

#### Ejemplo.
	nombre = str(input("Escribe tu nombre: "))
	# Bucle While para no dejar una variable vacia.
	while nombre == "":
	nombre = str(input("No escribiste nada, por favor Escribe tu nombre: "))

###### Y en la parte de las variables `<edad>`, `<peso>` y `<estatura>` utilicé `<while True>` para hacer un ciclo infinito mientras se validan los datos, como también `<try>`y `<except>` con `<ValueError>` para validar que se escriba un número y que no permita que el valor quede vacio.

###### Como también utilicé las sentencias `<if>` para validar que sea un número positivo.

###### Y las instrucciones `<continue>` y `<break>` las utilicé para controlar el bucle de `<while True>`

#### Ejemplo.
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
