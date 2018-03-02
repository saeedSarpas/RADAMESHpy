#!/usr/bin/env python
"""Generating a test RADAMESH (chombo) file for testing purposes."""

# to run this file go to the root directory of this package and run:
# $ python setup.py chombo

# +-------+-------+-------+-------+
# |_|_|   |       |       |       |
# |_|_|___|       |       |       |
# |   |   |       |       |       |
# |   |   |       |       |       |
# +-------+-------+-------+-------+
# |       |       |   |   |       |
# |       |       |___|___|       |
# |       |       |_|_|   |       |
# |       |       | | |   |       |
# +-------+-------+-------+-------+
# |       |   |_|_|_|_|   |       |
# |       |___|_|_|_|_|___|       |
# |       |   |   |   |   |       |
# |       |   |   |   |   |       |
# +-------+-------+-------+-------+
# |       |       |       |       |
# |       |       |       |       |
# |       |       |       |       |
# |       |       |       |       |
# +-------+-------+-------+-------+

import h5py
import numpy as np

# box type
boxtype = [
    ('lo_i', np.int),
    ('lo_j', np.int),
    ('hi_i', np.int),
    ('hi_j', np.int),
]

# Constants
FILENAME = 'radamesh_py/tests/assets/chombo.h5'
NUM_LEVELS = 3
INIT_DX = 0.25
INIT_PROB_DOMAIN = np.array([(0, 0, 3, 3)], dtype=boxtype)

BOXES = {
    'level_0': [(0, 0, 3, 3)],
    'level_1': [
        (0, 6, 1, 7),
        (4, 4, 5, 5),
        (2, 2, 5, 3),
    ],
    'level_2': [
        (0, 14, 1, 15),
        (8, 8, 9, 9),
        (6, 6, 9, 7),
    ]
}

DATA = {
    'level_0': np.arange(32),
    'level_1': np.arange(32),
    'level_2': np.arange(32),
}


def create():
    """Creating a chombo file based on above constants."""
    chombo = h5py.File(FILENAME, 'w')

    # Chombo format attributes
    chombo.attrs['iteration'] = 1
    chombo.attrs['time'] = 1.23e4
    chombo.attrs['num_levels'] = NUM_LEVELS
    chombo.attrs['num_components'] = 2
    chombo.attrs['component_0'] = np.string_('field_0')
    chombo.attrs['component_1'] = np.string_('field_1')

    chombo_global = chombo.create_group('Chombo_global')
    chombo_global.attrs['SpaceDim'] = 2

    # Extra attributes
    chombo.attrs['ProblemDomain'] = np.array([4, 4], dtype=np.int)

    # level 0
    lev_0 = chombo.create_group('level_0')

    lev_0.attrs['dx'] = INIT_DX
    lev_0.attrs['prob_domain'] = INIT_PROB_DOMAIN
    lev_0.attrs['ref_ratio'] = 2

    boxes_0 = lev_0.create_dataset('boxes', (1,), dtype=boxtype)

    boxes_0[0] = BOXES['level_0'][0]

    lev_0['data:datatype=0'] = DATA['level_0']

    # level 1
    lev_1 = chombo.create_group('level_1')

    lev_1.attrs['dx'] = INIT_DX / 2
    lev_1.attrs['ref_ratio'] = 2

    boxes_1 = lev_1.create_dataset('boxes', (3,), dtype=boxtype)

    boxes_1[0] = BOXES['level_1'][0]
    boxes_1[1] = BOXES['level_1'][1]
    boxes_1[2] = BOXES['level_1'][2]

    lev_1['data:datatype=0'] = DATA['level_1']

    # level 2
    lev_2 = chombo.create_group('level_2')

    lev_2.attrs['dx'] = INIT_DX / 4
    lev_2.attrs['ref_ratio'] = 2

    boxes_2 = lev_2.create_dataset('boxes', (3,), dtype=boxtype)

    boxes_2[0] = BOXES['level_2'][0]
    boxes_2[1] = BOXES['level_2'][1]
    boxes_2[2] = BOXES['level_2'][2]

    lev_2['data:datatype=0'] = DATA['level_2']

    chombo.close()
