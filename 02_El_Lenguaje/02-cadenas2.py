edad = 4
#cadena "Ivan tiene " + edad + " años" #esto no funciona, ya que no se puede concatenar un string con un entero, por lo que hay que convertir el entero a string usando la funcion str()
cadena = "Ivan tiene " + str(edad) + " años" #esto si funciona
print(cadena)
#Podemos usar el asterisco para multiplicar
print("Batman "*2 + "na"*5)
#La clase str tiene varios metodos para manipular las cadenas de texto, como por ejemplo el metodo upper(), lower(), capitalize(), title(), swapcase(), strip(), lstrip(), rstrip(), replace(), split(), join(), find(), index(), count(), startswith(), endswith(), etc.
print(cadena.upper()) #convierte la cadena a mayusculas
print(cadena.lower()) #convierte la cadena a minusculas
print(cadena.capitalize()) #convierte la primera letra de la cadena a mayusculas
print(cadena.title()) #convierte la primera letra de cada palabra de la cadena a mayusculas
print(cadena.swapcase()) #convierte las mayusculas a minusculas y viceversa
print(cadena.strip()) #elimina los espacios en blanco al inicio y al final de la cadena
print(cadena.strip("Ivan ")) #Elimina "Ivan " al inicio y al final de la cadena
print(cadena.lstrip()) #elimina los espacios en blanco al inicio de la cadena
print(cadena.rstrip()) #elimina los espacios en blanco al final de la cadena
print(cadena.replace("a", "o")) #reemplaza todas las ocurrencias de la primera letra por la segunda
print(cadena.split()) #divide la cadena en una lista de palabras
print(cadena.join(["a", "b", "c"])) #une los elementos de la lista en una cadena
