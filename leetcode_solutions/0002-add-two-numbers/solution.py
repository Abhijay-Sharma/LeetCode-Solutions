# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a,b=l1,l2
        carry,summ=0,0
        answer=ListNode()
        x=answer
        while a or b or carry:
            summ+=carry
            carry=0
            if a:
                summ+=a.val
                a=a.next
            if b:
                summ+=b.val
                b=b.next
            carry=summ//10
            x.val=summ%10
            if a or b or carry:
                x.next=ListNode()
                x=x.next
            summ=0
            
        return answer


