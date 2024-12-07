# main.py -- put your code here!
from machine import Pin
import time

led13 = Pin(13, Pin.OUT)  # Configura el pin 13 como salida
led12 = Pin(12, Pin.OUT)  # Configura el pin 12 como salida
led14 = Pin(14, Pin.OUT)  # Configura el pin 14 como salida
led27 = Pin(27, Pin.OUT)  # Configura el pin 27 como salida
led26 = Pin(26, Pin.OUT)  # Configura el pin 26 como salida
led25 = Pin(25, Pin.OUT)  # Configura el pin 25 como salida

while True:
    led13.value(1)  # Enciende el led
    time.sleep(0.5)  # Espera 0.5 segundos
    led13.value(0)  # Apaga el led
    led12.value(1)  # Enciende el led
    time.sleep(0.5)  # Espera 0.5 segundos
    led12.value(0)  # Apaga el led
    led14.value(1)  # Enciende el led
    time.sleep(0.5)  # Espera 0.5 segundos
    led14.value(0)  # Apaga el led
    led27.value(1)  # Enciende el led
    time.sleep(0.5)  # Espera 0.5 segundos
    led27.value(0)  # Apaga el led
    led26.value(1)  # Enciende el led
    time.sleep(0.5)  # Espera 0.5 segundos
    led26.value(0)  # Apaga el led
    led25.value(1)  # Enciende el led
    time.sleep(0.5)  # Espera 0.5 segundos
    led25.value(0)  # Apaga el led
