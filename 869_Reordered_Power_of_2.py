"""
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109
"""
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Convert n to a sorted string of digits
        target = sorted(str(n))
        
        # Check all powers of 2 up to 2^30
        for i in range(31):
            power_str = sorted(str(1 << i))  # 1 << i = 2^i
            if power_str == target:
                return True
        return False
