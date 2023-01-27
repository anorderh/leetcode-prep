# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        # Uses curr to relink list
        # Uses head to identify when list is iterated

        while head:
            curr = head         # track head
            head = head.next    # progress head

            curr.next = prev   # curr.next is previous
            prev = curr         # assign prev w/ curr
        
        return prev        
