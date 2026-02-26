"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
 

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
 

Constraints:

3 <= num.length <= 1000
num only consists of digits.
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_no = ""
        curr_max = ''
        count = 0
        for i in range(len(num)):
            if curr_max == num[i]:
                count += 1
            else:
                curr_max = num[i]
                count = 1
            if count == 3:
                if max_no == "":
                    max_no = curr_max*3
                else:
                    max_no = curr_max*3 if int(max_no[0]) < int(curr_max[0]) else max_no
                count = 0 
                curr_max = ''

        return max_no