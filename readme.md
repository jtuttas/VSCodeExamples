# Konfigurationen f. Visual Studio Code
Hier sind einige beispielhafte Konfigurationen von Visual Studio Code f. diverse Programmiersprachen (siehe readme.md in den einzelnen Unterordnern).

## Extensions
Wer meine Erweiterungen installieren will, der führt einfach folgende Befehlssequenz aus (diese wurde erzeugt mittels..)
```
code --list-extensions | xargs -L 1 echo code --install-extension
```

Hier meine Extensions zum installieren..
```
code --install-extension abusaidm.html-snippets                                   
code --install-extension alefragnani.Bookmarks                                    
code --install-extension alexcvzz.vscode-sqlite                                   
code --install-extension christian-kohler.npm-intellisense                        
code --install-extension christian-kohler.path-intellisense                       
code --install-extension dbaeumer.vscode-eslint                                   
code --install-extension donjayamanne.githistory                                  
code --install-extension donjayamanne.jquerysnippets                              
code --install-extension DotJoshJohnson.xml                                       
code --install-extension dracula-theme.theme-dracula                              
code --install-extension ecmel.vscode-html-css                                    
code --install-extension eg2.vscode-npm-script                                    
code --install-extension felixfbecker.php-intellisense                            
code --install-extension formulahendry.auto-close-tag                             
code --install-extension formulahendry.azure-virtual-machine-explorer             
code --install-extension formulahendry.code-runner                                
code --install-extension formulahendry.vscode-mysql                               
code --install-extension GrapeCity.gc-excelviewer                                 
code --install-extension Gruntfuggly.todo-tree                                    
code --install-extension humao.rest-client                                        
code --install-extension jebbs.plantuml                                           
code --install-extension johnpapa.Angular2                                        
code --install-extension mongoose-os.mongoose-os-ide                              
code --install-extension ms-azuretools.vscode-azureappservice                     
code --install-extension ms-azuretools.vscode-azurefunctions                      
code --install-extension ms-azuretools.vscode-cosmosdb                            
code --install-extension MS-CEINTL.vscode-language-pack-de                        
code --install-extension ms-python.python                                         
code --install-extension ms-vscode.azure-account                                  
code --install-extension ms-vscode.azurecli                                       
code --install-extension ms-vscode.cpptools                                       
code --install-extension ms-vscode.PowerShell                                     
code --install-extension ms-vsliveshare.vsliveshare                               
code --install-extension ms-vsts.team                                             
code --install-extension msjsdiag.debugger-for-chrome                             
code --install-extension mtxr.sqltools                                            
code --install-extension natewallace.angular2-inline                              
code --install-extension PeterJausovec.vscode-docker                              
code --install-extension platformio.platformio-ide                                
code --install-extension rafaelmaiolla.remote-vscode                              
code --install-extension redhat.java                                              
code --install-extension ritwickdey.LiveServer                                    
code --install-extension shakram02.bash-beautify                                  
code --install-extension Shan.code-settings-sync                                  
code --install-extension streetsidesoftware.code-spell-checker                    
code --install-extension streetsidesoftware.code-spell-checker-german             
code --install-extension tht13.python                                             
code --install-extension vsciot-vscode.azure-iot-toolkit                          
code --install-extension vscjava.vscode-java-debug                                
code --install-extension vscjava.vscode-java-pack                                 
code --install-extension vscjava.vscode-java-test                                 
code --install-extension vscjava.vscode-maven                                     
code --install-extension wcwhitehead.bootstrap-3-snippets                         
code --install-extension webfreak.debug                                           
code --install-extension xyz.local-history                                        
code --install-extension Zignd.html-css-class-completion                          ```
## Tipps
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


