import pytest
from calculator import add, divide  # Import functions from our main file

def test_add_positive_numbers():
    # Pytest uses standard Python 'assert' statements
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # To test if an error/exception is raised, we use pytest.raises
    with pytest.raises(ValueError):
        divide(10, 0)