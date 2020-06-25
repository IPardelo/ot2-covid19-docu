# -*- coding: utf-8 -*-

import math
import importlib
from opentrons import protocol_api

# Load library
LIBRARY_PATH = '/root/ot2-covid19/library/'
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
    'protocolName': 'C1',
    'author': 'Luis Lorenzo Mosquera, Victor Soñora Pombo & Ismael Castiñeira Paz',
    'source': 'Hospital Clínico Universitario de Santiago (CHUS)',
    'apiLevel': '2.0',
    'description': 'PCR preparation, mix the master mix and rna sample in pcr plate'
}

# ------------------------
# Protocol parameters
# ------------------------
NUM_SAMPLES = 96
brand_name = 'seegene'

num_cols = math.ceil(NUM_SAMPLES / 8)
x_offset = [0, 0]
air_gap_vol_source = 2
diameter_sample = 8.25
area_section_sample = (math.pi * diameter_sample**2) / 4

(brand_master_mix, arn) = lab_stuff.brands(brand_name)

# following volumes in ul
master_mix = {
    'name': 'master mix',
    'flow_rate_aspirate': 1,
    'flow_rate_dispense': 1,
    'rinse': False,
    'delay': 0,
    'reagent_reservoir_volume': 1500,
    'num_wells': 1,
    'h_cono': 4,
    'v_cono': 4 * area_section_sample * diameter_sample * 0.5 / 3,
    'vol_well_original': 1500,
    'vol_well': 1500,
    'unused': [],
    'col': 0,
    'vol_well': 0
}

rna_sample = {
    'name': 'RNA samples',
    'flow_rate_aspirate': 1,
    'flow_rate_dispense': 1,
    'rinse': False,
    'delay': 0,
    'reagent_reservoir_volume': 200 * 24,
    'num_wells': 24,
    'h_cono': 4,
    'v_cono': 4 * area_section_sample * diameter_sample * 0.5 / 3,
    'vol_well_original': 200,
    'vol_well': 200,
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
    tips = [ctx.load_labware('opentrons_96_filtertiprack_20ul', slot, '20µl filter tiprack') for slot in ['11']]

    # Pipettes
    p20 = ctx.load_instrument('p20_single_gen2', 'right', tip_racks=tips)
    m20 = ctx.load_instrument('p20_multi_gen2', 'left', tip_racks=tips)

    # Source (master_mix in and deep-weel with NUM SAMPLES x RNA samples)
    source_master_mix = ctx.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', '7', 'Bloque Aluminio opentrons 24 screwcaps 2000 µL')
    source_master_mix = source_master_mix.wells()

    source_rna_samples = ctx.load_labware('abgene_96_wellplate_800ul', '5', 'ABGENE 96 Well Plate 800 µL')
    sources_rna = source_rna_samples.rows()[0][:num_cols]

    # Destination (NUM SAMPLES x pcr plate)
    pcr_plate_destination = ctx.load_labware('abi_fast_qpcr_96_alum_opentrons_100ul', '1', 'chilled qPCR final plate')
    destinations = pcr_plate_destination.wells()[:NUM_SAMPLES]
    destinations_by_columns = pcr_plate_destination.rows()[0][:num_cols]

    # ------------------
    # Protocol
    # ------------------
    # Dispense master mix
    i = 0
    for d in destinations:
        if not p20.hw_pipette['has_tip']:
            common.pick_up(p20)
        ctx.comment(str(d))
        source = source_master_mix[1] if i > 47 else source_master_mix[0]
        common.move_vol_multichannel(ctx, p20, reagent=master_mix, source=source, dest=d,
                                     vol=brand_master_mix, air_gap_vol=air_gap_vol_source,
                                     x_offset=x_offset, pickup_height=1, disp_height=-10,
                                     blow_out=True, touch_tip=True)
        i += 1
    p20.return_tip()

    # Dispense RNA samples
    for s, d in zip(sources_rna, destinations_by_columns):
        if not m20.hw_pipette['has_tip']:
            common.pick_up(m20)

        common.move_vol_multichannel(ctx, m20, reagent=rna_sample, source=s, dest=d,
                                     vol=arn, air_gap_vol=air_gap_vol_source,
                                     x_offset=x_offset, pickup_height=1, disp_height=-10,
                                     blow_out=True, touch_tip=True)
        m20.drop_tip()
