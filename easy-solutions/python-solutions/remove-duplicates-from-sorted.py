class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                del nums[i+1]
                
