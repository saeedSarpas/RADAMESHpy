"""main.py."""

import h5py as h5


class RadameshPy:
    """Handling actions aiming at reading and processing RADAMESH outputs."""

    def __init__(self, path):
        """
        Initializing an instance of RadameshPy by loading attributes.

        parameters:
        path -- path to a RADAMESH output
        """
        self.file = h5.File(path, 'r')
        self.path = path
        self.attrs = self.__load_attrs()
        self.levels = {}

        for l in range(self.attrs['num_levels']):
            level = "level_%d" % l
            self.levels[level] = {}
            self.levels[level]['data'] = []
            self.levels[level]['boxes'] = []
            self.levels[level]['attrs'] = {}

    def load(self):
        """Loading all levels."""
        for l in range(self.attrs['num_levels']):
            self.load_level(l)

    def load_level(self, l):
        """
        Loading different fields of one of the given levels of the chombo file.

        parameters:
        l -- level (integer)
        """
        level = 'level_%d' % l

        attrs = self.levels[level]['attrs']
        chombo_attrs = self.file[level].attrs

        attrs['dx'] = chombo_attrs.get('dx')
        attrs['ref_ratio'] = chombo_attrs.get('ref_ratio')

        if level is 'level_0':
            attrs['prob_domain'] = chombo_attrs.get('prob_domain')

        self.levels[level]['boxes'] = self.file[level]['boxes']
        self.levels[level]['data'] = self.file[level]['data:datatype=0']

    def __load_attrs(self):
        """Loading RADAMESH main attributes."""
        attrs = {}

        chombo_attrs = self.file['/'].attrs

        for key in chombo_attrs.keys():
            v = chombo_attrs.get(key)
            attrs[key] = v[0] if isinstance(v, list) and len(v) == 1 else v

        for i in range(attrs['num_components']):
            comp = 'component_%d' % i
            attrs[comp] = attrs[comp].decode("utf-8")

        return attrs
