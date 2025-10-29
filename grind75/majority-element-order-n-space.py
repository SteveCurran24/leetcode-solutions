class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1

        for num in count:
            if count[num] > len(nums)/2:
                return num
