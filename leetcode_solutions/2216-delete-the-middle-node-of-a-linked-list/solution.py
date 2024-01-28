# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast,slow=head,head
        prev_slow=None
        while fast and fast.next:
            fast=fast.next.next
            prev_slow=slow
            slow=slow.next
        if prev_slow:
            prev_slow.next=slow.next
        else:
            head=head.next
        return head

