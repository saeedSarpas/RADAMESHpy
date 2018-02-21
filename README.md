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
