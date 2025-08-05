class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={')':'(', ']':'[', '}':'{'}
        for i, symbol in enumerate(s):
            if symbol in "({[" and i+1 < len(s):
                stack.append(symbol)
            elif symbol in ")}]":
                if not stack:
                    return False
                popped_symbol = stack.pop()
                if pairs[symbol] != popped_symbol:
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False
