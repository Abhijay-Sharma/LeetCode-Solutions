"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        a=head
        while a:                #creating duplicates
            temp=a.next
            a.next=Node(a.val)
            a.next.next=temp
            a=temp
        
        a=head
        while a and a.next:        #copying randoms
            temp=a.random
            if temp:        #checking if random is null
                a.next.random=temp.next
            a=a.next.next

        a=head
        b=head.next
        answer=b
        while a  and b and b.next:
            a.next=b.next
            a=a.next
            b.next=b.next.next
            b=b.next
        a.next=None

        return answer
