class Calculator:
    """
    This class provides basic arithmetic operations.
    """

    def division(self, a, b):
        """
        Divides a by b.
        """
        if b == 0:
            raise ValueError("Division by zero is undefined.")
        return a / b

    def addition(self, a, b):
        """
        Adds a and b.
        """
        return a + b

    def soustraction(self, a, b):
        """
        Subtracts b from a.
        """
        return a - b

