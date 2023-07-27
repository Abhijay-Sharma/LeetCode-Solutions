class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count, current_count =0,0
        for number in nums:
            if number==1:
                current_count+=1
                if current_count>max_count:
                    max_count=current_count
            else:
                current_count=0
        return max_count
