"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constrains:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binSearch (nums , target , True)
        right = self.binSearch (nums , target , False)
        return [left,right]

    def binSearch (self , nums , target , leftbias ):
        l, r= 0, len(nums)-1    #Initilize left and right pointer
        i=-1   #Default index if Target is not found in array

        while l<=r:
            m=(l+r)//2     #calculate the midddle index 
            if target > nums[m]:
                l=m+1
            elif target < nums[m]:
                r=m-1
            else:
                i=m   #if looking for the first occurenece
                if leftbias:
                    r=m-1   #move left to cintinue searching
                else: 
                    l=m+1    #move right to continue searching
        return i