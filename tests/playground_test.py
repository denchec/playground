import pytest
import playground


@pytest.mark.parametrize("a,b,c", [
    (1, 2, 3),
    (23, 45, 12)
])
def test_add1(a, b, c):
    assert playground.add(a, b) == c
