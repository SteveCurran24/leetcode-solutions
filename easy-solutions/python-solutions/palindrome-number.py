class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = x%10
        original = x
        if(x>0):
            while(x/10>0):
                x=x/10
                reverse=reverse*10 + x%10
        
        if(reverse == original):
            return True
        
        return False
            

        