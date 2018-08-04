# Konfigurationen f. Visual Studio Code
Hier sind einige beispielhafte Konfigurationen von Visual Studio Code f. diverse Programmiersprachen (siehe readme.md in den einzelnen Unterordnern).

## Extensions
Wer meine Erweiterungen installieren will, der führt einfach folgende Befehlssequenz aus (diese wurde erzeugt mittels..)
```
code --list-extensions | xargs -L 1 echo call code --install-extension
```

Hier meine Extensions zum installieren..
```
call code --install-extension abusaidm.html-snippets                                   
call code --install-extension alefragnani.Bookmarks                                    
call code --install-extension alexcvzz.vscode-sqlite                                   
call code --install-extension christian-kohler.npm-intellisense                        
call code --install-extension christian-kohler.path-intellisense                       
call code --install-extension dbaeumer.vscode-eslint                                   
call code --install-extension donjayamanne.githistory                                  
call code --install-extension donjayamanne.jquerysnippets                              
call code --install-extension DotJoshJohnson.xml                                       
call code --install-extension dracula-theme.theme-dracula                              
call code --install-extension ecmel.vscode-html-css                                    
call code --install-extension eg2.vscode-npm-script                                    
call code --install-extension felixfbecker.php-intellisense                            
call code --install-extension formulahendry.auto-close-tag                             
call code --install-extension formulahendry.azure-virtual-machine-explorer             
call code --install-extension formulahendry.code-runner                                
call code --install-extension formulahendry.vscode-mysql                               
call code --install-extension GrapeCity.gc-excelviewer                                 
call code --install-extension Gruntfuggly.todo-tree                                    
call code --install-extension humao.rest-client                                        
call code --install-extension jebbs.plantuml                                           
call code --install-extension johnpapa.Angular2                                        
call code --install-extension mongoose-os.mongoose-os-ide                              
call code --install-extension ms-azuretools.vscode-azureappservice                     
call code --install-extension ms-azuretools.vscode-azurefunctions                      
call code --install-extension ms-azuretools.vscode-cosmosdb                            
call code --install-extension MS-CEINTL.vscode-language-pack-de                        
call code --install-extension ms-python.python                                         
call code --install-extension ms-vscode.azure-account                                  
call code --install-extension ms-vscode.azurecli                                       
call code --install-extension ms-vscode.cpptools                                       
call code --install-extension ms-vscode.PowerShell                                     
call code --install-extension ms-vsliveshare.vsliveshare                               
call code --install-extension ms-vsts.team                                             
call code --install-extension msjsdiag.debugger-for-chrome                             
call code --install-extension mtxr.sqltools                                            
call code --install-extension natewallace.angular2-inline                              
call code --install-extension PeterJausovec.vscode-docker                              
call code --install-extension platformio.platformio-ide                                
call code --install-extension rafaelmaiolla.remote-vscode                              
call code --install-extension redhat.java                                              
call code --install-extension ritwickdey.LiveServer                                    
call code --install-extension shakram02.bash-beautify                                  
call code --install-extension Shan.code-settings-sync                                  
call code --install-extension streetsidesoftware.code-spell-checker                    
call code --install-extension streetsidesoftware.code-spell-checker-german             
call code --install-extension tht13.python                                             
call code --install-extension vsciot-vscode.azure-iot-toolkit                          
call code --install-extension vscjava.vscode-java-debug                                
call code --install-extension vscjava.vscode-java-pack                                 
call code --install-extension vscjava.vscode-java-test                                 
call code --install-extension vscjava.vscode-maven                                     
call code --install-extension wcwhitehead.bootstrap-3-snippets                         
call code --install-extension webfreak.debug                                           
call code --install-extension xyz.local-history                                        
call code --install-extension Zignd.html-css-class-completion
```

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


