from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='radamesh_py',
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
      zip_safe=False)
