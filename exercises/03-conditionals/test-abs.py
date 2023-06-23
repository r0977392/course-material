import pytest
import student


@pytest.mark.parametrize('value', range(-100, 100))
def test_abs(value):
    expected = abs(value)
    actual = student.abs(value)

    assert actual == expected