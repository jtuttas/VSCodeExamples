# Platform IO
Installation des Paketes und Initialisierung eines Projektes über den Dialog der Erweiterung.

## Tips
Die Geschwindigkeit der seriellen Schnittstelle kann über in der Datei *platform.ini* eingestellt werden.
```ini
; Serial Monitor options
monitor_baud = 115200
```

Werden Libraries importiert, so landen diese im Verzeichnis **{Home}/.platformio/lib/** , damit Intellisense funktioniert müssen diese Libraries (die .h Dateien) in der Datei  *c_cpp_propoerties.json* bekannt gemacht werden, d.h. der Pfad zu diesen Dateien mit eingefügt werden und zwar unter *includePath* und *browse.path*. 
```js
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "C:/Users/jtutt/.platformio/packages/tool-unity",
                "C:/Users/jtutt/.platformio/lib/PubSubClient_ID89/src",
                ""
            ],
            "browse": {
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": "${workspaceRoot}/.vscode/.browse.c_cpp.db",
                "path": [
                    "C:/Users/jtutt/.platformio/packages/tool-unity",
                    "C:/Users/jtutt/.platformio/lib/PubSubClient_ID89/src",
                    ""
                ]
            },
            //etc......
```

## Video
### Platform IO mit ESP32 
[![1Aj bis 3AJ](http://img.youtube.com/vi/vkuoOES5KHg/0.jpg)](http://www.youtube.com/watch?v=vkuoOES5KHg)
