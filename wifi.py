#
# Wrapper of convenience functions for the WiFi control
# of an ESP8266 device
# 
# Author: J.G. Wezensky

import network

def connect(ssid, password="", silent=True):
    ap = network.WLAN(network.AP_IF)    
    ap.active(False)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        if not silent:
            print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

    if not silent:
        print('network config:', wlan.ifconfig())

def disconnect(silent=True):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    while wlan.isconnected():
        pass

    if not silent:
        print('disconnected.')

def access_point(ssid, passphrase="", dns=False, silent=True):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    while wlan.isconnected():
        pass

    ap = network.WLAN(network.AP_IF)    
    ap.active(True)
    if dns:
        local_ip = "192.168.4.1"
        ap.ifconfig((local_ip, "255.255.255.0", local_ip, local_ip))
    if (passphrase == ''):
        ap.config(essid=ssid, password="", authmode=1)
    else:
        ap.config(essid=ssid, password=passphrase, authmode=4)

    if not silent:
        print('network config:', ap.ifconfig())

def none(silent=True):
    ap = network.WLAN(network.AP_IF)    
    ap.active(False)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    while wlan.isconnected():
        pass

    if not silent:
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
    if (ap.active()):
        (address, mask, gateway, dns) = ap.ifconfig()
        print('  IP :{0}'.format(address))
        print('  GW :{0}'.format(gateway))
        print('  DNS:{0}'.format(dns))

    sta = network.WLAN(network.STA_IF)
    print('STA:{0}'.format(sta.active()))
    if (sta.active()):
        (address, mask, gateway, dns) = sta.ifconfig()
        print('  IP :{0}'.format(address))
        print('  GW :{0}'.format(gateway))
        print('  DNS:{0}'.format(dns))
    ma = ":".join(map(lambda x: "%02x" % x, sta.config('mac')))
    print('MAC:{0}'.format(ma))

def connected():
    wlan = network.WLAN(network.STA_IF)
    return wlan.isconnected()

def debug(state=True):
    import esp
    if state:
        esp.osdebug(0)
    else:
        esp.osdebug(None)

def man():
    print("""
Commands:
    connect(ssid, [password], [silent]) - Connect to and access point*
    disconnect([silent]) - Diconnect from the current access point*
    access_point(ssid, [passphrase], [dns], [silent]) - Create an Access Point*
    none([silent]) - Turn all WiFi interfaces off*
    off() - Same as none()
    scan() - List avaiable access points
    status() - Show current WiFi status
    connected() - Return status of the STA connection
    debug(state) - Turns the debug messages on and off*

    * = Setting will PERSIST a reboot
""")

def help():
    man()

def version():
    return '1.3.0'