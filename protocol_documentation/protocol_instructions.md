# Instrucciones para ejecutar los protocolos y manejo del programa
> por Luis Lorenzo Mosquera, Victor Soroña Pombo & Ismael Castiñeira Paz 
<pre>
      @@@@@    @@@@@                                                                               
    @@@@          @@@@                                                         
   @@@      @@      @@@    @@@@@@   @@@@@
  @@@      @@@@      @@@   @@@@@@  &amp;@&apos; &apos;@@
  @@     @@@@@@@@    &amp;@@     @@         @@
  @@    .@@@    @    #@@     @@        @@
  @@@    @      @    @@@     @@       @@
   @@@    @@..@@    @@@      @@      @@
    @@@@          @@@@       @@     @@@@@&amp;
      @@@@@@@@@@@@@@         ##    &amp;@@@@@#
         (@@@@@@.
</pre>

:warning: **IMPORTANTÍSIMO:** ANTES DE CARGAR NINGÚN PROTOCOLO ES IMPORTANTE TENER EL LABWARE COLOCADO EN SU CORRESPONDIENTE LUGAR. Para saber más consulta [los protocolos](chus_protocols.md) :warning:


# Cómo cargar un protocolo
Una vez [conectado a un robot](#conexion) nos dirigimos a la pestaña *PROTOCOL* y seleccionamos, luego de pulsar el boton *OPEN*, el archivo.

El robot hará una simulación al cargar el archivo y si todo sale bien, estará todo listo para poder iniciar el protocolo. Con la simulación terminada, vamos a pa pestaña *RUN* y pulsamos *START RUN*.  

> Todos los pasos en el siguiente vídeo:

![cargar_protocolo](img/protocol_instructions/cargar_protocolo.gif)


# Protocolo A

## Protocolo A0
```py
# ------------------------
# Tube physical parameters
# ------------------------
tube_type = 'falcon'                           # Selected tube for this protocol
```

```py
# ------------------------
# Buffer specific parameters (INPUTS)
# ------------------------
buffer_name = 'Lisis'                           # Selected buffer for this protocol
```

```py
# ------------------------
# Protocol parameters (OUTPUTS)
# ------------------------
num_destinations = 96                           # Number of slots for the destination rack
volume_to_be_moved = 300                        # Volume in µL to be moved from 1 source to 1 destination
```
## Protocolo A1 (SAR1)

```
TODO
```

## Protocolo A1 (SAR2)

```
TODO
```

## Protocolo A2

```
TODO
```


# Protocolo B

```
TODO
```

# Protocolo C

```
TODO
```

# Otros

<a id="conexion"></a>

## Cómo saber si estoy conectado
En la siguiente imagen podemos ver que al robot '*SAR1*' estamos conectados y por consiguiente al '*SAR2*' no.  
![ejemplo_conexion](img/protocol_instructions/ejemplo_conexion.png)
* **Cómo puedo conectarme a un robot?**  
Para conectarme a un robot debes hacer click en el *botón de activación* (![toggle_button](img/protocol_instructions/toggle_button_off.png)) y pasará a estado activado (![toggle_button](img/protocol_instructions/toggle_button_on.png)).

## **Aviso de protocolo cargado**
Este aviso salta si el robot ya tiene un protocolo cargado y estamos intentado cargarle otro. **No es un mensaje de error**, sólo es una advertencia, para continuar cargando el protocolo pulsamos el botón *CONTINUE*.  
![cargar_protocolo](img/protocol_instructions/warning_protocolo.png)

## Apagar/Encender luces

Una vez [conectado a un robot](#conexion) nos quedamos en la pestaña *ROBOT* y bajamos hasta el *botón de activación* "Lights".  

> Todos los pasos en el siguiente vídeo:

![luces](img/protocol_instructions/luces.gif)

> Demostración:

![luces_gif](img/protocol_instructions/luces_outside.gif)