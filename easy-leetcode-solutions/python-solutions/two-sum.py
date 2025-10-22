class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num]=i