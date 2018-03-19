# Konfigurationen f. Visual Studio Code
Hier sind einige beispielhafte Konfigurationen von Visual Studio Code f. diverse Programmiersprachen 

## Extensions
Meine Extension..
```
  azure-account v0.3.3
  bash-beautify v0.1.1
  bootstrap-3-snippets v0.1.0
  code-settings-sync v2.9.0
  cpptools v0.15.0
  debugger-for-chrome v4.2.1
  githistory v0.4.0
  html-css-class-completion v1.17.1
  html-snippets v0.2.1
  java v0.21.0
  jquerysnippets v0.0.1
  LiveServer v3.2.1
  npm-intellisense v1.3.0
  okazukiplantuml v0.2.2
  php-intellisense v2.2.9
  plantuml v2.5.5
  PowerShell v1.6.0
  python v0.2.3
  python v2018.2.1
  remote-vscode v1.1.0
  rest-client v0.17.0
  theme-dracula v2.9.0
  vscode-arduino v0.2.11
  vscode-azureappservice v0.6.1
  vscode-cosmosdb v0.5.0
  vscode-docker v0.0.25
  vscode-html-css v0.2.0
  vscode-java-debug v0.7.0
  vscode-java-pack v0.3.0
  vscode-java-test v0.4.0
  vscode-mysql v0.3.0
  vscode-npm-script v0.3.3
```
## Konfiguration
Meine Konfiguration
```js
{
    "editor.fontSize": 12,
    "workbench.colorTheme": "Dracula",
    "terminal.integrated.shell.windows": "cmd.exe",
    // Diese Einstellungen sind nur wenn cmder genutzt wird, sonst kann dieses hier gelöscht werden
    "terminal.integrated.shellArgs.windows": [
        "/k",
        "c:\\Users\\jtutt\\OneDrive\\bin\\cmder\\vendor\\init.bat"
    ],
    "editor.mouseWheelZoom": true,
    "git.confirmSync": false,
    "files.exclude": {
        "**/.git": true,
    },
    // Pfad zur Powershell!
    "powershell.powerShellExePath": "C:\\WINDOWS\\SysWow64\\WindowsPowerShell\\v1.0\\powershell.exe",
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
    // Arduiono Settings (Pfad zur Arduino IDE)
    "arduino.path": "c:\\Users\\jtutt\\OneDrive\\bin\\arduino-1.6.13",
    "arduino.additionalUrls": "",
    "arduino.logLevel": "info",
    "arduino.enableUSBDetection": true,
    // JAVA Plugin
    // Pfad zur Java JDK
    "java.home": "C:\\Program Files\\Java\\jdk1.8.0_131",
    // Python
    // Pfad zur Python Executable
    "python.pythonPath": "c:\\Users\\jtutt\\AppData\\Local\\Programs\\Python\\Python36-32\\",
    "python.autoComplete.extraPaths": [],
    // HTML
    "view-in-browser.customBrowser": "chrome",
    "git.enableSmartCommit": true,
    // Sync setting
    "sync.gist": "0c034bdc6361c92b3c233e9cdb0de18f",
    "sync.lastUpload": "2018-03-18T18:45:35.137Z",
    "sync.autoDownload": false,
    "sync.autoUpload": false,
    "sync.lastDownload": "2018-02-12T08:30:52.036Z",
    "sync.forceDownload": false,
    "sync.host": "",
    "sync.pathPrefix": "",
    "sync.quietSync": false,
    "sync.askGistName": false,
    // Path to the Mongo shell executable
    "mongo.shell.path": "C:\\Program Files\\MongoDB\\bin",
    "cosmosDB.showSavePrompt": false,
    // Misc
    "explorer.confirmDelete": false,
    "workbench.startupEditor": "newUntitledFile",
    "files.autoSave": "onFocusChange",
    "sync.removeExtensions": true,
    "sync.syncExtensions": true,
    "liveServer.settings.donotShowInfoMsg": true,
    "java.errors.incompleteClasspath.severity": "ignore",
    "liveServer.settings.donotVerifyTags": true,
    "plantuml.render": "PlantUMLServer",
    "plantuml.server": "http://www.plantuml.com/plantuml",
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
In Anlehnung an [diesen Artikel](https://codepen.io/ginfuru/post/remote-editing-files-with-ssh "VS Code Remote")
Um Remote VS Code zu verwenden (z.B. für den Raspberry PI) sollte in CMDER Aliasse eingerichtet werden (unter {cmder}/config/userer-aliases)
```
code="%CMDER_ROOT%\..\VSCode\Code.exe" $*
connect-pi2b= ssh -R 52698:127.0.0.1:52698 pi@service.joerg-tuttas.de -p 8201
```

Auf dem PI muss *rcode* installiert werden!
```bash
sudo wget -O /usr/local/bin/rcode https://raw.github.com/aurora/rmate/master/rmate
chmod a+x /usr/local/bin/rcode
```
Dann sollte noch ein alias eingerichtet werden z.B. unter */etc/profile*
```bash
alias code='rmate -p 52698'
```
## Videos
### Einsatz von VS Code im 1. bis 3. AJ
[![1Aj bis 3AJ](http://img.youtube.com/vi/Fzd6rFyOPVs/0.jpg)](http://www.youtube.com/watch?v=Fzd6rFyOPVs)
### Remote eine HTML Seite auf dem Raspberry PI editieren
[![Remote HTML Page](http://img.youtube.com/vi/l5Y_P8w07PY/0.jpg)](http://www.youtube.com/watch?v=l5Y_P8w07PY)
### ESP32 Programmieren
[![ESP 32](http://img.youtube.com/vi/pG5JEoUC2Hc/0.jpg)](http://www.youtube.com/watch?v=pG5JEoUC2Hc)
### Powershell Core auf dem Raspberry PI
[![Powershell Core](http://img.youtube.com/vi/WO0DqRpR5hs/0.jpg)](http://www.youtube.com/watch?v=WO0DqRpR5hs)


