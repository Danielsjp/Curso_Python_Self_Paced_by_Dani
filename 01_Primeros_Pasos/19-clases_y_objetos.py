numero = 10
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
#la forma de llamar a un método es: nombre_del_objeto.nombre_del_metodo()
#los pararentesis son necesarios aunque el método no reciba argumentos.
#ya que hay meteodos que reciben argumentos, por ejemplo:
cadena = "Hola Mundo"
cadena_con_sustitucion = cadena.replace("Mundo", "Python")
print(cadena_con_sustitucion)  # Imprime: 'Hola Python'
