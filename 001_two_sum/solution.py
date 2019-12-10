class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = []
        for i in range(len(nums)):
            m = target - nums[i]
            if m in h:
                return [nums.index(m), i]
            h.append(nums[i])