"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
 
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures) #result array, default '0'
        stack = [] #Storing Pair [temp,index]

        for i, t in enumerate(temperatures): #loop through days 
            #check if current temp is warmer than stack top
            while stack and t>stack[-1][0]:
                stackTemp , stackIndex = stack.pop()  #pop colder days
                result [stackIndex] = (i - stackIndex)  #days waited 
            stack.append([t,i]) #pust current day
        return result