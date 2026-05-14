"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        slist = list(s)

        left = 0
        right = len(slist)-1

        while left<right:
            #move left pointer
            while left < right and slist[left] not in vowels:
                left += 1
            
            #move right pointer
            while left < right and slist[right] not in vowels:
                right -= 1
            
            slist[left],slist[right] = slist[right],slist[left]

            left+=1
            right-=1

        return "".join(slist)