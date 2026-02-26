"""
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.

 

Constraints:

1 <= word.length <= 20
word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
"""

class Solution:
    def isValid(self, word: str) -> bool:
        # If word length is less than 3, it's not valid
        if len(word) < 3:
            return False
        # Convert word to lowercase to handle both upper and lower case uniformly
        word = word.lower()
        # Set of vowels for easy lookup
        vowel = {'a','e','i','o','u'}
        # Counters for vowels and consonants
        v_n = 0  # vowel count
        c_n = 0  # consonant count
        # Iterate over each character in the word
        for i in word:
            # If the character is not a letter or digit, return False
            if not i.isalnum():  # only allows a-z, A-Z, 0-9
                return False
            # If the character is a digit (0–9), skip it
            if i.isdigit():
                continue
            # If the character is a vowel, increase vowel count
            elif i in vowel:
                v_n += 1
            # Otherwise, it’s a consonant (since it's a letter but not a vowel)
            else:
                c_n += 1
        # Word is valid only if it has **at least one vowel** and **at least one consonant**
        if v_n and c_n:
            return True
        else:
            return False
