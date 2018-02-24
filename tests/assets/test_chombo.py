#!/usr/bin/env python

# +-------+-------+-------+-------+
# |   |   |       |       |       |
# |___|___|       |       |       |
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

FILENAME = 'test.chombo.h5'

if __name__ == '__main__':

    chombo = h5py.File(FILENAME, 'w')

    # Chombo format attributes
    chombo.attrs['iteration'] = 1
    chombo.attrs['time'] = 1.23e4
    chombo.attrs['num_levels'] = 3
    chombo.attrs['num_components'] = 2
    chombo.attrs['component_0'] = np.string_('field_0')
    chombo.attrs['component_1'] = np.string_('field_1')

    chombo_global = chombo.create_group('Chombo_global')
    chombo_global.attrs['SpaceDim'] = 2

    # Extra attributes
    chombo.attrs['ProblemDomain'] = np.array([4, 4], dtype=np.int)

    # box type
    boxtype = [
        ('lo_i', np.int),
        ('lo_j', np.int),
        ('hi_i', np.int),
        ('hi_j', np.int),
    ]

    # level 0
    lev_0 = chombo.create_group('level_0')

    lev_0.attrs['dx'] = 0.25
    lev_0.attrs['prob_domain'] = np.array([(0, 0, 3, 3)], dtype=boxtype)
    lev_0.attrs['ref_ratio'] = 2

    lev_0['GridId'] = np.array([1], dtype=np.int)

    boxes_0 = lev_0.create_dataset('boxes', (1,), dtype=boxtype)

    boxes_0[0] = (0, 0, 3, 3)

    lev_0['data:datatype=0'] = np.arange(32)

    # level 1
    lev_1 = chombo.create_group('level_1')

    lev_1.attrs['dx'] = 0.125
    lev_1.attrs['ref_ratio'] = 2

    lev_1['GridId'] = np.arange(2, 18)

    boxes_1 = lev_1.create_dataset('boxes', (3,), dtype=boxtype)

    boxes_1[0] = (0, 6, 1, 7)
    boxes_1[1] = (4, 4, 5, 5)
    boxes_1[2] = (2, 2, 5, 3)

    lev_1['data:datatype=0'] = np.arange(32, 64)

    # level 2
    lev_2 = chombo.create_group('level_2')

    lev_2.attrs['dx'] = 0.0625
    lev_2.attrs['ref_ratio'] = 2

    lev_2['GridId'] = np.arange(18, 30)

    boxes_2 = lev_2.create_dataset('boxes', (2,), dtype=boxtype)

    boxes_2[0] = (8, 8, 9, 9)
    boxes_2[1] = (6, 6, 9, 7)

    lev_2['data:datatype=0'] = np.arange(64, 76)

    chombo.close()
