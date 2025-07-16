"""
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.


Example 1:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for ch in s:
            stack.append(ch)
            # Check if the last few characters match 'part'
            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                del stack[-part_len:]  # Remove last 'part_len' characters

        return ''.join(stack)

s = "daabcbaabcbc"
part = "abc"
sol = Solution()
result = sol.removeOccurrences(s, part)