"""Testing main.py, load method."""

from ..main import RadameshPy
import radamesh_py.tests.chombo as chombo


def test_if_it_loads_different_levels_properly():
    rp = RadameshPy(chombo.FILENAME)
    rp.load()

    for l in range(chombo.NUM_LEVELS):
        level = 'level_%d' % l
        attrs = rp.levels[level]['attrs']
        boxes = rp.levels[level]['boxes']
        data = rp.levels[level]['data']

        assert attrs['dx'] == (chombo.INIT_DX / 2**l)
        assert attrs['ref_ratio'] == 2

        if level is 'level_0':
            assert attrs['prob_domain'] == chombo.INIT_PROB_DOMAIN

        for i in range(len(chombo.BOXES[level])):
            assert set(boxes[i]) == set(chombo.BOXES[level][i])

        assert set(data) == set(chombo.DATA[level])
