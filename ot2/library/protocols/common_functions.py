import time

# from opentrons.drivers.rpi_drivers import gpio
from opentrons.types import Point


def move_vol_multichannel(pipette, reagent, source, dest, vol, air_gap_vol, x_offset, pickup_height, rinse, disp_height,
                          blow_out, touch_tip):
    """

    :param pipette:
    :param reagent:
    :param source:
    :param dest:
    :param vol:
    :param air_gap_vol:
    :param x_offset:
    :param pickup_height:
    :param rinse:
    :param disp_height:
    :param blow_out: if True they will be done after dispensing
    :param touch_tip: if True they will be done after dispensing

    :return:
    """
    # Rinse before aspirating
    if rinse:
        custom_mix(pipette, reagent, location=source, vol=vol, rounds=2, blow_out=True, mix_height=0, x_offset=x_offset)
    # Source
    s = source.bottom(pickup_height).move(Point(x=x_offset[0]))
    pipette.aspirate(vol, s)
    # If there is air_gap_vol, switch pipette to slow speed
    if air_gap_vol != 0:
        pipette.aspirate(air_gap_vol, source.top(z=-2), rate=reagent.flow_rate_aspirate)
    # Go to destination
    drop = dest.top(z=disp_height).move(Point(x=x_offset[1]))
    pipette.dispense(vol + air_gap_vol, drop, rate=reagent.flow_rate_dispense)
    # ctx.delay(seconds=reagent.delay)
    if blow_out:
        pipette.blow_out(dest.top(z=-2))
    if touch_tip:
        pipette.touch_tip(speed=20, v_offset=-5)


def custom_mix(pipette, reagent, location, vol, rounds, blow_out, mix_height, x_offset, source_height=3):
    """
    Function for mixing a given [vol] in the same [location] a x number of [rounds].

    :param pipette:
    :param reagent:
    :param location:
    :param vol:
    :param rounds:
    :param blow_out: Blow out optional [True,False]
    :param x_offset: [source, destination]
    :param source_height: height from bottom to aspirate
    :param mix_height: height from bottom to dispense

    :return:
    """
    mix_height = 3 if mix_height == 0 else mix_height
    pipette.aspirate(1, location=location.bottom(z=source_height).move(Point(x=x_offset[0])), rate=reagent.get('flow_rate_aspirate'))

    for _ in range(rounds):
        pipette.aspirate(vol, location=location.bottom(z=source_height).move(Point(x=x_offset[0])), rate=reagent.get('flow_rate_aspirate'))
        pipette.dispense(vol, location=location.bottom(z=mix_height).move(Point(x=x_offset[1])), rate=reagent.get('flow_rate_dispense'))
    pipette.dispense(1, location=location.bottom(z=mix_height).move(Point(x=x_offset[1])), rate=reagent.get('flow_rate_dispense'))

    if blow_out:
        pipette.blow_out(location.top(z=-2))


def calc_height(ctx, reagent, cross_section_area, aspirate_volume, min_height=0.5):
    """
    Calculate pickup_height based on remaining volume and shape of container

    :param reagent:
    :param cross_section_area:
    :param aspirate_volume:
    :param min_height:

    :return:
    """
    if reagent.get('vol_well') < aspirate_volume:
        ctx.comment('if')
        reagent.get('unused').append(reagent.get('vol_well'))
        reagent['col'] = reagent.get('col') + 1
        reagent['vol_well'] = reagent.get('vol_well_original')
        height = (reagent.get('vol_well') - aspirate_volume - reagent.get('v_cono')) / cross_section_area
        reagent['vol_well'] = reagent.get('vol_well') - aspirate_volume
        if height < min_height:
            height = min_height
        col_change = True
    else:
        ctx.comment('else')
        height = (reagent.get('vol_well') - aspirate_volume - reagent.get('v_cono')) / cross_section_area
        reagent['vol_well'] = reagent.get('vol_well') - aspirate_volume
        if height < min_height:
            height = min_height
        col_change = False
    return height, col_change


def generate_source_table(source):
    """
    Concatenate the wells from the different origin racks
    """
    for rack_number in range(len(source)):
        s = source[rack_number].wells() if rack_number == 0 else s + source[rack_number].wells()
    return s


def pick_up(pip):
    pip.pick_up_tip()

"""
def notify_finish_process():
    for i in range(3):
        gpio.set_rail_lights(False)
        gpio.set_button_light(1, 0, 0)
        time.sleep(0.3)
        gpio.set_rail_lights(True)
        gpio.set_button_light(0, 0, 1)
        time.sleep(0.3)
    gpio.set_button_light(0, 1, 0)
"""