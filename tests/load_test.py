from radamesh_py.main import RadameshPy

def test_if_it_loads_different_levels_properly():
    radamesh_py = RadameshPy('tests/assets/test.chombo.h5')
    radamesh_py.load()

    assert len(radamesh_py.levels) is 3
