import math
class Solution(object):
    def longestPalindrome(self, s):        
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        if len(s)==1:
            return 1
        letters={}
        palindrome_len=0
        is_odd = False

        for i in s:
            if i in letters:
                letters[i]+=1
            else:
                letters[i]=1
        
        for i in letters:
            if letters[i]%2 == 0:
                palindrome_len += (letters[i])
            else:
                is_odd = True
                palindrome_len += (letters[i] - 1)
        
        if is_odd:
            palindrome_len+=1
        
        return palindrome_len

            


            
