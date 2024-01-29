# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(node):
            front, previous = None, None
            x = node
            while x:
                front = x.next
                x.next = previous
                previous = x
                x = front
            return previous
        a=head
        length=1
        current_head=head       #head of first part
        tail=ListNode(-123) #dummy
        j=0
        answer_node=head
        while a and a.next:
            a=a.next
            length+=1
            if length==k:
                temp=current_head
                a_next=a.next
                a.next=None
                current_head=reverse(current_head)
                tail.next=current_head
                j+=1
                if j==1:
                    answer_node=a
                a=temp
                a.next=a_next
                length=0
                tail=a
                current_head=a_next
        return answer_node

            
