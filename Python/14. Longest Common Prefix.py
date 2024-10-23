class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        temp = strs[0]
        for i in range(len(temp)):
            for word in strs[1:]:
                if (i == len(word) or word[i] != temp[i]):
                    return temp[0:i]

        return temp