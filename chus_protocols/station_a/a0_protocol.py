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
    'protocolName': 'A0',
    'author': 'Luis Lorenzo Mosquera, Victor Soroña Pombo & Ismael Castiñeira Paz',
    'source': 'Hospital Clínico Universitario de Santiago (CHUS)',
    'apiLevel': '2.0',
    'description': 'Dispense buffer in 96 x tuberack'
}

# ------------------------
# Protocol parameters
# ------------------------
NUM_DESTINATIONS = 96

air_gap_vol_ci = 1

volume_control = 300
height_control = 0.5
x_offset = [0, 0]

diameter_falcon = 27
h_cone_falcon = 17.4

falcon_cross_section_area = math.pi * diameter_falcon**2 / 4
v_cone_falcon = 1 / 3*h_cone_falcon * falcon_cross_section_area

buffer = {
    'name': 'TNA+Beads+Isopropanol',
    'flow_rate_aspirate': 1,
    'flow_rate_dispense': 1,
    'rinse': False,
    'delay': 3,
    'reagent_reservoir_volume': 12000,
    'num_wells': 1,
    'h_cono': (v_cone_falcon * 3 / falcon_cross_section_area),
    'v_cono': v_cone_falcon,
    'vol_well_original': 12000,
    'vol_well': 12000,
    'unused': [],
    'col': 0
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
    reagents = ctx.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '8', 'Lysis buffer tuberack in Falcon tube')
    buffer['reagent_reservoir'] = reagents.wells()[0]

    # Destination (in this case 96 x tuberack of 2ml)
    rack_num = math.ceil(NUM_DESTINATIONS / 24) if NUM_DESTINATIONS < 96 else 4
    dest_racks = [ctx.load_labware(
        'opentrons_24_tuberack_generic_2ml_screwcap', slot,
        'source tuberack with screwcap' + str(i + 1)) for i, slot in enumerate(['5', '6', '2', '3'][:rack_num])
    ]
    dest_racks = common.generate_source_table(dest_racks)
    destinations = dest_racks[:NUM_DESTINATIONS]

    # ------------------
    # Protocol
    # ------------------
    if not p1000.hw_pipette['has_tip']:
        common.pick_up(p1000)

    for d in destinations:
        # Calculate pickup_height based on remaining volume and shape of container
        pickup_height, _ = common.calc_height(ctx, buffer, falcon_cross_section_area, volume_control)
        common.move_vol_multichannel(ctx, p1000, reagent=buffer, source=buffer.get('reagent_reservoir'),
                                     dest=d, vol=volume_control, air_gap_vol=air_gap_vol_ci,
                                     x_offset=x_offset, pickup_height=pickup_height, rinse=buffer.get('rinse'),
                                     disp_height=height_control, blow_out=True, touch_tip=True)
    # Drop pipette tip
    p1000.drop_tip()

    # Notify users
    # common.notify_finish_process()
