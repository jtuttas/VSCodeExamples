# Java Maven Projekt mit JUNIT4 Test
## Voraussetzungen
- Es muss Maven installiert sein, dazu ist das Maven Paket herunter zu laden und die PATH Variable zu setzten, so dass *mvn.exe* gestartet werden kann.

## Installation
Mittels des Befehls..
```
mvn archetype:generate -DartifactId=Projektname -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false -DgroupId=paketName
```
Wird ein neues Projekt angelegt. *Projektname* und *PaketName* müssen dazu auf sinnvolle Namen geändert werden.

Die pom.xml muss geändert werden, so dass JUNIT4 geladen wird.
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>mmbbs</groupId>
  <artifactId>JavaMaven</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>JavaMaven</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.12</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```
## Ergebnis
![Junit4](junit.gif "Unit Tests")

## Tips
Kommt es zu einem Fehler beim Starten des Debuggers *Build failed, do you whant to continue?* empfiehlt es sich das Verzeichnis WorkspaceStorage zu löschen. Dieses befindet sich..

- Windows : ```%APPDATA%\Code[ - Variant]\User\workspaceStorage\```
- MacOS : ```$HOME/Library/Application Support/Code[ - Variant]/User/workspaceStorage/```
- Linux : ```$HOME/.config/Code[ - Variant]/User/workspaceStorage/```

Weitere Hinweise auf den Fehler lassen sich auch finden in der Console unter *Ausgabe/Debugger for Java*.

