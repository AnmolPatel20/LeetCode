"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise. 

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: left (l) at the beginning, right (r) at the end of the string
        l , r = 0 , len(s)-1
        
        # Loop until the two pointers meet
        # Alphanumeric means a character is either (A-Z or a-z) or (0-9)
        while l<r :
            #Move left pointer forward if current character is not alphanumeric
            while l<r  and not self.alphaNum(s[l]):
                l+=1
            #Move right pointer backward if current character is not alphanumeric
            while r>l  and not self.alphaNum(s[r]):
                r-=1
            # Compare characters at left and right (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False   # Not a Palindrome 
            # Move both pointers closer towards the center
            l,r = l+1, r-1
        return True   # It is a Palindrome
    
    # Helper function to check if a character is alphanumeric
    def alphaNum(self,c):
        # ord returns the ASCII number
        return(ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or 
               ord('0') <= ord(c) <= ord('9'))