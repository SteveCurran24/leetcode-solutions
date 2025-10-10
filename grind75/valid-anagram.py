class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_counts={}

        if len(s)!=len(t):
            return False

        for char in s:
            if char in letter_counts:
                letter_counts[char]+=1
            else:
                letter_counts[char]=1

        for char in t:
            if char  not in letter_counts:
                return False
            else:
                letter_counts[char]-=1
                if letter_counts[char]<0:
                    return False

        for count in letter_counts.values():
            if count !=0:
                return False
        
        return True
