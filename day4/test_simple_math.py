from simple_math import *
import pytest


@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (2, 3, 5)])
def test_simple_add(a, b, expected):
    assert simple_add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 1, 0), (2, 3, -1)])
def test_simple_sub(a, b, expected):
    assert simple_sub(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 1, 1), (2, 3, 6)])
def test_simple_mult(a, b, expected):
    assert simple_mult(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 1, 1), (2, 3, 2 / 3)])
def test_simple_div(a, b, expected):
    assert simple_div(a, b) == expected


@pytest.mark.parametrize("x, a0, a1, expected", [(1, 1, 1, 2), (2, 3, 5, 13)])
def test_poly_first(x, a0, a1, expected):
    assert poly_first(x, a0, a1) == expected


@pytest.mark.parametrize(
    "x, a0, a1, a2, expected",
    [
        (1, 1, 1, 1, 3),
    ],
)
def test_poly_second(x, a0, a1, a2, expected):
    assert poly_second(x, a0, a1, a2) == expected
