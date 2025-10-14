# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slowptr = head
        fastptr = head

        if head and fastptr.next is None:
            return False

        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if fastptr == slowptr:
                return True
        
        return False
