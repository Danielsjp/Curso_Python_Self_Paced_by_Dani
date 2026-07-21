cadena= "Esto es una cadena de texto"
print(cadena)
cadena = "Esto" "es" "una" "cadena" "de" "texto"
print(cadena)
cadena = "Esto es una 'cadena de texto' con comillas simples"
print(cadena)
cadena = "Esto es una \"cadena de texto\" con comillas dobles usando el caracter de escape"
print(cadena)
cadena = 'Esto es una cadena de varias lineas \
abarcando varias lineas de texto \
y permiter que el texto se vea mas ordenado'
print(cadena)
cadena = "usando salto de linea \npara separar el texto en varias lineas"
print(cadena)
cadena = """Esto es una cadena de varias lineas
abarcando varias lineas de texto
y permite que el texto se vea mas ordenado"""
print(cadena)
print("hay muchos otros caracteres de escape, como por ejemplo: \t para tabulador, \r para retorno de carro, \b para retroceso, entre otros") #esto no ha funcionado en 
# la terminal de windows, pero si en la de linux.
print("Tambien existen caracteres unicode, como por ejemplo: \u00A9 para el simbolo de copyright, \u00AE para el simbolo de marca registrada, entre otros")
#hay otras formas de formatear cadenas de texto, como por ejemplo usando el metodo format() o f-strings, que veremos en los siguientes ejemplos.
nombre = "juan"
edad = 30.667
print(f"Hola, mi nombre es {nombre.capitalize()} y tengo {edad:.1f} años")
#esto es una forma de formatear cadenas de texto usando f-strings, que es una forma mas moderna y recomendada de hacerlo por su simplicidad y legibilidad.
