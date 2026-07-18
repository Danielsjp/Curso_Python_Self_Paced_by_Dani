#las variables en python son contenedores de informacion que nos permiten almacenar datos y manipularlos a lo largo del programa.
Nombre = "Juan"
Apellido = "Perez"
#en python las variables no necesitan ser declaradas con un tipo de dato especifico, ya que python es un lenguaje de tipado dinamico.
Edad = 30
#en python a las variables se le llaman nombres de variables, y se pueden utilizar para almacenar diferentes tipos de datos como numeros, cadenas de texto, listas, diccionarios, entre otros.
alto = 1.75
ancho = 0.75
area = alto * ancho
#no es muy habitual pero podemos asignar la funcion print a una variable y luego utilizarla para imprimir en pantalla.
imprime = print
imprime("El area es: ", area)
#podemos asignar el mismo valor a varias variables al mismo tiempo.
alto1 = alto2 = 1.80
#podemos asignar el valor de una variable a otra variable.
alto3 = alto2
print(alto3)
#podemos utilizar la funcion id() para obtener el identificador unico de una variable, que nos permite saber si dos variables apuntan al mismo objeto en memoria.
print(id(alto1))
print(id(alto3))
valor1 = alto1 * 2
valor2 = alto2 * 2
#podemos utilizar la funcion id() para obtener el identificador unico de una variable, que nos permite saber si dos variables apuntan al mismo objeto en memoria.
#en este caso, como alto1 y alto2 tienen el mismo valor, pero son variables diferentes, sus identificadores seran diferentes.
print(id(valor1))
print(id(valor2))
#en este caso, como a y b tienen el mismo valor, pero son variables diferentes, sus identificadores seran diferentes. ( me han salido iguales, pero en realidad son diferentes, ya que python optimiza el uso de memoria y reutiliza objetos inmutables como los numeros enteros y las cadenas de texto.)
a = 2*2
b = 2*2
print(id(a))
print(id(b))
