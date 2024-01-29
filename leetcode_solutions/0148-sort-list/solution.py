# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merger(node1,node2):
            temp=ListNode()
            a=node1
            b=node2
            c=temp
            while a and b:
                if a.val<b.val:
                    c.val=a.val
                    a=a.next
                else:
                    c.val = b.val
                    b = b.next
                if a or b:
                    c.next = ListNode()
                    previous = c
                    c = c.next
            while a:
                c.val = a.val
                a = a.next
                c.next = ListNode()
                previous = c
                c = c.next

            while b:
                c.val = b.val
                c.next = ListNode()
                previous = c
                c = c.next
                b = b.next
            previous.next=None          #it removes one extra node created in merged ll in end
            return temp

        def middle_merge_helper(headnode):
            fast = headnode.next       #because in merge sort middle element is different then whats normally in tortoise hare method
            slow = headnode
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def merge_sort(head):
            if head and head.next:
                lefthead=head              #left half
                righthead=middle_merge_helper(head)     #right half
                temp=righthead.next
                righthead.next=None
                righthead=temp

                lefthead=merge_sort(lefthead)
                righthead=merge_sort(righthead)

                newhead=merger(lefthead,righthead)
                return newhead
            else:
                return head
        return merge_sort(head)
        
