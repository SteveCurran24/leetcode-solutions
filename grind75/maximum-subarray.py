class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_ = nums[0]
        current = nums[0]

        for i in range(1, n):
            x = nums[i]
            if current + x > x:
                current = current + x
            else:
                current = x

            if current > max_:
                max_ = current

        return max_
