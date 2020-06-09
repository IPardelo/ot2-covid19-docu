# ot2-covid19
Several scripts for Opentrons covid19 PCR preparation

## Install Library
To install our library with common functions to abstract the ot2 protocols, just required copy this folder in certain
folder of Opentron's Raspberry Pi (in this case root's home, but could be wherever):

```sh
# Before anything you required ssh access to RaspberryPi
# Check this out ~> https://support.opentrons.com/en/articles/3203681-setting-up-ssh-access-to-your-ot-2
scp -r -i ot2_ssh_key ot2-covid19 root@<robot-ip>:/root
```

If there is any update required you just have to upload a new version

## Development
For including our custom library in the ot2 protocols we just to follow the next python snippet:
```py
import importlib

# Load library
LIBRARY_PATH = '/root/ot2-covid19/library/'     # <-- replace this path for where you copy the library (using scp)
spec = importlib.util.spec_from_file_location("library.protocols.common_functions",                     # Which module are you loading
                                              "{}protocols/common_functions.py".format(LIBRARY_PATH))   # Where is the load module
common = importlib.util.module_from_spec(spec)
spec.loader.exec_module(common)

# .... 
# rest of your code here
common.generate_source_table(source)    # call the library's functions
# ....
```

## Common ot2 errors and possible solution

* **ACK timeout**: check if you have connection against the robot and then if everything is ok just wait a few minutes and
re-run the protocol

* **Robots pick up the tip and then doesn't move**: reboot robot using reboot command through ssh

* **Any error in library's subroutine**: when there is an error in library's subroutine the opentrons app doesn't show the line
just specify where you call the subroutine. Then a trick to find out the bug could be copy the common library function and
paste it in the protocol as a function then re-run the protocol in this way we can discovery where is the exactly line where 
the bug is.

## Configure opentrons simulator in PyCharm for debugging (WIP)