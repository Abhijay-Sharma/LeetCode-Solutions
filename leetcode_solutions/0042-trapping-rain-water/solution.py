class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_ptr=0
        right_ptr=len(height)-1
        leftmax,rightmax=0,0
        result=0
        while left_ptr<=right_ptr:
            if height[left_ptr]<=height[right_ptr]:
                if leftmax<=height[left_ptr]:
                    leftmax=height[left_ptr]

                else:
                    result+=leftmax-height[left_ptr]
                left_ptr+=1
            else:
                if rightmax<=height[right_ptr]:
                    rightmax=height[right_ptr]
                else:
                    result+=rightmax-height[right_ptr]
                right_ptr-=1
        return result
