"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
 
Constraints:

1 <= text.length <= 104
text consists of lower case English letters only

"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}

        for ch in text:
            count[ch] = count.get(ch,0) + 1

        #smallest available req count determines max ballons we can make
        return min(
            count.get('b',0),  #need only 1 of b,a,n
            count.get('a',0),
            count.get('l',0)//2,   #need 2 of l and o
            count.get('o',0)//2,
            count.get('n',0)
        )