# PHP und HTTP
Natürlich muss ein Webserver mit PHP installiert sein!
## Extensions
- [PHP IntelliSense](https://marketplace.visualstudio.com/items?itemName=felixfbecker.php-intellisense)
- [Rest Client (von Huachao Mao)](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
## Konfiguration
Pfad zur php.exe einstellen und ggf. shared Environments konfigurieren um unterschiedliche Konfigurationen zu testen!
```js
{
      // The path to a PHP 7+ executable.
  "php.executablePath": "c:\\Users\\jtutt\\OneDrive\\bin\\xampp\\php\\php.exe",
  "rest-client.environmentVariables": {
    "$shared": {
        "version": "v1"
    },
    "local": {
        "host": "localhost",
    },
    "production": {
        "host": "service.joerg-tuttas.de",
    }
  }
}
```
