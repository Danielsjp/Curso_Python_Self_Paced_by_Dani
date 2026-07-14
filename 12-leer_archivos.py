#la funcion open() permite abrir un archivo y devuelve un objeto de tipo archivo.
f = open('texto.txt')
#aqui se lee el contenido del archivo y se guarda en la variable texto
texto = f.read()
#aqui se cierra el archivo para liberar recursos
f.close()
#aqui se imprime el contenido del archivo
print(texto)
