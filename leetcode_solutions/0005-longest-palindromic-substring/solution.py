class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length_of_string=len(s)
        pallindrome=""
        length_of_longest_pallindrome=0
        for i in range (length_of_string):
            #for odd
            l , r = i , i  #l = left pointer and r = right pointer
            while l>=0 and r < length_of_string and s[l]==s[r]:
                if (r - l + 1)>length_of_longest_pallindrome:
                    pallindrome = s[l:r + 1]
                    length_of_longest_pallindrome=r-l+1
                l-=1
                r+=1
            #for even
            l ,r =i ,i+1
            while l>=0 and r < length_of_string and s[l]==s[r]:
                if (r - l + 1)>length_of_longest_pallindrome:
                    pallindrome = s[l:r + 1]
                    length_of_longest_pallindrome=r-l+1
                l-=1
                r+=1


        return pallindrome
