#straitforward. Uses a dictionary and a stack.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        paren_pairs = {'}':'{' ,']': '[',')': '('}
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in "}])":
                if not stack or stack.pop() != paren_pairs[char]:
                    return False
        if not stack:
            return True
        else:
            return False
               
