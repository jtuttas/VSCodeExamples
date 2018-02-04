# ESP32
## Extensions
- [Arduiono Extension v. Microsoft](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.vscode-arduino)
- [C/C++ Extension v. Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
## Konfiguration
Richtigen COM Port wählen und 'ES32 DEV Module' wählen.

Folgende Einstellung: Wichtig, der Pfad zur Arduino IDE
```js
{
      // Arduiono Settings
    "arduino.path": "c:\\Users\\jtutt\\OneDrive\\bin\\arduino-1.6.13",
    "arduino.additionalUrls": "",
    "arduino.logLevel": "info", 
    "arduino.enableUSBDetection": true,
    "C_Cpp.intelliSenseEngineFallback": "Disabled",
    "C_Cpp.intelliSenseEngine": "Tag Parser",

}
```
## Shortcuts
Mit *STRG+ALT+U* kann der Sketch hochgeladen werden.