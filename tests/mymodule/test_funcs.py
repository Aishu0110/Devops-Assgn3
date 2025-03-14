import pytest

from myapp.mymodule.funcs import *


@pytest.mark.easy_operation
def test_add():
    # This test will fail.
    assert add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.easy_operation
def test_multiply_by_two_with_id():
    assert multiply(8, 2) == 16  # Using the last two digits of my student ID
