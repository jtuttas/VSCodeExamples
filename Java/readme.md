# Java Beispiel
## Extensions
- [Java Extension Pack (inkludiert die beiden unteren Extensions)](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)
- [Debugger for JAVA](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)
- [Language Support for Java](https://marketplace.visualstudio.com/items?itemName=redhat.java)
## Hotkeys
Mit *F5* wird der Debugger gestartet. Mit *STRG-F5* wird lediglich das Programm ausgeführt.
## Konfiguration
### Einstellungen
Hier muss der Pfad zur Java-Home auf das JDK richtig eingestellt werden.
```js
{
     // JAVA Plugin
     "java.home": "C:\\Program Files\\Java\\jdk1.8.0_131",
}
```
### Build Task Erzeugen
Die Java-Dateien müssen mit Hilfe des Java-Compilers übersetzt werden, dazu wird folgender Build Task (*tasks,json*) angelegt:
```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Compile all Java Files",
            "command": "java",
            "windows": {
                "command": "C:\\Program Files\\Java\\jdk1.8.0_131\\bin\\javac.exe"
            },
            "args": [
                "*.java"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "never",
                "focus": false
            },
           
        }
    ]
} 
```
Dabei ist darauf zu achten, dass *command* den Java-Compiler *javac.exe* korrekt startet. Dieser Build Task kann gestartet werden mittels *STRG+SHIFT+B*.

### Automatisches Ausführen des BuildTasks
Um das Programm zu starten kann dann die normale *launch.json* verwendet werden. Wobei über das Attribut *classPaths* auch JAR Files mit angegeben werden können (wie in unterem Beispiel z.B. ein MySQL Connector). Damit der Build Task automatisch gestartet wird, bevor der Debugger startet muss in *preLaunchTask* der Name des Tasks angegeben werden. In *mainClass* muss der Name der Klasse eingetragen werden, die die main-Methode enthält.
```
{

    "version": "0.2.0",
    "configurations": [       
       {
            "type": "java",
            "name": "Debug (Launch)-Main1",
            "request": "launch",
            "cwd": "${workspaceFolder}",
            "console": "internalConsole",
            "stopOnEntry": false,
            "mainClass": "Main1",
            "preLaunchTask": "Compile all Java Files",
            "classPaths": [
                ".",
                "${workspaceFolder}\\mysql-connector-java-5.1.46.jar"
            ],
            "args": ""
        }  
    ]
}
``` 

Anschließend kann via *F5* das Programm kompiliert und gestartet werden!

## Tipps
Damit die kompilierten class Dateien nicht im Editor erscheinen, können diese ausgebelden werden über folgenden Eintrag in den Einstellungen:
```
     "files.exclude": {
         "*.class":true
     },

```


Kommt es zu einem Fehler beim Starten des Debuggers *Build failed, do you whant to continue?* liegt ein Compilerfehler vor, welcher genau steht in der Console unter *Ausgabe/Debugger for Java*.


## Snippets
```js
{
    "Main Class": {
		"prefix": "main",
		"body": [
			"public class $1 {",
			"public static void main(String[] args) {",
			"$2",
			"}",
			"}"
		],
		"description": "Main Class"
	},
	"Println to console": {
		"prefix": "sopl",
		"body": [
			"System.out.println(\"$1\");"
		],
		"description": "System.out.println()"
	},
	"Print to console": {
		"prefix": "sop",
		"body": [
			"System.out.print(\"$1\");"
		],
		"description": "System.out.print()"
    }
}
```
