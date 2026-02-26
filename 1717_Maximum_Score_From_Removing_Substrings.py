"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        total_score = 0

        def scoreOf(ms,c1,c2,point,total_score):
            stack.append(ms[0])
            for i in range(1,len(ms)):
                if stack:
                    if ms[i] == c2 and stack[-1] == c1:
                        stack.pop()
                        total_score += point
                        continue
                stack.append(ms[i])
            return total_score,stack
        
        if x>y:
            total_score,stack = scoreOf(s,'a','b',x,total_score)
            s = ''.join(stack)
            if s:
                stack = []
                total_score,stack = scoreOf(s,'b','a',y,total_score)

        else:
            total_score,stack = scoreOf(s,'b','a',y,total_score)
            s = ''.join(stack)
            if s:
                stack = []
                total_score,stack = scoreOf(s,'a','b',x,total_score)

        
        
        return total_score