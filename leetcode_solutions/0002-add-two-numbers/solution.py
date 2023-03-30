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
        first=l1
        second=l2
        carry=0
        new=ListNode()
        temp=new
        while first or second:
            result=carry
            if first:
                result+=first.val
                first=first.next
            if second:
                result+=second.val
                second=second.next
            carry=result//10
            temp.val=result%10
            if not (first or second):
                if carry==0:
                    break
                else:
                    temp.next=ListNode()
                    temp=temp.next
                    temp.val=carry
                    break

            temp.next=ListNode()
            temp=temp.next
        return new


