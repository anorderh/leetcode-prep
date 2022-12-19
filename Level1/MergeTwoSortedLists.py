# https://leetcode.com/problems/merge-two-sorted-lists/description/

# 1st submission, unoptimized, beats 54% of cases, abysmal memory usage
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (list1 is None and list2 is None):
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2

# 2nd submission, beats 80% of cases
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = cur = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        
        if list1 or list2:
            cur.next = list1 if list1 else list2
        
        return head.next
