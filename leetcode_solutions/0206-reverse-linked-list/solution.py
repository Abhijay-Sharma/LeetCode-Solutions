# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head or not head.next:
        # # If the list is empty or has only one element, no need to reverse
        #     return
        front,previous=None,None
        a=head
        while a:
            front=a.next
            a.next=previous
            previous=a
            a=front
        return previous
