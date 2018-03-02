# RadameshPy
A package to handle different actions aiming at reading and processing
RADAMESH (RADAMESH: Cosmological Radiative Transfer for Adaptive Mesh Refinement
Simulations, Cantalupo, S. & Porciani, C. (2010)) outputs.

## Installation

Using ```setyp.py```:
```bash
$ git clone https://github.com/saeedSarpas/radamesh-py.git
$ cd radamesh-py
$ python3 setup.py install # --user in case you want to install it locally
```

Using ```pip```:
```bash
$ git clone https://github.com/saeedSarpas/radamesh-py.git
$ cd radamesh-py
$ pip install . # --user in case you want to install it locally
$ pip3 install . # --user in case you want to install it locally
```

## Usage

```
    >>> from radamesh_py import RadameshPy
    >>> rp = RadameshPy()
```


## Running tests

To make sure that the CHOMBO test file is updated, run
```bash
$ python3 setup.py chombo
```
This command will create a CHOMBO test file inside ```radamesh_py/tests/assets```.

To run the tests, execute the following command:
```bash
$ python3 ./setup.py test
```
or
```bash
$ py.test # -s to show stdout
```
from the root directory of the package.
