import socket
from machine import Pin

led = Pin(2, Pin.OUT) 

def start_webserver():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1] 
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Servidor web escuchando en http://{}:80'.format(addr))

    while True:
        cl, addr = s.accept()
        print('Cliente conectado desde', addr)
        request = cl.recv(1024)
        request = str(request)

        if '/on' in request:
            led.value(1)
            response = '''HTTP/1.1 302 Found
Location: /
Content-Type: text/html
Connection: close

<h1>LED Encendido</h1><p>Redirigiendo al inicio...</p>
'''
        elif '/off' in request:
            led.value(0) 
            response = '''HTTP/1.1 302 Found
Location: /
Content-Type: text/html
Connection: close

<h1>LED Apagado</h1><p>Redirigiendo al inicio...</p>
'''
        else:
            try:
                with open('web/index.html', 'r') as f:
                    response = f.read()
            except OSError:
                response = '<h1>Error al cargar el archivo HTML</h1>'

        cl.send(response)
        cl.close()

start_webserver()
