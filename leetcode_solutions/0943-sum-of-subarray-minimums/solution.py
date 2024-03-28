class stack:
    def __init__(self):
        self.list=[0]*10
        self.pointer=0

    def insert(self,value):
        self.list[self.pointer]=value
        self.pointer+=1
        self.list+=[0]*3

    def pop(self):
        if self.pointer:
            self.pointer = self.pointer - 1
            popped=self.list[self.pointer]
            self.list[self.pointer]=0
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
        self.list=[0]*10
        self.pointer=0

    def is_empty(self):
        return self.pointer == 0



class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        listt=stack()
        result=0
        len_of_arr=len(arr)
        Mod=10**9+7
        for i in range(len_of_arr):
            while not listt.is_empty() and arr[i]<=listt.check_top()[1]:
                index , value = listt.pop()
                left = index - listt.check_top()[0] if not listt.is_empty() else index + 1
                right = i - index
                result += value * left * right
                result %= Mod
            listt.insert((i,arr[i]))


        while not listt.is_empty():
            index, value = listt.pop()
            left = index - listt.check_top()[0] if not listt.is_empty() else index + 1
            right = len_of_arr - index
            result += value * left * right
            result %= Mod


        return result
            
