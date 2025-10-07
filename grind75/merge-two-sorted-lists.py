# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = ListNode()
        list3head = list3
        
        if list2 is None:
            return list1
        
        if list1 is None:
            return list2

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
            else:
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
        
        if list2 is None and list1 is not None:
            list3.next = list1
        elif list1 is None and list2 is not None:
            list3.next = list2
        
        return list3head.next
