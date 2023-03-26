from scripts.calculator import add, substract, multiply, division
from pytest import mark


@mark.parametrize("x, y, expected_result", [
    (20, 10, 10),
    (40, 10, 30),
    (70, 20, 50),
    (60, 40, 20)
])
def test_substract_function(x, y, expected_result):
    assert substract(x, y) == expected_result


@mark.parametrize("x, y, expected_result", [
    (20, 10, 30),
    (40, 10, 50),
    (70, 20, 90),
    (60, 40, 100)
])
def test_addition_function(x, y, expected_result):
    assert add(x, y) == expected_result
