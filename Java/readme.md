# Java Beispiel
## Extensions
- [Java Extension Pack (inkludiert die beiden unteren Extensions)](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)
- [Debugger for JAVA](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)
- [Language Support for Java](https://marketplace.visualstudio.com/items?itemName=redhat.java)
## Hotkeys
Mit *F5* wird der Debugger gestartet. Mit *STRG-F5* wird lediglich das Programm ausgeführt.
## Konfiguration
```js
{
     // JAVA Plugin
     "java.home": "C:\\Program Files\\Java\\jdk1.8.0_131",
}
```

Am einfachsten man fängt mit dem Projekt als Maven Projekt an. Wenn maven installiert ist, so kann einfach über folgenden Befehl die notwendigen Dateien und Ordner erstellt werden (Wobei *Projektname* und *Paketname* durch sinnvolle Worte ergänz werden soll):

```
mvn archetype:generate -DartifactId=Projektname -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false -DgroupId=Paketname
```
Ist es nicht möglich ein Maven-Projekt anzulegen, so bietet sich immer noch die Möglichkeit die Java Class Dateien durch den javac Compiler erzeugen. Hierzu muss ein Build Task erzeugt werden, z.B. wie folgt:
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
            }
        }
    ]
} 
```
Dieser Build Task kann gestartet werden mittels *STRG+SHIFT+B*.

Um das Programm zu starten kann dann die normale launch.json verwendet werden. Wobei über das Attribut classPaths auch JAR Files mit angegeben werden können (wie in unterem Beispiel z.B. ein MySQL Connector).
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
            "classPaths": [
                ".",
                "${workspaceFolder}\\mysql-connector-java-5.1.46.jar"
            ],
            "args": ""
        }       
    ]
}
``` 

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
