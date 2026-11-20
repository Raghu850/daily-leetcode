# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None:
        #     return head
        # temp=head
        # while temp!=None:
        #     runner=temp
        #     while runner.next!=None:
        #         if runner.next.val==temp.val:
        #             runner.next=runner.next.next
        #         else:
        #             runner=runner.next
        #     temp=temp.next
        # return head
        cur=head
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head