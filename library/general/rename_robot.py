import os

from opentrons import robot


def rename(new_serial_number):
    robot.comment(f"Setting serial number to {new_serial_number}.")
    
    if not robot.is_simulating():
        with open("/var/serial", "w") as serial_number_file:
            serial_number_file.write(new_serial_number + "\n")
        with open("/etc/machine-info", "w") as serial_number_file:
            serial_number_file.write(f"DEPLOYMENT=production\nPRETTY_HOSTNAME={new_serial_number}\n")
        with open("/etc/hostname", "w") as serial_number_file:
            serial_number_file.write(new_serial_number + "\n")
    
    os.sync()
    
    robot.comment("Done.")
