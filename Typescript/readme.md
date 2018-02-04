# TypeScript
## Extensions
keine Extensions notwendig
## Konfiguartion
CMDER darf nicht als Terminal verwendet werden, daher muss in den Einstellungen folgendes eingetragen werden. Ferner sollen die generierten Dateien nicht angezeigt werden!
```json
{
    "terminal.integrated.shell.windows": "cmd.exe",
    "terminal.integrated.shellArgs.windows": [],
    "files.exclude": {
        "**/*.js": { "when": "$(basename).ts"},
        "**/*.*.map": true
    },
    
}
```
Im Basisverzeichnis muss sich die *tsconfig.json* befinden!
```json
{
    "compilerOptions": {
        "target": "es5",
        "module": "commonjs",
        "sourceMap": true
    }
}
```
Anschließend kann die Build Aufgabe ausgeführt werden.
