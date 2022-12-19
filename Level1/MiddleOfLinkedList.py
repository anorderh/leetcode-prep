#https://leetcode.com/problems/middle-of-the-linked-list/description/

#Unoptimized, finding length then iterating to length/2
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        cur = head

        while (cur):
            cur = cur.next
            length += 1
        
        for x in range(length/2):
            head = head.next
        
        return head

# Optimized, two pointers, 1 travels 2x speed. If 2x speed reaches end, other
# pointer is in middle
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        
        return slow
