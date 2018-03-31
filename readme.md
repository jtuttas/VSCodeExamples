# Konfigurationen f. Visual Studio Code
Hier sind einige beispielhafte Konfigurationen von Visual Studio Code f. diverse Programmiersprachen 

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
okazuki.okazukiplantuml
PeterJausovec.vscode-docker
platformio.platformio-ide
rafaelmaiolla.remote-vscode
ritwickdey.LiveServer
shakram02.bash-beautify
Shan.code-settings-sync
tht13.python
vsciot-vscode.azure-iot-toolkit
vscjava.vscode-java-debug
vscjava.vscode-java-pack
vscjava.vscode-java-test
wcwhitehead.bootstrap-3-snippets
webfreak.debug
Zignd.html-css-class-completion
```
## Tips
### Azure
Wird die Azure CLI verwendet, so muss diese erst angemeldet werden, dieses geschieht über den Befehl *az login* anshcließend muss auf der angezeigten Webseite der angezeigte Code eingegeben werden.
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


