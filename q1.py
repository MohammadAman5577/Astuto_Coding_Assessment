"""
Q1: Stable Character

You are given a string `s`.

In this string, some characters may appear multiple times.

A character is called **stable** if all of its occurrences appear **together as
one continuous group**, without being interrupted by other characters.

Your task is to identify the **first stable character** you encounter when
reading the string from left to right.

If the string does not contain any stable character, return `None`.

Examples:
---------
Input: "aaabccddde"  → Output: 'a'
Input: "abccba"      → Output: 'c'
Input: "aabbcc"      → Output: 'a'
Input: "abc"         → Output: None
Input: "a"           → Output: None

Explanation:
- In "abccba", 'c' appears at positions 2,3 (continuous), while 'a' and 'b'
  are interrupted
- Single character occurrences are not considered stable (must appear at least
  twice)
"""


def first_stable_character(s):
    """
    Find the first stable character in the string.

    A character is stable if:
    1. It appears at least twice
    2. All occurrences are in one continuous group

    Args:
        s (str): Input string

    Returns:
        str or None: First stable character, or None if no stable character exists

    Examples:
        >>> first_stable_character("abccba")
        'c'
        >>> first_stable_character("abc")
        None
        >>> first_stable_character("a")
        None
    """
    stable_chars = set()
    char_positions = {}
    i = 0
    while i < len(s):
        c = s[i]
        if c in char_positions:
            char_positions[c].append(i)
        else:
            char_positions[c] = [i]
        i += 1
    for c, positions in char_positions.items():
        if len(positions) >= 2:
            is_stable = True
            j = 1
            while j < len(positions):
                if positions[j] != positions[j - 1] + 1:
                    is_stable = False
                    break
                j += 1
            if is_stable:
                stable_chars.add(c)
    for c in s:
        if c in stable_chars:
            return c
    return None


if __name__ == "__main__":
    # Test your solution here
    print(first_stable_character("abccba"))  # Should print: c
    print(first_stable_character("abc"))     # Should print: None
    print(first_stable_character("a"))       # Should print: None
