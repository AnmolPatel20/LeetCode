"""
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

 

Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:



The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[1,0],[0,0]]

Output: 1

Explanation:



The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid
"""

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        area = 0
        l = 1
        left_l = -1
        right_l = -1
        b = 1
        top_b = -1
        bot_b = -1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:

                    if left_l == -1 and right_l == -1:
                        left_l , right_l = j , j+1
                        top_b , bot_b = i , i+1
                    else:
                        left_l = min(left_l,j)
                        right_l = max(right_l,j+1)
                        bot_b = max(bot_b,i+1)       

            l = max(l , right_l-left_l)
        b = bot_b - top_b
        return l * b