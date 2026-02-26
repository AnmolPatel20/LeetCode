""" 
9. Palindrome Number

Easy
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1 

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Step 1: Negative numbers are not palindrome
        # Also, if number ends with 0 and is not 0, it cannot be a palindrome
        if x<0 or (x%10==0 and x!=0):
            return False

        rev=0  # This will store the reversed half of the number
        # Step 2: Reverse only the second half of the number
        
        while x>rev:
            rev=rev*10+x%10 # Add the last digit of x to rev
            x//=10  # Remove the last digit from x
        # For even length numbers, x == rev
        # For odd length numbers, x == rev // 10 (middle digit is ignored)
        return x==rev or x==rev //10