# bdf font to pyton dictFont utility
WIP..
## Setup
install the patched bsdparser:

This is in a submodule so you must have run `git submodule init` and `git submodule update` in the repo prior to this.

```console
# create venv if needed
~/microPyEZfonts/mpy-fonts $ python -m venv env

# activate it
~/microPyEZfonts/mpy-fonts $ source env/bin/activate

# upgrade pip (optional)
(env) ~/microPyEZfonts/mpy-fonts $ pip install --upgrade pip
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: pip in ./env/lib/python3.11/site-packages (23.0.1)
Collecting pip
  Using cached https://www.piwheels.org/simple/pip/pip-24.0-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.0.1
    Uninstalling pip-23.0.1:
      Successfully uninstalled pip-23.0.1
Successfully installed pip-24.0owen@sam:~/MPython-fonts/microPyEZfonts/dictFont$ python -m venv env

# install bdfparser from the local folder
(env) ~/microPyEZfonts/mpy-fonts $ pip install bdfparser/
Processing ./bdfparser
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: bdfparser
  Building wheel for bdfparser (pyproject.toml) ... done
  Created wheel for bdfparser: filename=bdfparser-2.2.0-py3-none-any.whl size=12612 sha256=9cfd638c1656d99cb325fcdc48d8ec19f361912a27655c23177c3bf99238cda9
  Stored in directory: /tmp/pip-ephem-wheel-cache-nu3wzqom/wheels/66/b1/fa/d8461f4f9b98d936e78a32f60cadeee78161047d08888d0ecc
Successfully built bdfparser
Installing collected packages: bdfparser
Successfully installed bdfparser-2.2.0
```
