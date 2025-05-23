"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

class Solution:
        def lengthOfLastWord(self, s: str) -> int:

            words = s.strip().split()
            print(f"String: {s}, Words: {words}")
            length = len(words[-1])
            return length
        
       
obj = Solution()
s = "   fly me   to   the moon  "
r = obj.lengthOfLastWord(s)
print(f"length of last word: {r}")