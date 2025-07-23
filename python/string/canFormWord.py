def can_form_word(word: str, word_map: dict[str, int]) -> bool:
    """
    Check if the given word can be formed using the characters in the word map.
    This function modifies the input `word_map` by decrementing character counts.

    Args:
        word (str): The word to form.
        word_map (dict[str, int]): Dictionary of available characters and their counts.

    Returns:
        bool: True if the word can be formed, False otherwise.

    Example:
    input: word = "cab", word_map = {'a': 2, 'b': 1, 'c': 1})
    output: True
    """
    for char in word:
        if char not in word_map or word_map[char] == 0:
            return False
        word_map[char] -= 1

    return True

word_map = {'a': 2, 'b': 1, 'c': 1}
word = "cab"
print(can_form_word(word, word_map))