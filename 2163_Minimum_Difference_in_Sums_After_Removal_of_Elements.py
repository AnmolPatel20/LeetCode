"""
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

 

Example 1:

Input: nums = [3,1,2]
Output: -1
Explanation: Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
Example 2:

Input: nums = [7,9,5,8,1,3]
Output: 1
Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.
 

Constraints:

nums.length == 3 * n
1 <= n <= 105
1 <= nums[i] <= 105
"""

# class Solution:
#     def minimumDifference(self, nums: List[int]) -> int:
#         # l = len(nums)
#         # n = l//3
#         # remove_counter = 0
#         # for i in range(n*2):
#         #     if remove_counter == n:
#         #         break

from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total_len = 3 * n

        # Min sum prefix for first 2n elements
        left_heap = []
        left_sum = 0
        left_min_sum = [0] * total_len

        for i in range(n):
            left_sum += nums[i]
            heappush(left_heap, -nums[i])  # max-heap using negative values
        left_min_sum[n - 1] = left_sum

        for i in range(n, 2 * n):
            heappush(left_heap, -nums[i])
            left_sum += nums[i]
            removed = -heappop(left_heap)  # Remove largest
            left_sum -= removed
            left_min_sum[i] = left_sum

        # Max sum suffix for last 2n elements
        right_heap = []
        right_sum = 0
        right_max_sum = [0] * total_len

        for i in range(total_len - 1, total_len - n - 1, -1):
            right_sum += nums[i]
            heappush(right_heap, nums[i])  # min-heap
        right_max_sum[total_len - n] = right_sum

        for i in range(total_len - n - 1, n - 1, -1):
            heappush(right_heap, nums[i])
            right_sum += nums[i]
            removed = heappop(right_heap)  # Remove smallest
            right_sum -= removed
            right_max_sum[i] = right_sum

        # Compare prefix and suffix sums
        res = float('inf')
        for i in range(n - 1, 2 * n):
            res = min(res, left_min_sum[i] - right_max_sum[i + 1])

        return res
