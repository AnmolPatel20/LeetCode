"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resultList = []

        def backtrack(tempList):
            #if permutation is complete
            if len(tempList) == len(nums):
                resultList.append(tempList[:])  #make a copy
                return
            
            for number in nums:
                #skip if already used
                if number in tempList:
                    continue
                
                #choose
                tempList.append(number)
                #explore
                backtrack(tempList)
                #undo(backtrack)
                tempList.pop()
            
        backtrack([])
        return resultList