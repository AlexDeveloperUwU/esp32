import socket
from machine import Pin

led_pins = [13, 12, 14, 27, 26, 25]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

def start_webserver():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1] 
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Servidor web escuchando en http://{}:80'.format(addr))

    def handle_request(request):
        if '/on' in request:
            try:
                led_index = int(request.split('/on')[1][0]) - 1
                if 0 <= led_index < len(leds):
                    leds[led_index].value(1)
                    return '''HTTP/1.1 302 Found
Location: /
Content-Type: text/html
Connection: close

<h1>LED {} Encendido</h1><p>Redirigiendo al inicio...</p>
'''.format(led_index + 1)
            except (ValueError, IndexError):
                pass
        elif '/off' in request:
            try:
                led_index = int(request.split('/off')[1][0]) - 1
                if 0 <= led_index < len(leds):
                    leds[led_index].value(0)
                    return '''HTTP/1.1 302 Found
Location: /
Content-Type: text/html
Connection: close

<h1>LED {} Apagado</h1><p>Redirigiendo al inicio...</p>
'''.format(led_index + 1)
            except (ValueError, IndexError):
                pass
        else:
            try:
                with open('web/index.html', 'r') as f:
                    return f.read()
            except OSError:
                return '<h1>Error al cargar el archivo HTML</h1>'
        return '<h1>Solicitud no válida</h1>'

    while True:
        cl, addr = s.accept()
        print('Cliente conectado desde', addr)
        request = cl.recv(1024).decode('utf-8')
        response = handle_request(request)
        cl.send(response.encode('utf-8'))
        cl.close()

start_webserver()
