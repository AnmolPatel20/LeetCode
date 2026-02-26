"""
Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.

You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.

 

Example 1:

Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]
Explanation:
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.
Example 2:

Input: n = 2, queries = [[0,0]]
Output: [2]
Explanation:
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 109 + 7 is the same, so [2] is returned.
 

Constraints:

1 <= n <= 109
1 <= queries.length <= 105
0 <= starti <= endi < powers.length
"""

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        bin_n = bin(n)[2:]
        # print(bin_n)
        powers = []
        current_power = 1
        for i in range(len(bin_n)-1,-1,-1):
            if bin_n[i] == '1':
                powers.append(current_power)
            current_power *= 2
        # print(powers)

        result = []
        for i in queries:
            left , right = i[0],i[1]
            total_value = 1
            while left<=right:
                if left == right:
                    total_value *= powers[left]
                    break
                total_value = total_value * powers[left] * powers[right]
                left += 1
                right -= 1
            result.append(total_value % (10**9 + 7))
        return result