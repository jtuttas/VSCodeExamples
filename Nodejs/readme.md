# NodeJS
## Extensions
keine Extension notwendig
## Konfiguration
keine besondere Konfiguration notwendig.

Ggf. kann der Folder *node_modules* ausgeblendet werden via.
```js
{
    "files.exclude": {
        "**/.git": true,         // this is a default value

        "**/node_modules": true, // this excludes all folders 
                                 // named "node_modules" from 
                                 // the explore tree

    },
}
```