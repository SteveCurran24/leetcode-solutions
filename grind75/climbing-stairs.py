class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<=1:
            return 1
        
        oneStep = 1
        twoStep = 2

        for i in range(3, n+1):
            temp = twoStep
            twoStep = oneStep + twoStep
            oneStep = temp
        
        return twoStep
