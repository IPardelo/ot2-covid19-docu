from opentrons import robot
import importlib.util

# Load Constants
spec = importlib.util.spec_from_file_location("ot2.library.constants", "/root/ot2-covid19-master/ot2/library/constants.py")
constants = importlib.util.module_from_spec(spec)
spec.loader.exec_module(constants)


# Load Rename function
spec = importlib.util.spec_from_file_location("ot2.library.general.rename_robot", "/root/ot2-covid19-master/ot2/library/general/rename_robot.py")
rename_robot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rename_robot)


# Load Constants
spec = importlib.util.spec_from_file_location("ot2.library.general.configure_static_ip", "/root/ot2-covid19-master/ot2/library/general/configure_static_ip.py")
configure_static_ip = importlib.util.module_from_spec(spec)
spec.loader.exec_module(configure_static_ip)

IP = constants.IP

if not robot.is_simulating():
    rename_robot.rename('sbr2')
    configure_static_ip.set_static_ip(IP.replace('x', '55'))

robot.comment("Please, reboot")
