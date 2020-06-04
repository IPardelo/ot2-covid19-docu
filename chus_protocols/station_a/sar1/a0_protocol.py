import math
from opentrons import protocol_api


import sys
sys.path.append('/home/luis/Escritorio/ot2-covid19/ot2/library')
from protocols.common_functions import pick_up, calc_height, move_vol_multichannel

metadata = {
    'protocolName': 'Station A Template version for OMEGA type reactives',
    'author': 'Aitor Gastaminza, Alex Gasulla & José Luis Villanueva (Hospital Clinic Barcelona)',
    'source': 'Hospital Clínic Barcelona',
    'apiLevel': '2.0',
    'description': 'Protocol for sample setup (A) for OMEGA protocol'
}

# ------------------------
# Protocol parameters
# ------------------------
NUM_SAMPLES = 47

air_gap_vol_ci = 2
air_gap_vol_sample = 5

TNA_VOLUME = 240
ISO_VOLUME = 280
BEADS_VOLUME = 10

volume_control = TNA_VOLUME + ISO_VOLUME + BEADS_VOLUME
volume_sample = 200
height_control = 0.5
x_offset = [0, 0]

diameter_sample = 8.25
volume_cone = 50

diameter_falcon = 27
h_cone_falcon = 17.4

area_section_sample = (math.pi * diameter_sample**2) / 4
falcon_cross_section_area = math.pi * diameter_falcon**2 / 4
v_cone_falcon = 1 / 3*h_cone_falcon * falcon_cross_section_area

buffer = {
    'name': 'TNA+Beads+Isopropanol',
    'flow_rate_aspirate': 1,
    'flow_rate_dispense': 1,
    'rinse': False,
    'delay': 0,
    'reagent_reservoir_volume': 50000,
    'num_wells': 1,
    'h_cono': (v_cone_falcon * 3 / falcon_cross_section_area),
    'v_fondo': v_cone_falcon,
    'vol_well_original': 50000,
    'vol_well': 50000,
    'unused': [],
    'col': 0,
    'vol_well': 0
}

samples = {
    'name': 'Samples',
    'flow_rate_aspirate': 1,
    'flow_rate_dispense': 1,
    'rinse': False,
    'delay': 0,
    'reagent_reservoir_volume': 700 * 24,
    'num_wells': 24,
    'h_cono': 4,
    'v_fondo': 4 * area_section_sample * diameter_sample * 0.5 / 3,
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
    # Source
    if NUM_SAMPLES < 96:
        rack_num = math.ceil(NUM_SAMPLES / 24)
        samples_last_rack = NUM_SAMPLES - rack_num * 24
    else:
        rack_num = 4
    source_racks = [ctx.load_labware(
        'opentrons_24_tuberack_generic_2ml_screwcap', slot,
        # FIXME rack enumaate
        'source tuberack with screwcap' + str(i + 1)) for i, slot in enumerate(['4', '1', '6', '3'][:rack_num])
    ]

    # Destination TODO: CHANGE
    dest_plate = ctx.load_labware(
        'abgene_96_wellplate_800ul', '5',
        'ABGENE 96 Well Plate 800 µL')

    # Tip racks
    tips = [ctx.load_labware('opentrons_96_filtertiprack_1000ul', slot, '1000µl filter tiprack') for slot in ['10']]

    reagents = ctx.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '7', 'Lysis buffer tuberack in Falcon tube')

    # Pipette
    p1000 = ctx.load_instrument('p1000_single_gen2', 'right', tip_racks=tips)

    # LabWare source & destination
    buffer['reagent_reservoir'] = reagents.wells()[0]
    destinations = dest_plate.wells()[:NUM_SAMPLES]

    # ------------------
    # Protocol
    # ------------------
    if not p1000.hw_pipette['has_tip']:
        pick_up(p1000)

    pickup_height, _ = calc_height(buffer, falcon_cross_section_area, volume_control)

    for d in destinations:
        # Calculate pickup_height based on remaining volume and shape of container
        pickup_height, _ = calc_height(buffer, falcon_cross_section_area, volume_control)
        move_vol_multichannel(p1000, reagent=buffer, source=buffer.get('reagent_reservoir'),
                              dest=d, vol=volume_control, air_gap_vol=air_gap_vol_ci,
                              x_offset=x_offset, pickup_height=pickup_height, rinse=buffer.get('rinse'),
                              disp_height=height_control, blow_out=True, touch_tip=True)
