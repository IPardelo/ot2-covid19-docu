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

## Protocolo A

### Paso 1: A0
Con la pipeta [p1000](labware.md/#puntas1000) cojemos cantidades de 300µl de *buffer* del recipiente llamado [**FALCON**](labware.md/#falcon) y las distribuímos por todos los pocillos de los [racks de 24](labware.md/#rack24).  
![a0](img/a0.gif)

### Paso 2-1: A1 (SAR1)

Luego del paso anterior, las muestras inactivadas son introducidas en el robot manualmente.
Con la pipeta [p1000](labware.md/#puntas1000) cojemos cantidades de XXXml de cada pocillo del [rack de 24](labware.md/#rack24) y se coloca en la coordenada correspondiente en el [deepwell](labware.md/#deepwell2ml). De cada instrucción se coje una punta, se lleva a cabo la acción y se tira.  
![a1](img/a1-1.gif)

### Paso 2-2: A1 (SAR2)

Luego del paso anterior, las muestras inactivadas son introducidas en el robot manualmente.
Con la pipeta [p300](labware.md/#puntas300) cojemos cantidades de XXXml de cada pocillo del [rack de 24](labware.md/#rack24) y se deposita **N** veces en un pocillo en concreto.
> Ej: Los 5 primeros pocillos del rack van al deepwell A1, los 5 siguientes va a B1, etc.  

![a1](img/a1-2.gif)

### Paso 3: A2

Con la pipeta de [p1000](labware.md/#puntas1000) cojemos cantidades de XXXml de cada pocillo del [rack de 24 de aluminio](labware.md/#rack24_alum) y lo depositamos en su correspondiente coordenada del [rack de 24](labware.md/#rack24). De cada instrucción se coje una punta, se lleva a cabo la acción y se tira.  
![a2](img/a2.gif)

***

## Protocolo B

***

## Protocolo C
Con la pipeta de [p20](labware.md/#puntas20) cojemos cantidades de XXXml de un pocillo del [rack de 24 de aluminio](labware.md/#rack24_alum) y lo depositamos en **N** coordenadas del [rack de 96 de aluminio](labware.md/#rack96_alum).
> Ej: El contenido del primer pocillo (A1) del rack de aluminio se reparte en las 6 primeras columnas del rack de 96 de aluminio y el contenido del segundo (B1) entre las otras 6.

![a2](img/c0.gif)