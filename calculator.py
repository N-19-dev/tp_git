class Division:
    @staticmethod
    def divide(a, b):
        """Divise a par b."""
        if b == 0:
            raise ValueError("Division by zero is undefined.")
        return a / b

class Addition:
    @staticmethod
    def add(a, b):
        """Additionne a et b."""
        return a + b

class Soustraction:
    @staticmethod
    def subtract(a, b):
        """Soustrait b de a."""
        return a - b

# Exemple d'utilisation :
divide_instance = Division()
result_division = divide_instance.divide(10, 2)

add_instance = Addition()
result_addition = add_instance.add(5, 3)

subtract_instance = Soustraction()
result_soustraction = subtract_instance.subtract(8, 2)

print("Résultat de la division :", result_division)
print("Résultat de l'addition :", result_addition)
print("Résultat de la soustraction :", result_soustraction)

