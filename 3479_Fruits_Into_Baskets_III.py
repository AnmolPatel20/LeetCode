"""
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

 

Example 1:

Input: fruits = [4,2,5], baskets = [3,5,4]

Output: 1

Explanation:

fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.

Example 2:

Input: fruits = [3,6,1], baskets = [6,4,7]

Output: 0

Explanation:

fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.

 

Constraints:

n == fruits.length == baskets.length
1 <= n <= 105
1 <= fruits[i], baskets[i] <= 109
"""

import bisect
from typing import List

class Solution:
  def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
    n = len(fruits)
    if n == 0:
        return 0
    
    # A large value to represent an invalid or used basket
    inf = float('inf')

    # Step 1: Prepare basket data by creating (capacity, original_index) pairs
    # and sorting by capacity. This allows for efficient binary search.
    b_sorted = sorted([(baskets[i], i) for i in range(n)])
    
    # Separate into two lists for easier access
    sorted_capacities = [c for c, i in b_sorted]
    original_indices = [i for c, i in b_sorted]

    # Step 2: Build a Segment Tree for Range Minimum Query (RMQ).
    # The tree finds the minimum original_index in a given range of the sorted list.
    # The tree is 1-indexed and stores (value, position) pairs.
    tree = [(inf, -1)] * (4 * n)

    def build(v: int, tl: int, tr: int):
        """Builds the segment tree recursively."""
        if tl == tr:
            tree[v] = (original_indices[tl], tl)
        else:
            tm = (tl + tr) // 2
            build(2 * v, tl, tm)
            build(2 * v + 1, tm + 1, tr)
            # An internal node stores the minimum of its children
            tree[v] = min(tree[2 * v], tree[2 * v + 1])

    def query(v: int, tl: int, tr: int, l: int, r: int):
        """Queries the tree for the minimum value in the range [l, r]."""
        if l > r:
            return (inf, -1)
        if l == tl and r == tr:
            return tree[v]
        tm = (tl + tr) // 2
        left_res = query(2 * v, tl, tm, l, min(r, tm))
        right_res = query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
        return min(left_res, right_res)

    def update(v: int, tl: int, tr: int, pos: int, new_val: float):
        """Updates the value at a specific position in the tree."""
        if tl == tr:
            tree[v] = (new_val, pos)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                update(2 * v, tl, tm, pos, new_val)
            else:
                update(2 * v + 1, tm + 1, tr, pos, new_val)
            tree[v] = min(tree[2 * v], tree[2 * v + 1])

    build(1, 0, n - 1)

    # Step 3: Process fruits and place them in baskets
    unplaced_count = 0
    for fruit in fruits:
        # Find the first basket with capacity >= fruit using binary search.
        # 'k' is the starting index in our capacity-sorted list.
        k = bisect.bisect_left(sorted_capacities, fruit)

        if k == n:
            # No basket has enough capacity.
            unplaced_count += 1
            continue

        # Query the segment tree for the available basket with the smallest
        # original index. The candidates are in the range [k, n-1].
        min_original_idx, pos_in_sorted_array = query(1, 0, n - 1, k, n - 1)

        if min_original_idx == inf:
            # All suitable baskets are already used.
            unplaced_count += 1
        else:
            # A basket is found. Mark it as used by updating its value in the
            # tree to infinity.
            update(1, 0, n - 1, pos_in_sorted_array, inf)
            
    return unplaced_count
    