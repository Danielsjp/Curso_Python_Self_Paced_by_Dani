# si desde la consola ejecuta: python -m http.server
# arranca un servidor web en el puerto 8000, y si se accede a http://localhost:8000/ se puede ver el contenido del directorio actual.
#aqui un script que ejecuta un servidor web en el puerto 8000 y se queda escuchando hasta que se interrumpa con Ctrl+C
import http.server
port = 8000
#esto es para que el servidor se quede escuchando en el puerto 8000
handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(('', port), handler) as httpd:
    print(f"Servidor corriendo en http://localhost:{port}")
    httpd.serve_forever()
