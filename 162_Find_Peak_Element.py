"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

"""
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m = l + ((r-l)//2)    #Calculating the middle 
            #if the left neighbour is greater
            #which means peak was lie on the left side 
            if m>0 and nums[m]<nums[m-1]:
                r=m-1

            #if right neighbour is greater
            #which means peak was lie on the right side 
            elif m<len(nums)-1 and nums[m]<nums[m+1]:
                l=m+1

            #if both the neighbour are smaller Or we are on the edge
            #Then nums[m] is a peak value 
            else:
                return m