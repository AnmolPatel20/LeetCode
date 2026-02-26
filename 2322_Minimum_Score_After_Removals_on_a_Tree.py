"""
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

Get the XOR of all the values of the nodes for each of the three components respectively.
The difference between the largest XOR value and the smallest XOR value is the score of the pair.
For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
Return the minimum score of any possible pair of edge removals on the given tree.

 

Example 1:


Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
Output: 9
Explanation: The diagram above shows a way to make a pair of removals.
- The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
- The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
- The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
It can be shown that no other pair of removals will obtain a smaller score than 9.
Example 2:


Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
Output: 0
Explanation: The diagram above shows a way to make a pair of removals.
- The 1st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
- The 2nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
- The 3rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
We cannot obtain a smaller score than 0.
 

Constraints:

n == nums.length
3 <= n <= 1000
1 <= nums[i] <= 108
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.

"""

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        xor = [0] * n
        parent = [-1] * n
        tin = [0] * n
        tout = [0] * n
        time = [0]

        # DFS to calculate subtree XOR and in/out times
        def dfs(u, par):
            xor[u] = nums[u]
            parent[u] = par
            time[0] += 1
            tin[u] = time[0]
            for v in graph[u]:
                if v != par:
                    dfs(v, u)
                    xor[u] ^= xor[v]
            time[0] += 1
            tout[u] = time[0]

        dfs(0, -1)
        total_xor = xor[0]
        ans = float('inf')

        # Helper: Check if u is ancestor of v
        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        # Try all pairs of edges (node-parent relationships)
        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = i, j
                if is_ancestor(a, b):
                    x = xor[b]
                    y = xor[a] ^ xor[b]
                    z = total_xor ^ xor[a]
                elif is_ancestor(b, a):
                    x = xor[a]
                    y = xor[b] ^ xor[a]
                    z = total_xor ^ xor[b]
                else:
                    x = xor[a]
                    y = xor[b]
                    z = total_xor ^ xor[a] ^ xor[b]

                max_x = max(x, y, z)
                min_x = min(x, y, z)
                ans = min(ans, max_x - min_x)

        return ans
