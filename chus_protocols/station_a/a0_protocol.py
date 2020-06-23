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

# Load Brands & other stuff
spec2 = importlib.util.spec_from_file_location("library.protocols.lab_stuff",
                                              "{}protocols/lab_stuff.py".format(LIBRARY_PATH))
lab_stuff = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(lab_stuff)


metadata = {
    'protocolName': 'A0',
    'author': 'Luis Lorenzo Mosquera, Victor Soroña Pombo & Ismael Castiñeira Paz',
    'source': 'Hospital Clínico Universitario de Santiago (CHUS)',
    'apiLevel': '2.0',
    'description': 'Dispense buffer in 96 x tuberack'
}


# ------------------------
# Tuberack parameters (CONSTANTS)
# ------------------------
MAX_NUM_OF_SOURCES = 96
MIN_NUM_OF_SOURCES = 4
NUM_OF_SOURCES_PER_RACK = 24


# ------------------------
# Tube physical parameters
# ------------------------
tube_type = 'falcon'                           # Selected tube for this protocol
(area, volume, vcono, hcono) = lab_stuff.tubes(tube_type)

tube_physical_description = {
    'h_cono': hcono,
    'v_cono': vcono
}


# ------------------------
# Pipette parameters
# ------------------------
air_gap_vol_ci = 1
x_offset = [0, 0]
disp_height = 0.5


# ------------------------
# Buffer specific parameters (INPUTS)
# ------------------------
buffer_name = 'Lisis'                           # Selected buffer for this protocol

(flow_rate_aspirate, flow_rate_dispense, delay, vol_well) = lab_stuff.buffer(buffer_name)
buffer = {
    'flow_rate_aspirate': flow_rate_aspirate,
    'flow_rate_dispense': flow_rate_dispense,
    'delay': delay,
    'vol_well': vol_well
}


# ------------------------
# Protocol parameters (OUTPUTS)
# ------------------------
num_destinations = 96                      # total number of destinations
volume_to_be_transfered = 300              # volume in uL to be moved from 1 source to 1 destination


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
    reagents = ctx.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '8', 'Buffer tuberack in Falcon tube')
    source_labware = reagents.wells()[0]

    # Destination (in this case 96 x tuberack of 2ml)
    rack_num = math.ceil(num_destinations / NUM_OF_SOURCES_PER_RACK) if num_destinations < MAX_NUM_OF_SOURCES else MIN_NUM_OF_SOURCES
    dest_racks = common.generate_source_table([ctx.load_labware(
        'opentrons_24_tuberack_generic_2ml_screwcap', slot,
        'source tuberack with screwcap' + str(i + 1)) for i, slot in enumerate(['5', '6', '2', '3'][:rack_num])
    ])

    destinations = dest_racks[:num_destinations]

    # ------------------
    # Protocol
    # ------------------
    if not p1000.hw_pipette['has_tip']:
        common.pick_up(p1000)

    for destination_labware in destinations:
        # Calculate pickup_height based on remaining volume and shape of container
        pickup_height, _ = common.calc_height(ctx, buffer, tube_physical_description,
                                              area, volume_to_be_transfered)
        common.move_vol_multichannel(ctx, p1000, reagent=buffer, source=source_labware, dest=destination_labware,
                                     vol=volume_to_be_transfered, air_gap_vol=air_gap_vol_ci,
                                     pickup_height=pickup_height, disp_height=disp_height,
                                     x_offset=x_offset, blow_out=True, touch_tip=True)
    # Drop pipette tip
    p1000.drop_tip()

    # Notify users
    # common.notify_finish_process()
