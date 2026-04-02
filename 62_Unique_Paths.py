"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]

        #iterate over the grid
        for i in range(m):
            for j in range(n):

                #if we are at the first row and first column 
                #there is only one way to reach that cell (i.e = 1)
                if i==0 or j==0:
                    grid[i][j] = 1
                else:
                    #memoize the no. of ways to reach that cell
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]

        #return the number of ways to reach last cell 
        #[m-1][n-1] due to 0th indexing

        return grid[m-1][n-1]