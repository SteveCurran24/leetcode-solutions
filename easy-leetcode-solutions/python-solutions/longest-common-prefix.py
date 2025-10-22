class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        solution = ""
        for k in range(len(strs[0])):
            c = strs[0][k]
            for i in range(1, len(strs)):
                if k >= len(strs[i]) or strs[i][k] != c:
                    return solution
            solution += c
        return solution
