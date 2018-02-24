import numpy as np

class Grid:
    '''Grid Type'''

    def __init__(self, shape, rank=3, nspecies=3):
        '''Initializing a Grid instance by allocating arrays'''
        self.cell = {}

        self.cell['rho'] = np.zeros(shape=shape, dtype=np.float)
        self.cell['ntr_frac'] = np.zeros(shape=shape+(nspecies,), dtype=np.float)
        self.cell['temp'] = np.zeros(shape=shape, dtype=np.float)
        self.cell['gdown'] = np.zeros(shape=shape, dtype=np.int)
        self.cell['size'] = 0.0

        self.edges = [
            np.zeros(shape=(rank), dtype=np.float),
            np.zeros(shape=(rank), dtype=np.float)
        ]

        self.cell_size = 0.0

        self.up = None
        self.down = None
        self.next = None
