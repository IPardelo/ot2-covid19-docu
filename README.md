# ot2-covid19
Several scripts for Opentrons covid19 PCR preparation

## Install
install library locally using pip

```sh
# In project's root folder (where is this files)
python setup.py install

# Check installation was sucessfull
pip list packages
Package              Version            
-------------------- -------------------
# ... other packages ...
ot2-sergas           1.0.0
# ... other packages ...
```

## Development
Just import the library
```py
from ot2.library.general.rename_robot import rename
from ot2.library.general.rename_robot import rename
# .... 
# rest of your code here
# ....
```

## Update library
TODO

## Remove library
```sh
pip uninstall ot2-sergas
```