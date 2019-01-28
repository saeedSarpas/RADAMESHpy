"""Testing main.py, lineout method."""

from ..main import RadameshPy
import radamesh_py.tests.chombo as chombo


def test_if_it_returns_proper_data():
    rp = RadameshPy(chombo.FILENAME)
    rp.load()

    expected_xs = (
        chombo.DX / 8,
        1 * chombo.DX / 4 + chombo.DX / 8,
        1 * chombo.DX / 2 + chombo.DX / 4,
        1 * chombo.DX + chombo.DX / 2,
        8 * chombo.DX / 4 + chombo.DX / 8,
        9 * chombo.DX / 4 + chombo.DX / 8,
        5 * chombo.DX / 2 + chombo.DX / 4,
        3 * chombo.DX + chombo.DX / 2,
    )

    expected_dxs = (
        chombo.DX / 8,
        chombo.DX / 8,
        chombo.DX / 4,
        chombo.DX / 2,
        chombo.DX / 8,
        chombo.DX / 8,
        chombo.DX / 4,
        chombo.DX / 2,
    )

    expected_ys = (3, 1, 1, 9, 14, 11, 11, 3)

    xs, ys, dxs = rp.lineout((0., 1.), (1., 0.), 'field_0')

    assert set(xs) == set(expected_xs)
    assert set(ys) == set(expected_ys)
    assert set(dxs) == set(expected_dxs)
