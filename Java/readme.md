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
