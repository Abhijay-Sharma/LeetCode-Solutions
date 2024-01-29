# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length1,length2=0,0
        a,b=headA,headB
    
        while a or b:
            if a:
                length1+=1
                a=a.next
            if b:
                length2+=1
                b=b.next
        if length1>=length2:
            difference=length1-length2
            a,b=headA,headB
            for i in range(difference):
                a=a.next
            while a:
                if a==b:
                    return a
                a=a.next
                b=b.next
        else:
            difference=length2-length1
            a,b=headA,headB
            for i in range(difference):
                b=b.next
            while b:
                if a==b:
                    return a
                a=a.next
                b=b.next  
