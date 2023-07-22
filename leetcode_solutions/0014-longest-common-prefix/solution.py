class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix=""
        for i in range (len(strs[0])):
            for s in strs:
                if i == len(s) or s[i]!= strs[0][i]:
                    return longest_prefix
            longest_prefix+=strs[0][i]
        return longest_prefix
