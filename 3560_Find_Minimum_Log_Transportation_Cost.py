"""
You are given integers n, m, and k.

There are two logs of lengths n and m units, which need to be transported in three trucks where each truck can carry one log with length at most k units.

You may cut the logs into smaller pieces, where the cost of cutting a log of length x into logs of length len1 and len2 is cost = len1 * len2 such that len1 + len2 = x.

Return the minimum total cost to distribute the logs onto the trucks. If the logs don't need to be cut, the total cost is 0.

 

Example 1:

Input: n = 6, m = 5, k = 5

Output: 5

Explanation:

Cut the log with length 6 into logs with length 1 and 5, at a cost equal to 1 * 5 == 5. Now the three logs of length 1, 5, and 5 can fit in one truck each.

Example 2:

Input: n = 4, m = 4, k = 6

Output: 0

Explanation:

The two logs can fit in the trucks already, hence we don't need to cut the logs.

 

Constraints:

2 <= k <= 105
1 <= n, m <= 2 * k
The input is generated such that it is always possible to transport the logs.

"""

class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        def get_min_cost(length):
            if length <= k:  #id log already fits , no cutting needed
                return 0

            min_cost = float('inf')
            #try all single cuts: divide into two parts a and b
            for i in range(1,length):
                a=i
                b=length-i
                #check both parts fit in truck
                if a <=k and b<=k:
                    min_cost = min(min_cost,a*b)
                    
            #if no valid cut , return -1
            return min_cost if min_cost != float('inf') else -1

        min_total_cost = float('inf')
        #try all possible ways to divide the two logs into a+b <=3 pieces
        for a in range(1,3):    #a= no of pieces for log n
            for b in range(1,3):  #= for log m
                if a+b > 3:
                    continue
                if n> a*k or m>b*k :
                    continue
                #if split log n and log m into 2 parts, calculate itscutting cost
                cost=0
                if a == 2:
                    cost += get_min_cost(n)
                if b == 2:
                    cost += get_min_cost(m)

                min_total_cost = min(min_total_cost , cost)
        return 0 if min_total_cost == float('inf') else min_total_cost