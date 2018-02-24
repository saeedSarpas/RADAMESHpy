from radamesh_py.main import RadameshPy

def test_if_it_loads_attributes():

    attrs = [
        ('num_levels', 2),
        ('num_components', 2),
        ('component_0', 'field_0'),
        ('component_1', 'field_1'),
        ('iteration', 10),
    ]

    radamesh_py = RadameshPy('tests/assets/test.chombo.h5')

    for attr in attrs:
        assert radamesh_py.attrs[attr[0]] == attr[1]

    assert (radamesh_py.attrs['ProblemDomain'] == [4, 4]).all()
