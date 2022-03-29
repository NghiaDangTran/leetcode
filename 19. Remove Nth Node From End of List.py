# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#          the reason we need dummy node is 
#         prev is child of dummy which create runtime dummy and prev point to the same address 
#  so when run time we change the prev it actually change the value in the address of the dummy
#  kinda cheating but we dont ha
        dummy= ListNode(0,head)
        prev=dummy
        curr=head
        
        for _ in range(n):
            curr=curr.next
            
        while curr:
            curr=curr.next
            prev=prev.next
            
        prev.next= prev.next.next
        return dummy.next