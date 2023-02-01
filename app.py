# Vamos a ver como se maneja la lectura y escritura de archivos en python, se utiliza una libreria ya integrada con python
# de modo q no es neceario instalar nada adicional para la lectura y escritura

# Utilizaremos el archivo sample.log q ya contiene informacion
contenido = None    #   none es igual a null
valor = None
#   El parametro r despues del nombre del archivo quiere decir q el acceso al archivo es de solo lectura
with open("sample.log", 'r') as readingfile:
    #   readingfile es el objeto q ya hace referencia al archivo abierto mientras este dentro de la etiqueta with con un tabulador
    #   Si esta al nivel de la etiqueta with, dejare de estar abierto y se cerrar y ya no habra acceso a al mismo
    contenido = readingfile.readlines()
    # voy a leer el archivo linea por linea
    for line in contenido:
        line = line.replace('\n', '')
        print(f"line => {line}")
    #   Al asignar el valor del contenido del archivo a una variable aun habiendose cerrado el archivo ya no se perdera la informacion
    #    El contenido es regresado como una lista de lineas o un arreglo de lineas
# print(f"contenido => {contenido}")
#   Ahora voy a extraer una linea espeficica del archivo y la voy a imprimir para despues guardarla en un archivo nuevo
    lineas = list(elemento for elemento in contenido if "31" in elemento)
    # en caso de haber mas de una coincidencia, me regresara todos los q coincidan en un arreglo o lista
    print(f"lineas => {lineas}")
    #    Aqui vlaidaremos q no venga vacio el arreglo y tomamos la posicion 1 del arreglo
    if len(lineas) > 0:
        valor = lineas[0]
        print(f"valor => {valor}")

# Ahora, una vez q se obtiene el valor, debemos verificar q sea diferente de nulo y procedemos q escribir su valor en el archivo
if valor != None:
    with open("salida.log", 'w') as escribesalida:
        escribesalida.write(valor)
