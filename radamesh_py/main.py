'''main.py'''

import h5py as h5

class RadameshPy:
    '''
    Simple class to handle different actions aiming at reading and processing
    RADAMESH outputs
    '''

    def __init__(self, path):
        '''
        Initializing an instance of RadameshPy by loading attributes

        parameters:
        path -- path to a RADAMESH output
        '''
        self.path = path
        self.attrs = _load_attrs(path)
        self.levels = {}

        for l in range(self.attrs['num_levels']):
            self.levels["level_%d" % l] = {}

    def load(self):
        '''Loading different fields of the chombo file'''


def _load_attrs(path):
    '''Loading RADAMESH main attributes'''

    attrs = {}

    _file = h5.File(path, 'r')
    _file_attrs = _file['/'].attrs

    for key in _file_attrs.keys():
        val = _file_attrs.get(key)
        attrs[key] = val[0] if isinstance(val, list) and len(val) == 1 else val

    for i in range(attrs['num_components']):
        attrs['component_%d' % i] = attrs['component_%d' % i].decode("utf-8")

    _file.close()

    return attrs
