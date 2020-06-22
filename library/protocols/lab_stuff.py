import math

# following volumes in ul
def brands(brand_name):
    brands = {
        'seegene': {
           'mastermix': 17,
            'arn': 8
        },
        'thermofisher': {
            'mastermix': 15,
            'arn': 10
        },
        'roche': {
            'mastermix': 10,
            'arn': 10
        },
        'vircell': {
            'mastermix': 15,
            'arn': 5
        }
    }
    mastermix = brands.get(brand_name).get('mastermix')
    arn = brands.get(brand_name).get('arn')
    return mastermix, arn

def tubes(tube_tipe):
    tubes = {
        'falcon': {
            'volume': 4000,
            'diameter': 28,
            'hcono': 14 #17.4
        },
        'ependor1.5': {
            'volume': 1500,
            'diameter': 9,
            'hcono': 19
        },
        'ependor2': {
            'volume': 2000,
            'diameter': 9,
            'hcono': 19
        },
        'criotubo': {
            'volume': 2000,
            'diameter': 8,
            'hcono': 2
        },
        'f_redondo': {
            'volume': 3000,
            'diameter': 9,
            'hcono': 3
        }
    }
    volume = tubes.get(tube_tipe).get('volume')
    diameter = tubes.get(tube_tipe).get('diameter')
    hcono = tubes.get(tube_tipe).get('hcono')
    #Calculos
    area = (math.pi * diameter**2) / 4

    if tube_tipe == 'falcon':
        vcono = 1 / 3 * hcono * area
        hcono = vcono * 3 / area
    else:
        vcono = 4 * area * diameter * 0.5 / 3
    return area, volume, vcono, hcono

def buffer(buffer_name):
    buffer = {
        'Lisis': {
            'flow_rate_aspirate': 1,  # multiplier
            'flow_rate_dispense': 1,  # multiplier
            'delay': 0,  # delay after aspirate: to allow drops to fall before moving the pipette
            'vol_well': 20000
        },
        'Roche Cobas': {
            'flow_rate_aspirate': 1,  # multiplier
            'flow_rate_dispense': 1,  # multiplier
            'delay': 0,  # delay after aspirate: to allow drops to fall before moving the pipette
            'vol_well': 20000
        },
        'UXL Longwood': {
            'flow_rate_aspirate': 1,  # multiplier
            'flow_rate_dispense': 1,  # multiplier
            'delay': 1,  # delay after aspirate: to allow drops to fall before moving the pipette
            'vol_well': 20000
        },
        'Roche Bleau': {
            'flow_rate_aspirate': 1,  # multiplier
            'flow_rate_dispense': 1,  # multiplier
            'delay': 1,  # delay after aspirate: to allow drops to fall before moving the pipette
            'vol_well': 20000
        },
    }
    flow_rate_aspirate = buffer.get(buffer_name).get('flow_rate_aspirate')
    flow_rate_dispense = buffer.get(buffer_name).get('flow_rate_dispense')
    delay = buffer.get(buffer_name).get('delay')
    vol_well = buffer.get(buffer_name).get('vol_well')
    return flow_rate_aspirate, flow_rate_dispense, delay, vol_well
