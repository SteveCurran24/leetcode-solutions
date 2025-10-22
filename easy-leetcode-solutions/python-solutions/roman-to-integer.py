class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        for i in range(len(s)):
            match s[i]:
                case 'I':
                    if i+1 < len(s) and (s[i+1] == 'V' or s[i+1] == 'X'):
                        total-=1
                    else:
                        total+=1
                case 'V':
                    total+=5
                case 'X':
                    if i+1 < len(s) and s[i+1] == 'L' or s[i+1] == 'C':
                        total-=10
                    else:    
                        total+=10
                case 'L':
                    total+=50
                case 'C':
                    if i+1 < len(s) and s[i+1] == 'D' or s[i+1] == 'M':
                        total-=100
                    else:
                        total+=100
                case 'D':
                    total+=500
                case 'M':
                    total+=1000
        return total
                