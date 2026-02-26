"""
You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Choose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i], basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.

 

Example 1:

Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
Example 2:

Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.
 

Constraints:

basket1.length == basket2.length
1 <= basket1.length <= 105
1 <= basket1[i], basket2[i] <= 109
"""

from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total_count = count1 + count2

        # Step 1: Check if all fruits can be balanced
        for fruit, total in total_count.items():
            if total % 2 != 0:
                return -1  # Not possible to make baskets equal

        # Step 2: Calculate the excess in each basket
        excess1 = []
        excess2 = []
        for fruit in total_count:
            diff = count1[fruit] - (total_count[fruit] // 2)
            if diff > 0:
                excess1.extend([fruit] * diff)
            elif diff < 0:
                excess2.extend([fruit] * (-diff))

        # Step 3: Sort to minimize cost
        excess1.sort()
        excess2.sort(reverse=True)  # So we can pair smallest with largest

        # Step 4: Get minimum cost fruit in either basket
        min_fruit = min(min(basket1), min(basket2))
        cost = 0
        for a, b in zip(excess1, excess2):
            cost += min(min(a, b), 2 * min_fruit)

        return cost