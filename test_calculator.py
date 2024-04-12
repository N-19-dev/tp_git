from calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.addition(5, 5) == 10

def test_soustraction():
    calc = Calculator()
    assert calc.soustraction(15, 5) == 10

def test_division():
    calc = Calculator()
    assert calc.division(100, 10) == 10

