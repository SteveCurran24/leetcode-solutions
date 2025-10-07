#This is my solution for TwoSum with O(n) using a python dictionary has a hash map
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hash_dict:
                return(i, hash_dict[complement])
            elif nums[i] not in hash_dict:
                hash_dict[nums[i]] = i
            else:
                continue
