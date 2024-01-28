# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow,fast=head,head           #using tortoise hare to get middle
        while fast and fast.next:       # O(N/2)
            fast=fast.next.next
            slow=slow.next
        def reverse(head):
            front,previous=None,None
            a=head
            while a:
                front=a.next
                a.next=previous
                previous=a
                a=front
            return previous

        slow=reverse(slow)
        pointer1=head
        pointer2=slow
        while pointer1 and pointer1.next:
            if pointer1.val==pointer2.val:
                pointer1=pointer1.next
                pointer2=pointer2.next
            else:
                reverse(slow)
                return False
        reverse(slow)
        return True
        
        
