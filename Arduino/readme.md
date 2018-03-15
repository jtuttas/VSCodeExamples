# ESP32
## Extensions
- [Arduiono Extension v. Microsoft](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.vscode-arduino)
- [C/C++ Extension v. Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
## Konfiguration
Richtigen COM Port wählen und 'ES32 DEV Module' wählen. Diese Einstellungen laden in einer Datei mit dem Namen *arduino.json*, die dann z.B. So aussieht:
```json
{
    "port": "COM3",
    "board": "expressif:esp32:esp32",
    "configuration": "FlashMode=qio,FlashFreq=80,FlashSize=4M,UploadSpeed=921600,DebugLevel=none",
    "sketch": "blink.ino",
    "output": "..\\ArduinoOutput"
}
```
Wichtig ist es hier das Attribut "output" zu setzen, damit nicht ständig neu kompiliert und gelinkt werden muss.

In *settings.json* sind folgende Einstellung notwendiug.
```json
{
    "arduino.path": "c:\\Users\\jtutt\\OneDrive\\bin\\arduino-1.6.13",
    "arduino.additionalUrls": "",
    "arduino.logLevel": "info", 
    "arduino.enableUSBDetection": true,
    "C_Cpp.intelliSenseEngine": "Tag Parser",
}
```

Ebenso im Ordner .vscode zu finden eine Datei mit dem Namen *c_cpp_properties.json* die die Pfade zu den notwendigen Bibliotheken enthält. Bei mir sieht diese Datei wie folgt aus:
```json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "C:\\Users\\jtutt\\Documents\\Arduino\\hardware\\expressif\\esp32\\cores\\esp32",
                "C:\\Users\\jtutt\\OneDrive\\bin\\arduino-1.6.13\\libraries",
                "C:\\Users\\jtutt\\Documents\\Arduino\\hardware\\expressif\\esp32\\tools\\sdk\\include\\esp32"
            ],
            "browse": {
                "limitSymbolsToIncludedHeaders": false,
                "path": [
                    "C:\\Users\\jtutt\\Documents\\Arduino\\hardware\\expressif\\esp32\\cores\\esp32",
                    "C:\\Users\\jtutt\\OneDrive\\bin\\arduino-1.6.13\\libraries",
                    "C:\\Users\\jtutt\\Documents\\Arduino\\hardware\\expressif\\esp32\\tools\\sdk\\include\\esp32"
                ]
            },
            "intelliSenseMode": "msvc-x64"
        }
    ],
    "version": 3
}
```



## Shortcuts
- Mit *STRG+ALT+U* kann der Sketch hochgeladen werden.