# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head:
            length=1
            a=head
            while a:
                a=a.next
                length+=1

            k=k%(length-1)
            if k==0:
                return head
            a=head
            for i in range(length-k-2):
                a=a.next
            temp=a.next
            a.next=None
            answer_node=temp
            while temp and temp.next:
                temp=temp.next
            temp.next=head
            return answer_node
        
