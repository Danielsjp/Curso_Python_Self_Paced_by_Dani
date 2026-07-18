RUTA_ARCHIVO = "C:/Users/Usuario/Documents/archivo.txt"
IVA = 0.21
IVA_REDUCIDO = 0.10
IVA_SUPER_REDUCIDO = 0.04
#el uso de constantes en python es una buena practica de programacion, ya que nos permite definir valores que no deben cambiar a lo largo del programa, y nos ayuda a mejorar la legibilidad del codigo.
#Ejercicio pizza con constantes
PI = 3.14159
PRECIO_CM_CUADRADO = 0.05
IMPUESTO = 0.21
radio = float(input("Ingrese el radio de la pizza en cm: "))
area = PI * radio**2
#precio con impuesto
precio_sin_impuesto = area * PRECIO_CM_CUADRADO
precio_con_impuesto = precio_sin_impuesto * (1 + IMPUESTO)
print(f"El precio de la pizza es: {precio_con_impuesto:.2f}")
#la f se utiliza para formatear la cadena de texto, y el .2f indica que queremos mostrar 2 decimales en el precio final.

