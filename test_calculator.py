from calculator import Addition, Soustraction, Division

def test_addition():
    add_instance = Addition()
    assert add_instance.add(1, 1) == 2

def test_soustraction():
    subtract_instance = Soustraction()
    assert subtract_instance.subtract(1, 1) == 0

def test_division():
    divide_instance = Division()
    assert divide_instance.divide(1, 1) == 1

# Exécuter les tests
test_addition()
test_soustraction()
test_division()

print("Tous les tests ont réussi !")

