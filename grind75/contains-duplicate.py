class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        num_dictionary={}

        for i in nums:
            if i in num_dictionary:
                return True
            else:
                num_dictionary[i]=1
        
        return False
        """
        Set can also be used rather than dictionary:
        def containsDuplicate(self, nums):
            seen = set()
            for n in nums:
                if n in seen:
                    return True
                seen.add(n)
            return False
        """
