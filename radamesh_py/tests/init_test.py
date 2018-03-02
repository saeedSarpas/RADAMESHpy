"""Testing main.py, RadameshPy initializations."""

from ..main import RadameshPy
import radamesh_py.tests.chombo as chombo


def test_if_it_loads_attributes():
    attrs = [
        ('num_levels', 3),
        ('num_components', 2),
        ('component_0', 'field_0'),
        ('component_1', 'field_1'),
        ('iteration', 1),
    ]

    rp = RadameshPy(chombo.FILENAME)

    for attr in attrs:
        assert rp.attrs[attr[0]] == attr[1]

    assert (rp.attrs['ProblemDomain'] == [4, 4]).all()

    assert len(rp.levels) is chombo.NUM_LEVELS

    fields = ['boxes', 'data', 'attrs']

    for l in range(chombo.NUM_LEVELS):
        level = "level_%d" % l

        assert (level in rp.levels) is True
        assert all((f in rp.levels[level]) is True for f in fields)
