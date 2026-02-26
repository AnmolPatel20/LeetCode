"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""  #store Longest Palindrome
        resultLen = 0  #len of longest palindrome

        for i in range(len(s)):
            #For odd Length
            l,r = i,i
            #Expand outwards while char matchs
            while l>=0 and r<len(s) and s[l]==s[r]:
                #to check current palindrome is longer than prev one
                if(r-l+1) > resultLen:
                    result = s[l:r+1]  #update result
                    resultLen = r-l+1   #update length
                l -= 1 #move left & right pointer outwards
                r += 1

            #For even Length
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1) > resultLen:
                    result = s[l:r+1]
                    resultLen = r-l+1
                l -= 1
                r += 1

        return result