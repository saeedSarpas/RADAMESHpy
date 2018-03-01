from setuptools import setup
from distutils.command.build_py import build_py as _build_py
import radamesh_py.tests.chombo as _chombo
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class CreateTestChombo(_build_py):
    '''Custom build command to create a test CHOMBO file'''

    def run(self):
        '''run `python setup.py chombo` to create a new test file'''
        _chombo.create()
        _build_py.run(self)


setup(
    name='radamesh_py',
    version='0.0',
    description='Simple code to read and process RADAMESH outputs',
    long_description=read('README.md'),
    url='http://github.com/saeedSarpas/radamesh_py',
    keywords='RADAMESH',
    author='Saeed Sarpas',
    author_email='saeed.sarpas@phys.ethz.ch',
    license='GPLv3',
    packages=['radamesh_py'],
    install_requires=[
        'h5py',
        'numpy'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    cmdclass={
        'chombo': CreateTestChombo,
    },
    zip_safe=False
)
