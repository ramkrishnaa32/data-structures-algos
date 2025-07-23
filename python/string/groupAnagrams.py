"""
An anagram is a word or phrase formed by rearranging the letters of another.
Example: "eat" and "tea" are anagrams because they contain the same letters.

Given a list of words, group the anagrams together into lists.
The output should be a list of lists, where each inner list contains words that are anagrams of each other.

Example:
input: ['eat', 'cba', 'tae', 'abc', 'xyz']
output: [['eat', 'tae'], ['cba', 'abc'], ['xyz']]
"""

from collections import defaultdict


class Solution:
    def groupAnagramsBruteForce(self, word_list):
        result = {}
        for word in word_list:
            sorted_word = ''.join(sorted(word))
            result.setdefault(sorted_word, []).append(word)

        return list(result.values())

    def groupAnagramsOptimized(self, word_list):
        result = defaultdict(list)

        for word in word_list:
            count = [0] * 26  # Build a 26-letter count tuple (for a-z)
            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            result[key].append(word)

        return list(result.values())


word_list = ['eat', 'cba', 'tae', 'abc', 'xyz']
s = Solution()
result = s.groupAnagramsBruteForce(word_list)
print(result)

result = s.groupAnagramsOptimized(word_list)
print(result)