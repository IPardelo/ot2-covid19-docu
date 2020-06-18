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
            'hcone': 17.4
        },
        'ependor1.5': {
            'volume': 1500,
            'diameter': 9,
            'hcone': 17
        },
        'ependor2': {
            'volume': 2000,
            'diameter': 9,
            'hcone': 0
        },
        'congelacion': {
            'volume': 2000,
            'diameter': 0,
            'hcone': 0
        },
        'f_redondo': {
            'volume': 3000,
            'diameter': 9,
            'hcone': 3
        }
    }
    volume = tubes.get(tube_tipe).get('volume')
    diameter = tubes.get(tube_tipe).get('diameter')
    hcone = tubes.get(tube_tipe).get('hcone')
    return volume, diameter, hcone

def buffer(buffer_name):
    buffer = {
        'Lisis': {
            'flow_rate_aspirate': 1,  # multiplier
            'flow_rate_dispense': 1,  # multiplier
        },
        'Roche Cobas': {
            'flow_rate_aspirate': 1,  # multiplier
            'flow_rate_dispense': 1,  # multiplier
        },
        'UXL Longwood': {
            'flow_rate_aspirate': 1,  # multiplier
            'flow_rate_dispense': 1,  # multiplier
            'delay': 1,  # delay after aspirate: to allow drops to fall before moving the pipette
        },
        'Roche Bleau': {
            'flow_rate_aspirate': 1,  # multiplier
            'flow_rate_dispense': 1,  # multiplier
            'delay': 1,  # delay after aspirate: to allow drops to fall before moving the pipette
        },
    }
    flow_rate_aspirate = buffer.get(buffer_name).get('flow_rate_aspirate')
    flow_rate_dispense = buffer.get(buffer_name).get('flow_rate_dispense')
    delay = buffer.get(buffer_name).get('delay')
    return flow_rate_aspirate, flow_rate_dispense, delay
