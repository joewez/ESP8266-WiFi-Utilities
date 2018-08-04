#
# Wrapper of convenience functions for the WiFi control
# of an ESP8266 device
# 
# Author: J.G. Wezensky

import network

def connect(ssid, password=""):
    ap = network.WLAN(network.AP_IF)    
    ap.active(False)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

    print('network config:', wlan.ifconfig())

def disconnect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    while wlan.isconnected():
        pass

    print('disconnected.')

def access_point(ssid, passphrase=""):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    while wlan.isconnected():
        pass

    ap = network.WLAN(network.AP_IF)    
    ap.active(True)
    if (passphrase == ''):
        ap.config(essid=ssid, password="", authmode=1)
    else:
        ap.config(essid=ssid, password=passphrase, authmode=4)

    print('network config:', ap.ifconfig())

def none():
    ap = network.WLAN(network.AP_IF)    
    ap.active(False)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    while wlan.isconnected():
        pass

    print('wifi off')

def off():
    none()

def scan():
    import esp
    import time
    esp.osdebug(None)
    wlan = network.WLAN(network.STA_IF)
    state = wlan.active()
    wlan.active(True)
    time.sleep(2)
    print('Scanning...')
    nets = wlan.scan()
    for net in nets:
        print(' ' + str(net[0], "utf-8"))
    if not state:
        wlan.active(False)
    esp.osdebug(0)

def status():
    ap = network.WLAN(network.AP_IF)
    print('AP :{0}'.format(ap.active()))

    sta = network.WLAN(network.STA_IF)
    print('STA:{0}'.format(sta.active()))
    if (sta.active()):
        (address, mask, gateway, dns) = sta.ifconfig()
        print('IP :{0}'.format(address))
        print('GW :{0}'.format(gateway))
        print('DNS:{0}'.format(dns))
    ma = ":".join(map(lambda x: "%02x" % x, sta.config('mac')))
    print('MAC:{0}'.format(ma))
