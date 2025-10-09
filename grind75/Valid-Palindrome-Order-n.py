#this is my order N solution to Valid Palindrome. It is order n because it creates a sanitized list first and then compares
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_cleaned=[]
        for letter in s:
            if letter.lower().isalnum():
                s_cleaned.append(letter.lower())
        j=len(s_cleaned)-1
        i=0

        while i<j:
            if s_cleaned[i] != s_cleaned[j]:
                return False
            i+=1
            j-=1

        return True
