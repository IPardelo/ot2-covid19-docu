NEW_NAME = "ROBOT_01"               #CHANGE THIS PARAMETER BY THE NAME YOU WANT

from opentrons import robot
import os

robot.comment(f"Setting serial number to {NEW_NAME}.")

if not robot.is_simulating():
    with open("/var/serial", "w") as serial_number_file:
        serial_number_file.write(NEW_NAME + "\n")
    with open("/etc/machine-info", "w") as serial_number_file:
        serial_number_file.write(f"DEPLOYMENT=production\nPRETTY_HOSTNAME={NEW_NAME}\n")
    with open("/etc/hostname", "w") as serial_number_file:
        serial_number_file.write(NEW_NAME + "\n")
  
    os.sync()
  
    robot.comment("Done.")
