# Mongoose-os
## Vorbereitungen
Die Pfadvariable muss so eingestellt werden, dass *mos.exe* aufgerufen werden kann. 

Ansonsten startet die Erweiterung dann, wenn sich im Projektordner eine Datei *mos.yml* befindet. Diese Datei definiert den build des Projektes und hat z.B. folgendes Aussehen:
```yml
author: tuttas
description: A JS build with DS180B2 temperature Sensor
# arch: PLATFORM
version: 1.0
manifest_version: 2017-05-18
libs_version: ${mos.version}
modules_version: ${mos.version}
mongoose_os_version: ${mos.version}

tags:
  - js

filesystem:
  - fs

libs:
  - origin: https://github.com/mongoose-os-libs/js-demo-bundle

    # libs necessary for the current app
  - origin: https://github.com/mongoose-os-libs/arduino-dallas-temperature
  - origin: https://github.com/mongoose-os-libs/mjs
```

Am einfachsten man cloned dieses Repository, um alle Dateien zu haben:
```
git clone https://github.com/mongoose-os-libs/js-demo-bundle.git
```

Anschließend kann unten in der MenuLeiste der COM Port eingestellt und die IP Adresse konfiguriert werden!

Die Web Entwicklungsoberfläche kann aufgrufen werden über: http://127.0.0.1:1992

## Wlan Konfiguration
Die WLAN Konfiguration kann entweder unter Expert-View eingestellt werden, oder aber man erstellt eine Datei z.B. *conf8.json* mit folgenden Inhalt:
```js
{
  "wifi": {
    "sta": {
      "enable": true,         
      "ssid": "MMBBS-Puplic",        
      "pass": "Kennwort",           
      "user": "mmbbs\\Klasse.Nachname",          
      "anon_identity": "",   
      "cert": "",           
      "key": "",            
      "ca_cert": "",        
      "ip": "",           
      "netmask": "",        
      "gw": "",             
      "nameserver": "",    
      "dhcp_hostname": ""   
    }
  }
}
```

## Sonstiges
Ansonsten wird das Image erzeugt über den Befehl *mos build --platform esp32*
