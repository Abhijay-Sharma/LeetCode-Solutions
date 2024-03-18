class stack:
    def __init__(self):
        self.size=1000
        self.list=[0]*self.size
        self.pointer=0

    def insert(self,value):
        if self.pointer<self.size:
            self.list[self.pointer]=value
            self.pointer+=1
        else:
            print("list is full")

    def pop(self):
        if self.pointer:
            self.pointer = self.pointer - 1
            popped=self.list[self.pointer]
            return popped
        else:
            print("list empty")

    def check_top(self):
        if self.pointer:
            top=self.list[self.pointer-1]
            return top
        else:
            return None

    def clear_stack(self):
        self.list=[0]*self.size
        self.pointer=0
stck=stack()
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hmap={}
        for element in nums2[::-1]:           #reverse traversal
            if not stck.pointer:
                stck.insert(element)
                hmap[element]=-1
            if element<stck.check_top():
                hmap[element]=stck.check_top()
                stck.insert(element)
            else:
                while stck.pointer:
                    if element < stck.check_top():
                        hmap[element] = stck.check_top()
                        stck.insert(element)
                        break
                    stck.pop()
                if not stck.pointer:
                    stck.insert(element)
                    hmap[element] = -1
        result=[]
        stck.clear_stack()
        for number in nums1:
            result.append(hmap[number])
        return result

