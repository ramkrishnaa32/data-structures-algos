"""
Module: print_numbers_recursive
Description:
This module defines a class with a recursive method to print numbers from a given number down to 1.
"""

class Solutions:
    """
    A class that provides basic recursion utilities.
    """
    def printNumbers(self, num: int) -> None:
        """
        Recursively prints numbers from the given number down to 1.
        Parameters:
        num (int): The starting number.
        Returns:
        None
        """
        if num == 1:
            print(1, end="\n")  # Base case: print 1 and newline
            return

        print(num, end=', ')  # Print the current number with space
        self.printNumbers(num - 1)  # Recursive call

if __name__ == '__main__':
    sol = Solutions()
    num = 20
    sol.printNumbers(num)
