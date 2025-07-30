class Solution:
    def fibonacci(self, n: int) -> int:
        """
        Recursively computes the nth Fibonacci number.
        Parameters:
        n (int): The position in the Fibonacci sequence (0-indexed).
        Returns:
        int: The nth Fibonacci number.
        """
        if n == 0 or n == 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

s = Solution()
n = 5
for i in range(n + 1):
    print(f"fibonacci({i}) = {s.fibonacci(i)}")


