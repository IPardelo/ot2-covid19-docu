# Instrucciones para ejecutar los protocolos A
> por Luis Lorenzo Mosquera, Victor Soroña Pombo & Ismael Castiñeira Paz  
<pre>
      @@@@@    @@@@@
    @@@@          @@@@
   @@@      @@      @@@    @@@@@@   @@@@@
  @@@      @@@@      @@@   @@@@@@  @@@ @@@
  @@     @@@@@@@@    @@@     @@         @@
  @@    @@@    @@    @@@     @@        @@
  @@@    @      @    @@@     @@       @@
   @@@    @@@@@@    @@@      @@      @@
    @@@@          @@@@       @@     @@@@@@
      @@@@@@@@@@@@@@         @@    @@@@@@#
         @@@@@@@@
</pre>

:warning: **IMPORTANTÍSIMO:** ANTES DE CARGAR NINGÚN PROTOCOLO ES IMPORTANTE TENER EL LABWARE COLOCADO EN SU CORRESPONDIENTE LUGAR. Pincha en el título de cada protocolo para ver que labware necesita :warning:

## Protocolo [**Dispensar buffer**](img/labware_schema/protocol_a_dispensarbuffer.jpg)

Con la pipeta [P1000](labware.md/#puntas1000) cojemos cantidades de X µl de *buffer* del recipiente llamado [**FALCON**](labware.md/#falcon) y las distribuímos por todos los pocillos de los [racks de 24](labware.md/#rack24).  

![a0](img/protocol_example/a0.gif)

```py
# ------------------------
# Buffer specific parameters (INPUTS)
# ------------------------
buffer_name = 'Lisis'                           # Selected buffer for this protocol
tube_type_source = 'falcon'                     # Selected buffer tube for this protocol
```

> **1er parámetro:** establece el buffer a utilizar. ***Ej: Lisis, UXL Longwood, Roche Cobas, Roche Bleau***  
**2º parámetro:** tipo de tubo de origen (tubo en el que va a ir el buffer).

```py
# ------------------------
# Protocol parameters (OUTPUTS)
# ------------------------
num_destinations = 96                           # number of slots for the destination rack
volume_to_be_moved = 300                        # volume in uL to be moved from 1 source to 1 destination
tube_type_dest = 'eppendorf'                    # Selected destination tube for this protocol
```

> **1er parámetro:** establece el número total de tubos a atender (como destino del buffer).  
**2º parámetro:** cantidad en µL a dispensar de buffer en los tubos.  
**3er parámetro:** tipo de tubo a usar como destino. ***Ej: eppendorf, criotubo***

## Protocolo [**Dispensar muestras deepwell**](img/labware_schema/protocol_a_dispensardeepwell.jpg)

Luego del paso anterior, las muestras inactivadas son introducidas en el robot manualmente.
Con la pipeta [P1000](labware.md/#puntas1000) cojemos cantidades de X ml de cada pocillo del [rack de 24](labware.md/#rack24) y se coloca en la coordenada correspondiente en el [deepwell  de 96](labware.md/#deepwell2ml). De cada instrucción se coje una punta, se lleva a cabo la acción y se tira.  

![a1](img/protocol_example/a1.gif)

```py
# ------------------------
# Sample specific parameters (INPUTS)
# ------------------------
buffer_name = 'Lisis'                      # Selected buffer for this protocol
num_samples = 96                           # total number of samples
tube_type_source = 'eppendorf'             # Selected source tube for this protocol
```

> **1er parámetro:** establece el buffer que contienen los tubos.  
**2º parámetro:** establece el número total de tubos a atender, es decir, los quevan a ser trasladados a la [deepwell](labware.md/#deepwell2ml).  
**3er parámetro:** tipo de tubo a usar.

```py
# ------------------------
# Protocol parameters (OUTPUTS)
# ------------------------
num_destinations = 96                      # total number of destinations
volume_to_be_transfered = 300              # volume in uL to be moved from 1 source to 1 destination
```

> **1er parámetro:** este parámetro debe llevar el mismo número que el anterior llamado ***num_samples*** ya que es el número de destinos en la [deepwell](labware.md/#deepwell2ml).  
**2º parámetro:** cantidad en µL a dispensar en cada pocillo de la [deepwell](labware.md/#deepwell2ml).

## Protocolo [**Pooling Deepwell**](img/labware_schema/protocol_a_poolingdeepwell.jpg) & [**Pooling Hamilton**](img/labware_schema/protocol_a_poolinghamilton.jpg)  

Luego del paso anterior, las muestras inactivadas son introducidas en el robot manualmente.
Con la pipeta [P300](labware.md/#puntas300) cojemos cantidades de X ml de cada pocillo del [rack de 24](labware.md/#rack24) y se deposita **N** veces en un pocillo en concreto.

La única diferencia entre las dos variantes es que en **pooling deepwell** el destino sería un *deepwell* y en **pooling hamilton** sería un rack de tubos.
> Ej: Los 5 primeros pocillos del *rack de 24* van al *deepwell* A1, los 5 siguientes al B1, etc.  

![a1](img/protocol_example/a2.gif)

```py
# ------------------------
# Sample specific parameters (INPUTS)
# ------------------------
buffer_name = 'Lisis'                        # Selected buffer for this protocol
tube_type_source = 'eppendorf'                 # Selected destination tube for this protocol                        # Selected buffer for this protocol
```

> **1er parámetro:** establece el buffer que contienen los tubos.  
**2º parámetro:** tipo de tubo de origen (tubo en el que va a ir el buffer).

```py
# ------------------------
# Protocol parameters (OUTPUTS)
# ------------------------
num_samples = 95                      # total number of destinations
volume_to_be_transfered = 300         # final volume in uL in the tube
pooling_factor = 5                    # num of destinations per source
dispense_height = -10                 # dispense height in the deepwell
```

> **1er parámetro:** número total de destinos.  
**2º parámetro:** cantidad en µL a dispensar.  
**3er parámetro:** número de origenes para un destino.  
**P. ej:** Si *pooling_factor* es igual a 4 -> `las coordenadas A1, B1, C1, D1 del rack, van al A1 del deepwell`
**4º parámetro:** altura de dispensado en el deepwell.  

## Protocolo [**Seroteca**](img/labware_schema/protocol_a_seroteca.jpg)

Con la pipeta [P1000](labware.md/#puntas1000) cojemos cantidades de X ml de cada pocillo del [rack de 24 de aluminio](labware.md/#rack24_alum) y lo depositamos en su correspondiente coordenada del [rack de 24](labware.md/#rack24). De cada instrucción se coje una punta, se lleva a cabo la acción y se tira.  

![a2](img/protocol_example/a3.gif)

```py
# ------------------------
# Sample specific parameters (INPUTS)
# ------------------------
buffer_name = 'Lisis'                           # Selected buffer for this protocol
tube_type_source = 'criotubo'                   # Selected destination tube for this protocol
```

> **1er parámetro:** establece el buffer que contienen los tubos.  
**2º parámetro:** tipo de tubo en el que se encuentran las muestras.

```py
# ------------------------
# Protocol parameters  (OUTPUTS)
# ------------------------
num_samples = 96                                # num of samples
volume_sample = 995                             # final volume of sample
tube_type_dest = 'criotubo'                     # Selected destination tube for this protocol
```

> **1er parámetro:** número de tubos a usar.  
**2º parámetro:** volumen de liquido a mover en μl.
**3er parámetro:** tipo de tubo de destino.
