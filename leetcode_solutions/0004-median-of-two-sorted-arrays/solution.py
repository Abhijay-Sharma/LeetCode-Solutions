class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """ 
        merged_nums=[]
        i=0        #nums1 traverser
        k=0         #nums2 traverser
        len1=len(nums1) #length of array1
        len2=len(nums2) #length of array2

        while i<len1 and k<len2:
            if nums1[i] <= nums2[k]:
                value=nums1[i]
                merged_nums.append(value)
                i+=1
            else:
                merged_nums.append(nums2[k])
                k+=1
        while i<len1:
            merged_nums.append(nums1[i])
            i += 1
        while k<len2:
            merged_nums.append(nums2[k])
            k += 1

        length=len(merged_nums)
        if length%2!=0:
            return merged_nums[length//2]
        else:
            sum=merged_nums[(length//2)]+merged_nums[(length//2)-1]
            return sum/2.0

