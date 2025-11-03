# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return 0

        lead_pointer = head
        middle = head

        while lead_pointer and lead_pointer.next:
            middle = middle.next
            lead_pointer = lead_pointer.next.next
        
        return middle
