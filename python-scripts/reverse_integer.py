"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""
class Solutions:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # 32-bit integer range
        rev = 0
        sign = -1 if x < 0 else 1  # Extract sign
        x = abs(x)  # Work with absolute value

        while x != 0:
            digit = x % 10  # Extract last digit
            x //= 10  # Remove last digit

            # Check for overflow before adding the digit
            if rev > (INT_MAX - digit) // 10:
                return 0  # Overflow case
            
            rev = rev * 10 + digit
        
        return sign * rev  # Restore sign

s = Solutions()
# Test cases
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(0))
print(s.reverse(1534236469))
