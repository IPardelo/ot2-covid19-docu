# Protocolos Opentrons CHUS y CHUAC
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

# [Protocolo A](img/labware_schema/protocol_a.png)

## Paso 1: A0
Con la pipeta [p1000](labware.md/#puntas1000) cojemos cantidades de 300µl de *buffer* del recipiente llamado [**FALCON**](labware.md/#falcon) y las distribuímos por todos los pocillos de los [racks de 24](labware.md/#rack24).  
![a0](img/a0.gif)

## Paso 2-1: A1 (SAR1)

Luego del paso anterior, las muestras inactivadas son introducidas en el robot manualmente.
Con la pipeta [p1000](labware.md/#puntas1000) cojemos cantidades de XXXml de cada pocillo del [rack de 24](labware.md/#rack24) y se coloca en la coordenada correspondiente en el [deepwell  de 96](labware.md/#deepwell2ml). De cada instrucción se coje una punta, se lleva a cabo la acción y se tira.  
![a1](img/a1-1.gif)

## Paso 2-2: A1 (SAR2)

Luego del paso anterior, las muestras inactivadas son introducidas en el robot manualmente.
Con la pipeta [p300](labware.md/#puntas300) cojemos cantidades de XXXml de cada pocillo del [rack de 24](labware.md/#rack24) y se deposita **N** veces en un pocillo en concreto.
> Ej: Los 5 primeros pocillos del *rack de 24* van al *deepwell* A1, los 5 siguientes al B1, etc.  

![a1](img/a1-2.gif)

## Paso 3: A2

Con la pipeta [p1000](labware.md/#puntas1000) cojemos cantidades de XXXml de cada pocillo del [rack de 24 de aluminio](labware.md/#rack24_alum) y lo depositamos en su correspondiente coordenada del [rack de 24](labware.md/#rack24). De cada instrucción se coje una punta, se lleva a cabo la acción y se tira.  
![a2](img/a2.gif)


# [Protocolo B](img/labware_schema/protocol_b.png)

~~~
TODO
~~~

# [Protocolo C](img/labware_schema/protocol_c.png)

## Paso 0: pcr_full_setup

Con la pipeta de [p20](labware.md/#puntas20) cojemos cantidades de 20ml de un pocillo del [rack de 24 de aluminio](labware.md/#rack24_alum) y lo depositamos en los pocillos del [rack de 96 de aluminio](labware.md/#rack96_alum).  
![c0-0](img/c0-0.gif)

Luego, con la pipeta [p20 (8 canales)](labware.md/#puntas20) cojemos cantidades de 20ml de los pocillos del [deepwell de 96](labware.md/#deepwell2ml) y lo depositamos en los pocillos del [rack de 96 de aluminio](labware.md/#rack96_alum).  
![c0-1](img/c0-1.gif)

## Paso 1: pcr_setup
Con la pipeta de [p20](labware.md/#puntas20) cojemos cantidades de 20ml de un pocillo del [rack de 24 de aluminio](labware.md/#rack24_alum) y lo depositamos en **N** coordenadas del [rack de 96 de aluminio](labware.md/#rack96_alum).
> Ej: El contenido del primer pocillo (A1) del *rack de 24 de aluminio* se reparte en las 6 primeras columnas del *rack de 96 de aluminio* y el contenido del segundo (B1) entre 6 restantes.

![c0](img/c1.gif)


## Paso 2: rna_teca
Con la pipeta de [p20](labware.md/#puntas20) cojemos dos veces 20µl de un pocillo del [deepwell de 96](labware.md/#deepwell2ml) y lo depositamos en UN pocillo del [rack de 24](labware.md/#rack24) (deben contener 40µl cada pocillo).  
> Ej: Del pocillo A1 del *deepwell* deben salir 40µl para el pocillo A1 del *rack de 24*, es decir, coger dos veces 20µl.  

![c1](img/c2.gif)