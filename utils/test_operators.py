import pytest
import operators as op


#  ADD
def test_add_valid():
    assert op.add(5, 7) == 12
    assert op.add(5, 7) == 12
    assert op.add("3.5", 2.5) == 6.0


def test_add_invalid():
    with pytest.raises(ValueError):
        op.add("abc", "3")
    with pytest.raises(TypeError):
        op.add([1, 2], 5)


#  MULTIPLY
def test_multiply_valid():
    assert op.multiply(5, 5) == 25
    assert op.multiply("5", 5) == 25
    assert op.multiply("3.5", 2) == 7.0


def test_multiply_invalid():
    with pytest.raises(ValueError):
        op.multiply("a", "b")
    with pytest.raises(TypeError):
        op.multiply([1, 2], 5)


#  MODULUS
def test_modulus_valid():
    assert op.modulus(10, 3) == 1
    assert op.modulus(10, 4) == 2
    assert op.modulus(7.5, 2.5) == 0.0


def test_modulus_invalid():
    with pytest.raises(ValueError):
        op.modulus("abc", 3)
    with pytest.raises(TypeError):
        op.modulus({"x": 1}, 5)
    with pytest.raises(ZeroDivisionError):
        op.modulus(10, 0)
