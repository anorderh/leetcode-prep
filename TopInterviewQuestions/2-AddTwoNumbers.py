# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Leetcode solution, iterative
     def addTwoNumbers(self, l1, l2):
        carry = 0              # Storing total sum per digit
        res = n = ListNode(0)  # 'Res' -> head, 'n' -> dummy ptr

        while l1 or l2 or carry:    # While numbes not iterated or carry present
            if l1:                  # Add & iterate l1 if present
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val     # Add & iterate l2 if present
                l2 = l2.next

            carry, val = divmod(carry, 10)      # Calculating carry & digit place's val
            n.next = n = ListNode(val)          # Creating new node from val & incrementing
        return res.next

