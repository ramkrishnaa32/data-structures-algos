"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        binForm = n
        ans = 1
        if n < 0:
            x = 1 / x
            binForm = -binForm

        while binForm > 0:
            print(binForm)
            if binForm % 2 == 1:
                ans *= x
            x *= x
            binForm //= 2

        return ans


x = 2.00000
n = 10
s = Solution()
result = s.myPow(x, n)
print(result)