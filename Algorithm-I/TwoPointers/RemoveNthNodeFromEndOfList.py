# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan&id=algorithm-i

# Utilizing 'fast' and 'slow' pointers
# Fast has n steps head-start,
# Meaning when fast.next iterates to None, slow.next has iterated to node to be removed

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointers
        slow = head
        fast = head
        # Giving 'fast' a headstart
        for x in range(n):
            fast = fast.next

        if fast is None: # 'n' is list's starting element. 
            head = head.next
        else: # iterate both ptrs until n'th node from END reached
            while fast.next != None:
                slow = slow.next
                fast = fast.next
        
            # skip node, removing from list
            slow.next = slow.next.next

        return head
