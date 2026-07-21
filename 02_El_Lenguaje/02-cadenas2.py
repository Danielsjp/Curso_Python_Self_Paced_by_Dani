edad = 4
#cadena "Ivan tiene " + edad + " años" #esto no funciona, ya que no se puede concatenar un string con un entero, por lo que hay que convertir el entero a string usando la funcion str()
cadena = "Ivan tiene " + str(edad) + " años" #esto si funciona
print(cadena)
#Podemos usar el asterisco para multiplicar
print("Batman "*2 + "na"*5)
#1...