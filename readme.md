# Konfigurationen f. Visual Studio Code
Hier sind einige beispielhafte Konfigurationen von Visual Studio Code f. diverse Programmiersprachen 
## Extensions
Meine Extension (aus *{HOME}/.vscode/extensions*):
```
GrapeCity.gc-excelviewer-2.0.17/         felixfbecker.php-intellisense-2.2.6/  rafaelmaiolla.remote-vscode-1.1.0/
Mikael.angular-beastcode-5.2.10/         humao.rest-client-0.17.0/             redhat.java-0.18.1/
PeterJausovec.vscode-docker-0.0.24/      johnpapa.angular2-2.12.0/             shakram02.bash-beautify-0.1.1/
Zignd.html-css-class-completion-1.16.1/  ms-python.python-2018.1.0/            tht13.python-0.2.3/
abusaidm.html-snippets-0.2.1/            ms-vscode.cpptools-0.14.6/            vsciot-vscode.vscode-arduino-0.2.10/
donjayamanne.jquerysnippets-0.0.1/       ms-vscode.powershell-1.5.1/           vscjava.vscode-java-debug-0.6.0/
dracula-theme.theme-dracula-2.8.0/       msjsdiag.debugger-for-chrome-4.1.0/   vscjava.vscode-java-pack-0.2.0/
ecmel.vscode-html-css-0.2.0/             qinjia.view-in-browser-0.0.5/         wcwhitehead.bootstrap-3-snippets-0.1.0/
```
## Konfiguration
Meine Konfiguration
```js
{
    "editor.fontSize": 12,
    "workbench.colorTheme": "Dracula",
    "terminal.integrated.shell.windows": "cmd.exe",
    "terminal.integrated.shellArgs.windows": [
        "/k",
        "c:\\Users\\jtutt\\OneDrive\\bin\\cmder\\vendor\\init.bat"
    ],
    "editor.mouseWheelZoom": true,
    "git.confirmSync": false,
    "files.exclude": {
        "**/.git": true       
    },
    "powershell.powerShellExePath": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
    "python.disablePromptForFeatures": [
        "pylint"
    ],
    "window.zoomLevel": 1,
    //-------- Remote VSCode configuration --------
    // Port number to use for connection.
    "remote.port": 52698,

    // Launch the server on start up.
    "remote.onstartup": true,

    // Address to listen on.
    "remote.host": "127.0.0.1",
    
    // Arduiono Settings
    "arduino.path": "c:\\Users\\jtutt\\OneDrive\\bin\\arduino-1.6.13",
    "arduino.additionalUrls": "",
    "arduino.logLevel": "info", 
    "arduino.enableUSBDetection": true,
    "C_Cpp.intelliSenseEngineFallback": "Disabled",
    "C_Cpp.intelliSenseEngine": "Tag Parser",

    // JAVA Plugin
    "java.home": "C:\\Program Files\\Java\\jdk1.8.0_131",
    "java.errors.incompleteClasspath.severity": "ignore",
 
    
    // Python
    "python.pythonPath": "c:\\Users\\jtutt\\AppData\\Local\\Programs\\Python\\Python36-32\\",
    "python.autoComplete.extraPaths": [],

    // HTML
    "extension.viewInBrowser":"chrome",
}
```
## Tipps
### CMDER
*cmder* kann als Terminal installiert werden, dazu folgende Einstellungen ändern:
```json
    "terminal.integrated.shell.windows": "cmd.exe",
    "terminal.integrated.shellArgs.windows": [
        "/k",
        "c:\\Users\\jtutt\\OneDrive\\bin\\cmder\\vendor\\init.bat"
    ],
```
### Remote VS Code
In Anlehnung an [diesen Artikel](https://codepen.io/ginfuru/post/remote-editing-files-with-ssh "Google's Homepage")
Um Remote VS Code zu verwenden (z.B. für den Raspberry PI) sollte in CMDER Aliasse eingerichtet werden (unter {cmder}/config/userer-aliases)
```
connect-pi2b= ssh -R 52698:127.0.0.1:52698 pi@service.joerg-tuttas.de -p 8201
```

Auf dem PI muss *rcode* installiert werden!
```bash
sudo wget -O /usr/local/bin/rcode \
https://raw.github.com/aurora/rmate/master/rmate
chmod a+x /usr/local/bin/rcode
```
Dann sollte noch ein alias eingerichtet werden z.B. unter */etc/profile*
```bash
alias code='rmate -p 52698'
```
## Videos
[![Remote HTML Page](http://img.youtube.com/vi/l5Y_P8w07PY/0.jpg)](http://www.youtube.com/watch?v=l5Y_P8w07PY)


[![ESP 32](http://img.youtube.com/vi/pG5JEoUC2Hc/0.jpg)](http://www.youtube.com/watch?v=pG5JEoUC2Hc)

[![Powershell Core](http://img.youtube.com/vi/WO0DqRpR5hs/0.jpg)](http://www.youtube.com/watch?v=WO0DqRpR5hs)


