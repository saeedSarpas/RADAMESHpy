from radamesh_py.grid import Grid

import numpy as np

def test_if_it_has_necessary_members():
    grid = Grid((2, 3, 4))

    assert grid.cell['rho'].shape == (2, 3, 4)
    assert grid.cell['rho'].dtype == np.float

    assert grid.cell['ntr_frac'].shape == (2, 3, 4, 3)
    assert grid.cell['ntr_frac'].dtype == np.float

    assert grid.cell['temp'].shape == (2, 3, 4)
    assert grid.cell['temp'].dtype == np.float

    assert grid.cell['gdown'].shape == (2, 3, 4)
    assert grid.cell['gdown'].dtype == np.int

    assert('size' in grid.cell)

    assert grid.edges[0].shape[0] == 3
    assert grid.edges[0].dtype == np.float
    assert grid.edges[1].shape[0] == 3
    assert grid.edges[1].dtype == np.float

    for field in ['up', 'down', 'next']:
        assert hasattr(grid, field) is True
