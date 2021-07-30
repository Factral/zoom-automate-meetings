# Automatiza tus reuniones de zoom

Este script de python permite ingresar automaticamente a las reuniones programadas de zoom configurado mediante un archivo csv
* **Importante**: Solo funciona para windows

## Instalacion

#### 1. Tener instalado [python](https://www.python.org/downloads/) y [zoom](https://zoom.us/download) en el equipo  
#### 2. Descargar la [ultima version del codigo](https://github.com/Factral/zoom-automate-meetings/releases)
#### 3. Instalar los requerimientos en la terminal: `pip install -r requirements.txt`

## Uso

#### 1. Edita el archivo csv para programar tus propias reuniones, toma este formato como referencia
```
DiaDeLaSemana,HoraEn24H,IDreunion,Contraseña,Duracion(En minutos),comentario
1,08:00,123456789,347372,120,Seminario web de ejemplo
4,20:00,123456789,432002,60, Asamblea de ejemplo
```
* `DiaDeLaSemana` puede tener cualquier valor del 1 al 7, representando cada número un día de la semana a partir del lunes.
* NO elimines la primera linea del archivo csv, si no el programa no funcionara correctamente

#### 2. Ejecuta el archivo [ZoomBot.bat]() 
* **Important**: Por defecto el archivo bat tiene la ruta al archivo csv del proyecto, pero si es necesario se puede editar para enlazar a otro csv


## Contribuir
 Cualquier [contribucion](https://github.com/Factral/zoom-automate-meetings/pulls) sobre el codigo es de mucha ayuda, o para algun error, abre un [tema](https://github.com/Factral/zoom-automate-meetings/issues)