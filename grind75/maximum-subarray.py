class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_nums = len(nums)
        max_ = nums[0]
        current = nums[0]

        for i in range(1, total_nums):
            temp = nums[i]
            if current + temp > temp:
                current = current + temp
            else:
                current = temp

            if current > max_:
                max_ = current

        return max_
