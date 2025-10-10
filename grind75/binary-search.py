import math

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums) -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
            #left side logic
                high = mid-1

            if nums[mid] < target:
            #right side logic
                low = mid+1
       
        return -1
