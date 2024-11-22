import ubluetooth
from machine import Pin
import time

# Configuración del LED
led_pin = Pin(2, Pin.OUT)  # GPIO 2

# Crear una instancia de BLE
ble = ubluetooth.BLE()
ble.active(True)
print("BLE activado.")

# Definir el servicio y la característica
LED_SERVICE_UUID = ubluetooth.UUID(0x1812)  
LED_CMD_CHAR_UUID = ubluetooth.UUID(0x2A56)

# Crear la característica para el control del LED (escritura)
LED_CMD_CHAR = (LED_CMD_CHAR_UUID, ubluetooth.FLAG_WRITE,)

# Registrar el servicio
led_service = (LED_SERVICE_UUID, (LED_CMD_CHAR,))
ble.gatts_register_services([led_service])

# Función de callback para manejar las escrituras
def on_write(event, data):
    print("Comando recibido:", data)
    if data == b'1':
        led_pin.on()
        print("LED Encendido")
    elif data == b'0':
        led_pin.off()
        print("LED Apagado")

# Configurar el evento BLE para manejar la escritura
ble.irq(on_write)

# Hacer publicidad para permitir que otros dispositivos se conecten
def advertise():
    name = "ESP32_LED"
    ble.gap_advertise(100, name)
    print("Anuncio BLE iniciado. Esperando conexión...")

advertise()

# Ciclo principal
while True:
    time.sleep(1)
