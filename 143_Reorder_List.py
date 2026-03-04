"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """     
        if head is None or head.next is None:
            return  
        p1 = head
        p2 = head

        while p2.next is not None and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        
        preMid = p1
        preCurr = p1.next

        while preCurr.next is not None:
            curr = preCurr.next
            preCurr.next = curr.next
            curr.next = preMid.next
            preMid.next = curr

        x = head
        y = preMid.next
        while x is not preMid:
            preMid.next = y.next
            y.next = x.next
            x.next = y 
            x = y.next
            y = preMid.next