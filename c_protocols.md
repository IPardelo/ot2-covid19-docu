# Instrucciones para ejecutar los protocolos C
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

## Protocolos [**PCR Full Setup**](img/labware_schema/protocol_c_pcrfullsetup.jpg) - [**PCR Setup**](img/labware_schema/protocol_c_pcrsetup.jpg) - [**RNA-Teca**](img/labware_schema/protocol_c_rnateca.jpg)

```py
# ------------------------
# Protocol parameters (OUTPUTS)
# ------------------------
NUM_SAMPLES = 16                            # total number of destinations
brand_name = 'vircell'                      # commercial brand name
```

> **1er parámetro:** establece el número de destinos.  
**2º parámetro:** nombre de la marca comercial.

## Protocolo [**Fast PCR Full Setup**](img/labware_schema/protocol_c_fastpcrfullsetup.jpeg)

```py
# ------------------------
# Protocol parameters
# ------------------------
numero_muestras = 10                        # Número de muestras (sin las muestras de control)
                                            # (máximo 94 si es una mastermix, o 44 si es doble)
master_mix = 10                             # Cantidad de mastermix
arn = 5                                     # Cantidad de arn
doble_master_mix = False                    # True si doble mastermix, False si unha unica                                 

tipo_de_tubo = 'eppendorf'                  # Tipo de tubo que contiene el ARN: 'labturbo' o 'criotubo'
```

> **1er parámetro:** establece el número de muestras SIN MUESTRAS DE CONTROL.  
**2º parámetro:** cantidad de mastermix.  
**3er parámetro:** cantidad de arn.  
**4º parámetro:** parámetro que es **True** si se utilizan dos mastermix y **False** si se usa una.  
**5º parámetro:** tipo de tubo a utilizar.