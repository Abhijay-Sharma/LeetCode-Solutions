# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ahead=head
        behind=head
        for i in range(n+1):
            if ahead:
                ahead=ahead.next
            else:
                head=head.next
                return head
        while ahead:
            ahead=ahead.next
            behind=behind.next
        behind.next=behind.next.next
        return head

        
