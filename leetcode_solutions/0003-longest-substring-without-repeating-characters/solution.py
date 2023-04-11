class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
          counter=0
          checker=0
          t=0
          checkdict={}
          for i in s:
            t+=1
            checkdict[i]=0
            for j in s[t:]:
              if j not in checkdict:
                counter+=1
                checkdict[j]=0
              else:
                break
            if counter>checker:
              checker=counter
            counter=0
            checkdict={}
          return checker+1
        else:
          return 0
