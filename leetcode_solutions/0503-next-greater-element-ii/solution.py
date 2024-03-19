class stack:
    def __init__(self):
        self.size=10000
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

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]       # we will reverse it in end
        for element in nums[::-1]:
            if not stck.pointer:
                result.append(-10000)
                stck.insert(element)
            elif element<stck.check_top():
                result.append(stck.check_top())
                stck.insert(element)
            else:
                while stck.pointer:
                    if element<stck.check_top():
                        result.append(stck.check_top())
                        stck.insert(element)
                        break
                    stck.pop()
                if not stck.pointer:
                    stck.insert(element)
                    result.append(-10000)

        result=result[::-1]

        for i in range(len(result)):
            if result[i]==-10000:
                for j in nums[:i]:
                    if j>nums[i]:
                        result[i]=j
                        break
        for x in range(len(result)):
            if result[x]==-10000:
                result[x]=-1
        stck.clear_stack()
        return result
            
