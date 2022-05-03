# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from asyncio.windows_events import NULL
from curses.ascii import NUL
from pickle import NONE


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  naiev thinking
        # temp= ListNode(0,head)
        # curr=temp.next
        # pst=temp
        # ok=True
        # while curr!=None:

        #     while curr!=None and curr.next!=None and curr.val==curr.next.val:

        #         curr=curr.next

        #         ok=False

        #     if not ok:
        #         pst.next=curr.next
        #         ok=True
        #     else:
        #         pst=curr

        #     curr=curr.next
        # it work but kinda slow compare to orther work so let see what we can fix
        # first do we really need to check the curr!=None in the second loop because it will always anw
        # second can we do better for the flag ok one thing we can see its that we can change it by compare the pst.next and the curr if they are the same
        temp = ListNode(0, head)
        curr = temp.next
        pst = temp

        while curr != None:

            while curr.next != None and curr.val == curr.next.val:

                curr = curr.next

            if pst.next == curr:
                pst = curr

            else:
                pst.next = curr.next
            curr = curr.next

        return temp.next
