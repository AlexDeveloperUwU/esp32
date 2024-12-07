import network

def setup_wifi():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)  
    ap.config(essid='ESP32_AlexDevUwU', authmode=3, password='MiWiFi00') 
    
    print('Red WiFi activada: {}'.format(ap.config('essid')))
    print('Dirección IP: {}'.format(ap.ifconfig()[0])) 

setup_wifi()
