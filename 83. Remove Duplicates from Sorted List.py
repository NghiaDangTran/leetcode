# //Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        find=head
        curr=find
        past=None
        while (curr!=None):
            if curr.next!=None:
                curr=curr.next
                past=curr
            else: break
            if curr.val==past.val:
                past.next=curr.next
                curr=past
        return curr