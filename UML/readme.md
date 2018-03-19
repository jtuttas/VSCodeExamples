# UML mit Visual Studio Code
## Vorbereitungen
### Externen Server benutzen
Am einfachsten man benutzt einen Externen PlantUML Server, dazu muss folgendes in den Benutzereinstellungen geändert werden:
```
"plantuml.render": "PlantUMLServer",
"plantuml.server": "http://www.plantuml.com/plantuml",
```
### Lokale Instllation
Zunächst muss das Plugin PlantUML installiert werden
- [Plant UML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)

Anschließend muss noch PlantUML und Graphviz installiert werden, am einfachsten geht dieses über Powershell-Chocolate, dazu muss eine Eingabeaufforderung als Administrator gestartet werden und folgende zwei Befehle ausgeführt werden:

```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

choco install plantuml
```

Sind alle Fragen bei der Installation mit "y" beantwortet worden, steht das Plugin zur Verfügung.
## Nutzen des Plugins
Es muss eine Datei mit dem Suffix *.wsd* erstellt werden (siehe Beispiele hier im Repositpory). Wird dann *ALT-D* gedrückt, wird das entsprechende UML Diagramm erzeugt.
## Meine Snippets
Hier noch meine Snippets:
```json
{
	"Basic UseCase": {
		"prefix": "bspUseCase",
		"body": [
			"@startuml",
			"title Basic UseCase",
			"left to right direction ",
			":Main Admin: as Admin",
			"User <|- Admin",
			"rectangle CAS <<extrenal>>",
			"rectangle System {",
			"User --- (Ein UseCase)",
			"(Ein UseCase) --> CAS : delegate",
			"(special Usecase) -|> (Ein UseCase)",
			"(Ein UseCase) .> (Included UserCase):<<include>>",
			"(Extended UseCasse) ..> (Ein UseCase):<<extends>>",
			"}",
			"@enduml"
		],
		"description": "draw a basic UseCase"
	},
	"Basic Activity": {
		"prefix": "bspActivity",
		"body": [
			"@startuml",
			"|Actor1|",
			"start",
			":Eine Activity;",
			"note left",
			"This note is on several",
			"//lines// and can",
			"contain <b>HTML</b>",
			"====",
			"* Calling the method \"\"foo()\"\" is prohibited",
			"end note",
			"|#AntiqueWhite|Actor2|",
			":Eine weitere Aktivity;",
			"if () then (yes)",
			":true Activity;",
			"else (no)",
			":false Activity;",
			"endif",
			"|Actor1|",
			"fork",
			":parallel1;",
			"end",
			"fork again",
			":parallel2;",
			"fork again",
			":parallel3;",
			"end fork",
			"|Actor2|",
			":send Signal>",
			"end",
			"|Actor3|",
			":receive Message<",
			":do Something;",
			":send Message>",
			"stop",
			"@enduml"
		],
		"description": "draw a basic ActivityDiagram with all elements"
	},
	"Basic Sequenz": {
		"prefix": "bspSequenz",
		"body": [
			"@startuml",
			"actor User",
			"User -> client: Start Application",
			"activate User",
			"client -> Server: GET-Request",
			"activate Server",
			"create Obj",
			"Server -> Obj: new()",
			"Server -> Server: test()",
			"alt successful case",
			"Server -> client: sucess    ",
			"else some kind of failure",
			"Server -> client: failed",
			"end    ",
			"deactivate Server",
			"Server ->> Obj:kill",
			"destroy Obj",
			"client <-- Server: XML Responce",
			"client ->> Server: async Call",
			"deactivate User",
			"@enduml"
		],
		"description": "draw a basic SequenzDiagram with all elements"
	},
	"Basic State": {
		"prefix": "bspState",
		"body": [
			"@startuml",
			"[*] --> Zustand1",
			"Zustand1 --> [*]",
			"Zustand1 : entry: Entry Aktion",
			"Zustand1 : do: Do Aktion",
			"Zustand1 : exit: Exit Aktion",
			"state Zustand5 <<choice>>",
			"Zustand1 ---> Zustand5 ",
			"Zustand5 --> Zustand1: true",
			"Zustand5 ---> Zustand3: false",
			"Zustand3 -> Zustand1",
			"Zustand1 -> Zustand2: [Bedingung]",
			"Zustand2 -> Zustand2: [Bedingung]",
			"Zustand2 --> [*]",
			"@enduml"
		],
		"description": "draw a basic StateDiagram with all elements"
	},
	"Basic Class": {
		"prefix": "bspClass",
		"body": [
			"@startuml",
			"abstract class Eltern <<abstract>> {",
			"+{static} PUBLIC_STATIC_VARIABLE:int",
			"- privateVariable:String",
			"~ packagePrivateVariable:String",
			"# protectedVariable:String",
			"~packagePrivateMethod():int",
			"+{abstract} abstractMethod(int param):int",
			"+{static} staticMethod(int param):int",
			"}",
			"class Kind {",
			"+ Kind(int)",
			"}",
			"class Assoziation {",
			"}",
			"class Assoziation2 {",
			"}",
			"class ImplementInterface {",
			"+ InterfaceMethode():void",
			"}",
			"class Interface <<Interface>> {",
			"}",
			"Eltern <|-- Kind",
			"Kind \"0..1\" o-- \"n\" Assoziation2",
			"Kind *- Assoziation",
			"Kind .-> Interface: <<use>>",
			"ImplementInterface .-|> Interface",
			"@enduml",
		],
		"description": "draw a basic ClassDiagram with all elements"
	},
}
```



