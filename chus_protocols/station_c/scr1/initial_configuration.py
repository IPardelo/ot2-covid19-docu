from library.constants import IP
from library.general.rename_robot import rename
from library.general.configure_static_ip import set_static_ip

rename('sar2')
set_static_ip(IP.replace('x', '58'))
