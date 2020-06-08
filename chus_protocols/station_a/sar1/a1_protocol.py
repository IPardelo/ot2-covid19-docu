# -*- coding: utf-8 -*-

import math
import importlib
from opentrons import protocol_api

LIBRARY_PATH = '/root/ot2-covid19/library/'

# Load library
spec = importlib.util.spec_from_file_location("library.protocols.common_functions",
                                              "{}protocols/common_functions.py".format(LIBRARY_PATH))
common = importlib.util.module_from_spec(spec)
spec.loader.exec_module(common)


metadata = {
    'protocolName': 'A1',
    'author': 'Luis Lorenzo Mosquera, Victor Soroña Pombo & Ismael Castiñeira Paz',
    'source': 'Hospital Clínico Universitario de Santiago (CHUS)',
    'apiLevel': '2.0',
    'description': 'Dispense samples from 96 x tube rack in 96 Well Plate'
}

# ------------------------
# Protocol parameters
# ------------------------
NUM_SAMPLES = 96
air_gap_vol_sample = 5
volume_sample = 300
diameter_sample = 8.25
volume_cone = 50 # TODO
area_section_sample = (math.pi * diameter_sample**2) / 4
x_offset = [0,0]

sample = {
    'name': 'Samples',
    'flow_rate_aspirate': 1,
    'flow_rate_dispense': 1,
    'rinse': False,
    'delay': 0,
    'reagent_reservoir_volume': 700 * 24,
    'num_wells': 24,
    'h_cono': 4,
    'v_cono': 4 * area_section_sample * diameter_sample * 0.5 / 3,
    'vol_well_original': 700,
    'vol_well': 700,
    'unused': [],
    'col': 0,
    'vol_well': 0
}


# ----------------------------
# Main
# ----------------------------
def run(ctx: protocol_api.ProtocolContext):
    # ------------------------
    # Load LabWare
    # ------------------------
    # Tip racks
    tips = [ctx.load_labware('opentrons_96_filtertiprack_1000ul', slot, '1000µl filter tiprack') for slot in ['11']]

    # Pipette
    p1000 = ctx.load_instrument('p1000_single_gen2', 'right', tip_racks=tips)

    # Source (in this case falcon 50ml of buffer)
    rack_num = math.ceil(NUM_SAMPLES / 24) if NUM_SAMPLES < 96 else 4
    source_racks = [ctx.load_labware(
        'opentrons_24_tuberack_generic_2ml_screwcap', slot,
        'source tuberack with screwcap' + str(i + 1)) for i, slot in enumerate(['5', '6', '2', '3'][:rack_num])
    ]
    sample_sources_full = common.generate_source_table(source_racks)
    sample_sources = sample_sources_full[:NUM_SAMPLES]

    # Destination (in this case 96 well plate)
    dest_plate = ctx.load_labware('abgene_96_wellplate_800ul', '9', 'ABGENE 96 Well Plate 800 µL')
    destinations = dest_plate.wells()[:NUM_SAMPLES]

    # ------------------
    # Protocol
    # ------------------
    if not p1000.hw_pipette['has_tip']:
        common.pick_up(p1000)

    for s, d in zip(sample_sources, destinations):
        if not p1000.hw_pipette['has_tip']:
            common.pick_up(p1000)

        # Calculate pickup_height based on remaining volume and shape of container
        common.move_vol_multichannel(p1000, reagent=sample, source=s, dest=d,
                              vol=volume_sample, air_gap_vol=air_gap_vol_sample, x_offset=x_offset,
                              pickup_height=1, rinse=sample.get('rinse'), disp_height=-10,
                              blow_out=True, touch_tip=True)
        # Drop pipette tip
        p1000.drop_tip()

    # Notify users
    # common.notify_finish_process()
