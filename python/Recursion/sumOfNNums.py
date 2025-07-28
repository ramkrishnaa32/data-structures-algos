
class Solutions:
    def sumOfNumbers(self, num: int) -> int:
        """
        Recursively calculates the sum of first N natural numbers.
        Parameters:
        num (int): A positive integer
        Returns:
        int: Sum from 1 to num
        """
        if num == 1:
            return 1  # Base case: a sum of first 1 number is 1

        return num + self.sumOfNumbers(num - 1)  # Recursive case

if __name__ == '__main__':
    sol = Solutions()
    num = 100
    result = sol.sumOfNumbers(num)
    print(f"Sum of first {num} natural numbers is {result}")
