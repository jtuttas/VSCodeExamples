# Konfigurationen f. Visual Studio Code
Hier sind einige beispielhafte Konfigurationen von Visual Studio Code f. diverse Programmiersprachen (siehe readme.md in den einzelnen Unterordnern).

## Extensions
Meine Extension, aus .vscode/Extensions, angezeigt mit *code --list-extensions*.
```
abusaidm.html-snippets
christian-kohler.npm-intellisense
christian-kohler.path-intellisense
donjayamanne.githistory
donjayamanne.jquerysnippets
dracula-theme.theme-dracula
ecmel.vscode-html-css
eg2.vscode-npm-script
felixfbecker.php-intellisense
formulahendry.azure-virtual-machine-explorer
formulahendry.code-runner
formulahendry.vscode-mysql
humao.rest-client
jebbs.plantuml
johnpapa.Angular2
mongoose-os.mongoose-os-ide
ms-azuretools.vscode-azureappservice
ms-azuretools.vscode-azurefunctions
ms-azuretools.vscode-cosmosdb
ms-mssql.mssql
ms-python.python
ms-vscode.azure-account
ms-vscode.azurecli
ms-vscode.cpptools
ms-vscode.PowerShell
msjsdiag.debugger-for-chrome
natewallace.angular2-inline
PeterJausovec.vscode-docker
platformio.platformio-ide
rafaelmaiolla.remote-vscode
redhat.java
ritwickdey.LiveServer
shakram02.bash-beautify
Shan.code-settings-sync
vsciot-vscode.azure-iot-toolkit
vscjava.vscode-java-debug
vscjava.vscode-java-pack
vscjava.vscode-java-test
vscjava.vscode-maven
wcwhitehead.bootstrap-3-snippets
webfreak.debug
Zignd.html-css-class-completion
```
## Tips
### Azure
Wird die Azure CLI verwendet, so muss diese erst angemeldet werden, dieses geschieht über den Befehl *az login* anschließend muss auf der angezeigten Webseite der angezeigte Code eingegeben werden.

Die MS Azure Extensions müssen ebenso angemeldet sein, dieses geschieht über den Befehl (also *F1* drücken) und dann *Azure Sign in*.

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

Auf dem PI muss *rmate* installiert werden!
```bash
sudo wget -O /usr/local/bin/rcode https://raw.github.com/aurora/rmate/master/rmate
chmod a+x /usr/local/bin/rmate
```
Dann sollte noch ein alias eingerichtet werden z.B. unter */etc/profile*
```bash
alias code='rmate -p 52698'
```

## Umgebungsvariablen im System
Ein 'schön' eingerichteter Rechner sollte folgende Umgebungsvariablen richtig gesetzt haben:
```
JAVA_HOME ... auf JDK
PATH ... auf npm ({User}/AppData/Roaming/npm), python (auf python.exe), maven (auf mvn.exe), MongoDB (auf mongo.exe), mongoose-os, NuGet.exe, JavaJSK/bin
```
## Videos
### Einsatz von VS Code im 1. bis 3. AJ
[![1Aj bis 3AJ](http://img.youtube.com/vi/Fzd6rFyOPVs/0.jpg)](http://www.youtube.com/watch?v=Fzd6rFyOPVs)
### VS Code und Azure
[![1Aj bis 3AJ](http://img.youtube.com/vi/uKqMbRh3Aoo/0.jpg)](http://www.youtube.com/watch?v=uKqMbRh3Aoo)
### Remote eine HTML Seite auf dem Raspberry PI editieren
[![Remote HTML Page](http://img.youtube.com/vi/l5Y_P8w07PY/0.jpg)](http://www.youtube.com/watch?v=l5Y_P8w07PY)
### ESP32 Programmieren
[![ESP 32](http://img.youtube.com/vi/pG5JEoUC2Hc/0.jpg)](http://www.youtube.com/watch?v=pG5JEoUC2Hc)
### Powershell Core auf dem Raspberry PI
[![Powershell Core](http://img.youtube.com/vi/WO0DqRpR5hs/0.jpg)](http://www.youtube.com/watch?v=WO0DqRpR5hs)


