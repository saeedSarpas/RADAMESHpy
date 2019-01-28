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
        self.num_levels = int ( self.attrs['num_levels'] )

        for l in range ( self.num_levels ):
            level = "level_%d" % l
            self.levels[level] = {}
            self.levels[level]['data'] = []
            self.levels[level]['boxes'] = []
            self.levels[level]['attrs'] = {}

    def __del__ ( self ):
        if isinstance ( self.file, h5py.File ):
            self.file.close()

    def close ( self ):
        self.file.close()

    def load(self):
        """Loading all levels."""
        for l in range ( self.num_levels ):
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

    def lineout(x0, x1, field):
        """
        Constructing data points on a given line segment.

        parameters:
        x0 -- initial point of the line (tuple)
        x1 -- final point of the line (tuple)
        field -- field of interest
        """
