from ..main import RadameshPy
import radamesh_py.tests.chombo as chombo

def test_if_it_loads_different_levels_properly():
    rp = RadameshPy(chombo.FILENAME)
    rp.load()

    assert len(rp.levels) is 3
