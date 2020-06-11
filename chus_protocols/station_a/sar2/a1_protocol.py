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
POOLING_FACTOR = 5
NUM_SAMPLES = 95

air_gap_vol_sample = 5
volume_sample = 300
diameter_sample = 8.25
volume_cone = 35
area_section_sample = (math.pi * diameter_sample**2) / 4
x_offset = [0, 0]

sample = {
    'name': 'Samples',
    'flow_rate_aspirate': 1,
    'flow_rate_dispense': 1,
    'rinse': False,
    'delay': 0,
    'reagent_reservoir_volume': 35 * 24,
    'num_wells': 24,
    'h_cono': 4,
    'v_cono': 4 * area_section_sample * diameter_sample * 0.5 / 3,
    'vol_well_original': 35,
    'vol_well': 35,
    'unused': [],
    'col': 0
}


# ----------------------------
# Aux functions
# ----------------------------
def split_list(l: list, n: int):
    """
    Split list in several chunks of n elements

    :param l: list to split in chunks
    :param n: number of elements per chunk

    :return: chunk list's generator

    :example of use:
    list(split_list(list(range(0,100)), 10))
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]


# ----------------------------
# Main
# ----------------------------
def run(ctx: protocol_api.ProtocolContext):
    # ------------------------
    # Load LabWare
    # ------------------------
    # Tip racks
    tips = [ctx.load_labware('opentrons_96_filtertiprack_200ul', slot, '200µl filter tiprack') for slot in ['11']]

    # Pipette
    p300 = ctx.load_instrument('p300_single_gen2', 'left', tip_racks=tips)

    # Source (in this case X opentrons 24 tube rack 2ml)
    rack_num = math.ceil(NUM_SAMPLES / 24) if NUM_SAMPLES < 96 else 4
    source_racks = [ctx.load_labware(
        'opentrons_24_tuberack_generic_2ml_screwcap', slot,
        'source tuberack with screwcap' + str(i + 1)) for i, slot in enumerate(['5', '6', '2', '3'][:rack_num])
    ]
    sample_sources_full = common.generate_source_table(source_racks)
    sample_sources = sample_sources_full[:NUM_SAMPLES]

    # Destination (in this case Xs well plate)
    dest_plate = ctx.load_labware('abgene_96_wellplate_800ul', '9', 'ABGENE 96 Well Plate 800 µL')
    destinations = dest_plate.wells()[:NUM_SAMPLES]

    # ------------------
    # Protocol
    # ------------------
    if not p300.hw_pipette['has_tip']:
        common.pick_up(p300)

    custom_sources = split_list(sample_sources, POOLING_FACTOR)

    for sources, dest in zip(custom_sources, destinations):
        for source in sources:
            if not p300.hw_pipette['has_tip']:
                common.pick_up(p300)

            # Calculate pickup_height based on remaining volume and shape of container
            common.move_vol_multichannel(ctx, p300, reagent=sample, source=source, dest=dest, vol=volume_sample / POOLING_FACTOR,
                                         air_gap_vol=air_gap_vol_sample, x_offset=x_offset, pickup_height=1.5,
                                         rinse=sample.get('rinse'), disp_height=-10, blow_out=True, touch_tip=True)
            # Drop pipette tip
            p300.drop_tip()

    # Notify users
    # common.notify_finish_process()
