# ESP8266-WiFi-Utilities
My personal MicroPython wrapper around the WiFi controls of the ESP8266

FROM the Help:
 * connect(ssid, [password], [silent]) - Connect to and access point* 
 * disconnect([silent]) - Diconnect from the current access point*
 * access_point(ssid, [passphrase], [dns], [silent]) - Create an Access Point*
 * none([silent]) - Turn all WiFi interfaces off*
 * off() - Same as none()
 * scan() - List avaiable access points
 * status() - Show current WiFi status
 * connected() - Return status of the STA connection
 * debug(state) - Turns the debug messages on and off*

(* Means setting are persistent upon reset)
