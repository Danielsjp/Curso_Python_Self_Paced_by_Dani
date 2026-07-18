numero = 10 # Creamos un objeto de tipo entero (int) y lo asignamos a la variable numero
#los objetos de tipo entero tienen métodos que nos permiten manipularlos, por ejemplo:
cadena = str(numero)
print(cadena)  # Imprime: '10' que es una cadena de texto
#el resultado es el mismo que si hicieramos...
numero = "10"
numero = '10'
#las comillas simples y dobles son equivalentes para definir cadenas de texto en Python.
#todos los objetos de tipo string tienen métodos que nos permiten manipularlos, por ejemplo:
cadena = "Hola Mundo"
cadena_mayusculas = cadena.upper()  # Convierte la cadena a mayúsculas
print(cadena_mayusculas)  # Imprime: 'HOLA MUNDO'
cadena_minusculas = cadena.lower()  # Convierte la cadena a minúsculas
print(cadena_minusculas)  # Imprime: 'hola mundo'
print(cadena_mayusculas.islower())  # Imprime: False
print(cadena_minusculas.islower())  # Imprime: True
#la forma de llamar a un método es: nombre_del_objeto.nombre_del_metodo()
#los pararentesis son necesarios aunque el método no reciba argumentos.
#ya que hay meteodos que reciben argumentos, por ejemplo:
cadena = "Hola Mundo"
cadena_con_sustitucion = cadena.replace("Mundo", "Python")
print(cadena_con_sustitucion)  # Imprime: 'Hola Python'
#otro ejemplo de método que recibe argumentos es el método count(), que cuenta cuántas veces aparece un substring en la cadena:
cantidad_mundos = cadena.count("Mundo")
print(cantidad_mundos)  # Imprime: 1
#podriamos ahorranos una línea de código y hacer todo en una sola línea:
print(cadena.count("Mundo"))  # Imprime: 1
#los objetos de la clase int no tienen métodos que nos permitan manipularlos, pero si queremos convertir un entero a una cadena de texto, podemos usar la función str() como vimos al principio.
# numero = 10.lower()  # Esto generará un error, ya que los enteros no tienen el método lower()
longitud = (10).bit_length() 
print(longitud)  # Imprime: 4 porque el número 10 en binario es 1010, que tiene 4 bits.