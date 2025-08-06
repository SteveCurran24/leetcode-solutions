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

        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            outList = list1
            list1=list1.next
        else:
            outList = list2
            list2=list2.next

        ptr = outList

        while list1 and list2:
            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next

            ptr = ptr.next
        
        if not list1:
            ptr.next = list2
        elif not list2:
            ptr.next = list1
        return outList