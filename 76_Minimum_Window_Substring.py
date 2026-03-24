"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        mapT = [0]*256
        mapS = [0]*256

        #COunt Character to T
        for ch in t:
            mapT[ord(ch)] += 1

        left = 0
        min_len = float('inf')
        min_start = 0

        for right in range(len(s)):
            mapS[ord(s[right])] += 1

            while self.contains( mapS, mapT):
                #Shrink win while it is valid
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                mapS[ord(s[left])] -= 1
                left += 1
        return "" if min_len == float('inf') else s[min_start : min_start + min_len]

    def contains(self,mapS,mapT):
        for i in range(256):
            if mapT[i] > mapS[i]:
                return False
        return True