"""
This module contains unit tests for the calculator module.
"""

from calculator import Calculator

def test_addition():
    """
    Test addition function.
    """
    calc = Calculator()
    assert calc.addition(5, 5) == 10

def test_soustraction():
    """
    Test soustraction function.
    """
    calc = Calculator()
    assert calc.soustraction(15, 5) == 10

def test_division():
    """
    Test division function.
    """
    calc = Calculator()
    assert calc.division(100, 10) == 10

