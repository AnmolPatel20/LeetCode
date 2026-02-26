"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0   # This keeps track of where the next non-zero number should go

        # Go through each number in the list
        for r in range(len(nums)):
            if nums[r]:
            # If the number is not zero, swap it with the number at index 'l'
                nums[r],nums[l] = nums[l],nums[r]
                l+=1    # Move 'l' to the next spot
        return nums