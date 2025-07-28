"""
Module: factorial_recursive
Description:
This module defines a class with a recursive method to calculate the factorial of a given number.
"""

class Solutions:
    """
    A class that provides basic recursion utilities.
    """
    def nFactorial(self, num: int) -> int:
        """
        Recursively calculates the factorial of a number.
        Parameters:
        num (int): A non-negative integer whose factorial is to be computed.
        Returns:
        int: Factorial of the input number.
        """
        if num == 0 or num == 1:
            return 1  # Base case: 0! = 1! = 1

        return num * self.nFactorial(num - 1)  # Recursive case

if __name__ == '__main__':
    sol = Solutions()
    num = 5
    result = sol.nFactorial(num)
    print(f"Factorial of {num} is {result}")
