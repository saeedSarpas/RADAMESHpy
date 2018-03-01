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

    radamesh_py = RadameshPy(chombo.FILENAME)

    for attr in attrs:
        assert radamesh_py.attrs[attr[0]] == attr[1]

    assert (radamesh_py.attrs['ProblemDomain'] == [4, 4]).all()
