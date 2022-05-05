# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Dumppy = ListNode(0, None)
        data = Dumppy

        while list1 and list2:
            if list1.val < list2.val:
                data.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                data.next = ListNode(list2.val, None)
                list2 = list2.next

        while list1:
            data.next = ListNode(list1.val, None)
            list1=list1.next
        while list2:
            data.next = ListNode(list2.val, None)
            list2=list2.next

        return Dumppy.next
