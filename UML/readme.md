# UML mit Visual Studio Code
## Vorbereitungen
Zunächst muss das Plugin PlantUML installiert werden
- [Plant UML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)

Anschließend muss noch PlantUML und Graphviz installiert werden, am einfachsten geht dieses über Powershell-Chocolate, dazu muss eine Eingabeaufforderung als Administrator gestartet werden und folgende zwei Befehle ausgeführt werden:

```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

choco install plantuml
```

Sind alle Fragen bei der Installation mit "y" beantwortet worden, steht das Plugin zur Verfügung.
## Nutzen des Pluins
Es muss eine Datei mit dem Suffix *.wsd* erstellt werden (siehe Beispiele hier im Repositpory). Wird dann *ALT-D* gedrückt, wird das entsprechende UML Diagramm erzeugt.



